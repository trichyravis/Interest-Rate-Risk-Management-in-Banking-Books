
"""
Interest Rate Risk in the Banking Book (IRRBB) — Interactive Learning Application
The Mountain Path Academy — World of Finance
Prof. V. Ravichandran
https://themountainpathacademy.com
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# ─── Page Config ───
st.set_page_config(
    page_title="IRRBB | The Mountain Path Academy",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Mountain Path Design System ───
GOLD = "#FFD700"
BLUE = "#003366"
MID_BLUE = "#004d80"
CARD_BG = "#112240"
TEXT = "#e6f1ff"
MUTED = "#8892b0"
GREEN = "#28a745"
RED = "#dc3545"
LIGHT_BLUE = "#ADD8E6"
ORANGE = "#FF8C00"
PURPLE = "#7B1FA2"
TEAL = "#00796B"
BG_GRADIENT = "linear-gradient(135deg,#1a2332,#243447,#2a3f5f)"

# ─── Custom CSS (permanent dark-theme fix for all controls) ───
st.html(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;800&family=Source+Sans+3:wght@300;400;500;600;700&display=swap');

    .stApp {{
        background: {BG_GRADIENT};
        font-family: 'Source Sans 3', sans-serif;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #0a1628, #112240, #1a2332) !important;
        border-right: 2px solid {GOLD} !important;
    }}
    section[data-testid="stSidebar"] * {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stRadio label {{
        color: {GOLD} !important;
        -webkit-text-fill-color: {GOLD} !important;
        font-weight: 600 !important;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* ══════════════════════════════════════════════════════════════
       PERMANENT DARK THEME FIX for all BaseWeb components
       ══════════════════════════════════════════════════════════════ */
    .stSelectbox [data-baseweb="select"],
    .stMultiSelect [data-baseweb="select"],
    div[data-baseweb="select"] {{
        background-color: {CARD_BG} !important;
        border-color: rgba(255,215,0,0.25) !important;
    }}
    .stSelectbox [data-baseweb="select"]:hover,
    .stMultiSelect [data-baseweb="select"]:hover {{
        border-color: {GOLD} !important;
    }}
    .stSelectbox [data-baseweb="select"] span,
    .stSelectbox [data-baseweb="select"] div,
    .stSelectbox [data-baseweb="select"] p,
    .stSelectbox [data-baseweb="select"] input,
    .stMultiSelect [data-baseweb="select"] span,
    .stMultiSelect [data-baseweb="select"] div,
    .stMultiSelect [data-baseweb="select"] p,
    .stMultiSelect [data-baseweb="select"] input,
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div,
    div[data-baseweb="select"] p {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
        background-color: transparent !important;
    }}
    .stSelectbox svg, .stMultiSelect svg {{
        fill: {GOLD} !important;
    }}

    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    [data-baseweb="popover"] > div > div {{
        background-color: {CARD_BG} !important;
        background: {CARD_BG} !important;
        border: 1px solid rgba(255,215,0,0.3) !important;
        border-radius: 8px !important;
    }}
    [data-baseweb="menu"],
    [data-baseweb="menu"] > div,
    ul[role="listbox"],
    ul[role="listbox"] > li {{
        background-color: {CARD_BG} !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}
    li[role="option"] {{
        background-color: {CARD_BG} !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}
    li[role="option"] * {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
        background: transparent !important;
    }}
    li[role="option"]:hover,
    li[role="option"][aria-selected="true"],
    li[role="option"]:focus,
    li[role="option"]:hover *,
    li[role="option"][aria-selected="true"] *,
    li[role="option"]:focus * {{
        background-color: {MID_BLUE} !important;
        color: {GOLD} !important;
        -webkit-text-fill-color: {GOLD} !important;
    }}

    .stTextInput input, .stNumberInput input, .stTextArea textarea {{
        background-color: {CARD_BG} !important;
        border-color: rgba(255,215,0,0.25) !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    .stSelectbox label, .stMultiSelect label, .stTextInput label,
    .stNumberInput label, .stTextArea label, .stSlider label,
    .stRadio label, .stCheckbox label {{
        color: {GOLD} !important;
        -webkit-text-fill-color: {GOLD} !important;
        font-weight: 600 !important;
    }}

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px;
        background: rgba(17,34,64,0.6);
        border-radius: 12px;
        padding: 4px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: 8px;
        color: {MUTED} !important;
        -webkit-text-fill-color: {MUTED} !important;
        font-weight: 600;
        padding: 8px 16px;
    }}
    .stTabs [aria-selected="true"] {{
        background: {BLUE} !important;
        color: {GOLD} !important;
        -webkit-text-fill-color: {GOLD} !important;
        border-bottom: 2px solid {GOLD} !important;
    }}

    /* Metrics */
    [data-testid="stMetric"] {{
        background: {CARD_BG};
        border: 1px solid rgba(255,215,0,0.15);
        border-radius: 12px;
        padding: 16px;
    }}
    [data-testid="stMetric"] label {{
        color: {MUTED} !important;
        -webkit-text-fill-color: {MUTED} !important;
        font-size: 0.85rem !important;
    }}
    [data-testid="stMetric"] [data-testid="stMetricValue"] {{
        color: {GOLD} !important;
        -webkit-text-fill-color: {GOLD} !important;
        font-family: 'Playfair Display', serif !important;
    }}

    /* Expander */
    details[data-testid="stExpander"] {{
        background: {CARD_BG} !important;
        border: 1px solid rgba(255,215,0,0.2) !important;
        border-radius: 8px !important;
    }}
    details[data-testid="stExpander"] summary,
    details[data-testid="stExpander"] summary *,
    details[data-testid="stExpander"] summary span,
    details[data-testid="stExpander"] summary p,
    details[data-testid="stExpander"] summary div {{
        color: {GOLD} !important;
        -webkit-text-fill-color: {GOLD} !important;
        background: transparent !important;
        background-color: transparent !important;
    }}
    details[data-testid="stExpander"] > div,
    details[data-testid="stExpander"] > div * {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
        background-color: transparent !important;
    }}
    details[data-testid="stExpander"] summary:hover,
    details[data-testid="stExpander"] summary:focus,
    details[data-testid="stExpander"] summary:hover *,
    details[data-testid="stExpander"] summary:focus * {{
        background: transparent !important;
        background-color: transparent !important;
        outline: none !important;
        box-shadow: none !important;
    }}

    /* Markdown text */
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] li {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    .stDataFrame, .stTable {{
        border: 1px solid rgba(255,215,0,0.15) !important;
        border-radius: 8px !important;
    }}

    .stSlider [data-baseweb="slider"] [role="slider"] {{
        background: {GOLD} !important;
    }}
</style>
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DATA LAYER — Three Distinct Case Studies
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BUCKETS = ["0-3M", "3-6M", "6M-1Y", "1-3Y", "3-5Y+"]

# ── Case 1: Bharat National Bank (Asset-Sensitive, Mild Risk) ──
CASE_1 = {
    "name": "Bharat National Bank (BNB)",
    "profile": "Asset-Sensitive · Mild IRRBB Exposure · India",
    "description": "A mid-sized Indian commercial bank with a balanced book. Mildly asset-sensitive with positive cumulative 1-year rate gap.",
    "currency": "INR crore",
    "total_assets": 120000,
    "tier1": 15000,
    "base_nii": 3600,
    "cum_1y_gap": 3000,
    "nim_pct": 3.00,
    # Balance sheet
    "assets": {
        "Cash & RBI Balances":      {"amount": 10000, "rate": 4.50, "type": "Fixed"},
        "Government Securities":     {"amount": 30000, "rate": 7.00, "type": "Fixed"},
        "Loans — Fixed Rate":        {"amount": 35000, "rate": 9.50, "type": "Fixed"},
        "Loans — Floating (MCLR)":   {"amount": 30000, "rate": 10.00, "type": "Floating"},
        "Interbank Placements":      {"amount": 8000,  "rate": 6.50, "type": "Fixed"},
        "Fixed Assets & Others":     {"amount": 7000,  "rate": 0.00, "type": "Non-earning"},
    },
    "liabilities": {
        "CASA Deposits":             {"amount": 36000, "rate": 3.50, "type": "Floating"},
        "Term Deposits":             {"amount": 42000, "rate": 7.00, "type": "Fixed"},
        "Interbank Borrowings":      {"amount": 15000, "rate": 6.80, "type": "Floating"},
        "Bonds Issued":              {"amount": 5000,  "rate": 8.00, "type": "Fixed"},
        "Other Liabilities":         {"amount": 7000,  "rate": 2.50, "type": "Fixed"},
        "Shareholders' Equity":      {"amount": 15000, "rate": 0.00, "type": "Non-interest"},
    },
    # Rate sensitivity gap by bucket
    "rsa": [22000, 15000, 18000, 25000, 13000],
    "rsl": [18000, 14000, 20000, 22000, 6000],
    # EVE discount factors (base and +200bps shocked)
    "df_base": [0.98, 0.96, 0.93, 0.85, 0.75],
    "df_shock_up": [0.97, 0.94, 0.90, 0.81, 0.70],
    "df_shock_down": [0.99, 0.98, 0.96, 0.89, 0.80],
    # Six-scenario results (pre-calculated from the case study)
    "scenarios": {
        "Parallel Up (+200)":    {"dNII": 60,   "dEVE": -470},
        "Parallel Down (-200)":  {"dNII": -60,  "dEVE": 510},
        "Steepener":             {"dNII": -15,  "dEVE": -380},
        "Flattener":             {"dNII": 25,   "dEVE": 120},
        "Short Rate Up":         {"dNII": 45,   "dEVE": -210},
        "Short Rate Down":       {"dNII": -40,  "dEVE": 180},
    },
}

# ── Case 2: Heritage Savings Bank (Liability-Sensitive, Medium-High Risk) ──
CASE_2 = {
    "name": "Heritage Savings Bank (HSB)",
    "profile": "Liability-Sensitive · Elevated IRRBB · USA",
    "description": "A US regional bank with heavy fixed-rate mortgage book funded by short-term deposits. Significant liability-sensitive exposure and high EVE risk.",
    "currency": "USD mm",
    "total_assets": 25000,
    "tier1": 2800,
    "base_nii": 650,
    "cum_1y_gap": -2200,  # Liability-sensitive
    "nim_pct": 2.60,
    "assets": {
        "Cash & Fed Reserves":       {"amount": 1500,  "rate": 4.75, "type": "Fixed"},
        "Treasury Securities":        {"amount": 3500,  "rate": 4.25, "type": "Fixed"},
        "30-Year Fixed Mortgages":    {"amount": 12000, "rate": 5.80, "type": "Fixed"},
        "Commercial Loans (Prime)":   {"amount": 5500,  "rate": 7.50, "type": "Floating"},
        "Auto Loans (Fixed)":         {"amount": 1800,  "rate": 6.90, "type": "Fixed"},
        "Other Assets":               {"amount": 700,   "rate": 0.00, "type": "Non-earning"},
    },
    "liabilities": {
        "Savings Deposits":          {"amount": 9500,  "rate": 2.80, "type": "Floating"},
        "Money Market Accounts":     {"amount": 6500,  "rate": 3.90, "type": "Floating"},
        "CDs (1-Year)":              {"amount": 4500,  "rate": 4.60, "type": "Fixed"},
        "Fed Funds / Repo":          {"amount": 1200,  "rate": 5.25, "type": "Floating"},
        "Subordinated Debt":         {"amount": 500,   "rate": 6.50, "type": "Fixed"},
        "Shareholders' Equity":      {"amount": 2800,  "rate": 0.00, "type": "Non-interest"},
    },
    "rsa": [3500, 2500, 4000, 6500, 7500],      # Heavy long-end concentration
    "rsl": [8200, 3500, 3700, 4200, 2400],      # Front-loaded liabilities
    "df_base": [0.98, 0.96, 0.93, 0.85, 0.72],
    "df_shock_up": [0.97, 0.94, 0.90, 0.80, 0.62],
    "df_shock_down": [0.99, 0.98, 0.96, 0.90, 0.82],
    "scenarios": {
        "Parallel Up (+200)":    {"dNII": -44,   "dEVE": -380},
        "Parallel Down (-200)":  {"dNII": 44,    "dEVE": 420},
        "Steepener":             {"dNII": 15,    "dEVE": -280},
        "Flattener":             {"dNII": -35,   "dEVE": 85},
        "Short Rate Up":         {"dNII": -55,   "dEVE": -85},
        "Short Rate Down":       {"dNII": 48,    "dEVE": 92},
    },
}

# ── Case 3: Fortis European Bank (Near Threshold, High EVE Risk) ──
CASE_3 = {
    "name": "Fortis European Bank (FEB)",
    "profile": "Near-Threshold EVE Risk · Duration Mismatch · EU",
    "description": "A European universal bank with significant long-duration assets and short-duration funding. EVE sensitivity approaches the 15% Tier 1 SOT threshold.",
    "currency": "EUR mm",
    "total_assets": 80000,
    "tier1": 6500,
    "base_nii": 1800,
    "cum_1y_gap": 1200,   # Slightly asset-sensitive on NII
    "nim_pct": 2.25,
    "assets": {
        "Cash & ECB Deposits":       {"amount": 4000,  "rate": 3.75, "type": "Fixed"},
        "Sovereign Bonds (Long)":    {"amount": 18000, "rate": 3.50, "type": "Fixed"},
        "Corporate Bonds":           {"amount": 8000,  "rate": 4.80, "type": "Fixed"},
        "Mortgages (Fixed 15-30Y)":  {"amount": 28000, "rate": 4.20, "type": "Fixed"},
        "Corporate Loans":           {"amount": 15000, "rate": 5.50, "type": "Floating"},
        "Other Assets":              {"amount": 7000,  "rate": 0.00, "type": "Non-earning"},
    },
    "liabilities": {
        "Current Accounts":          {"amount": 18000, "rate": 0.50, "type": "Floating"},
        "Savings Deposits":          {"amount": 22000, "rate": 2.25, "type": "Floating"},
        "Term Deposits (< 2Y)":      {"amount": 16000, "rate": 3.40, "type": "Fixed"},
        "Wholesale Funding":         {"amount": 12000, "rate": 4.10, "type": "Floating"},
        "Covered Bonds":             {"amount": 5500,  "rate": 3.80, "type": "Fixed"},
        "Shareholders' Equity":      {"amount": 6500,  "rate": 0.00, "type": "Non-interest"},
    },
    "rsa": [8500, 6000, 9500, 18000, 26000],     # Very heavy long-end
    "rsl": [15000, 7500, 5500, 16500, 5500],     # Heavy front-end
    "df_base": [0.99, 0.97, 0.94, 0.86, 0.70],
    "df_shock_up": [0.98, 0.95, 0.91, 0.80, 0.58],
    "df_shock_down": [1.00, 0.99, 0.97, 0.92, 0.82],
    "scenarios": {
        "Parallel Up (+200)":    {"dNII": 24,    "dEVE": -920},   # ~14% of Tier 1 — near breach
        "Parallel Down (-200)":  {"dNII": -24,   "dEVE": 1050},
        "Steepener":             {"dNII": -45,   "dEVE": -780},
        "Flattener":             {"dNII": 32,    "dEVE": 150},
        "Short Rate Up":         {"dNII": -35,   "dEVE": -150},
        "Short Rate Down":       {"dNII": 40,    "dEVE": 180},
    },
}

CASES = {
    "Case 1: Bharat National Bank (BNB) — Asset-Sensitive, Mild Risk": CASE_1,
    "Case 2: Heritage Savings Bank (HSB) — Liability-Sensitive, Medium Risk": CASE_2,
    "Case 3: Fortis European Bank (FEB) — Near-Threshold EVE Risk": CASE_3,
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def plotly_theme():
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(17,34,64,0.4)",
        font=dict(family="Source Sans 3, sans-serif", color=TEXT),
        xaxis=dict(gridcolor="rgba(136,146,176,0.15)", zerolinecolor=GOLD),
        yaxis=dict(gridcolor="rgba(136,146,176,0.15)", zerolinecolor=GOLD),
    )


def section_header(title, subtitle="", icon=""):
    st.html(f"""
    <div style="user-select:none; margin-bottom:20px;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:4px;">
            <span style="font-size:1.8rem;">{icon}</span>
            <h2 style="margin:0; font-family:'Playfair Display',serif; font-weight:700;
                color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:1.7rem; letter-spacing:-0.5px;">{title}</h2>
        </div>
        {"<p style='margin:0 0 0 44px; color:" + MUTED + "; -webkit-text-fill-color:" + MUTED + "; font-size:0.95rem;'>" + subtitle + "</p>" if subtitle else ""}
        <div style="height:2px; background:linear-gradient(90deg, {GOLD}, transparent); margin-top:8px;"></div>
    </div>
    """)


def metric_card(label, value, threshold="", status="PASS", risk="Low"):
    sc = GREEN if status == "PASS" else (RED if status == "BREACH" else (ORANGE if status == "WATCH" else MUTED))
    rc_map = {"Low": GREEN, "Medium": ORANGE, "High": RED, "—": MUTED}
    ri_map = {"Low": "✅", "Medium": "⚠️", "High": "❌", "—": ""}
    rc = rc_map.get(risk, MUTED)
    ri = ri_map.get(risk, "")
    st.html(f"""
    <div style="user-select:none; background:{CARD_BG}; border:1px solid rgba(255,215,0,0.15);
        border-radius:12px; padding:18px; text-align:center; min-height:145px;
        display:flex; flex-direction:column; justify-content:center;">
        <div style="color:{MUTED}; -webkit-text-fill-color:{MUTED}; font-size:0.78rem; font-weight:600;
            text-transform:uppercase; letter-spacing:0.8px; margin-bottom:6px;">{label}</div>
        <div style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:'Playfair Display',serif;
            font-size:1.7rem; font-weight:700; margin-bottom:4px;">{value}</div>
        <div style="color:{MUTED}; -webkit-text-fill-color:{MUTED}; font-size:0.72rem; margin-bottom:6px;">
            Threshold: {threshold}</div>
        <div style="display:flex; justify-content:center; gap:10px; font-size:0.78rem;">
            <span style="color:{sc}; -webkit-text-fill-color:{sc}; font-weight:700;">{status}</span>
            <span style="color:{rc}; -webkit-text-fill-color:{rc};">{ri} {risk}</span>
        </div>
    </div>
    """)


def info_card(title, content, border_color=GOLD):
    st.html(f"""
    <div style="user-select:none; background:{CARD_BG}; border-left:4px solid {border_color};
        border-radius:0 8px 8px 0; padding:16px 20px; margin:10px 0;">
        <div style="color:{border_color}; -webkit-text-fill-color:{border_color};
            font-weight:700; font-size:1rem; margin-bottom:8px; font-family:'Playfair Display',serif;">{title}</div>
        <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.9rem; line-height:1.6;">{content}</div>
    </div>
    """)


def compute_gaps(rsa, rsl):
    periodic = [a - l for a, l in zip(rsa, rsl)]
    cumulative = list(np.cumsum(periodic))
    ratio = [a / l if l != 0 else 0 for a, l in zip(rsa, rsl)]
    return periodic, cumulative, ratio


def compute_eve(gaps, discount_factors):
    return sum(g * df for g, df in zip(gaps, discount_factors))


def classify_status(value, threshold):
    abs_pct = abs(value)
    if abs_pct >= threshold:
        return "BREACH", "High"
    if abs_pct >= threshold * 0.67:
        return "WATCH", "Medium"
    return "PASS", "Low"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SIDEBAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

with st.sidebar:
    st.html(f"""
    <div style="user-select:none; text-align:center; padding:10px 0 15px 0;">
        <div style="font-size:2.2rem; margin-bottom:4px;">🏔️</div>
        <div style="font-family:'Playfair Display',serif; font-weight:700; font-size:1.2rem;
            color:{GOLD}; -webkit-text-fill-color:{GOLD};">THE MOUNTAIN PATH</div>
        <div style="color:{LIGHT_BLUE}; -webkit-text-fill-color:{LIGHT_BLUE}; font-size:0.75rem;
            letter-spacing:2px; text-transform:uppercase; margin-top:2px;">Academy — World of Finance</div>
        <div style="height:2px; background:linear-gradient(90deg, transparent, {GOLD}, transparent);
            margin:12px 20px 0 20px;"></div>
    </div>
    """)

    page = st.radio(
        "📑 Navigation",
        [
            "📖 IRRBB Overview",
            "🎯 Four Types of IRRBB",
            "📊 EVE & NII Fundamentals",
            "🏦 Case Studies (3 Banks)",
            "🎛️ Rate Shock Simulator",
            "📚 Knowledge Base",
        ],
        index=0,
    )

    st.html(f"""
    <div style="user-select:none; margin-top:40px; padding:15px 10px; text-align:center;
        border-top:1px solid rgba(255,215,0,0.2);">
        <div style="color:{MUTED}; -webkit-text-fill-color:{MUTED}; font-size:0.72rem; margin-bottom:4px;">
            Prof. V. Ravichandran</div>
        <div style="color:{MUTED}; -webkit-text-fill-color:{MUTED}; font-size:0.65rem; margin-bottom:8px;">
            NMIMS Bangalore | BITS Pilani<br>RV University Bangalore | GIM</div>
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
            <a href="https://www.linkedin.com/in/trichyravis" target="_blank"
                style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:0.72rem; text-decoration:none;">LinkedIn</a>
            <a href="https://github.com/trichyravis" target="_blank"
                style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:0.72rem; text-decoration:none;">GitHub</a>
            <a href="https://themountainpathacademy.com" target="_blank"
                style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:0.72rem; text-decoration:none;">themountainpathacademy.com</a>
        </div>
    </div>
    """)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HEADER BANNER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.html(f"""
