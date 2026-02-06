import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data_loader import get_matches_overview, get_agent_pick_rates, get_match_scores
from utils import render_kpi, apply_plot_theme

def show_overview():
    st.markdown("## 🌐 VCT Command Center")
    st.markdown("<div style='color: #FF4655; font-weight: 600; margin-bottom: 20px;'>ACTIVE ECOSYSTEM VIEW • 2021-2025</div>", unsafe_allow_html=True)
    
    # Load Data
    with st.spinner("Loading aggregated VCT data..."):
        df_overview = get_matches_overview()
        df_agents = get_agent_pick_rates()
        df_scores = get_match_scores()
    
    if df_overview.empty:
        st.error("No data available. Please check the data source.")
        return

    # --- Top KPIs ---
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        total_matches = df_scores['Match Name'].nunique()
        render_kpi("Total Matches", f"{total_matches:,}", help_text="Across all tracked tournaments")
        
    with kpi_col2:
        total_players = df_overview['Player'].nunique()
        render_kpi("Active Players", f"{total_players:,}", help_text="Unique players who played at least 1 map")
        
    with kpi_col3:
        total_teams = df_overview['Team'].nunique()
        render_kpi("Teams", f"{total_teams:,}", help_text="Unique teams competing")

    with kpi_col4:
        latest_year = df_overview['Source_Year'].max().replace('vct_', '')
        render_kpi("Latest Season", latest_year)
        
    st.markdown("---")
    
    # --- Global Trends ---
    col_chart1, col_chart2 = st.columns([2, 1])
    
    with col_chart1:
        st.subheader("📈 Meta Evolution (Top Agents)")
        if not df_agents.empty:
            yearly_picks = df_agents.groupby(['Source_Year', 'Agent'])['Pick Rate'].mean().reset_index()
            top_agents = yearly_picks.groupby('Agent')['Pick Rate'].sum().nlargest(5).index.tolist()
            filtered_trends = yearly_picks[yearly_picks['Agent'].isin(top_agents)]
            
            fig_meta = px.line(filtered_trends, x='Source_Year', y='Pick Rate', color='Agent',
                               markers=True, title="Top 5 Agents Adoption Trends",
                               color_discrete_sequence=['#FF4655', '#46D9FF', '#FFC846', '#B446FF', '#46FFA6'])
            
            # Customizing line styles
            fig_meta.update_traces(line=dict(width=3), marker=dict(size=8, line=dict(width=2, color='#0F1923')))
            
            st.plotly_chart(apply_plot_theme(fig_meta), use_container_width=True)
            
    with col_chart2:
        st.subheader("🌍 Regional Activity")
        matches_per_year = df_scores.groupby('Source_Year')['Match Name'].nunique().reset_index()
        fig_activity = px.bar(matches_per_year, x='Source_Year', y='Match Name',
                              title="Matches per Season",
                              color='Match Name', color_continuous_scale='Reds')
        
        st.plotly_chart(apply_plot_theme(fig_activity), use_container_width=True)

    # --- Quick Stats Grid ---
    st.subheader("🏆 Hall of Fame")
    row1_1, row1_2, row1_3 = st.columns(3)
    
    # Custom CSS for these info boxes
    box_style = """
        padding: 20px;
        background-color: #1C2733;
        border-radius: 10px;
        border-left: 4px solid #FF4655;
    """
    
    with row1_1:
         player_stats = df_overview.groupby(['Player']).agg({'Average Combat Score': 'mean', 'Match Name': 'nunique'}).reset_index()
         experienced = player_stats[player_stats['Match Name'] >= 50]
         if not experienced.empty:
             top_acs = experienced.nlargest(1, 'Average Combat Score').iloc[0]
             st.markdown(f"""
             <div style="{box_style}">
                <div style="font-size: 0.9em; color: #B4BCC8;">HIGHEST CAREER ACS</div>
                <div style="font-size: 1.5em; font-weight: bold; color: white;">{top_acs['Player']}</div>
                <div style="color: #FF4655; font-family: 'JetBrains Mono';">{top_acs['Average Combat Score']:.1f}</div>
             </div>
             """, unsafe_allow_html=True)
             
    with row1_2:
        if not df_scores.empty:
             df_scores['Winner'] = df_scores['Match Result'].str.replace(' won', '', regex=False)
             top_team = df_scores['Winner'].value_counts().idxmax()
             win_count = df_scores['Winner'].value_counts().max()
             st.markdown(f"""
             <div style="{box_style.replace('#FF4655', '#46FFA6')}">
                <div style="font-size: 0.9em; color: #B4BCC8;">MOST WINS</div>
                <div style="font-size: 1.5em; font-weight: bold; color: white;">{top_team}</div>
                <div style="color: #46FFA6; font-family: 'JetBrains Mono';">{win_count} Matches</div>
             </div>
             """, unsafe_allow_html=True)
             
    with row1_3:
        if not df_agents.empty:
            top_agent = df_agents.groupby('Agent')['Pick Rate'].mean().idxmax()
            st.markdown(f"""
             <div style="{box_style.replace('#FF4655', '#FFC846')}">
                <div style="font-size: 0.9em; color: #B4BCC8;">ICONIC AGENT</div>
                <div style="font-size: 1.5em; font-weight: bold; color: white;">{top_agent.title()}</div>
                <div style="color: #FFC846; font-family: 'JetBrains Mono';">Most Picked All-Time</div>
             </div>
             """, unsafe_allow_html=True)
