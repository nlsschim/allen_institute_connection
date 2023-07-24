import streamlit as st

# Function to update the value in session state
def clicked(button):
    st.session_state.clicked[button] = True