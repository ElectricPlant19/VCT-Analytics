import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_loader import get_matches_overview, get_match_scores
from utils import apply_plot_theme

def show_h2h():
    st.markdown("## ⚔️ Head-to-Head Analyzer")
    
    mode = st.selectbox("Comparison Mode", ["Player vs Player", "Team vs Team"])
    
    if mode == "Player vs Player":
        compare_players()
    else:
        compare_teams()

def compare_players():
    df = get_matches_overview()
    if df.empty:
        return
        
    players = sorted(df['Player'].dropna().astype(str).unique())
    col1, col2 = st.columns(2)
    
    with col1:
        p1 = st.selectbox("Player 1", players, index=0)
    with col2:
        # Default to a different player if possible
        default_idx = 1 if len(players) > 1 else 0
        p2 = st.selectbox("Player 2", players, index=default_idx)
        
    if p1 and p2:
        # Filter Data
        p1_data = df[df['Player'] == p1]
        p2_data = df[df['Player'] == p2]
        
        # Calculate Metrics
        metrics = {
            "ACS": "Average Combat Score",
            "KD": "KD", # Make sure this matches data_loader cleaning
            "ADR": "Average Damage Per Round",
            "KAST%": "Kill, Assist, Trade, Survive %",
            "HS%": "Headshot %"
        }
        
        # Prepare Comparison Table
        comp_data = []
        for label, col in metrics.items():
            if col in df.columns:
                val1 = p1_data[col].mean()
                val2 = p2_data[col].mean()
                diff = val1 - val2
                comp_data.append({
                    "Metric": label,
                    p1: f"{val1:.1f}",
                    p2: f"{val2:.1f}",
                    "Diff": diff
                })
        
        # Display Stats Side-by-Side
        st.markdown("### Career Average Comparison")
        
        # Custom HTML comparison
        for item in comp_data:
            val1 = float(item[p1])
            val2 = float(item[p2])
            
            # Color logic
            c1 = "#46FFA6" if val1 >= val2 else "#FF4655"
            c2 = "#46FFA6" if val2 > val1 else "#FF4655"
            
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
                <div style="flex: 1; text-align: left; font-weight: bold; color: {c1};">{val1}</div>
                <div style="flex: 1; text-align: center; color: #B4BCC8; text-transform: uppercase; font-size: 0.9em;">{item["Metric"]}</div>
                <div style="flex: 1; text-align: right; font-weight: bold; color: {c2};">{val2}</div>
            </div>
            """, unsafe_allow_html=True)
            
        # Export
        export_df = pd.DataFrame(comp_data)
        csv = export_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Comparison CSV",
            data=csv,
            file_name=f"{p1}_vs_{p2}_comparison.csv",
            mime="text/csv",
        )
            
        # Radar Comparison
        st.markdown("### Attribute Radar")
        
        # Normalize for chart
        categories = list(metrics.keys())
        
        # Helper to get normalized mean (0-1 approx)
        def get_norm(d, col):
            if col not in d.columns: return 0
            m = d[col].mean()
            # Rough max scaling values based on domain knowledge
            scales = {"Average Combat Score": 300, "KD": 1.5, "Average Damage Per Round": 180, "Kill, Assist, Trade, Survive %": 100, "Headshot %": 40}
            return min(m / scales.get(col, 100), 1.0)

        vals1 = [get_norm(p1_data, metrics[c]) for c in categories]
        vals2 = [get_norm(p2_data, metrics[c]) for c in categories]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=vals1, theta=categories, fill='toself', name=p1,
            line_color='#FF4655', fillcolor='rgba(255, 70, 85, 0.3)'
        ))
        fig.add_trace(go.Scatterpolar(
            r=vals2, theta=categories, fill='toself', name=p2,
            line_color='#46D9FF', fillcolor='rgba(70, 217, 255, 0.3)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1], showticklabels=False),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color='white'),
             legend=dict(orientation="h", y=-0.1)
        )
        st.plotly_chart(fig, use_container_width=True)


def compare_teams():
    df = get_match_scores()
    if df.empty: return
    
    teams = sorted(list(set(df['Team A'].unique()) | set(df['Team B'].unique())))
    
    col1, col2 = st.columns(2)
    with col1: t1 = st.selectbox("Team 1", teams, index=0)
    with col2: t2 = st.selectbox("Team 2", teams, index=1 if len(teams)>1 else 0)
    
    if t1 and t2:
        # Find Direct Matchups
        head_to_head = df[
            ((df['Team A'] == t1) & (df['Team B'] == t2)) |
            ((df['Team A'] == t2) & (df['Team B'] == t1))
        ]
        
        st.subheader(f"History: {t1} vs {t2}")
        
        if head_to_head.empty:
            st.info("No direct matches found in record.")
        else:
            # Calculate Wins
            # Assuming 'Match Result' is "TeamName won"
            wins1 = head_to_head['Match Result'].str.contains(t1).sum()
            wins2 = head_to_head['Match Result'].str.contains(t2).sum()
            
            # Display Score
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; gap: 40px; margin: 30px 0;">
                <div style="text-align: center;">
                    <div style="font-size: 3em; font-weight: bold; color: #FF4655;">{wins1}</div>
                    <div style="color: #B4BCC8;">{t1} Wins</div>
                </div>
                <div style="font-size: 1.5em; color: #6E7A8A;">vs</div>
                <div style="text-align: center;">
                    <div style="font-size: 3em; font-weight: bold; color: #46D9FF;">{wins2}</div>
                    <div style="color: #B4BCC8;">{t2} Wins</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Match Log
            st.subheader("Match Log")
            display_cols = ['Source_Year', 'Tournament', 'Stage', 'Match Name', 'Match Result', 'Team A Score', 'Team B Score']
            st.dataframe(head_to_head[display_cols].sort_values('Source_Year', ascending=False), use_container_width=True, hide_index=True)
