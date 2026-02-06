import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import get_agent_pick_rates
from utils import apply_plot_theme

def show_agents():
    st.markdown("## 🤖 Agent Meta Tracker")
    
    df = get_agent_pick_rates()
    if df.empty:
        st.warning("Loading data...")
        return

    years = sorted(df['Source_Year'].unique())
    selected_year = st.selectbox("Select Season:", years, index=len(years)-1)
    
    year_df = df[df['Source_Year'] == selected_year]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"Agent Pick Rates ({selected_year.replace('vct_', '')})")
        avg_pick = year_df.groupby('Agent')['Pick Rate'].mean().sort_values(ascending=False).reset_index()
        
        # Consistent color scale
        fig_bar = px.bar(avg_pick.head(15), x='Pick Rate', y='Agent', orientation='h',
                         title="Top 15 Most Picked Agents",
                         color='Pick Rate', color_continuous_scale=['#2E3A47', '#46FFA6']) # Dark to Sentinel Green
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(apply_plot_theme(fig_bar), use_container_width=True)
        
    with col2:
        st.subheader("👑 S-Tier Agents")
        s_tier = avg_pick[avg_pick['Pick Rate'] > 50]
        if not s_tier.empty:
            for _, row in s_tier.iterrows():
                st.markdown(f"""
                <div style="background: linear-gradient(90deg, #1C2733, #232E3C); padding: 10px; border-radius: 6px; margin-bottom: 8px; border-left: 3px solid #FFC846;">
                    <span style="color: white; font-weight: bold;">{row['Agent'].title()}</span>
                    <span style="float: right; color: #FFC846; font-family: 'JetBrains Mono';">{row['Pick Rate']:.1f}%</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No agents > 50% avg pick rate this season.")
            
        st.subheader("📉 Emerging / Niche")
        niche = avg_pick[(avg_pick['Pick Rate'] < 10) & (avg_pick['Pick Rate'] > 2)]
        t_list = ", ".join([a.title() for a in niche['Agent'].head(5).tolist()])
        st.info(f"Watchlist: {t_list}")

    st.markdown("---")
    st.subheader("📈 Adoption History (All Time)")
    
    all_agents = sorted(df['Agent'].unique())
    default_agents = avg_pick['Agent'].head(3).tolist()
    compare_agents = st.multiselect("Compare Agents:", all_agents, default=default_agents)
    
    if compare_agents:
        trend_df = df[df['Agent'].isin(compare_agents)]
        trend_agg = trend_df.groupby(['Source_Year', 'Agent'])['Pick Rate'].mean().reset_index()
        
        fig_trend = px.line(trend_agg, x='Source_Year', y='Pick Rate', color='Agent',
                            markers=True, title="Pick Rate Evolution")
        st.plotly_chart(apply_plot_theme(fig_trend), use_container_width=True)
