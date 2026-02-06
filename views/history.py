import streamlit as st
import pandas as pd
from data_loader import get_match_scores

def show_history():
    st.markdown("## 📜 Tournament History")
    
    df = get_match_scores()
    if df.empty:
        st.warning("Loading data...")
        return
        
    # --- Timeline Browser ---
    years = sorted(df['Source_Year'].unique(), reverse=True)
    
    for year in years:
        with st.expander(f"📅 {year.replace('vct_', '')} Season", expanded=(year==years[0])):
            year_data = df[df['Source_Year'] == year]
            
            # List Tournaments
            tournaments = year_data['Tournament'].unique()
            
            # Simple stats per tournament
            tourney_stats = []
            for t in tournaments:
                t_matches = year_data[year_data['Tournament'] == t]
                match_count = len(t_matches)
                # Winner heuristic: Team with most wins in 'Finals' or just last winner?
                # Let's just list match count for now
                tourney_stats.append({
                    "Tournament": t,
                    "Matches": match_count,
                    "Teams": len(set(t_matches['Team A'].unique()) | set(t_matches['Team B'].unique()))
                })
            
            t_df = pd.DataFrame(tourney_stats).sort_values('Matches', ascending=False)
            st.dataframe(t_df, use_container_width=True, hide_index=True)
            
            # Highlight 'Champions' if present
            champs = [t for t in tournaments if 'Champions' in t]
            if champs:
                st.caption(f"🏆 Major Event: {champs[0]}")

