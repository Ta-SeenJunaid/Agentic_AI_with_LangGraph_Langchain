import streamlit as st
from src.langgraph_agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgraph_agentic_app():
    """
    Loads and runs the LangGraph Agentic AI Streamlit application.
    """

    ui=LoadStreamlitUI()
    loaded_ui=ui.load_streamlit_ui()

    if not loaded_ui:
        st.error("Failed to load the UI components.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        pass