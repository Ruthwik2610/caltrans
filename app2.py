import streamlit as st
import time

# Define your app key (for simplicity, hardcoded here)
APP_KEY = "abcd"

# Store authentication status in Streamlit session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Function to check app key and authenticate user
def authenticate(key):
    if key == APP_KEY:
        st.session_state.authenticated = True
        st.session_state.auth_time = time.time()  # Store the time of authentication

# If user is not authenticated, prompt for the app key
if not st.session_state.authenticated:
    st.write("Please enter the app key to access the application:")
    app_key_input = st.text_input("App Key", type="password")
    if st.button("Submit"):
        authenticate(app_key_input)


print("time - ",time.time() - st.session_state.auth_time)
# Check the time since last authentication and prompt again if 3 minutes have passed
if time.time() - st.session_state.auth_time > 180:
    st.session_state.authenticated = False
    st.write("Your session has expired. Please enter the app key again.")
else:
    # If authenticated, show the main app
    if st.session_state.authenticated:
        st.write("Welcome to the app!")
        test = st.button("Button")
        if test:
            st.write("Button Clicked!")

    