<div style="user-select:none; background:linear-gradient(135deg, {BLUE}, {MID_BLUE}); border-radius:16px;
    padding:25px 35px; margin-bottom:25px; border:1px solid rgba(255,215,0,0.25);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px;">
        <div>
            <div style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:'Playfair Display',serif;
                font-size:1.8rem; font-weight:700; letter-spacing:-0.5px;">
                Interest Rate Risk in the Banking Book</div>
            <div style="color:{LIGHT_BLUE}; -webkit-text-fill-color:{LIGHT_BLUE}; font-size:0.95rem; margin-top:4px;">
                Comprehensive IRRBB Learning · Basel d368 · Three Case Studies</div>
        </div>
        <div style="text-align:right;">
            <div style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:'Playfair Display',serif;
                font-size:1.8rem; font-weight:800;">IRRBB</div>
            <div style="color:{LIGHT_BLUE}; -webkit-text-fill-color:{LIGHT_BLUE}; font-size:0.8rem;">Pillar 2 Risk</div>
        </div>
    </div>
</div>
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE 1: IRRBB OVERVIEW
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if page == "📖 IRRBB Overview":
    section_header("What is IRRBB?", "Definition, importance, and its critical role in ALM", "📖")

    info_card("📘 Definition — Interest Rate Risk in the Banking Book",
        "<b>IRRBB</b> is the risk that changes in market interest rates reduce a bank's <b>earnings</b> "
        "(Net Interest Income) or <b>economic value</b> (Economic Value of Equity) from its non-trading "
        "positions. The banking book comprises loans, deposits, bonds held to maturity, and funding instruments — "
        "the bank's core business. IRRBB is a <b>Pillar 2 risk</b> under Basel. Banks must measure it, "
        "manage it, and hold capital against it.", MID_BLUE)

    st.html(f"<div style='height:15px;'></div>")
    st.html(f"""<h3 style='color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:Playfair Display,serif;'>
        IRRBB as a Critical Pillar of ALM</h3>""")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.html(f"""
        <div style="background:{CARD_BG}; border-left:4px solid {RED}; border-radius:0 8px 8px 0;
            padding:16px; min-height:140px;">
            <div style="color:{RED}; -webkit-text-fill-color:{RED}; font-weight:700; font-size:1rem;
                margin-bottom:6px;">Liquidity Risk</div>
            <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.85rem; line-height:1.5;">
                Funding and cash flow risk — can the bank meet its obligations as they fall due?
            </div>
        </div>
        """)
    with c2:
        st.html(f"""
        <div style="background:{CARD_BG}; border-left:4px solid {PURPLE}; border-radius:0 8px 8px 0;
            padding:16px; min-height:140px;">
            <div style="color:{PURPLE}; -webkit-text-fill-color:{PURPLE}; font-weight:700; font-size:1rem;
                margin-bottom:6px;">⭐ Interest Rate Risk (IRRBB)</div>
            <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.85rem; line-height:1.5;">
                How do NII and EVE change when market rates move? The focus of this application.
            </div>
        </div>
        """)
    with c3:
        st.html(f"""
        <div style="background:{CARD_BG}; border-left:4px solid {GREEN}; border-radius:0 8px 8px 0;
            padding:16px; min-height:140px;">
            <div style="color:{GREEN}; -webkit-text-fill-color:{GREEN}; font-weight:700; font-size:1rem;
                margin-bottom:6px;">Capital Adequacy</div>
            <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.85rem; line-height:1.5;">
                EVE impact and solvency — does the bank have enough capital to absorb rate shocks?
            </div>
        </div>
        """)

    st.html(f"<div style='height:20px;'></div>")
    st.html(f"""<h3 style='color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:Playfair Display,serif;'>
        Regulatory Framework</h3>""")

    reg_df = pd.DataFrame([
        {"Framework": "BCBS d368 (2016)", "Key Requirements": "6 prescribed rate shock scenarios; dual EVE & NII measurement; Pillar 2 capital treatment", "Reference": "d368"},
        {"Framework": "Basel SRP/31", "Key Requirements": "IRRBB principles; board oversight; risk appetite; measurement systems", "Reference": "SRP/31"},
        {"Framework": "Basel SRP/98", "Key Requirements": "Application guidance; behavioural assumptions; commercial margin treatment", "Reference": "SRP/98"},
        {"Framework": "Basel DIS/70", "Key Requirements": "IRRBB disclosure: ΔEVE and ΔNII by scenario", "Reference": "DIS/70"},
        {"Framework": "EBA GL/2022/14", "Key Requirements": "Supervisory Outlier Tests: 15% EVE and 2.5% NII of Tier 1 capital", "Reference": "EBA"},
        {"Framework": "RBI (India)", "Key Requirements": "ALM/IRRBB reporting; Structural Liquidity Statement; duration gap limits; ALCO", "Reference": "RBI"},
        {"Framework": "OCC (USA)", "Key Requirements": "Interest rate risk management handbook; earnings-at-risk framework", "Reference": "OCC"},
    ])
    st.dataframe(reg_df, use_container_width=True, hide_index=True)

    info_card("🎯 Why This Matters for Your Career",
        "Finance students who aspire to senior roles in bank treasury management <b>must</b> understand and master "
        "IRRBB. This is the language that ALCO committees speak, that regulators examine, and that bank "
        "treasurers use to make decisions worth billions every day. There is no shortcut.",
        GOLD)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE 2: FOUR TYPES OF IRRBB
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

