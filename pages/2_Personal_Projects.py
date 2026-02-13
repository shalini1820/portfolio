# pages/2_Personal_Projects.py
import streamlit as st

st.set_page_config(page_title="Personal Projects", layout="wide", page_icon="🔬")

# Top Navigation - centered
nav_cols = st.columns(5)
with nav_cols[0]:
    if st.button("Home", key="nav0", use_container_width=True):
        st.switch_page("Home.py")
with nav_cols[1]:
    if st.button("Industry Cases", key="nav1", use_container_width=True):
        st.switch_page("pages/1_Industry_Case_Studies.py")
with nav_cols[2]:
    if st.button("Projects", key="nav2", use_container_width=True):
        st.switch_page("pages/2_Personal_Projects.py")
with nav_cols[3]:
    if st.button("Research", key="nav3", use_container_width=True):
        st.switch_page("pages/3_Research.py")
with nav_cols[4]:
    if st.button("Contact", key="nav4", use_container_width=True):
        st.switch_page("pages/4_Contact.py")

st.markdown("<div style='margin: 1rem 0;'></div>", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&family=Inter:wght@400;600;700&display=swap');

/* Hide sidebar completely */
[data-testid="stSidebar"] {
    display: none;
}

section[data-testid="stSidebarNav"] {
    display: none;
}

/* Remove default padding */
.main > div {
    padding-top: 0rem;
}

/* Main background */
.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Typography */
div[data-testid="stMarkdownContainer"] h1 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 3rem;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
}

div[data-testid="stMarkdownContainer"] h2 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 2rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    letter-spacing: -0.5px;
}

div[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Inter', sans-serif;
    color: #64ffda;
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}

div[data-testid="stMarkdownContainer"] h4 {
    font-family: 'Inter', sans-serif;
    color: #ffd700;
    font-size: 1.1rem;
    font-weight: 600;
    margin-top: 1rem;
}

div[data-testid="stMarkdownContainer"] p {
    font-family: 'DM Sans', sans-serif;
    color: #ccd6f6;
    line-height: 1.8;
    font-size: 1.05rem;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.08) 0%, rgba(20, 27, 61, 0.4) 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid rgba(244, 196, 48, 0.2);
}

div[data-testid="stMetricLabel"] {
    font-family: 'Space Mono', monospace;
    color: #f4c430 !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

div[data-testid="stMetricValue"] {
    font-family: 'Space Mono', monospace;
    color: #ffffff !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricDelta"] {
    font-family: 'DM Sans', sans-serif;
    color: #a8b2d1 !important;
    font-size: 0.85rem !important;
}

/* Download button */
.stDownloadButton button {
    background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%);
    color: #0a0e27 !important;
    font-family: 'Space Mono', monospace;
    font-weight: 700 !important;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 8px;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.stDownloadButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(244, 196, 48, 0.4);
    background: #ffd700;
}

.stDownloadButton button p {
    color: #0a0e27 !important;
    font-weight: 700 !important;
}

/* Navigation buttons - stylish version */
.stButton button {
    background: transparent;
    color: #ccd6f6;
    border: none;
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 500;
    padding: 0.6rem 1.5rem;
    border-radius: 6px;
    transition: all 0.3s ease;
    position: relative;
}

.stButton button:hover {
    color: #f4c430;
    background: rgba(244, 196, 48, 0.1);
    transform: translateY(-2px);
}

.stButton button::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%) scaleX(0);
    width: 80%;
    height: 2px;
    background: #f4c430;
    transition: transform 0.3s ease;
}

.stButton button:hover::after {
    transform: translateX(-50%) scaleX(1);
}

/* Info box */
div[data-testid="stAlert"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    border: 1px solid rgba(244, 196, 48, 0.3);
    border-radius: 12px;
    font-family: 'DM Sans', sans-serif;
}

/* Caption */
.stCaption {
    font-family: 'Inter', sans-serif;
    color: #8892b0 !important;
    font-size: 0.9rem !important;
}

/* Links */
a {
    color: #64ffda;
    text-decoration: none;
}

