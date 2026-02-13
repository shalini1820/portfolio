# pages/1_Industry_Case_Studies.py
import streamlit as st

st.set_page_config(page_title="Industry Case Studies", layout="wide", page_icon="💼")

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

# Page Title
st.title("Industry Case Studies")
st.markdown("### Professional work at Deutsche Börse Group and Arcadis")
st.write("""
Production analytics solutions, automation pipelines, and real-time dashboards deployed 
in financial markets and enterprise operations.
""")

st.markdown("---")

# Project 1
st.markdown("## Computer Vision-Based Document Verification")
st.caption("**Deutsche Börse AG** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Compliance team manually verified 400+ regulatory PDFs each month for stamps and signatures. 
    Manual process took 2-3 minutes per document and was prone to visual fatigue errors.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Developed computer vision-based verification tool using Python with OpenCV for stamp detection 
    and PyMuPDF for document processing. System automatically detects required elements and flags 
    exceptions for manual review.
    """)
    
    st.caption("**Tech Stack:** Python, OpenCV, PyMuPDF")

with col2:
    st.markdown("#### Impact")
    st.metric("Documents/Month", "400+", "Automated")
    st.metric("Time Saved", "20+ hrs/month", "50%+ reduction")
    st.metric("Error Reduction", "50%+", "Manual errors")

st.markdown("---")

# Project 2
st.markdown("## Power Automate Workflows for Cash Market Operations")
st.caption("**Deutsche Börse AG** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Cash market operations involved manual file processing and data entry across multiple systems. 
    Repetitive tasks consumed significant analyst time and introduced manual errors.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Engineered rule-based automation workflows using Power Automate with AI Builder for content recognition. 
    Automated reconciliation of 500K+ rows/month using Power Query and VBA, resolving inconsistent date 
    formats and field mappings across upstream trading systems.
    """)
    
    st.caption("**Tech Stack:** Power Automate, AI Builder, Power Query, VBA")

with col2:
    st.markdown("#### Impact")
    st.metric("Rows Reconciled", "500K+/month", "Automated")
    st.metric("Time Saved", "20+ hrs/month", "Workflow automation")
    st.metric("Data Defects", "30% reduction", "Quality improvement")

st.markdown("---")

# Project 3
st.markdown("## Real-Time Trading Analytics Dashboards")
st.caption("**Deutsche Börse AG** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Traders relied on static reports and ad-hoc data requests for analytics. No unified view of 
    trading KPIs led to information fragmentation and delayed decision-making.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Designed and deployed live Power BI dashboards integrating Scala and Apache Zeppelin data sources 
    for real-time trading analytics. Dashboards replaced ad-hoc report requests and provide traders 
    with self-service access to key metrics.
    """)
    
    st.caption("**Tech Stack:** Power BI, Apache Zeppelin, Scala, SQL")

with col2:
    st.markdown("#### Impact")
    st.metric("Adoption Rate", "Daily usage", "Traders check dashboards")
    st.metric("Ad-hoc Requests", "Significant reduction", "Self-service analytics")

st.markdown("---")

# Project 4
st.markdown("## Power BI Dashboards for Project KPI Tracking")
st.caption("**Arcadis** | Aug 2022 - July 2024")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Project teams needed real-time visibility into KPIs and resource allocation. 
    Manual reporting processes created delays in project tracking and decision-making.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Built Power BI dashboards and Power Apps for real-time project KPI tracking and resource management. 
    Automated data validation and transformation pipelines using Python, VBA, and Dynamo.
    """)
    
    st.caption("**Tech Stack:** Power BI, Power Apps, Python, VBA")

with col2:
    st.markdown("#### Impact")
    st.metric("Processing Time", "60% reduction", "Manual work eliminated")
    st.metric("Approval Time", "2 days saved", "Per project")

st.markdown("---")

# Project 5
st.markdown("## Power BI Dashboard for Commercial Sales Team")
st.caption("**Eurex (Deutsche Börse Group)** | Jan 2026 - Present")

st.info("""
**Current Project:** Designing and deploying Power BI dashboard to track client performance across 
derivatives products. Automating recurring BAU tasks using Python and VBA, including Most Liquid 
Products lists and interactive chart updates. Extracting and structuring trading data using SQL 
across TRF, FTSE 100, and ESG segments.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Approach")
    st.write("• Replacing static Excel reports with interactive Power BI dashboards")
    st.write("• Automating manual data extraction from StatistiX database")
    st.write("• Building SQL queries for derivatives product data")
    st.write("• Creating recurring task automation with Python and VBA")

with col2:
    st.markdown("#### Focus Areas")
    st.write("• Client performance tracking across derivatives products")
    st.write("• Most Liquid Products lists and interactive charts")
    st.write("• Product presentations for TRF, FTSE 100, ESG segments")
    st.write("• Monthly market analytics newsletters")

st.markdown("---")

st.caption("All projects deployed in production at Deutsche Börse Group and Arcadis")