elif page == "🎯 Four Types of IRRBB":
    section_header("The Four Types of IRRBB",
        "Each type requires different measurement and management approaches", "🎯")

    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Repricing Risk", "2. Yield Curve Risk", "3. Basis Risk", "4. Optionality Risk"
    ])

    with tab1:
        info_card("📘 Definition — Repricing Risk",
            "Repricing risk arises when assets and liabilities reset their interest rates at "
            "<b>different times</b>. A change in market rates affects them unevenly. It is the most "
            "basic IRRBB exposure — a 'gap risk' problem between the timing of rate-sensitive cash "
            "inflows and outflows.", RED)

        st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>How to Measure</h4>""")
        st.markdown("""
        1. Identify all rate-sensitive assets, liabilities, and off-balance-sheet items
        2. Group by repricing date or maturity bucket (8 RBI/Basel time buckets)
        3. Compare RSA with RSL in each bucket: **Gap = RSA − RSL**
        4. Stress test NII impact: **ΔNII = Cumulative Gap × ΔRate**
        """)

        info_card("💡 Worked Illustration",
            "A bank holds a <b>5-year fixed loan at 8.75%</b> funded by a <b>1-year deposit at 6.50%</b>. "
            "After one year, the deposit reprices. If rates rise 100bps, the deposit cost jumps to 7.50% "
            "while the loan stays at 8.75%. Net spread compresses from <b>225bps</b> to <b>125bps</b> — "
            "a 44% margin erosion purely from repricing mismatch.", GREEN)

    with tab2:
        info_card("📘 Definition — Yield Curve Risk",
            "Yield curve risk arises when rates at different maturities move by <b>different amounts</b> — "
            "not in a flat parallel shift. The curve can steepen, flatten, twist, or invert, affecting "
            "short-term and long-term positions differently.", PURPLE)

        # Yield curve visual
        maturities = [0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30]
        base_curve = [4.0, 4.2, 4.5, 4.8, 5.0, 5.2, 5.3, 5.4, 5.5, 5.6]
        steepener = [3.5, 3.6, 3.8, 4.3, 4.9, 5.7, 6.2, 6.5, 6.8, 7.0]
        flattener = [4.8, 4.9, 5.0, 5.0, 5.0, 4.9, 4.8, 4.7, 4.5, 4.4]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=maturities, y=base_curve, mode="lines+markers",
            name="Base Curve", line=dict(color=GOLD, width=3), marker=dict(size=6)))
        fig.add_trace(go.Scatter(x=maturities, y=steepener, mode="lines+markers",
            name="Steepener", line=dict(color=RED, width=2, dash="dash")))
        fig.add_trace(go.Scatter(x=maturities, y=flattener, mode="lines+markers",
            name="Flattener", line=dict(color=GREEN, width=2, dash="dot")))
        fig.update_layout(**plotly_theme(),
            title=dict(text="Yield Curve Scenarios", font=dict(color=GOLD, size=15)),
            xaxis_title="Maturity (Years)", yaxis_title="Rate (%)",
            height=380, margin=dict(l=50, r=20, t=50, b=50),
            legend=dict(orientation="h", yanchor="bottom", y=-0.25))
        st.plotly_chart(fig, use_container_width=True, key="yc_curves")

        info_card("💡 Worked Illustration",
            "A bank hedges a 10-year bond with 2-year funding. If the curve <i>steepens</i> "
            "(long rates +150bps, short rates +50bps), the hedge is far less effective. "
            "This is why Basel requires testing steepeners and flatteners, not just parallel shifts.", GREEN)

    with tab3:
        info_card("📘 Definition — Basis Risk",
            "Basis risk occurs when assets and liabilities are tied to <b>different benchmarks</b> "
            "(e.g., SOFR vs. Prime, MCLR vs. T-bill), and the spread between those benchmarks changes "
            "unpredictably.", ORANGE)

        info_card("💡 Worked Illustration",
            "A bank funds a loan linked to <b>SOFR + 200bps</b> with deposits tracking <b>Prime rate</b>. "
            "If SOFR rises 100bps but Prime rises 150bps, funding cost increases <i>faster</i> than loan "
            "income despite both being 'floating rate'. The spread between benchmarks creates "
            "unexpected margin compression.", GREEN)

    with tab4:
        info_card("📘 Definition — Optionality Risk",
            "Optionality risk comes from <b>embedded options</b> that customers hold: prepayment options "
            "on loans and early withdrawal options on deposits. When rates change, customers exercise "
            "these options in ways that are <i>systematically unfavourable</i> to the bank.", TEAL)

        c1, c2 = st.columns(2)
        with c1:
            st.html(f"""
            <div style="background:{CARD_BG}; border-left:4px solid {RED}; border-radius:0 8px 8px 0;
                padding:16px; min-height:160px;">
                <div style="color:{RED}; -webkit-text-fill-color:{RED}; font-weight:700; font-size:1rem;
                    margin-bottom:8px;">⬇️ When Rates Fall</div>
                <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.88rem; line-height:1.6;">
                    • Borrowers refinance mortgages early<br>
                    • Bank loses high-yielding assets<br>
                    • Must reinvest at lower rates<br>
                    • Depositors do NOT withdraw<br>
                    • Funding cost stays elevated
                </div>
            </div>
            """)
        with c2:
            st.html(f"""
            <div style="background:{CARD_BG}; border-left:4px solid {ORANGE}; border-radius:0 8px 8px 0;
                padding:16px; min-height:160px;">
                <div style="color:{ORANGE}; -webkit-text-fill-color:{ORANGE}; font-weight:700; font-size:1rem;
                    margin-bottom:8px;">⬆️ When Rates Rise</div>
                <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.88rem; line-height:1.6;">
                    • Borrowers do NOT prepay<br>
                    • Bank stuck with low-rate loans<br>
                    • Depositors withdraw early<br>
                    • Seeking higher yields elsewhere<br>
                    • Bank loses stable funding
                </div>
            </div>
            """)

        info_card("⚠️ The Asymmetry Problem",
            "In <b>both directions</b>, the embedded option works against the bank. This asymmetry "
            "makes optionality risk particularly dangerous and difficult to hedge.", GOLD)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE 3: EVE & NII FUNDAMENTALS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

elif page == "📊 EVE & NII Fundamentals":
    section_header("EVE and NII — The Two Core Metrics",
        "Both mandatory under Basel IRRBB (BCBS d368)", "📊")

    tab1, tab2, tab3 = st.tabs(["📗 NII (Earnings)", "📘 EVE (Economic Value)", "🔄 Side-by-Side"])

    with tab1:
        info_card("📘 Net Interest Income (NII)",
            "<b>NII</b> is the difference between interest <b>earned</b> on assets and interest <b>paid</b> "
            "on liabilities. It is the single largest revenue line for most banks (60–80% of operating income).<br><br>"
            "<b>NII = Interest Income − Interest Expense</b><br><br>"
            "ΔNII measures how this income changes under a rate shock over a <b>12-month horizon</b>.",
            MID_BLUE)

        c1, c2 = st.columns(2)
        with c1:
            st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>Why NII Matters</h4>""")
            st.markdown("""
            - **Primary profitability driver** — compression directly hits the P&L
            - **Short-term view** — 12-month earnings impact
            - Used by **ALCO** for tactical decisions: deposit pricing, loan origination, hedging
            - **EBA threshold:** |ΔNII| > 2.5% of Tier 1 capital triggers action
            """)

        with c2:
            st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>What Drives ΔNII</h4>""")
            st.markdown("""
            - **Repricing timing:** How quickly do yields and costs adjust?
            - **Deposit betas:** % of market rate change passed to deposits
            - **Funding mix:** Fixed vs. floating proportion
            - **Volume effects:** Balance sheet changes with rates
            """)

        info_card("💡 Asset-Sensitive vs Liability-Sensitive",
            "<b>Asset-Sensitive (RSA > RSL):</b> Rates rise → NII increases. Rates fall → NII decreases.<br>"
            "<b>Liability-Sensitive (RSL > RSA):</b> Rates rise → NII decreases. Rates fall → NII increases.<br>"
            "<b>Gap-Neutral:</b> NII immunised against parallel rate shifts.",
            GOLD)

    with tab2:
        info_card("📘 Economic Value of Equity (EVE)",
            "<b>EVE</b> is the present value of all future net cash flows from assets and liabilities. "
            "It represents the bank's <b>true economic net worth</b>.<br><br>"
            "<b>EVE = PV(Assets) − PV(Liabilities)</b><br><br>"
            "ΔEVE measures how this value changes when the yield curve shifts. Unlike NII, EVE captures "
            "the <b>full lifetime impact</b>, not just 12 months.",
            PURPLE)

        c1, c2 = st.columns(2)
        with c1:
            st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>Why EVE Matters</h4>""")
            st.markdown("""
            - Captures **long-term** exposure that NII misses
            - Preferred by **regulators** — reflects true solvency risk
            - **Basel/EBA threshold:** |ΔEVE| > 15% of Tier 1 → outlier requiring action
            - Driven primarily by **duration** — longer positions more sensitive
            """)

        with c2:
            st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>What Drives ΔEVE</h4>""")
            st.markdown("""
            - **Duration mismatch:** Asset vs. liability durations
            - **Discount rate changes:** Higher rates → lower PV
            - **Optionality:** Prepayments/withdrawals change duration
            - **NMD behavioural modelling:** Huge impact on liability duration
            """)

        info_card("💡 Example: 30-Year Mortgage Funded by 5-Year Deposit",
            "A 30-year fixed mortgage has minimal 1-year NII impact (rate locked) but <b>enormous EVE "
            "sensitivity</b> — its very high duration means any rate rise causes a large PV decline. "
            "The 5-year deposit's PV barely moves in comparison. EVE drops sharply. This is why EVE "
            "captures risks NII completely misses.",
            GOLD)

    with tab3:
        comp_df = pd.DataFrame([
            {"Dimension": "Main question", "NII (Earnings)": "What happens to near-term earnings?", "EVE (Economic Value)": "What happens to economic net worth?"},
            {"Dimension": "Horizon", "NII (Earnings)": "12 months (short-term)", "EVE (Economic Value)": "Full lifetime / run-off (long-term)"},
            {"Dimension": "Primary drivers", "NII (Earnings)": "Repricing timing, deposit betas, funding mix", "EVE (Economic Value)": "Duration, discount rates, optionality"},
            {"Dimension": "Perspective", "NII (Earnings)": "P&L / income statement", "EVE (Economic Value)": "Balance sheet / solvency"},
            {"Dimension": "Used by", "NII (Earnings)": "ALCO for tactical decisions", "EVE (Economic Value)": "Regulators, capital planning"},
            {"Dimension": "SOT threshold", "NII (Earnings)": ">2.5% of Tier 1 (EBA)", "EVE (Economic Value)": ">15% of Tier 1 (Basel/EBA)"},
            {"Dimension": "Captures", "NII (Earnings)": "Cash flow timing in next 12 months", "EVE (Economic Value)": "PV of all future cash flows"},
            {"Dimension": "Limitation", "NII (Earnings)": "Misses long-dated exposures", "EVE (Economic Value)": "Complex; requires DCF modelling"},
        ])
        st.dataframe(comp_df, use_container_width=True, hide_index=True)

        info_card("⚠️ A Bank Can Have Low NII Risk But High EVE Risk",
            "A bank with well-matched short-term positions (low NII risk) but large long-dated mismatches "
            "(e.g., 20-year fixed mortgages funded by 5-year deposits) may appear safe on an NII basis "
            "but face <b>significant EVE risk</b>. This is why <b>Basel mandates both metrics</b> — "
            "one alone gives an incomplete picture.", ORANGE)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE 4: CASE STUDIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

elif page == "🏦 Case Studies (3 Banks)":
    section_header("Case Studies — Three Distinct Bank Profiles",
        "Each bank illustrates a different IRRBB profile and regulatory outcome", "🏦")

    case_name = st.selectbox(
        "Select Case Study",
        list(CASES.keys()),
        key="case_selector"
    )
    case = CASES[case_name]

    # Case profile card
    profile_color = GREEN if "Mild" in case["profile"] else (ORANGE if "Medium" in case["profile"] else RED)
    st.html(f"""
    <div style="user-select:none; background:{CARD_BG}; border-left:5px solid {profile_color};
        border-radius:0 10px 10px 0; padding:18px 24px; margin-bottom:20px;">
        <div style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:'Playfair Display',serif;
            font-size:1.4rem; font-weight:700;">{case["name"]}</div>
        <div style="color:{profile_color}; -webkit-text-fill-color:{profile_color}; font-size:0.9rem;
            font-weight:600; margin-top:2px;">{case["profile"]}</div>
        <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.92rem; line-height:1.6;
            margin-top:8px;">{case["description"]}</div>
    </div>
    """)

    # Key metrics row
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Assets", f"{case['total_assets']:,} {case['currency'].split()[0]}")
    with c2:
        st.metric("Tier 1 Capital", f"{case['tier1']:,} {case['currency'].split()[0]}")
    with c3:
        st.metric("Base NII", f"{case['base_nii']:,} {case['currency'].split()[0]}")
    with c4:
        st.metric("NIM", f"{case['nim_pct']:.2f}%")

    # Tabs for each dimension
    t1, t2, t3, t4, t5 = st.tabs([
        "📋 Balance Sheet", "📊 Rate Sensitivity Gap", "💰 NII Impact",
        "📈 EVE Analysis", "🎯 Six-Scenario Results"
    ])

    with t1:
        c1, c2 = st.columns(2)
        with c1:
            st.html(f"<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>Assets</h4>")
            adf = pd.DataFrame([
                {"Category": k, "Amount": f"{v['amount']:,}", "Rate": f"{v['rate']:.2f}%", "Type": v["type"]}
                for k, v in case["assets"].items()
            ])
            st.dataframe(adf, use_container_width=True, hide_index=True)

            asset_labels = list(case["assets"].keys())
            asset_values = [v["amount"] for v in case["assets"].values()]
            fig_a = go.Figure(go.Pie(labels=asset_labels, values=asset_values, hole=0.5,
                marker=dict(colors=[MID_BLUE, TEAL, GREEN, LIGHT_BLUE, MUTED, ORANGE][:len(asset_labels)],
                    line=dict(color=BLUE, width=2)),
                textfont=dict(size=10, color=TEXT), textinfo="percent"))
            fig_a.update_layout(**plotly_theme(),
                title=dict(text=f"Asset Mix", font=dict(color=GOLD, size=14)),
                height=320, margin=dict(l=20, r=20, t=40, b=20), showlegend=True,
                legend=dict(orientation="v", font=dict(size=9)))
            st.plotly_chart(fig_a, use_container_width=True, key=f"pie_a_{case_name[:10]}")

        with c2:
            st.html(f"<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>Liabilities & Equity</h4>")
            ldf = pd.DataFrame([
                {"Category": k, "Amount": f"{v['amount']:,}", "Rate": f"{v['rate']:.2f}%", "Type": v["type"]}
                for k, v in case["liabilities"].items()
            ])
            st.dataframe(ldf, use_container_width=True, hide_index=True)

            liab_labels = list(case["liabilities"].keys())
            liab_values = [v["amount"] for v in case["liabilities"].values()]
            fig_l = go.Figure(go.Pie(labels=liab_labels, values=liab_values, hole=0.5,
                marker=dict(colors=[RED, ORANGE, PURPLE, MUTED, GOLD, LIGHT_BLUE][:len(liab_labels)],
                    line=dict(color=BLUE, width=2)),
                textfont=dict(size=10, color=TEXT), textinfo="percent"))
            fig_l.update_layout(**plotly_theme(),
                title=dict(text=f"Liability Mix", font=dict(color=GOLD, size=14)),
                height=320, margin=dict(l=20, r=20, t=40, b=20), showlegend=True,
                legend=dict(orientation="v", font=dict(size=9)))
            st.plotly_chart(fig_l, use_container_width=True, key=f"pie_l_{case_name[:10]}")

    with t2:
        periodic, cumulative, ratio = compute_gaps(case["rsa"], case["rsl"])

        # Gap table
        gap_df = pd.DataFrame({
            "Bucket": BUCKETS,
            "RSA": [f"{v:,}" for v in case["rsa"]],
            "RSL": [f"{v:,}" for v in case["rsl"]],
            "Periodic Gap": [f"{v:+,}" for v in periodic],
            "Cumulative Gap": [f"{v:+,}" for v in cumulative],
            "RSA/RSL Ratio": [f"{r:.2f}x" for r in ratio],
        })
        st.dataframe(gap_df, use_container_width=True, hide_index=True)

        # Gap chart
        fig = go.Figure()
        fig.add_trace(go.Bar(x=BUCKETS, y=periodic, name="Periodic Gap",
            marker=dict(color=[GREEN if v >= 0 else RED for v in periodic], opacity=0.8),
            text=[f"{v:+,}" for v in periodic], textposition="outside", textfont=dict(size=10)))
        fig.add_trace(go.Scatter(x=BUCKETS, y=cumulative, name="Cumulative Gap", mode="lines+markers",
            line=dict(color=GOLD, width=3), marker=dict(size=10, color=GOLD)))
        fig.add_hline(y=0, line_dash="solid", line_color=MUTED, line_width=1)
        fig.update_layout(**plotly_theme(),
            title=dict(text=f"Rate Sensitivity Gap — {case['name']}", font=dict(color=GOLD, size=15)),
            height=400, margin=dict(l=50, r=20, t=50, b=60),
            yaxis_title=f"Gap ({case['currency']})",
            legend=dict(orientation="h", yanchor="bottom", y=-0.25))
        st.plotly_chart(fig, use_container_width=True, key=f"gap_{case_name[:10]}")

        sensitivity = "Asset-Sensitive" if case["cum_1y_gap"] > 0 else ("Liability-Sensitive" if case["cum_1y_gap"] < 0 else "Gap-Neutral")
        sens_color = GREEN if case["cum_1y_gap"] > 0 else RED

        info_card(f"📌 Cumulative 1-Year Gap: {case['cum_1y_gap']:+,} {case['currency']}",
            f"This bank is <b style='color:{sens_color}; -webkit-text-fill-color:{sens_color};'>"
            f"{sensitivity}</b>. " +
            ("Rising rates will <b>increase</b> NII, falling rates will <b>decrease</b> NII."
             if case["cum_1y_gap"] > 0 else
             "Rising rates will <b>decrease</b> NII, falling rates will <b>increase</b> NII."
             if case["cum_1y_gap"] < 0 else
             "NII is broadly immunised against parallel rate shifts."),
            sens_color)

    with t3:
        st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>
            NII Impact: ΔNII = Cumulative 1Y Gap × ΔRate</h4>""")

        nii_thresh = case["tier1"] * 0.025
        nii_rows = []
        for s, vals in case["scenarios"].items():
            pct_t1 = abs(vals["dNII"]) / case["tier1"] * 100
            status, risk = classify_status(pct_t1, 2.5)
            nii_rows.append({
                "Scenario": s,
                "ΔNII": f"{vals['dNII']:+,}",
                "% Base NII": f"{vals['dNII']/case['base_nii']*100:+.2f}%",
                "% Tier 1": f"{pct_t1:.2f}%",
                "Status": status,
            })
        nii_df = pd.DataFrame(nii_rows)
        st.dataframe(nii_df, use_container_width=True, hide_index=True)

        # Bar chart of NII impact
        scenarios_list = list(case["scenarios"].keys())
        nii_vals = [case["scenarios"][s]["dNII"] for s in scenarios_list]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=scenarios_list, y=nii_vals,
            marker=dict(color=[GREEN if v >= 0 else RED for v in nii_vals], opacity=0.8),
            text=[f"{v:+,}" for v in nii_vals], textposition="outside"))
        fig.add_hline(y=nii_thresh, line_dash="dash", line_color=RED, line_width=1.5,
            annotation_text=f"EBA NII SOT: +2.5% T1 = {nii_thresh:,.0f}",
            annotation_font=dict(color=RED, size=9))
        fig.add_hline(y=-nii_thresh, line_dash="dash", line_color=RED, line_width=1.5,
            annotation_text=f"EBA NII SOT: -2.5% T1",
            annotation_font=dict(color=RED, size=9))
        fig.add_hline(y=0, line_dash="solid", line_color=MUTED, line_width=1)
        fig.update_layout(**plotly_theme(),
            title=dict(text="NII Impact by Scenario", font=dict(color=GOLD, size=14)),
            height=400, margin=dict(l=50, r=20, t=50, b=80),
            yaxis_title=f"ΔNII ({case['currency']})")
        fig.update_xaxes(tickangle=-25)
        st.plotly_chart(fig, use_container_width=True, key=f"nii_{case_name[:10]}")

    with t4:
        periodic, cumulative, _ = compute_gaps(case["rsa"], case["rsl"])
        base_eve = compute_eve(periodic, case["df_base"])
        up_eve = compute_eve(periodic, case["df_shock_up"])
        down_eve = compute_eve(periodic, case["df_shock_down"])

        d_eve_up = up_eve - base_eve
        d_eve_down = down_eve - base_eve
        pct_t1_up = abs(d_eve_up) / case["tier1"] * 100
        pct_t1_down = abs(d_eve_down) / case["tier1"] * 100

        eve_df = pd.DataFrame({
            "Bucket": BUCKETS,
            "Periodic Gap": [f"{v:+,}" for v in periodic],
            "Base DF": [f"{d:.3f}" for d in case["df_base"]],
            "Base PV": [f"{g*d:+,.0f}" for g, d in zip(periodic, case["df_base"])],
            "+200bps DF": [f"{d:.3f}" for d in case["df_shock_up"]],
            "Shocked PV": [f"{g*d:+,.0f}" for g, d in zip(periodic, case["df_shock_up"])],
        })
        st.dataframe(eve_df, use_container_width=True, hide_index=True)

        c1, c2, c3, c4 = st.columns(4)
        with c1: st.metric("Base EVE", f"{base_eve:+,.0f}")
        with c2: st.metric("EVE @ +200bps", f"{up_eve:+,.0f}", delta=f"{d_eve_up:+,.0f}")
        with c3: st.metric("ΔEVE / Tier 1", f"{pct_t1_up:.2f}%",
            delta=f"{'BREACH' if pct_t1_up > 15 else ('WATCH' if pct_t1_up > 10 else 'PASS')}")
        with c4: st.metric("EBA EVE Threshold", "15.0%")

        info_card("📘 EVE Calculation Methodology",
            f"<b>Base EVE</b> = Σ (Periodic Gap × Base Discount Factor) = <b>{base_eve:+,.0f}</b><br>"
            f"<b>Shocked EVE (+200bps)</b> = Σ (Gap × Shocked DF) = <b>{up_eve:+,.0f}</b><br>"
            f"<b>ΔEVE</b> = Shocked − Base = <b>{d_eve_up:+,.0f}</b> "
            f"({pct_t1_up:.2f}% of Tier 1)<br><br>"
            f"The {'asset' if case['cum_1y_gap'] > 0 else 'liability'}-sensitive gap structure means "
            f"that rising rates {'decrease' if case['cum_1y_gap'] > 0 else 'may increase'} EVE because "
            f"{'longer-duration assets lose more value than liabilities.' if case['cum_1y_gap'] > 0 else 'shorter-duration liabilities lose less than assets.'}",
            GOLD)

    with t5:
        st.html(f"""<h4 style='color:{GOLD}; -webkit-text-fill-color:{GOLD};'>
            All Six Basel Scenarios — ΔNII and ΔEVE</h4>""")

        summary_rows = []
        worst_nii = 0
        worst_eve = 0
        for s, vals in case["scenarios"].items():
            nii_pct = abs(vals["dNII"]) / case["tier1"] * 100
            eve_pct = abs(vals["dEVE"]) / case["tier1"] * 100
            worst_nii = max(worst_nii, nii_pct)
            worst_eve = max(worst_eve, eve_pct)
            nii_stat = "BREACH" if nii_pct > 2.5 else ("WATCH" if nii_pct > 1.5 else "PASS")
            eve_stat = "BREACH" if eve_pct > 15 else ("WATCH" if eve_pct > 10 else "PASS")
            overall = "BREACH" if "BREACH" in (nii_stat, eve_stat) else ("WATCH" if "WATCH" in (nii_stat, eve_stat) else "PASS")
            summary_rows.append({
                "Scenario": s,
                "ΔNII": f"{vals['dNII']:+,}",
                "ΔNII/T1": f"{nii_pct:.2f}%",
                "ΔEVE": f"{vals['dEVE']:+,}",
                "ΔEVE/T1": f"{eve_pct:.2f}%",
                "Status": overall,
            })
        summary_df = pd.DataFrame(summary_rows)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

        # Combined visualization
        scenarios_list = list(case["scenarios"].keys())
        nii_vals = [case["scenarios"][s]["dNII"] for s in scenarios_list]
        eve_vals = [case["scenarios"][s]["dEVE"] for s in scenarios_list]

        fig = make_subplots(rows=1, cols=2, subplot_titles=("ΔNII by Scenario", "ΔEVE by Scenario"))
        fig.add_trace(go.Bar(x=scenarios_list, y=nii_vals,
            marker=dict(color=[GREEN if v >= 0 else RED for v in nii_vals], opacity=0.8),
            name="ΔNII", showlegend=False), row=1, col=1)
        fig.add_trace(go.Bar(x=scenarios_list, y=eve_vals,
            marker=dict(color=[GREEN if v >= 0 else RED for v in eve_vals], opacity=0.8),
            name="ΔEVE", showlegend=False), row=1, col=2)
        fig.update_layout(**plotly_theme(),
            height=400, margin=dict(l=50, r=20, t=60, b=80),
            title=dict(text=f"Six-Scenario Impact — {case['name']}", font=dict(color=GOLD, size=14)))
        fig.update_xaxes(tickangle=-35, row=1, col=1)
        fig.update_xaxes(tickangle=-35, row=1, col=2)
        st.plotly_chart(fig, use_container_width=True, key=f"six_{case_name[:10]}")

        # Summary
        overall_color = GREEN if worst_nii < 1.5 and worst_eve < 10 else (
            ORANGE if worst_nii < 2.5 and worst_eve < 15 else RED)
        overall_label = "✅ ALL PASS" if worst_nii < 1.5 and worst_eve < 10 else (
            "⚠️ MONITOR" if worst_nii < 2.5 and worst_eve < 15 else "❌ BREACH")

        info_card(f"📋 Worst-Case Assessment: {overall_label}",
            f"<b>Worst NII impact:</b> {worst_nii:.2f}% of Tier 1 (threshold 2.5%)<br>"
            f"<b>Worst EVE impact:</b> {worst_eve:.2f}% of Tier 1 (threshold 15%)<br><br>"
            f"<b>Interpretation:</b> " +
            ("All scenarios within comfortable margins — IRRBB position is well-managed." if overall_color == GREEN else
             "Approaching regulatory thresholds — enhanced monitoring recommended." if overall_color == ORANGE else
             "Regulatory threshold breached — corrective action required (hedging, rebalancing, or capital add-on)."),
            overall_color)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE 5: RATE SHOCK SIMULATOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

