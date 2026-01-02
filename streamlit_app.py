import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

pages = [
    Page("pages/order_request_form.py", "Home", "🏠"),
    Page("pages/order_fulfillment.py", "Fulfillment", "📊"),
]

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a page above.")
