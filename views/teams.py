import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import get_matches_overview, get_match_scores
from utils import apply_plot_theme

def show_teams():
    st.markdown("## 🛡️ Team Analytics")
    
    df_scores = get_match_scores()
    df_overview = get_matches_overview()
    
    if df_scores.empty:
        st.warning("Loading data...")
        return

    all_teams = sorted(list(set(df_scores['Team A'].dropna().unique()) | set(df_scores['Team B'].dropna().unique())))
    selected_team = st.selectbox("Select Team:", all_teams, index=0)
    
    if selected_team:
        team_matches = df_scores[(df_scores['Team A'] == selected_team) | (df_scores['Team B'] == selected_team)]
        
        if not team_matches.empty:
            team_matches['Won'] = team_matches['Match Result'].apply(lambda x: selected_team in str(x))
            wins = team_matches['Won'].sum()
            total = len(team_matches)
            wr = (wins / total) * 100
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Overall Win Rate", f"{wr:.1f}%")
            col2.metric("Matches Played", f"{total}")
            col3.metric("Wins", f"{wins}")
        
            st.markdown("---")
            
            st.subheader("👥 Active Roster (Latest Season)")
            latest_year = team_matches['Source_Year'].max()
            
            roster_df = df_overview[
                (df_overview['Team'] == selected_team) & 
                (df_overview['Source_Year'] == latest_year)
            ]
            
            if not roster_df.empty:
                active_roster = roster_df.groupby('Player')['Match Name'].nunique().sort_values(ascending=False).head(5)
                cols = st.columns(len(active_roster))
                for i, (player, maps) in enumerate(active_roster.items()):
                    with cols[i]:
                        # Card Style for Players
                        st.markdown(f"""
                        <div style="background-color: #232E3C; padding: 15px; border-radius: 8px; text-align: center; border: 1px solid #2E3A47;">
                            <div style="color: #FF4655; font-weight: bold; font-size: 1.1em;">{player}</div>
                            <div style="color: #B4BCC8; font-size: 0.8em; margin-top: 5px;">{maps} Maps</div>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.write("No active roster data found for latest season.")

            st.subheader("🗺️ Map Performance")
            map_counts = roster_df['Map'].value_counts().reset_index()
            map_counts.columns = ['Map', 'Times Played']
            
            fig_map = px.bar(map_counts, x='Map', y='Times Played', 
                             title="Maps Played Distribution (Latest Season)",
                             color='Times Played', color_continuous_scale='Blues')
            
            st.plotly_chart(apply_plot_theme(fig_map), use_container_width=True)
