
import streamlit as st
import pandas as pd


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="McDonald's Outlet Menu",
    page_icon="🍔",
    layout="wide"
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🍔 McDonald's Outlet Menu")
st.caption("Welcome! Explore our menu and place your order.")


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🍟 Menu")

customer_name = st.sidebar.text_input(
    "Enter your name"
)

city = st.sidebar.selectbox(
    "Select your city",
    ["Jaipur", "Delhi", "Mumbai", "Bangalore"]
)

delivery = st.sidebar.radio(
    "Order Type",
    ["Dine In", "Takeaway", "Delivery"]
)

offers = st.sidebar.checkbox(
    "Apply special offer"
)


# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🏠 Home",
        "🍔 Menu",
        "🛒 Order",
        "🎁 Offers",
        "ℹ️ About"
    ]
)


# =========================================================
# TAB 1 - HOME
# =========================================================

with tab1:

    st.header("Welcome to McDonald's Outlet")

    st.write(
        "Enjoy burgers, fries, beverages and desserts."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Today's Orders",
            "250",
            "+12%"
        )

    with col2:
        st.metric(
            "Happy Customers",
            "1,200",
            "+8%"
        )

    with col3:
        st.metric(
            "Available Items",
            "20"
        )

    st.divider()

    st.subheader("Today's Special")

    st.info(
        "🍔 Get a burger + fries + drink combo at a special price!"
    )

    with st.expander("View Special Details"):

        st.write("Special Combo")
        st.write("Burger")
        st.write("French Fries")
        st.write("Soft Drink")
        st.write("Special Price: ₹199")


# =========================================================
# TAB 2 - MENU
# =========================================================

with tab2:

    st.header("🍔 Our Menu")

    category = st.selectbox(
        "Select Category",
        [
            "Burgers",
            "Fries",
            "Beverages",
            "Desserts"
        ]
    )

    # -----------------------------------------------------
    # BURGERS
    # -----------------------------------------------------

    if category == "Burgers":

        st.subheader("🍔 Burgers")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.subheader("Classic Burger")
            st.write("Price: ₹129")

            quantity1 = st.number_input(
                "Quantity",
                min_value=0,
                max_value=10,
                key="burger1"
            )

            if st.button(
                "Add Classic Burger",
                key="add1"
            ):
                st.success("Classic Burger added!")

        with col2:

            st.subheader("Cheese Burger")
            st.write("Price: ₹159")

            quantity2 = st.number_input(
                "Quantity",
                min_value=0,
                max_value=10,
                key="burger2"
            )

            if st.button(
                "Add Cheese Burger",
                key="add2"
            ):
                st.success("Cheese Burger added!")

        with col3:

            st.subheader("Veg Burger")
            st.write("Price: ₹149")

            quantity3 = st.number_input(
                "Quantity",
                min_value=0,
                max_value=10,
                key="burger3"
            )

            if st.button(
                "Add Veg Burger",
                key="add3"
            ):
                st.success("Veg Burger added!")


    # -----------------------------------------------------
    # FRIES
    # -----------------------------------------------------

    elif category == "Fries":

        st.subheader("🍟 Fries")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Regular Fries")
            st.write("Price: ₹99")

            fries_quantity = st.slider(
                "Select Quantity",
                0,
                10,
                1
            )

            if st.button("Add Fries"):

                st.success(
                    "Fries added to your order!"
                )

        with col2:

            st.subheader("Large Fries")
            st.write("Price: ₹129")

            large_fries = st.slider(
                "Select Quantity",
                0,
                10,
                1,
                key="large_fries"
            )

            if st.button(
                "Add Large Fries"
            ):

                st.success(
                    "Large Fries added!"
                )


    # -----------------------------------------------------
    # BEVERAGES
    # -----------------------------------------------------

    elif category == "Beverages":

        st.subheader("🥤 Beverages")

        drink = st.radio(
            "Select Beverage",
            [
                "Coke",
                "Sprite",
                "Fanta",
                "Iced Coffee"
            ]
        )

        size = st.selectbox(
            "Select Size",
            [
                "Small",
                "Medium",
                "Large"
            ]
        )

        st.write(
            "Selected:",
            drink,
            "-",
            size
        )

        if st.button("Add Beverage"):

            st.success(
                f"{drink} ({size}) added!"
            )


    # -----------------------------------------------------
    # DESSERTS
    # -----------------------------------------------------

    else:

        st.subheader("🍦 Desserts")

        dessert = st.multiselect(
            "Select Desserts",
            [
                "McFlurry",
                "Soft Serve",
                "Chocolate Sundae",
                "Apple Pie"
            ]
        )

        st.write(
            "Selected Desserts:",
            dessert
        )

        if st.button("Add Desserts"):

            if dessert:

                st.success(
                    "Desserts added!"
                )

            else:

                st.warning(
                    "Please select a dessert."
                )


