import streamlit as st

# Title of the application
st.title("Movie Ticket Booking System")

try:
    # GUI Components for user input
    customer_name = st.text_input("Enter Customer Name")
    movie_title = st.selectbox("Select Movie Title", ["Avengers", "Kung Fu Panda", "Frozen"])
    show_time = st.selectbox("Select Show Time", ["10:00 AM", "2:00 PM", "8:00 PM"])
    seat_type = st.radio("Select Seat Type", ["Standard", "Premium"])

    # Action when the button is clicked
    if st.button("Book Ticket"):
        
        # Exception Handling / Validation
        if not customer_name.strip():
            st.error("Error: Customer name cannot be empty. Please enter your name.")
        else:
            # Display success message and booking summary
            st.success("Ticket booked successfully!")
            st.write("--- Booking Summary ---")
            st.write(f"Customer Name: {customer_name}")
            st.write(f"Movie Title: {movie_title}")
            st.write(f"Show Time: {show_time}")
            st.write(f"Seat Type: {seat_type}")

except Exception as e:
    # Catching any unexpected errors
    st.error(f"An unexpected error occurred: {e}")
