import streamlit as st
from utils import setup_page_config
from views import overview, players, teams, agents, maps, history

# --- App Setup ---
setup_page_config(page_title="VCT 2021-2025 Analytics")

# --- Sidebar Navigation ---
st.sidebar.title("VCT Analytics 🏆")
st.sidebar.markdown("Professional Esports Dashboard")

page = st.sidebar.radio("Navigation", [
    "Overview", 
    "Players", 
    "Teams", 
    "Agents", 
    "Maps", 
    "History"
], index=0)

st.sidebar.markdown("---")
st.sidebar.info("Data source: Kaggle (Ryan Luong)\nCovers VCT 2021-2025")

# --- Page Routing ---
if page == "Overview":
    overview.show_overview()
elif page == "Players":
    players.show_players()
elif page == "Teams":
    teams.show_teams()
elif page == "Agents":
    agents.show_agents()
elif page == "Maps":
    maps.show_maps()
elif page == "History":
    history.show_history()
    
# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        Built with Streamlit • VCT Dashboard Project
    </div>
    """, unsafe_allow_html=True
)
