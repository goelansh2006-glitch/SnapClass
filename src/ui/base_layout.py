import streamlit as st

def style_background_home():
    st.markdown("""
        <style>

            .stApp{
                background: #0F172A   !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color:#F5F5DC !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>

            .stApp{
                background: #D8F9FF   !important;
            }
        </style>
        """,
        unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Sora:wght@100..800&display=swap');
        /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container{
            padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Sora', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 1rem !important;
                color: #263746 !important;
                opacity: 1 !important;
                visibility: visible !important;
            }

            h2 {
                font-family: 'Sora', sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.2 !important;
                margin-bottom: 1rem !important;
                color: #36454F !important;
                opacity: 1 !important;
                visibility: visible !important;
            }

            h3 ,h4, p {
            font-family: 'Outfit', sans-serif;
            color:black;
            }

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
            .stApp label {
                color: #263746 !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 500 !important;
            }

            button:hover{
                transform :scale(1.05)}

        </style>
        """,
        unsafe_allow_html=True)