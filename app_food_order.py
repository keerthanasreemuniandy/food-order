import streamlit as st

# Title
st.title("🍔 Food Ordering System")

# Input Fields
name = st.text_input("Enter Customer Name")

food = st.selectbox(
    "Select Food",
    ["Nasi Lemak (RM5)", "Chicken Chop (RM12)", "Burger (RM8)"]
)

quantity = st.number_input("Enter Quantity", min_value=0, step=1)

# Button
if st.button("Order"):
    try:
        # Validation
        if name.strip() == "":
            raise ValueError("Customer name cannot be empty!")

        if quantity <= 0:
            raise ValueError("Quantity must be more than 0!")

        # Price Logic
        if "Nasi Lemak" in food:
            price = 5
        elif "Chicken Chop" in food:
            price = 12
        elif "Burger" in food:
            price = 8

        total = price * quantity

        # Output
        st.success("✅ Order Successful!")

        st.subheader("🧾 Order Details")
        st.write(f"**Customer Name:** {name}")
        st.write(f"**Food Item:** {food}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Total Price:** RM {total:.2f}")

    except ValueError as e:
        st.error(f"❌ Error: {e}")

    except Exception as e:
        st.error(f"⚠ Unexpected Error: {e}")