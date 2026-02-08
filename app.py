import streamlit as st
import json
import os

DATA_FILE = "data.json"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Data Structure Playground",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CSS STYLING ----------------
BG_IMAGE = "https://img.freepik.com/free-vector/white-abstract-background_23-2148810113.jpg"

st.markdown(f"""
<style>
/* 1. REMOVE TOP PADDING & BAR */
.block-container {{
    padding-top: 1.5rem !important;
}}

/* 2. PAGE BACKGROUND SETUP */
.stApp {{
    background-image: url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* 3. MAIN TITLE STYLING */
.main-title {{
    text-align: center;
    font-size: 50px;
    font-weight: 900;
    color: #111111;
    margin-bottom: 25px;
    font-family: 'Segoe UI', sans-serif;
}}



/* 5. HEAVY BOLD BLACK LABELS */
[data-testid="stWidgetLabel"] p {{
    font-size: 1.2rem !important;
    font-weight: 1000 !important;
    color: black !important;
    letter-spacing: 0.5px;
}}

/* 6. BLACK BOXES WITH WHITE TEXT */
div[data-baseweb="input"], div[data-baseweb="select"] > div {{
    background-color: black !important;
    border-radius: 12px !important;
    border: none !important;
}}

/* FORCED WHITE TEXT FOR SELECTBOX (STACK LIFO WORD) */
div[data-testid="stSelectbox"] div[data-baseweb="select"] div[data-testid="stMarkdownContainer"] p {{
    color: white !important;
}}

/* Alternative target for the selected value text */
div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
    color: white !important;
    -webkit-text-fill-color: white !important;
}}

/* FORCED WHITE TEXT FOR INPUT BOX */
input {{
    color: white !important;
    background-color: black !important;
    -webkit-text-fill-color: white !important;
    font-weight: 600 !important;
}}

/* Make the dropdown arrow white */
svg[data-testid="stIcon-ChevronDown"] {{
    fill: white !important;
}}

/* 7. BLACK BUTTONS STYLING */
.stButton>button {{
    width: 100%;
    border-radius: 12px;
    background-color: black;
    color: #FFFFFF !important;
    font-weight: bold;
    height: 50px;
    border: none;
    transition: 0.3s;
}}

.stButton>button:hover {{
    background-color: #333333;
    color: #FF4B4B !important;
}}

/* Hide Streamlit default elements */
header {{visibility: hidden;}}
footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA FUNCTIONS ----------------
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except:
            return {"stack": [], "queue": []}
    return {"stack": [], "queue": []}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

# ---------------- UI LAYOUT ----------------

st.markdown('<h1 class="main-title">Data Structure Playground</h1>', unsafe_allow_html=True)

# Start Card
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Inputs
structure_mode = st.selectbox("Select Structure Type", ["Stack (LIFO)", "Queue (FIFO)"])
user_val = st.text_input("Enter Value to Add", placeholder="Type here...")

st.markdown("<hr style='border: 1px solid #EEEEEE; margin: 25px 0;'>", unsafe_allow_html=True)

if "Stack" in structure_mode:
    st.markdown("### 📚 Stack Operations")
    c1, c2, c3 = st.columns(3)
    
    if c1.button("Push"):
        if user_val:
            data["stack"].append(user_val)
            save_data(data)
            st.rerun()
            
    if c2.button("Pop"):
        if data["stack"]:
            item = data["stack"].pop()
            save_data(data)
            st.toast(f"Popped: {item}")
            st.rerun()
            
    if c3.button("Clear Stack"):
        data["stack"] = []
        save_data(data)
        st.rerun()

    st.write("**Current Stack State:**")
    st.info(f"Top ➔ {data['stack'][::-1]}" if data['stack'] else "The Stack is empty.")

else:
    st.markdown("### 🚶 Queue Operations")
    c1, c2, c3 = st.columns(3)
    
    if c1.button("Enqueue"):
        if user_val:
            data["queue"].append(user_val)
            save_data(data)
            st.rerun()
            
    if c2.button("Dequeue"):
        if data["queue"]:
            item = data["queue"].pop(0)
            save_data(data)
            st.toast(f"Dequeued: {item}")
            st.rerun()
            
    if c3.button("Clear Queue"):
        data["queue"] = []
        save_data(data)
        st.rerun()

    st.write("**Current Queue State:**")
    st.info(f"Front ➔ {data['queue']}" if data['queue'] else "The Queue is empty.")

st.markdown('</div>', unsafe_allow_html=True)