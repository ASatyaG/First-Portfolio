import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="ATTA SATYA GIRISH | Data Engineer", page_icon="⚙️", layout="wide")

# 2. Advanced CSS for Visual Effects & Animations
st.markdown("""
    <style>
    /* 1. ANIMATED GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e293b, #0f172a, #111827);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #f8fafc;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. GLOWING TEXT ANIMATION FOR NAME */
    .hero-name {
        font-size: 55px !important; /* Increased and forced */
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #38bdf8);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
        margin-bottom: 0px;
        line-height: 1.1;
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* 3. CARD HOVER EFFECTS */
    .project-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .project-card:hover {
        border-color: #38bdf8;
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(56, 189, 248, 0.2);
        background: rgba(30, 41, 59, 0.6);
    }

    /* 4. PULSING SKILL BADGES */
    .skill-badge {
        display: inline-block;
        border: 1px solid #38bdf8;
        color: #38bdf8;
        padding: 6px 16px;
        border-radius: 50px;
        font-size: 14px;
        margin: 5px;
        background: rgba(56, 189, 248, 0.05);
        transition: 0.3s;
    }
    .skill-badge:hover {
        background: #38bdf8;
        color: #0f172a;
        box-shadow: 0 0 15px #38bdf8;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Using details from your resume)
with st.sidebar:
    st.markdown("### 📬 Contact Portal")
    st.write("📧 attasatyagirish@gmail.com") # [cite: 2]
    st.write("📞 +91 9347795821") # [cite: 2]
    st.write("📍 Visakhapatnam, AP") # [cite: 2]
    st.write("---")
    st.markdown("### 🎓 Credentials")
    st.write("• M.Tech (CS) - GITAM University") # [cite: 10]
    st.write("• B.Tech (ECE) - NSRIT") # [cite: 11]

# 4. Hero Section
st.markdown('<p class="hero-name">ATTA SATYA GIRISH</p>', unsafe_allow_html=True) # 
st.markdown("### **Data Engineer | M.Tech Computer Science**")
st.write("Developing high-performance data pipelines and evidence-based ML systems.") # [cite: 4, 5]

# 5. Technical Arsenal (Pulsing Badges)
st.write("---")
st.subheader("🛠️ Technical Arsenal")
skills = {
    "Languages": ["Python", "SQL"], # [cite: 7]
    "Frameworks": ["Pandas", "NumPy", "Scikit-Learn", "ETL Pipelines"], # [cite: 7]
    "Tools": ["Power BI", "Git", "Agile/Scrum", "Prompt Engineering"] # [cite: 8, 20]
}

for cat, items in skills.items():
    st.markdown(f"**{cat}:** " + "".join([f'<span class="skill-badge">{i}</span>' for i in items]), unsafe_allow_html=True)

# 6. Projects Section (With Hover Reveal)
st.write("---")
st.subheader("🚀 Featured Engineering Projects")

# Churn Prediction System
with st.container():
    st.markdown(f"""
    <div class="project-card">
        <h2 style="color:#38bdf8; margin-top:0;">End-to-End Churn Prediction System</h2>
        <p>A full-lifecycle data engineering project: from data cleaning to real-time ML inference.</p>
        <p style="font-size:14px; color:#94a3b8;"><b>Key Tech:</b> Python, Scikit-Learn, Streamlit</p>
        <a href="https://github.com/ASatyaG/End-to-End-Churn-Prediction-System.git" target="_blank" style="color:#38bdf8; text-decoration:none; font-weight:bold;">View System Architecture →</a>
    </div>
    """, unsafe_allow_html=True)

# Network Security [cite: 13]
with st.container():
    st.markdown(f"""
    <div class="project-card">
        <h2 style="color:#38bdf8; margin-top:0;">Network Intrusion Detection System</h2>
        <p>M.Tech Thesis: Utilizing Hybrid Ensemble Learning and Automatic Feature Selection to mitigate sophisticated network attacks.</p>
        <p style="font-size:14px; color:#94a3b8;"><b>Focus:</b> High-Dimensional Data & Pattern Recognition</p> 
    </div>
    """, unsafe_allow_html=True)

if st.button("Activate System Check"):
    st.balloons()

