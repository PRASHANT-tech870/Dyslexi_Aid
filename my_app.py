import streamlit as st
from chatbot import app1
from readaloud import app2

# Custom CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .sidebar .sidebar-content .block-container {
        padding-top: 20px;
    }
    .sidebar .sidebar-content .stButton button {
        color: white;
        background-color: #2e7bcf;
        border: none;
    }
    .st-radio label {
        font-size: 18px;
        margin-right: 10px;
    }
    .st-radio input {
        width: 18px;
        height: 18px;
    }
    @keyframes slideIn {
        0% { transform: translateY(-100%); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    .welcome-note {
        animation: slideIn 2s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    app_choice = st.sidebar.radio("Go to", ("Home", "AI Chatbot", "AI Reading Assistant"))

    if app_choice == "Home":
        st.markdown("""
            <div class="welcome-note">
                <h1>Welcome to the Main Application</h1>
                <p>Use the sidebar to navigate to different applications.</p>
            </div>
        """, unsafe_allow_html=True)
    elif app_choice == "App 1":
        app1()
    elif app_choice == "App 2":
        app2()

if __name__ == "__main__":
    main()