# =========================================================
# TAB 3 - ORDER
# =========================================================

with tab3:

    st.header("🛒 Place Your Order")

    st.subheader("Customer Information")

    name = st.text_input(
        "Customer Name",
        value=customer_name
    )

    phone = st.text_input(
        "Phone Number"
    )

    address = st.text_area(
        "Delivery Address"
    )

    st.divider()

    st.subheader("Select Items")

    items = st.multiselect(
        "Choose your items",
        [
            "Classic Burger",
            "Cheese Burger",
            "Veg Burger",
            "Regular Fries",
            "Large Fries",
            "Coke",
            "McFlurry",
            "Apple Pie"
        ]
    )

    quantity = st.number_input(
        "Total Quantity",
        min_value=1,
        max_value=20,
        value=1
    )

    payment = st.radio(
        "Payment Method",
        [
            "Cash",
            "UPI",
            "Credit/Debit Card"
        ]
    )

    st.divider()

    if st.button(
        "🍔 Place Order",
        type="primary"
    ):

        if not name:

            st.error(
                "Please enter your name."
            )

        elif not items:

            st.warning(
                "Please select at least one item."
            )

        else:

            st.success(
                "Order placed successfully!"
            )

            st.write(
                "Customer:",
                name
            )

            st.write(
                "Order Type:",
                delivery
            )

            st.write(
                "Items:",
                items
            )

            st.write(
                "Quantity:",
                quantity
            )

            st.write(
                "Payment:",
                payment
            )

            st.write(
                "Outlet:",
                city
            )


# =========================================================
# TAB 4 - OFFERS
# =========================================================

with tab4:

    st.header("🎁 Special Offers")

    st.subheader("Today's Deals")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Burger Combo",
            "₹199",
            "Save ₹50"
        )

    with col2:

        st.metric(
            "Large Fries",
            "₹99",
            "Save ₹30"
        )

    with col3:

        st.metric(
            "Dessert Combo",
            "₹149",
            "Save ₹40"
        )

    st.divider()

    coupon = st.text_input(
        "Enter Coupon Code"
    )

    if st.button("Apply Coupon"):

        if coupon.upper() == "MCD50":

            st.success(
                "Coupon applied! ₹50 discount."
            )

        else:

            st.error(
                "Invalid coupon code."
            )


# =========================================================
# TAB 5 - ABOUT
# =========================================================

with tab5:

    st.header("ℹ️ About Our Outlet")

    st.write(
        "This is a Streamlit-based restaurant menu application."
    )

    st.subheader("Outlet Information")

    st.write("City:", city)
    st.write("Order Type:", delivery)

    st.divider()

    st.subheader("Opening Hours")

    opening_hours = pd.DataFrame(
        {
            "Day": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ],
            "Opening": [
                "9:00 AM",
                "9:00 AM",
                "9:00 AM",
                "9:00 AM",
                "9:00 AM",
                "9:00 AM",
                "9:00 AM"
            ],
            "Closing": [
                "11:00 PM",
                "11:00 PM",
                "11:00 PM",
                "11:00 PM",
                "12:00 AM",
                "12:00 AM",
                "11:00 PM"
            ]
        }
    )

    st.dataframe(
        opening_hours,
        use_container_width=True
    )

    st.divider()

    st.caption(
        "This project is created for Streamlit learning and practice."
    )