elif page == "🎛️ Rate Shock Simulator":
    section_header("Interactive Rate Shock Simulator",
        "Select a bank case and apply custom rate shocks to see NII and EVE impacts", "🎛️")

    c1, c2 = st.columns([2, 1])
    with c1:
        case_name = st.selectbox("Select Bank Case", list(CASES.keys()), key="sim_case")
    with c2:
        rate_shock = st.slider("Rate Shock (bps)", -300, 300, 100, step=25)

    case = CASES[case_name]

    # Dynamic NII impact
    d_nii = case["cum_1y_gap"] * (rate_shock / 10000)
    new_nii = case["base_nii"] + d_nii
    pct_base = d_nii / case["base_nii"] * 100 if case["base_nii"] != 0 else 0
    pct_t1 = d_nii / case["tier1"] * 100

    # Dynamic EVE impact (linear interpolation between shocks)
    periodic, _, _ = compute_gaps(case["rsa"], case["rsl"])
    base_eve = compute_eve(periodic, case["df_base"])
    # Interpolate discount factors for the given shock
    shock_fraction = rate_shock / 200  # scale by +200bps reference
    if shock_fraction > 0:
        shocked_dfs = [b + (u - b) * min(shock_fraction, 1.5) for b, u in zip(case["df_base"], case["df_shock_up"])]
    else:
        shocked_dfs = [b + (d - b) * min(abs(shock_fraction), 1.5) for b, d in zip(case["df_base"], case["df_shock_down"])]
    shocked_eve = compute_eve(periodic, shocked_dfs)
    d_eve = shocked_eve - base_eve
    pct_t1_eve = abs(d_eve) / case["tier1"] * 100

    # Metrics
    st.html(f"<div style='height:10px;'></div>")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Shock", f"{rate_shock:+d} bps")
    with c2:
        nii_status = "BREACH" if abs(pct_t1) > 2.5 else ("WATCH" if abs(pct_t1) > 1.5 else "PASS")
        st.metric("ΔNII", f"{d_nii:+,.0f}", delta=f"{pct_base:+.2f}% Base NII")
    with c3:
        st.metric("ΔEVE", f"{d_eve:+,.0f}", delta=f"{pct_t1_eve:.2f}% of T1")
    with c4:
        eve_status = "BREACH" if pct_t1_eve > 15 else ("WATCH" if pct_t1_eve > 10 else "PASS")
        overall = "BREACH" if "BREACH" in (nii_status, eve_status) else ("WATCH" if "WATCH" in (nii_status, eve_status) else "PASS")
        st.metric("Overall Status", overall,
            delta=f"NII: {nii_status} | EVE: {eve_status}")

    # Side-by-side impact chart
    bps_range = list(range(-300, 325, 25))
    nii_impacts = [case["cum_1y_gap"] * (s / 10000) for s in bps_range]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=[f"{s:+d}" for s in bps_range], y=nii_impacts,
        marker=dict(color=[GREEN if v >= 0 else RED for v in nii_impacts], opacity=0.6),
        hovertemplate="Rate: %{x}bps<br>ΔNII: %{y:,.0f}<extra></extra>",
        name="ΔNII"))
    # Highlight current
    fig.add_trace(go.Scatter(x=[f"{rate_shock:+d}"], y=[d_nii], mode="markers",
        marker=dict(size=20, color=GOLD, symbol="diamond", line=dict(width=2, color=BLUE)),
        name=f"Selected: {rate_shock:+d}bps"))
    # Thresholds
    nii_thresh = case["tier1"] * 0.025
    fig.add_hline(y=nii_thresh, line_dash="dash", line_color=RED, line_width=1.5)
    fig.add_hline(y=-nii_thresh, line_dash="dash", line_color=RED, line_width=1.5)
    fig.add_hline(y=0, line_dash="solid", line_color=MUTED, line_width=1)
    fig.update_layout(**plotly_theme(),
        title=dict(text=f"NII Impact Across Rate Shocks — {case['name']}",
            font=dict(color=GOLD, size=14)),
        height=400, margin=dict(l=50, r=20, t=50, b=60),
        xaxis_title="Rate Shock (bps)", yaxis_title=f"ΔNII ({case['currency']})",
        legend=dict(orientation="h", yanchor="bottom", y=-0.25))
    st.plotly_chart(fig, use_container_width=True, key="sim_chart")

    info_card("💡 What This Tells You",
        f"The <b>{case['name']}</b> has a cumulative 1-year rate gap of <b>{case['cum_1y_gap']:+,} "
        f"{case['currency']}</b>. " +
        ("Rising rates <b>improve</b> NII for this asset-sensitive bank."
         if case['cum_1y_gap'] > 0 else
         "Rising rates <b>compress</b> NII for this liability-sensitive bank."),
        GOLD)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE 6: KNOWLEDGE BASE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

