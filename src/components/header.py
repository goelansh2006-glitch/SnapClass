import streamlit as st
from pathlib import Path
import base64

def header_home():

    logo_path = Path(__file__).parent / "img" / "logohome.png"

    
    with open(logo_path, "rb") as f:
        logo_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:12px; margin-top:8px">
    <img
                src="data:image/png;base64,{logo_data}"
                style="
                    height: 110px;
                    width:auto;
                    object-fit:contain;
                    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.3));
                "
            />
    <h1 class="snapclass-title" style='text-align:center; color:#FFFFFF !important; margin:6px 0 0 0;'>SnapClass</h1>
    </div>
    """, unsafe_allow_html=True)
   

def header_dashboard():

    logo_path = Path(__file__).parent / "img" / "logohome.png"

    
    with open(logo_path, "rb") as f:
        logo_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
    <img
                src="data:image/png;base64,{logo_data}"
                style="
                    height: 70px;
                    width:auto;
                    object-fit:contain;
                "
            />
    <h2 style='text-align:left; color:#36454F; margin:0;'>SnapClass</h2>
    </div>
    """, unsafe_allow_html=True)