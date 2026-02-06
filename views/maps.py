import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import get_map_stats
from utils import apply_plot_theme

def show_maps():
    st.markdown("## 🗺️ Map Analytics")
    
    df = get_map_stats()
    if df.empty:
        st.warning("Loading data...")
        return
        
    st.subheader("⚖️ Attacker vs Defender Balance")
    
    df_clean = df[df['Map'] != 'All Maps']
    
    map_bal = df_clean.groupby('Map').agg({
        'Attacker Side Win Percentage': 'mean',
        'Defender Side Win Percentage': 'mean',
        'Total Maps Played': 'sum'
    }).sort_values('Total Maps Played', ascending=False).reset_index()
    
    map_melt = map_bal.melt(id_vars='Map', 
                            value_vars=['Attacker Side Win Percentage', 'Defender Side Win Percentage'],
                            var_name='Side', value_name='Win Rate')
    
    # Precise Palette
    color_map = {
        'Attacker Side Win Percentage': '#FF4655', # Val Red
        'Defender Side Win Percentage': '#46FFA6' # Success Green for defense? Or Navy? Design doc says Def usually neutral or opposing. 
        # Actually standard logic: Atk = Red (Destructive), Def = Green/Blue (Protective). Design doc says Success=Green.
        # Let's use Def=Green (Success/Defense) and Atk=Red (Danger/Attack)
    }
    
    fig_bal = px.bar(map_melt, y='Map', x='Win Rate', color='Side', orientation='h',
                     title="Side Win Rates (All Time)",
                     color_discrete_map=color_map,
                     text='Win Rate')
    
    fig_bal.update_traces(texttemplate='%{text:.1f}%', textposition='inside')
    fig_bal.update_layout(barmode='stack', xaxis=dict(range=[0, 100]),
                          legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    
    st.plotly_chart(apply_plot_theme(fig_bal), use_container_width=True)
    
    st.subheader("Map Popularity")
    fig_pop = px.pie(map_bal, values='Total Maps Played', names='Map', hole=0.4,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(apply_plot_theme(fig_pop), use_container_width=True)
