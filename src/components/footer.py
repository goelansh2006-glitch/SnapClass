import streamlit as st

def footer_home():

    st.markdown(f"""
    <div style="margin-top:0.75rem; display:flex; gap:6px; justify-content:center; align-items:center">
    <p style="font-weight:600; color:#94A3B8; font-size:0.9rem; margin:0;"> Created with ❤️ by Ansh Goel </p>
    </div>
    """, unsafe_allow_html=True)
   

def footer_dashboard():

    st.markdown(f"""
    <div style="margin-top:1rem; display:flex; gap:6px; justify-content:center; align-items:center">
    <p style="font-weight:bold; color:black; margin:0;"> Created with ❤️ by Ansh Goel </p>
    </div>
    """, unsafe_allow_html=True)