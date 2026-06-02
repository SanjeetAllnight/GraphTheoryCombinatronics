import streamlit as st
from experiments import dynamic_experiment
import re
import base64
import os

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

st.set_page_config(
    page_title="Graph Theory Lab Record",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'theme' not in st.session_state:
    st.session_state.theme = "Dark"
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

def get_css():
    if st.session_state.theme == "Dark":
        bg_color = "#0F172A"
        card_bg = "#1E293B"
        card_hover = "#334155"
        text_color = "#F8FAFC"
        text_muted = "#CBD5E1"
        accent_primary = "#10B981"
        border_color = "#334155"
    else:
        bg_color = "#F8FAFC"
        card_bg = "#FFFFFF"
        card_hover = "#F1F5F9"
        text_color = "#111827"
        text_muted = "#6B7280"
        accent_primary = "#10B981"
        border_color = "#E5E7EB"

    return f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
        font-family: 'Inter', sans-serif;
    }}
    .premium-card {{
        background-color: {card_bg};
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid {border_color};
        transition: transform 250ms ease, box-shadow 250ms ease, background-color 250ms ease;
        position: relative;
    }}
    .premium-card:hover {{
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        background-color: {card_hover};
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
    }}
    .accent-text {{
        color: {accent_primary};
        font-weight: 600;
    }}
    /* Hide Sidebar Collapse Button */
    [data-testid="collapsedControl"] {{
        display: none;
    }}
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background-color: transparent;
    }}
    .stTabs [data-baseweb="tab"] {{
        padding: 12px 24px;
        background-color: {card_bg};
        border-radius: 8px 8px 0 0;
        border: 1px solid {border_color};
        border-bottom: none;
        color: {text_muted};
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {accent_primary} !important;
        color: white !important;
        border-color: {accent_primary} !important;
    }}
    /* Buttons */
    .stButton>button {{
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    .stButton>button[kind="primary"] {{
        background-color: {accent_primary};
        color: white;
        border: none;
    }}
    .stButton>button[kind="primary"]:hover {{
        background-color: #059669;
    }}
    .stButton>button[kind="secondary"] {{
        background-color: {card_bg};
        color: {text_color};
        border: 1px solid {border_color};
    }}
    .stButton>button[kind="secondary"]:hover {{
        border-color: {accent_primary};
        color: {accent_primary};
    }}
    /* Invisible Overlay Button Hack for Clickable Cards */
    .card-overlay-btn .stButton>button {{
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        opacity: 0 !important;
        z-index: 10 !important;
        cursor: pointer !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: transparent !important;
        border: none !important;
    }}
    /* Inputs */
    .stTextInput input, .stDateInput input, .stSelectbox > div > div {{
        background-color: {card_bg} !important;
        color: {text_color} !important;
        border: 1px solid {border_color} !important;
        border-radius: 6px;
    }}
    /* Top Header */
    [data-testid="stHeader"] {{
        background-color: {bg_color} !important;
    }}
    </style>
    """

st.markdown(get_css(), unsafe_allow_html=True)

# Theme Toggle & Header
logo_b64 = get_base64_image("Goa_College_of_Engineering_logo.png")
theme_accent = '#10B981'
border_col = '#334155' if st.session_state.theme == 'Dark' else '#E5E7EB'
text_col = '#F8FAFC' if st.session_state.theme == 'Dark' else '#111827'

col_h1, col_h2 = st.columns([10, 2])
with col_h2:
    st.markdown("<div style='text-align: right; margin-top: 15px;'>", unsafe_allow_html=True)
    theme_toggle = st.toggle("🌙 Dark Mode", value=(st.session_state.theme == "Dark"))
    new_theme = "Dark" if theme_toggle else "Light"
    if new_theme != st.session_state.theme:
        st.session_state.theme = new_theme
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

header_html = f"""
<div style="display: flex; align-items: center; padding: 0 0 20px 0; border-bottom: 1px solid {border_col}; margin-bottom: 30px;">
    <img src="data:image/png;base64,{logo_b64}" style="height: 80px; max-width: 150px; object-fit: contain; margin-right: 25px; {'filter: drop-shadow(0px 0px 4px rgba(255,255,255,0.3));' if st.session_state.theme == 'Dark' else ''}">
    <div style="display: flex; flex-direction: column;">
        <h2 style="margin: 0 0 4px 0; font-size: 22px; font-weight: 700; color: {text_col}; letter-spacing: 0.5px;">GOA COLLEGE OF ENGINEERING</h2>
        <h3 style="margin: 0 0 4px 0; font-size: 18px; color: {theme_accent}; font-weight: 600;">CMP226 – Graph Theory and Combinatorics Laboratory</h3>
        <p style="margin: 0; font-size: 14px; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'};">Academic Year 2025–2026</p>
    </div>
</div>
"""
with col_h1:
    st.markdown(header_html, unsafe_allow_html=True)

# SVG Icons
icons = {
    "Graph": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="18" r="3"/><circle cx="19" cy="18" r="3"/><circle cx="12" cy="6" r="3"/><path d="M7 16l4-8"/><path d="M17 16l-4-8"/></svg>',
    "Compare": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3h5v5"/><path d="M8 3H3v5"/><path d="M12 22v-8"/><path d="M5 8l7 6 7-6"/></svg>',
    "Network": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3"/><path d="M12 8v3"/></svg>',
    "Chart": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>',
    "Link": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
    "Tree": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-8"/><path d="M12 14c-2.5-3-5.5-3-7-3s-2.5 1.5-2.5 4h19c0-2.5-1-4-2.5-4s-4.5 0-7 3z"/><path d="M12 14v-4"/><path d="M12 10c-2.5-2-5.5-2-7-2s-2.5 1-2.5 3h19c0-2-1-3-2.5-3s-4.5 0-7 2z"/><path d="M12 10V6"/><path d="M12 6c-2-1.5-4.5-1.5-6-1.5s-2 1-2 2h16c0-1-1-2-2-2s-4 0-6 1.5z"/></svg>',
    "Route": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/></svg>',
    "Footsteps": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16v-2.38C4 11.5 7.97 10.5 12 10.5s8 1 8 3.12V16"/><path d="M12 2v6"/><path d="M8 6h8"/></svg>',
    "Refresh": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2v6h-6"/><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M3 22v-6h6"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/></svg>',
    "Circle": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/></svg>',
    "Palette": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r=".5"/><circle cx="17.5" cy="10.5" r=".5"/><circle cx="8.5" cy="7.5" r=".5"/><circle cx="6.5" cy="12.5" r=".5"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/></svg>'
}

EXPERIMENT_LIST = [
    ("1 Basic Graphs", "Graph", "Hardcoded Demo"),
    ("2 Graph Isomorphism", "Compare", "Graph Algorithm"),
    ("3 Subgraphs", "Network", "Visualization"),
    ("4 Havel-Hakimi", "Chart", "Interactive"),
    ("5 Line Graph", "Link", "Hardcoded Demo"),
    ("6 Kruskal MST", "Tree", "Graph Algorithm"),
    ("7 Dijkstra", "Route", "Graph Algorithm"),
    ("8 Closed Walks Trails Paths", "Footsteps", "Visualization"),
    ("9 Eulerian Circuit", "Refresh", "Graph Algorithm"),
    ("10 Hamiltonian Circuit", "Circle", "Graph Algorithm"),
    ("11 Greedy Graph Colouring", "Palette", "NetworkX")
]

if st.session_state.current_page == "Home":
    
    # Dashboard Hero Section
    st.markdown(f"""
    <div style="display: flex; gap: 20px; margin-bottom: 40px; margin-top: 10px;">
        <div class="premium-card" style="flex: 1; padding: 20px; margin-bottom: 0;">
            <h4 style="margin: 0 0 5px 0; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'}; font-size: 13px; text-transform: uppercase;">Total</h4>
            <h2 style="margin: 0; color: {theme_accent}; font-size: 28px;">11 Experiments</h2>
        </div>
        <div class="premium-card" style="flex: 1; padding: 20px; margin-bottom: 0;">
            <h4 style="margin: 0 0 5px 0; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'}; font-size: 13px; text-transform: uppercase;">Powered By</h4>
            <h2 style="margin: 0; color: {text_col}; font-size: 24px;">NetworkX Algorithms</h2>
        </div>
        <div class="premium-card" style="flex: 1; padding: 20px; margin-bottom: 0;">
            <h4 style="margin: 0 0 5px 0; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'}; font-size: 13px; text-transform: uppercase;">Features</h4>
            <h2 style="margin: 0; color: {text_col}; font-size: 24px;">Graph Visualizations</h2>
        </div>
        <div class="premium-card" style="flex: 1; padding: 20px; margin-bottom: 0;">
            <h4 style="margin: 0 0 5px 0; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'}; font-size: 13px; text-transform: uppercase;">Tools</h4>
            <h2 style="margin: 0; color: {text_col}; font-size: 24px;">Interactive Solvers</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for idx, (exp, icon_key, category) in enumerate(EXPERIMENT_LIST):
        col = cols[idx % 3]
        match = re.match(r"(\d+)\s+(.+)", exp)
        exp_num = match.group(1).zfill(2)
        exp_title = match.group(2)
        svg_icon = icons.get(icon_key, "")
        
        with col:
            st.markdown(f"""
            <div class="premium-card" style="padding: 24px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                        <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 700; color: {theme_accent}; background: {'rgba(16, 185, 129, 0.15)' if st.session_state.theme=='Dark' else 'rgba(16, 185, 129, 0.1)'}; padding: 6px 12px; border-radius: 6px;">
                            {svg_icon}
                            Exp {exp_num}
                        </span>
                        <span style="font-size: 12px; font-weight: 600; color: {theme_accent}; display: flex; align-items: center; gap: 4px;">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
                            Ready
                        </span>
                    </div>
                    <h3 style="margin: 0 0 10px 0; font-size: 18px; line-height: 1.4; color: {text_col};">{exp_title}</h3>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 11px; font-weight: 500; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'}; border: 1px solid {border_col}; padding: 4px 10px; border-radius: 20px;">{category}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div class='card-overlay-btn' style='position: relative; margin-top: -190px; height: 180px; width: 100%; z-index: 20;'>", unsafe_allow_html=True)
            if st.button("Open", key=f"btn_{exp_num}", use_container_width=True):
                st.session_state.current_page = exp
                st.rerun()
            st.markdown("</div><div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

else:
    col_back, _ = st.columns([2, 10])
    with col_back:
        if st.button("← Back to Dashboard", use_container_width=True):
            st.session_state.current_page = "Home"
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    dynamic_experiment.render(st.session_state.current_page)

# Global Footer
footer_html = f"""
<div style="margin-top: 80px; padding-top: 30px; border-top: 1px solid {border_col}; font-size: 14px; color: {'#CBD5E1' if st.session_state.theme=='Dark' else '#6B7280'}; font-family: 'Inter', sans-serif;">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; background: {'rgba(255,255,255,0.03)' if st.session_state.theme=='Dark' else 'rgba(0,0,0,0.02)'}; padding: 15px 30px; border-radius: 12px; border: 1px solid {border_col};">
            <span><strong style="color: {text_col};">Student Name:</strong> Sanjeet Ghadi</span>
            <span><strong style="color: {text_col};">Roll Number:</strong> 24B-CO-056</span>
            <span><strong style="color: {text_col};">Semester:</strong> Fourth</span>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 5px; opacity: 0.9;">
            <strong style="color: {text_col}; font-size: 15px;">Goa College of Engineering</strong>
            <span>CMP226 – Graph Theory and Combinatorics Laboratory &nbsp;•&nbsp; Academic Year 2025–2026</span>
        </div>
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