a:hover {
    color: #ffd700;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

st.title("Personal Analytics Projects")
st.markdown("### Independent work demonstrating analytical thinking and technical execution")
st.write("Projects built to explore data transformation, visualization, and pipeline design.")

st.markdown("---")

# Project 1
st.markdown("## Interactive BI Analytics Dashboard")
st.caption("**Status:** In Progress")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Purpose")
    st.write("""
    Reusable dashboard template for rapid analytics deployment. Designed to be stakeholder-friendly 
    with interactive filters and export capabilities.
    """)
    
    st.markdown("#### Approach")
    st.write("""
    Built with Streamlit for UI, pandas for data processing, and Plotly for visualizations. 
    Implements KPI cards, time-series charts, dynamic filters, and CSV export functionality. 
    Mobile-responsive design following dashboard best practices.
    """)
    
    st.caption("**Tech Stack:** Streamlit, Pandas, Plotly")

with col2:
    st.markdown("#### Technical Focus")
    st.write("• Interactive data exploration with dynamic filters")
    st.write("• Clean UI/UX for non-technical users")
    st.write("• Export functionality for deeper analysis")
    st.write("• Zero licensing costs, deployable via Streamlit Cloud")

if st.button("View Code - Interactive BI App", key="proj1"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/interactive-bi-analytics-app)")

st.markdown("---")

# Project 2
st.markdown("## End-to-End Analytics Pipeline")
st.caption("**Status:** In Progress")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Purpose")
    st.write("""
    Demonstrate production-grade ETL pipeline with proper engineering practices. 
    Most portfolios show outputs but not the engineering behind them.
    """)
    
    st.markdown("#### Approach")
    st.write("""
    Modular pipeline with separation of concerns: ingestion, transformation, validation, aggregation, output. 
    Includes pytest for data quality tests, structured logging, and configuration management.
    """)
    
    st.caption("**Tech Stack:** Python, Pandas, Pytest")

with col2:
    st.markdown("#### Technical Focus")
    st.write("• Reproducible pipeline with clear folder structure")
    st.write("• Data quality tests prevent bad data downstream")
    st.write("• Logging enables debugging and audit trails")
    st.write("• Software engineering practices for analytics")

if st.button("View Code - Analytics Pipeline", key="proj2"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/end-to-end-analytics-pipeline)")

st.markdown("---")

# Project 3
st.markdown("## Data Cleaning and Preparation")
st.caption("**Status:** Completed")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Purpose")
    st.write("""
    Practical data wrangling demonstration. Real-world data is rarely clean - this project 
    addresses common issues encountered in BI work.
    """)
    
    st.markdown("#### Approach")
    st.write("""
    Multi-stage cleaning pipeline: date standardization with error handling, missing value 
    imputation based on business logic, duplicate detection and removal, aggregation to monthly KPIs. 
    Transactional dataset with inconsistent date formats and missing values.
    """)
    
    st.caption("**Tech Stack:** Python, Pandas")

with col2:
    st.markdown("#### Outcomes")
    st.write("• Cleaned dataset ready for monthly KPI reporting")
    st.write("• Standardized 5,000+ inconsistent date entries")
    st.write("• Documented decision logic for missing value handling")
    st.write("• Time-series visualization of transaction trends")

if st.button("View Code - Data Cleaning", key="proj3"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/bi-data-cleaning-case-study)")

st.markdown("---")

# Project 4
st.markdown("## Automated Data Reconciliation")
st.caption("**Status:** Completed")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Purpose")
    st.write("""
    Automate weekly reconciliation between two financial ledgers. Manual process involved 
    sorting in Excel, visual comparison, and flagging mismatches.
    """)
    
    st.markdown("#### Approach")
    st.write("""
    Built reconciliation script that joins datasets on transaction IDs, compares amounts and dates, 
    labels match status, and exports separate exception file for investigation. Implemented tolerance 
    thresholds for amount matching and date drift handling.
    """)
    
    st.caption("**Tech Stack:** Python, Pandas, Openpyxl")

with col2:
    st.markdown("#### Outcomes")
    st.write("• Weekly reconciliation automated from 4 hours to 5 minutes")
    st.write("• Reconciled dataset with clear match/mismatch labels")
    st.write("• Exception file with categorized issues for follow-up")
    st.write("• Caught edge cases previously missed in manual review")

if st.button("View Code - Data Reconciliation", key="proj4"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/data-reconciliation-exceptions)")

st.markdown("---")

st.info("All project code available on GitHub: [github.com/amit1820](https://github.com/amit1820)")
