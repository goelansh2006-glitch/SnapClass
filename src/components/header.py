import streamlit as st
from pathlib import Path
import base64

def header_home():

    logo_path = Path(__file__).parent / "img" / "logohome.png"

    
    with open(logo_path, "rb") as f:
        logo_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
    <img
                src="data:image/png;base64,{logo_data}"
                style="
                    height: 150px;
                    width:auto;
                    object-fit:contain;
                "
            />
    <h1 style='text-align:center; color:#E0E3FF'>SnapClass</h1>
    </div>
    """, unsafe_allow_html=True)
   

def header_dashboard():

    logo_path = Path(__file__).parent / "img" / "logohome.png"

    
    with open(logo_path, "rb") as f:
        logo_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center; gap=10px;">
    <img
                src="data:image/png;base64,{logo_data}"
                style="
                    height: 85px;
                    width:auto;
                    object-fit:contain;
                "
            />
    <h2 style='text-align:left; color:#36454F'>SnapClass</h2>
    </div>
    """, unsafe_allow_html=True)