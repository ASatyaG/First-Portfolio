import streamlit as st
import os
from pathlib import Path

# =========================
# Page Configuration
# =========================
st.set_page_config(page_title="ATTA SATYA GIRISH | Portfolio", page_icon="⚙️", layout="wide")

# =========================
# Session State Router (Single-file "pages")
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"  # home | anaverse

def go_home():
    st.session_state.page = "home"

def go_anaverse():
    st.session_state.page = "anaverse"

# =========================
# Global CSS (used in both views)
# =========================
st.markdown("""
<style>
/* ANIMATED GRADIENT BACKGROUND */
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

/* GLOWING TEXT ANIMATION FOR NAME */
.hero-name {
    font-size: 55px !important;
    font-weight: 900;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #38bdf8);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    margin-bottom: 0px;
    line-height: 1.1;
}
@keyframes shine { to { background-position: 200% center; } }

/* CARD HOVER EFFECTS */
.project-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(56, 189, 248, 0.2);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 20px;
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.project-card:hover {
    border-color: #38bdf8;
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 20px rgba(56, 189, 248, 0.2);
    background: rgba(30, 41, 59, 0.6);
}

/* PULSING SKILL BADGES */
.skill-badge {
    display: inline-block;
    border: 1px solid #38bdf8;
    color: #38bdf8;
    padding: 6px 16px;
    border-radius: 50px;
    font-size: 14px;
    margin: 5px 6px 0 0;
    background: rgba(56, 189, 248, 0.05);
    transition: 0.25s;
}
.skill-badge:hover {
    background: #38bdf8;
    color: #0f172a;
    box-shadow: 0 0 15px #38bdf8;
}

.small-muted { color: #94a3b8; font-size: 14px; }

/* Theme buttons */
div.stButton > button {
    background: rgba(56, 189, 248, 0.10);
    border: 1px solid rgba(56, 189, 248, 0.35);
    color: #e2e8f0;
    border-radius: 14px;
    padding: 10px 16px;
    font-weight: 700;
}
div.stButton > button:hover {
    border-color: #38bdf8;
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.35);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# =========================
# Sidebar (shown on every page)
# =========================
with st.sidebar:
    st.markdown("### 📬 Contact")
    st.write("📧 attasatyagirish@gmail.com")
    st.write("📞 +91 9347795821")
    st.write("📍 Visakhapatnam, AP")

    st.write("---")
    st.markdown("### 🔗 Links")
    st.link_button("GitHub", "https://github.com/ASatyaG")
    st.link_button("Linkedin", "https://www.linkedin.com/in/atta-satya-girish-089774338/")
    st.link_button("Competition Page", "https://www.kaggle.com/competitions/ana-verse-2-0-h/overview")

    st.write("---")
    st.markdown("### 🎓 Education")
    st.write("• M.Tech (CS) — GITAM University (2024)")
    st.write("• B.Tech (ECE) — NSRIT (2022)")

    st.write("---")
    st.markdown("### 🧭 Navigation")
    if st.button("🏠 Home"):
        go_home()
    if st.button("🏆 ANA-Verse Deep Dive"):
        go_anaverse()

# =========================
# Helpers: find leaderboard image
# =========================
def find_first_image_in_folder(folder_name: str):
    """
    Looks for the first image file inside the given folder (relative to app.py),
    supporting common image extensions.
    """
    base_dir = Path(__file__).resolve().parent
    folder = base_dir / folder_name
    if not folder.exists() or not folder.is_dir():
        return None

    exts = (".png", ".jpg", ".jpeg", ".webp")
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.suffix.lower() in exts:
            return str(p)
    return None

# =========================
# PAGE: HOME
# =========================
def render_home():
    st.markdown('<p class="hero-name">ATTA SATYA GIRISH</p>', unsafe_allow_html=True)
    st.markdown("### **Data / ML Portfolio | M.Tech Computer Science**")
    st.write("Building practical data solutions, dashboards, and machine learning experiments.")
    st.caption("Note: I use AI tools to speed up development, and I validate outcomes by running experiments and comparing results.")

    # Skills
    st.write("---")
    st.subheader("🛠️ Technical Arsenal")
    skills = {
        "Languages": ["Python", "SQL"],
        "ML / Data": ["Pandas", "NumPy", "Scikit-Learn", "LightGBM", "Feature Engineering"],
        "Data Engineering": ["ETL Pipelines", "PostgreSQL", "Data Cleaning"],
        "Tools": ["Power BI", "Git", "Streamlit", "Prompt Engineering"]
    }
    for cat, items in skills.items():
        st.markdown(
            f"**{cat}:** " + "".join([f'<span class="skill-badge">{i}</span>' for i in items]),
            unsafe_allow_html=True
        )

    # Kaggle
    st.write("---")
    st.subheader("🏆 Kaggle")

    st.markdown("""
    <div class="project-card">
        <h2 style="color:#38bdf8; margin-top:0;">ANA-Verse 2.0_H — Sensor Anomaly Detection</h2>
        <p>Predict anomalies from sensor readings (tabular classification). Evaluated using F1 Score + Accuracy per class.</p>
        <p class="small-muted"><b>Click below</b> to view the detailed deep dive (problem, approach, results, and proof screenshot).</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Deep Dive → ANA-Verse 2.0_H"):
        go_anaverse()

    # Projects
    st.write("---")
    st.subheader("🚀 Featured Projects")

    st.markdown("""
    <div class="project-card">
        <h2 style="color:#38bdf8; margin-top:0;">End-to-End Churn Prediction System</h2>
        <p>End-to-end ML project: data cleaning, ETL, model training, and BI reporting for churn risk insights.</p>
        <p class="small-muted"><b>Key Tech:</b> Python, Scikit-Learn, PostgreSQL, Power BI</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View on GitHub", "https://github.com/ASatyaG/End-to-End-Churn-Prediction-System")

    st.markdown("""
    <div class="project-card">
        <h2 style="color:#38bdf8; margin-top:0;">Network Intrusion Detection System</h2>
        <p>M.Tech thesis work exploring ML techniques for detecting malicious patterns in network data.</p>
        <p class="small-muted"><b>Focus:</b> Feature selection, anomaly detection concepts, evaluation metrics</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    if st.button("Activate System Check"):
        st.balloons()

# =========================
# PAGE: ANA-VERSE DEEP DIVE
# =========================
def render_anaverse():
    top = st.columns([1, 3, 2])
    with top[0]:
        if st.button("⬅️ Back"):
            go_home()
    with top[2]:
        st.link_button("Competition Page", "https://www.kaggle.com/competitions/ana-verse-2-0-h/overview")

    st.title("🏆 ANA-Verse 2.0_H — Sensor Anomaly Detection (Deep Dive)")
    st.caption("This page explains the competition, the solution strategy, and shows a leaderboard screenshot from your local folder.")

    st.write("---")

    st.markdown("""
    <div class="project-card">
      <h3 style="margin-top:0; color:#38bdf8;">Competition Objective</h3>
      <p>Predict whether each row of sensor readings corresponds to an anomaly (binary classification).</p>
      <p class="small-muted"><b>Metric:</b> F1 Score + Accuracy per class (threshold choice impacts F1 strongly).</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
      <h3 style="margin-top:0; color:#38bdf8;">How I Achieved #1 (High-Level)</h3>
      <ul>
        <li><b>Feature engineering:</b> added informative time features + sensor interaction features</li>
        <li><b>Model:</b> LightGBM with class-imbalance weighting</li>
        <li><b>Threshold tuning:</b> optimized the decision threshold to maximize F1 score</li>
      </ul>
      <p class="small-muted"></p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # Leaderboard image (auto-detect inside "Kaggle first win")
    # =========================
    st.markdown("### 📸 Leaderboard Screenshot (Local Proof)")
    img_path = find_first_image_in_folder("Kaggle first win")

    if img_path:
        st.image(img_path, caption="Kaggle Leaderboard — ANA-Verse 2.0_H", use_container_width=True)
        st.caption(" ")
    else:
        st.warning(
            "I couldn't find an image inside the folder: 'Kaggle first win'.\n\n"
            "✅ Fix:\n"
            "1) Put your screenshot (png/jpg/jpeg/webp) inside:\n"
            "   My Portfolio/Kaggle first win/\n"
            "2) Restart the app.\n\n"
            "Tip: Keep the image filename simple (e.g., leaderboard.png)."
        )

    st.write("---")

    st.markdown("""
    <div class="project-card">
      <h3 style="margin-top:0; color:#38bdf8;">Detailed Approach</h3>

      <h4>1) Datetime Feature Engineering</h4>
      <p>Converted datetime columns into month/day/hour/day-of-week, plus cyclic encodings (sin/cos) to capture periodic sensor behavior.</p>

      <h4>2) Data Cleaning + Imputation</h4>
      <p>Coerced values to numeric and used median imputation to handle missing values robustly.</p>

      <h4>3) Pairwise Sensor Interaction Features</h4>
      <p>Generated features between sensor pairs (difference, sum, product, ratio) to reveal cross-sensor relationships useful for separating normal vs anomaly patterns.</p>

      <h4>4) Model</h4>
      <p>Trained a tuned LightGBM classifier, applying class-imbalance weighting so anomalies are learned effectively.</p>

      <h4>5) Threshold Tuning</h4>
      <p>Instead of a fixed 0.5 cutoff, selected thresholds using quantiles to control the predicted anomaly count, improving F1 score.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
      <h3 style="margin-top:0; color:#38bdf8;">What I Learned</h3>
      <ul>
        <li>F1 score is very sensitive to the prediction threshold</li>
        <li>Feature engineering often beats complicated ensembles on tabular problems</li>
        <li>Tree-based models like LightGBM are strong baselines for sensor/tabular data</li>
        <li>Class imbalance must be handled explicitly to avoid majority-class bias</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    if st.button("⬅️ Back to Portfolio"):
        go_home()

# =========================
# Render Router
# =========================
if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "anaverse":
    render_anaverse()
else:
    go_home()
    render_home()