elif page == "📚 Knowledge Base":
    section_header("IRRBB Knowledge Base", "Key concepts, formulas, and FAQs", "📚")

    topic = st.selectbox(
        "Select Topic",
        [
            "Six Basel Rate Shock Scenarios",
            "Behavioural Assumptions",
            "Supervisory Outlier Tests",
            "Common FAQs",
        ],
        key="kb_topic"
    )

    if topic == "Six Basel Rate Shock Scenarios":
        info_card("📘 The Six Prescribed Scenarios (BCBS d368)",
            "Banks must test both EVE and NII under six standardised scenarios: two parallel moves, "
            "two curve-shape moves, and two short-end moves. Memory aid: <b>2 flat + 2 shape + 2 short-end = 6</b>.",
            MID_BLUE)

        scen_df = pd.DataFrame([
            {"#": 1, "Scenario": "Parallel Up", "Short (0-1Y)": "Rates up", "Long (3-5Y+)": "Rates up", "Tests": "Repricing risk (broad)"},
            {"#": 2, "Scenario": "Parallel Down", "Short (0-1Y)": "Rates down", "Long (3-5Y+)": "Rates down", "Tests": "Repricing risk (broad)"},
            {"#": 3, "Scenario": "Steepener", "Short (0-1Y)": "Short down", "Long (3-5Y+)": "Long up", "Tests": "Yield curve risk"},
            {"#": 4, "Scenario": "Flattener", "Short (0-1Y)": "Short up", "Long (3-5Y+)": "Long down", "Tests": "Yield curve risk"},
            {"#": 5, "Scenario": "Short Rate Up", "Short (0-1Y)": "Strong rise", "Long (3-5Y+)": "Smallest", "Tests": "Deposit/funding"},
            {"#": 6, "Scenario": "Short Rate Down", "Short (0-1Y)": "Strong fall", "Long (3-5Y+)": "Smallest", "Tests": "Short-end repricing"},
        ])
        st.dataframe(scen_df, use_container_width=True, hide_index=True)

    elif topic == "Behavioural Assumptions":
        info_card("📘 Why Behavioural Assumptions Matter",
            "Contractual cash flows rarely reflect how customers actually behave. Behavioural assumptions "
            "bridge the gap between legal contract terms and economic reality. Without them, both NII and "
            "EVE will be materially wrong.", MID_BLUE)

        beh_df = pd.DataFrame([
            {"Parameter": "Deposit Beta", "What It Measures": "% of market rate change passed to deposit rates", "Typical Values": "20–60% (CASA lower, term higher)"},
            {"Parameter": "Deposit Decay", "What It Measures": "Speed NMDs leave the bank", "Typical Values": "Core: 5% p.a.; rate-sensitive: 15–25% p.a."},
            {"Parameter": "Prepayment Speed", "What It Measures": "Rate at which borrowers repay early", "Typical Values": "5–15% CPR for mortgages"},
            {"Parameter": "Early Withdrawal", "What It Measures": "Term deposits broken early", "Typical Values": "3–5% break rate"},
            {"Parameter": "Repricing Lag", "What It Measures": "Delay between market and product rate change", "Typical Values": "1–3 months for CASA"},
        ])
        st.dataframe(beh_df, use_container_width=True, hide_index=True)

        info_card("💡 Deposit Beta Example",
            "A bank has $1,000mm savings deposits with a deposit beta of 20%. If market rates rise 100bps, "
            "the bank raises deposit rates by only 20bps. Funding cost increase = $1,000mm × 0.20% = $2mm "
            "(not $10mm). This protects NII in the short run — the bank captures the spread. But if "
            "customers become rate-sensitive and migrate elsewhere, the bank loses balances and the NII "
            "benefit evaporates.", GOLD)

    elif topic == "Supervisory Outlier Tests":
        info_card("📘 EBA/Basel Supervisory Outlier Tests (SOT)",
            "Banks must report worst-case ΔEVE and ΔNII across the six scenarios to supervisors. "
            "Breaching these thresholds triggers mandatory supervisory action.",
            MID_BLUE)

        c1, c2 = st.columns(2)
        with c1:
            st.html(f"""
            <div style="background:{CARD_BG}; border:2px solid {PURPLE}; border-radius:12px;
                padding:20px; text-align:center;">
                <div style="color:{PURPLE}; -webkit-text-fill-color:{PURPLE}; font-weight:700;
                    font-size:1.1rem; margin-bottom:10px;">ΔEVE SOT Threshold</div>
                <div style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:'Playfair Display',serif;
                    font-size:2.2rem; font-weight:700;">> 15%</div>
                <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.85rem; margin-top:8px;">
                    of Tier 1 Capital<br>→ Bank is "outlier"<br>→ Supervisory action required
                </div>
            </div>
            """)
        with c2:
            st.html(f"""
            <div style="background:{CARD_BG}; border:2px solid {MID_BLUE}; border-radius:12px;
                padding:20px; text-align:center;">
                <div style="color:{MID_BLUE}; -webkit-text-fill-color:{MID_BLUE}; font-weight:700;
                    font-size:1.1rem; margin-bottom:10px;">ΔNII SOT Threshold</div>
                <div style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-family:'Playfair Display',serif;
                    font-size:2.2rem; font-weight:700;">> 2.5%</div>
                <div style="color:{TEXT}; -webkit-text-fill-color:{TEXT}; font-size:0.85rem; margin-top:8px;">
                    of Tier 1 Capital<br>→ Enhanced monitoring<br>→ Corrective plan required
                </div>
            </div>
            """)

    elif topic == "Common FAQs":
        faqs = [
            ("Why is IRRBB a Pillar 2 risk and not Pillar 1?",
             "IRRBB is highly bank-specific — it depends on each bank's unique balance sheet structure, "
             "business model, and behavioural patterns. A standardised Pillar 1 capital charge would not "
             "adequately reflect this heterogeneity. Instead, Basel requires banks to measure and manage "
             "IRRBB under Pillar 2, with supervisory review ensuring adequate capital is held."),
            ("What is the difference between duration gap and repricing gap?",
             "Repricing gap uses simple bucket-based matching — it counts amounts in each bucket. "
             "Duration gap uses duration-weighted measures — it accounts for both amount and timing of "
             "cash flows. Duration gap is more accurate for EVE but more complex. Repricing gap is "
             "simpler and more suitable for NII."),
            ("Can a bank fully hedge IRRBB?",
             "In theory, a bank could match every asset cash flow with a liability of identical duration. "
             "In practice, this is impossible because: (1) banks want to earn the term premium from "
             "borrowing short and lending long, (2) customer behaviour (prepayments, withdrawals) "
             "cannot be fully predicted, (3) non-maturity deposits (CASA) have no contractual maturity. "
             "IRRBB management is about keeping risk within tolerable limits, not eliminating it."),
            ("How do interest rate swaps help manage IRRBB?",
             "Pay-fixed/receive-floating swaps convert fixed-rate liabilities to floating (or fixed-rate "
             "assets to floating in effect). They help asset-sensitive banks hedge against falling rates "
             "and help liability-sensitive banks hedge against rising rates. Swaps are the most common "
             "IRRBB hedging instrument."),
            ("What role do non-maturity deposits (NMDs) play?",
             "NMDs — CASA, savings, current accounts — have no contractual maturity but are economically "
             "stable. Banks apply behavioural modelling to estimate: (1) stable 'core' portion with long "
             "effective duration, (2) volatile portion with short effective duration. How NMDs are "
             "modelled dramatically affects EVE calculations and is a major area of regulatory focus."),
        ]
        for q, a in faqs:
            with st.expander(f"❓ {q}", expanded=False):
                st.html(f"""<div style='color:{TEXT}; -webkit-text-fill-color:{TEXT};
                    font-size:0.92rem; line-height:1.7;'>{a}</div>""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FOOTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.html(f"""
<div style="user-select:none; margin-top:40px; padding:20px; text-align:center;
    border-top:2px solid rgba(255,215,0,0.2);">
    <div style="font-family:'Playfair Display',serif; color:{GOLD}; -webkit-text-fill-color:{GOLD};
        font-size:1rem; font-weight:700; margin-bottom:4px;">
        🏔️ The Mountain Path Academy — World of Finance</div>
    <div style="color:{MUTED}; -webkit-text-fill-color:{MUTED}; font-size:0.8rem; margin-bottom:6px;">
        Prof. V. Ravichandran · Visiting Faculty ·
        NMIMS Bangalore | BITS Pilani | RV University Bangalore | Goa Institute of Management</div>
    <div style="display:flex; justify-content:center; gap:20px; margin-top:6px;">
        <a href="https://themountainpathacademy.com" target="_blank"
            style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:0.8rem; text-decoration:none; font-weight:600;">
            themountainpathacademy.com</a>
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank"
            style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:0.8rem; text-decoration:none;">LinkedIn</a>
        <a href="https://github.com/trichyravis" target="_blank"
            style="color:{GOLD}; -webkit-text-fill-color:{GOLD}; font-size:0.8rem; text-decoration:none;">GitHub</a>
    </div>
</div>
""")
