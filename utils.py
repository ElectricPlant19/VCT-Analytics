import streamlit as st

def setup_page_config(page_title="VCT Analytics"):
    st.set_page_config(
        page_title=page_title,
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    apply_custom_css()

def apply_custom_css():
    st.markdown("""
        <style>
        /* Import Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
        
        /* --- GLOBAL VARIABLES --- */
        :root {
            --bg-primary: #0F1923;
            --bg-secondary: #1C2733;
            --bg-elevated: #232E3C;
            --val-red: #FF4655;
            --val-red-hover: #FF6B76;
            --text-primary: #FFFFFF;
            --text-secondary: #B4BCC8;
            --border-color: #2E3A47;
        }

        /* --- MAIN LAYOUT --- */
        .stApp {
            background-color: var(--bg-primary);
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: var(--text-primary) !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
            text-transform: uppercase;
        }
        h1 { border-bottom: 2px solid var(--val-red); padding-bottom: 10px; }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: var(--bg-secondary);
            border-right: 1px solid var(--border-color);
        }
        
        /* --- COMPONENTS --- */
        
        /* KPI/Metric Cards */
        div[data-testid="metric-container"] {
            background: linear-gradient(135deg, var(--bg-secondary), var(--bg-elevated));
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }
        div[data-testid="metric-container"]:hover {
            transform: translateY(-4px);
            border-color: var(--val-red);
            box-shadow: 0 8px 20px rgba(255, 70, 85, 0.15);
        }
        div[data-testid="metric-container"] label {
            font-family: 'Inter', sans-serif;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-primary);
            font-size: 2rem !important;
            font-weight: 700;
        }
        
        /* Regular Cards (Expander/Containers) */
        div[data-testid="stExpander"] {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }
        
        /* Buttons */
        button[kind="primary"] {
            background: linear-gradient(90deg, var(--val-red), #E63946);
            border: none;
            color: white;
            font-weight: 600;
            transition: all 0.2s;
        }
        button[kind="primary"]:hover {
            box-shadow: 0 0 15px rgba(255, 70, 85, 0.5);
            transform: scale(1.02);
        }
        
        /* Inputs/Selectboxes */
        div[data-baseweb="select"] > div {
            background-color: var(--bg-elevated);
            border-color: var(--border-color);
            color: white;
        }
        
        /* Tables/Dataframes */
        div[data-testid="stDataFrame"] {
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }
        
        /* Custom Classes */
        .glass-card {
            background: rgba(28, 39, 51, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
        }
        
        /* Divider */
        hr {
            border-color: var(--border-color);
            margin: 30px 0;
        }
        
        </style>
    """, unsafe_allow_html=True)

def render_kpi(label, value, delta=None, help_text=None):
    st.metric(label=label, value=value, delta=delta, help=help_text)

def apply_plot_theme(fig):
    """
    Applies the Valorant Dashboard theme to a Plotly figure.
    """
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter", color="#B4BCC8"),
        title_font=dict(family="Inter", size=20, color="#FFFFFF"),
        xaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.05)',
            linecolor='#2E3A47',
            tickfont=dict(family='JetBrains Mono')
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.05)',
            linecolor='#2E3A47',
            tickfont=dict(family='JetBrains Mono')
        ),
        legend=dict(
            bgcolor='rgba(28, 39, 51, 0.9)',
            bordercolor='#2E3A47',
            borderwidth=1
        ),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig
