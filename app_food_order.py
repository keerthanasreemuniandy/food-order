import streamlit as st

st.title("Food Ordering System")

# Food prices
prices = {
    "Nasi Lemak": 5.00,
    "Chicken Chop": 12.00,
    "Burger": 8.00
}

try:
    customer_name = st.text_input("Enter Customer Name")
    food_selection = st.selectbox("Select Food", list(prices.keys()))
    quantity = st.number_input("Enter Quantity", min_value=0, value=0, step=1)

    if st.button("Order"):
        
        # Validation Checks
        if not customer_name.strip():
            st.error("Error: Customer name cannot be empty.")
        elif quantity <= 0:
            st.error("Error: Quantity must be greater than 0.")
            
        else:
            # Price Calculation 
            unit_price = prices[food_selection]
            total_price = unit_price * quantity
            
            # Display order summary
            st.success("Order placed successfully!")
            st.write("--- Order Summary ---")
            st.write(f"Customer Name: {customer_name}")
            st.write(f"Food: {food_selection}")
            st.write(f"Quantity: {quantity}")
            st.write(f"Total Price: RM {total_price:.2f}")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

