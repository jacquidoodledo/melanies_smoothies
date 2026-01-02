from streamlit_pages import Page, navigation

# Define your pages
pages = [
    Page("pages/order_request_form.py", "Home", "🏠"),
    Page("pages/order_fulfillment.py", "Fulfillment", "📊"),
]

# Initialize and run navigation
app = navigation.StreamlitNavigation(pages, initial_page="Home")
app.run()