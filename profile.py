# app.py
import streamlit as st
from pathlib import Path
from datetime import datetime
import pandas as pd

# ---------- Page Setup ----------
st.set_page_config(page_title="Ayush | Portfolio", page_icon="💼", layout="wide")

# ---------- Global Styles (Black Theme + Sidebar + Topbar + Button Fix) ----------
st.markdown("""
<style>
/* Full black app */
.stApp, .main, .block-container { background: #000 !important; }
h1,h2,h3,h4,h5,h6,p,li,span,div, label { color: #e5e5e5 !important; }
a { color: #5eead4 !important; text-decoration: none; }
hr { border: 0; height: 1px; background: #1f2937; margin: 1rem 0; }

/* Remove stray bullets/markers/empties in main content */
.stMarkdown ul, .stMarkdown ol { list-style: none !important; margin-left: 0 !important; padding-left: 0 !important; }
.stMarkdown li::marker { content: "" !important; }
p:empty, div:empty { display: none !important; }

/* Cards & badges */
.card { background:#0a0a0a; border:1px solid #1f2937; border-radius:16px; padding:20px; }
.badge { display:inline-block; padding:6px 10px; border-radius:999px; background:#0b0b0b; border:1px solid #1f2937; margin:0 8px 8px 0; font-size:0.85rem; }

/* Inputs */
.stTextInput>div>div>input, .stTextArea textarea {
  background:#0a0a0a !important; color:#e5e5e5 !important; border:1px solid #1f2937;
}
.stImage img { border-radius:16px; }

/* Sidebar Styles */
[data-testid="stSidebar"] { background-color: #000000 !important; }
[data-testid="stSidebar"] * { color: #e5e5e5 !important; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label { color: #e5e5e5 !important; }

/* Top Toolbar (Deploy bar) */
[data-testid="stHeader"] { background-color: #000000 !important; color: #e5e5e5 !important; }
[data-testid="stHeader"] * { color: #e5e5e5 !important; }

/* Send button styling */
.stButton>button {
    color: #000000 !important;          /* dark text */
    background-color: #f0f0f0 !important; /* light background */
    border: 1px solid #444444 !important;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.6rem 1.2rem;
}
.stButton>button:hover {
    background-color: #5eead4 !important;  /* teal hover */
    color: #000000 !important;             /* keep text dark */
    border: 1px solid #5eead4 !important;
}

/* Certification image card + spacing fix */
.cert-card { background:#0a0a0a; border:1px solid #1f2937; border-radius:16px; padding:16px; margin-top:8px; display:inline-block; }
.certification-title { margin-top: 0 !important; margin-bottom: 8px !important; padding: 0 !important; font-weight:700; }
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.markdown(
    "<h1 style='font-size:28px; font-weight:700; color:#e5e5e5;'>💼 Portfolio</h1>",
    unsafe_allow_html=True
)
page = st.sidebar.radio("Navigate", ["About Me", "My Projects", "My Certifications", "Contact Me"])

# Quick links
st.sidebar.markdown("---")
st.sidebar.caption("Quick Links")
st.sidebar.markdown("- [GitHub](#)")
st.sidebar.markdown("- [LinkedIn](https://www.linkedin.com/in/ayush-velhal/)")
st.sidebar.markdown("- [Email](mailto:ayush.velhal@gmail.com)")

# ---------- Page 1: About Me ----------
def page_about():
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        img_path = Path("portrait.jpg")
        if img_path.exists():
            st.image(str(img_path), caption="Ayush Velhal", use_container_width=True)
        else:
            st.info("Add your headshot as **portrait.jpg** next to this file.")
            st.image("https://via.placeholder.com/600x800?text=portrait.jpg+missing", caption="(placeholder)")

    with col2:
        st.title("Hey, I'm Ayush 👋")
        st.write(
            "I’m a CS student at UT Dallas focused on **AI/ML**, and **Cloud**"
        )
        st.write("This portfolio highlights my projects, certifications, and an easy way to contact me.")

        st.markdown("**Tech I use often**")
        st.markdown(
            '<div class="badge">Python</div>'
            '<div class="badge">Java</div>'
            '<div class="badge">Streamlit</div>'
            '<div class="badge">React</div>'
            '<div class="badge">TensorFlow</div>'
            '<div class="badge">MediaPipe</div>',
            unsafe_allow_html=True
        )

    st.markdown("<hr/>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.write("📍 Dallas, TX")
    with c2: st.write("🎓 University of Texas at Dallas")
    with c3: st.write(" 🏫 Coppell High School 2020-2023")

# ---------- Page 2: My Projects ----------
def page_projects():
    st.title("📂 My Projects")
    st.write("IN PROGRESS")
    st.markdown("<hr/>", unsafe_allow_html=True)

# ---------- Page 3: My Certifications ----------
def page_certs():
    st.title("🎓 My Certifications")
    # no <hr/> here to avoid extra gap

    # Single-column layout (Google cert removed)
    st.markdown('<div class="certification-title">AWS Cloud Practitioner — Completion Certificate</div>', unsafe_allow_html=True)

    aws_path = Path("AWSCloudPractionerSS.png")
    if aws_path.exists():
        st.markdown("<div class='cert-card'>", unsafe_allow_html=True)
        # Increased size (was 400)
        st.image(str(aws_path), width=250)   # << increase/decrease here if you want
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(
            """
            **Issued by AWS Training & Certification**  
            Completed: *August 16, 2025*    
            I learned that AWS Cloud provides a wide 
            """
        )
    else:
        st.warning("Place **AWSCloudPractionerSS.png** in the same folder as `app.py` to display it here.")

# ---------- Page 4: Contact Me ----------
def page_contact():
    st.title("✉️ Contact Me")
    st.write("Send me a message and I’ll get back to you.")
    st.markdown("<hr/>", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message", height=160)
        submitted = st.form_submit_button("Send")

    if submitted:
        if not name or not email or not message:
            st.error("Please fill out all fields.")
        else:
            row = {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "name": name,
                "email": email,
                "message": message.replace("\\n", "  ")
            }
            csv_path = Path("contact_messages.csv")
            if csv_path.exists():
                df = pd.read_csv(csv_path)
                df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
            else:
                df = pd.DataFrame([row])
            df.to_csv(csv_path, index=False)
            st.success("Message sent! (Saved to contact_messages.csv)")

    # Show messages if file exists (local only)
    csv_path = Path("contact_messages.csv")
    if csv_path.exists():
        with st.expander("📥 View received messages (local file)"):
            df = pd.read_csv(csv_path)
            st.dataframe(df, use_container_width=True)

# ---------- Router ----------
if page == "About Me":
    page_about()
elif page == "My Projects":
    page_projects()
elif page == "My Certifications":
    page_certs()
else:
    page_contact()
