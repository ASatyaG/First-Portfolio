import streamlit as st

# 1. System Setup
st.set_page_config(page_title="System: Monarch of Data", page_icon="🗡️", layout="wide")

# 2. Simple, Safe Styling
st.markdown("""
    <style>
    /* Dark background */
    .stApp {
        background-color: #0a0e14;
        color: #e0e0e0;
    }
    /* Glowing Blue Text */
    h1, h2, h3 {
        color: #00D4FF !important;
        text-shadow: 0 0 10px #00D4FF;
    }
    /* Box Borders */
    div[data-testid="stVerticalBlock"] > div > div {
        border-color: rgba(0, 212, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header - Identity
st.title("🗡️ ATTA SATYA GIRISH")
st.write("M.TECH | COMPUTER SCIENCE | DATA ANALYTICS")
st.markdown("---")

# 4. Profile Section (Using Columns for the HUD feel)
col1, col2 = st.columns([2, 1])

with col1:
    st.header("👤 PLAYER PROFILE")
    st.info("**CLASS:** SHADOW EXTRACTOR (DATA ENGINEER)")
    
    # Skills from your Resume
    st.subheader("🛠️ TECHNICAL SKILLS")
    skills = ["Python", "SQL", "Machine Learning", "Pandas", "NumPy", "Scikit-Learn", "Power BI", "Agile"]
    st.write(" | ".join([f"**{s}**" for s in skills]))
    
    st.write("\n")
    st.subheader("📂 DUNGEONS CLEARED (PROJECTS)")
    
    with st.expander("NETWORK INTRUSION DETECTION (A-RANK)", expanded=True):
        st.write("Developed an original machine learning framework to analyze network attacks using Hybrid Ensemble Learning.")
        st.caption("Tech: Python, ML, Hybrid Ensemble Learning")

    with st.expander("FINANCIAL FRAUD DETECTION (A-RANK)", expanded=True):
        st.write("Implemented ML algorithms to identify transaction patterns and mitigate risks in financial systems.")
        st.caption("Tech: Python, Risk Assessment, ML")

with col2:
    st.header("⚡ SYSTEM STATS")
    st.metric(label="M.Tech CGPA", value="8.01", delta="GITAM University")
    st.metric(label="B.Tech CGPA", value="7.20", delta="NSRIT")
    
    st.write("---")
    st.subheader("🎭 INTERESTS")
    
    # Simple Interest Tags
    c1, c2 = st.columns(2)
    with c1:
        st.success("🎮 GAMER")
    with c2:
        st.success("🏃 ATHLETE")
        
    st.write("\n")
    st.subheader("📜 INVENTORY")
    st.write("✅ IBM: Agile & Scrum")
    st.write("✅ UCSD: Data Structures")
    st.write("✅ Office Master: Power BI")

# 5. Bottom Interaction
if st.button('ARISE'):
    st.balloons()
    st.success("System updated. No errors detected.")