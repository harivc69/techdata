import streamlit as st
import requests

# Backend API URLs
BACKEND_BASE_URL = "http://127.0.0.1:8000"  # Replace with your hosted backend URL if deployed
ADD_CLIENT_URL = f"{BACKEND_BASE_URL}/add_client/"
GET_CLIENT_URL = f"{BACKEND_BASE_URL}/get_client/"

# Streamlit Application
st.title("Client Management System")

# Add Client Section
st.header("Add Client")
with st.form("add_client_form"):
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    submit_add = st.form_submit_button("Add Client")

    if submit_add:
        if name and phone and email:
            # Call the backend API to add the client
            response = requests.post(
                ADD_CLIENT_URL,
                json={"name": name, "phone": phone, "email": email}
            )
            if response.status_code == 200:
                st.success("Client added successfully!")
            else:
                st.error(f"Failed to add client: {response.text}")
        else:
            st.warning("All fields are required!")

# Search Client Section
st.header("Search Client")
search_phone = st.text_input("Enter phone number to search:")
if st.button("Search"):
    if search_phone:
        # Call the backend API to get client details
        response = requests.get(f"{GET_CLIENT_URL}{search_phone}")
        if response.status_code == 200:
            client_data = response.json()
            st.write("Client Details:")
            st.json(client_data)
        else:
            st.error(f"Client not found: {response.text}")
    else:
        st.warning("Please enter a phone number.")

