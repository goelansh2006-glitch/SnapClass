import streamlit as st

def style_background_home():
    st.markdown("""
        <style>

            .stApp{
                background: #0F172A !important;
            }

            /* Prevent scrollbar and scrolling on the landing page */
            html, body, [data-testid="stAppViewContainer"], .main {
                overflow: hidden !important;
                height: 100vh !important;
            }

            /* Hide scrollbars across browsers */
            ::-webkit-scrollbar {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
            }
            * {
                scrollbar-width: none !important;
                -ms-overflow-style: none !important;
            }

            /* SnapClass Heading on Dark Background - Academic / College Crisp White */
            .snapclass-title, h1 {
                color: #FFFFFF !important;
                font-family: 'Sora', sans-serif !important;
                font-size: 2.8rem !important;
                font-weight: 700 !important;
                letter-spacing: -0.5px !important;
                text-shadow: 0 2px 10px rgba(0, 0, 0, 0.4) !important;
            }

            /* Refined and responsive card styling */
            .stApp div[data-testid="stColumn"]{
                background-color: #F5F5DC !important;
                padding: 1.5rem 1.8rem !important;
                border-radius: 2.5rem !important;
                text-align: center !important;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4) !important;
            }

            .stApp div[data-testid="stColumn"] h2 {
                color: #1E293B !important;
                font-size: 1.7rem !important;
                margin-bottom: 0.5rem !important;
                font-weight: 700 !important;
            }

            /* Center images and buttons inside cards */
            .stApp div[data-testid="stColumn"] [data-testid="stImage"] {
                display: flex !important;
                justify-content: center !important;
                margin-bottom: 0.4rem !important;
            }

            .stApp div[data-testid="stColumn"] div.stButton {
                display: flex !important;
                justify-content: center !important;
                margin-top: 0.4rem !important;
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

            h1 {
                color: #263746 !important;
            }
        </style>
        """,
        unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Sora:wght@100..800&display=swap');
        /* Hide Top Bar and Header of streamlit completely so they occupy 0 height */
                
            #MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"] {
                display: none !important;
                visibility: hidden !important;
                height: 0 !important;
            }

            /* Hide scrollbars across the entire app */
            ::-webkit-scrollbar {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
            }
            * {
                scrollbar-width: none !important;
                -ms-overflow-style: none !important;
            }

            .block-container{
                padding-top: 1rem !important;
                padding-bottom: 0rem !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
                max-width: 850px !important;
            }

            h1 {
                font-family: 'Sora', sans-serif !important;
                font-size: 2.8rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0.5rem !important;
                color: #FFFFFF !important;
                opacity: 1 !important;
                visibility: visible !important;
            }

            h2 {
                font-family: 'Sora', sans-serif !important;
                font-size: 1.8rem !important;
                line-height: 1.2 !important;
                margin-bottom: 0.8rem !important;
                color: #1E293B !important;
                opacity: 1 !important;
                visibility: visible !important;
            }

            h3 ,h4, p {
                font-family: 'Outfit', sans-serif;
                color: black;
            }

            /* White Input Boxes for all text and password fields */
            div[data-testid="stTextInput"] div[data-baseweb="base-input"],
            div[data-testid="stTextInput"] div[data-baseweb="input"],
            div[data-testid="stTextInput"] input {
                background-color: #FFFFFF !important;
                color: #1E293B !important;
                -webkit-text-fill-color: #1E293B !important;
            }

            div[data-testid="stTextInput"] div[data-baseweb="base-input"] {
                background-color: #FFFFFF !important;
                border: 1.5px solid #CBD5E1 !important;
                border-radius: 0.75rem !important;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
            }

            div[data-testid="stTextInput"] div[data-baseweb="base-input"]:focus-within {
                border-color: #5865F2 !important;
                box-shadow: 0 0 0 3px rgba(88, 101, 242, 0.2) !important;
            }

            div[data-testid="stTextInput"] input {
                border-radius: 0.75rem !important;
                padding: 0.5rem 0.75rem !important;
                font-size: 1rem !important;
            }

            div[data-testid="stTextInput"] input::placeholder {
                color: #94A3B8 !important;
                -webkit-text-fill-color: #94A3B8 !important;
            }

            /* Password reveal button inside the text input */
            div[data-testid="stTextInput"] button {
                background-color: transparent !important;
                color: #64748B !important;
                border-radius: 0 !important;
                padding: 0 10px !important;
                border: none !important;
                box-shadow: none !important;
            }

            div[data-testid="stTextInput"] button:hover {
                transform: none !important;
                color: #1E293B !important;
                background-color: transparent !important;
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
                transform :scale(1.05);
            }

        </style>
        """,
        unsafe_allow_html=True)