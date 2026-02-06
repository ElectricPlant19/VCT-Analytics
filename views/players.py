import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data_loader import get_matches_overview
from utils import apply_plot_theme

def show_players():
    st.markdown("## 👤 Player Analytics")
    
    df = get_matches_overview()
    if df.empty:
        st.warning("Data loading...")
        return

    # --- Search & Filter ---
    all_players = sorted(df['Player'].dropna().unique().tolist())
    selected_player = st.selectbox("Select Player:", all_players, index=0)
    
    if selected_player:
        player_df = df[df['Player'] == selected_player]
        
        # --- Header Stats ---
        col1, col2, col3, col4, col5 = st.columns(5)
        avg_acs = player_df['Average Combat Score'].mean()
        avg_kd = player_df['KD'].mean() if 'KD' in player_df.columns else 0
        total_maps = player_df['Match Name'].count()
        avg_hs = player_df['Headshot %'].mean() if 'Headshot %' in player_df.columns else 0
        
        col1.metric("Avg ACS", f"{avg_acs:.0f}")
        col2.metric("Avg K/D", f"{avg_kd:.2f}")
        col3.metric("Maps Played", f"{total_maps}")
        col4.metric("HS %", f"{avg_hs:.1f}%")
        col5.metric("Active Since", player_df['Source_Year'].min().replace('vct_', ''))
        
        st.markdown("---")
        
        # --- Visualizations ---
        row1_1, row1_2 = st.columns([1, 2])
        
        with row1_1:
            st.subheader("Performance Profile")
            categories = ['ACS', 'K/D', 'HS%', 'KAST', 'ADR']
            kast = player_df['Kill, Assist, Trade, Survive %'].mean() if 'Kill, Assist, Trade, Survive %' in player_df.columns else 70
            adr = player_df['Average Damage Per Round'].mean() if 'Average Damage Per Round' in player_df.columns else 130
            
            values = [
                min(avg_acs / 300, 1), 
                min(avg_kd / 1.5, 1), 
                min(avg_hs / 40, 1),
                min(kast / 100, 1),
                min(adr / 180, 1)
            ]
            
            fig_radar = go.Figure(data=go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name=selected_player,
                line_color='#FF4655',
                fillcolor='rgba(255, 70, 85, 0.4)'
            ))
            
            # Styles specific to polar chart
            fig_radar.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Inter", color="white"),
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#2E3A47'),
                    angularaxis=dict(linecolor='#2E3A47', gridcolor='rgba(255,255,255,0.05)'),
                    bgcolor='#1C2733'
                ),
                showlegend=False,
                margin=dict(t=20, b=20, l=40, r=40)
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with row1_2:
            st.subheader("Form Over Time (ACS)")
            player_df_sorted = player_df.reset_index()
            
            fig_line = px.line(player_df_sorted, y='Average Combat Score', 
                               title="ACS Trend across Maps Played",
                               labels={'index': 'Maps Played'},
                               template='plotly_dark')
            fig_line.update_traces(line=dict(color='#FF4655', width=2))
            st.plotly_chart(apply_plot_theme(fig_line), use_container_width=True)

        # --- Agent Pool ---
        st.subheader("Agent Mastery")
        if 'Agents' in player_df.columns:
            agent_list = player_df['Agents'].astype(str).str.split(', ').explode()
            agent_counts = agent_list.value_counts().reset_index()
            agent_counts.columns = ['Agent', 'Matches']
            
            fig_bar = px.bar(agent_counts.head(5), x='Matches', y='Agent', orientation='h',
                             color='Matches', color_continuous_scale=['#2E3A47', '#FF4655'],
                             title="Top 5 Played Agents")
            fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(apply_plot_theme(fig_bar), use_container_width=True)
