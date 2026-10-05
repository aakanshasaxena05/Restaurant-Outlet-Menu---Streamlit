# 🍔 Restaurant Outlet Menu - Streamlit

## 📌 Project Overview

This project is an interactive **restaurant outlet menu web application** built using **Python and Streamlit**.

The application provides a user-friendly interface where customers can explore different food categories, select menu items, choose quantities, enter customer information, select an order type, choose a payment method, apply coupons, and place an order.

The project is designed as a **Streamlit learning and portfolio project** to demonstrate how Python can be used to build interactive web applications without directly writing HTML, CSS, or JavaScript.

> Note: This is a learning project inspired by the general concept of a fast-food outlet menu. It is not an official McDonald's application and does not use official McDonald's systems, branding assets, or ordering services.

---

# 🎯 Project Objectives

The main objectives of this project are:

* Learn the fundamentals of Streamlit.
* Create an interactive web application using Python.
* Understand Streamlit widgets.
* Learn how tabs work in Streamlit.
* Learn how to create a sidebar.
* Understand columns and page layouts.
* Create interactive forms.
* Handle user inputs.
* Display success, warning, error, and information messages.
* Display data using DataFrames.
* Create a restaurant-style menu interface.
* Practice conditional statements with Streamlit.
* Understand how buttons trigger actions.
* Build a foundation for future ML and data science applications.

---

# 🚀 Features

## 1. Home Tab

The Home tab provides an overview of the restaurant application.

It includes:

* Welcome message
* Today's orders
* Happy customers
* Available menu items
* Today's special
* Expandable special-offer details

Streamlit functions used:

```python
st.title()
st.caption()
st.header()
st.metric()
st.info()
st.expander()
```

---

# 🍔 2. Menu Tab

The Menu tab allows users to browse food categories.

Available categories include:

* Burgers
* Fries
* Beverages
* Desserts

The category is selected using:

```python
st.selectbox()
```

The displayed menu changes according to the selected category.

---

## 🍔 Burgers

The burger section contains:

* Classic Burger
* Cheese Burger
* Veg Burger

Users can:

* Select quantity
* Add items
* Receive a success message

Example:

```python
quantity = st.number_input(
    "Quantity",
    min_value=0,
    max_value=10
)
```

---

## 🍟 Fries

The fries section contains:

* Regular Fries
* Large Fries

Users can select the quantity using a slider.

```python
st.slider()
```

Example:

```python
fries_quantity = st.slider(
    "Select Quantity",
    0,
    10,
    1
)
```

---

## 🥤 Beverages

The beverage section allows users to select:

* Coke
* Sprite
* Fanta
* Iced Coffee

Users can also choose the size:

* Small
* Medium
* Large

The project uses:

```python
st.radio()
st.selectbox()
```

---

## 🍦 Desserts

Available desserts include:

* McFlurry
* Soft Serve
* Chocolate Sundae
* Apple Pie

Users can select multiple desserts using:

```python
st.multiselect()
```

The selected values are stored as a Python list.

Example:

```python
dessert = st.multiselect(
    "Select Desserts",
    [
        "McFlurry",
        "Soft Serve",
        "Chocolate Sundae",
        "Apple Pie"
    ]
)
```

---

# 🛒 3. Order Tab

The Order tab provides a basic ordering form.

Customers can enter:

* Customer name
* Phone number
* Delivery address
* Food items
* Quantity
* Payment method

The project uses several Streamlit widgets:

```python
st.text_input()
st.text_area()
st.multiselect()
st.number_input()
st.radio()
st.button()
```

---

## Customer Information

The user enters their name:

```python
name = st.text_input(
    "Customer Name"
)
```

Phone number:

```python
phone = st.text_input(
    "Phone Number"
)
```

Address:

```python
address = st.text_area(
    "Delivery Address"
)
```

---

## Selecting Items

Users can select multiple food items:

```python
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
```

---

## Payment Method

The user can select:

* Cash
* UPI
* Credit/Debit Card

using:

```python
st.radio()
```

---

## Order Validation

The application checks whether the customer has entered the required information.

For example:

```python
if not name:
    st.error("Please enter your name.")
```

If no food item is selected:

```python
elif not items:
    st.warning(
        "Please select at least one item."
    )
```

If all required information is available:

```python
st.success(
    "Order placed successfully!"
)
```

---

# 🎁 4. Offers Tab

The Offers tab displays special restaurant deals.

It uses:

```python
st.metric()
```

to display:

* Burger Combo
* Large Fries
* Dessert Combo

Example:

```python
st.metric(
    "Burger Combo",
    "₹199",
    "Save ₹50"
)
```

---

# 🏷️ Coupon System

The application includes a basic coupon system.

The user enters a coupon code:

```python
coupon = st.text_input(
    "Enter Coupon Code"
)
```

The application checks the entered value:

```python
if coupon.upper() == "MCD50":
    st.success(
        "Coupon applied! ₹50 discount."
    )
else:
    st.error(
        "Invalid coupon code."
    )
```

The example coupon is:

```text
MCD50
```

This is only a demonstration for the project and is not an actual restaurant coupon.

---

# ℹ️ 5. About Tab

The About tab provides information about the outlet.

It displays:

* Selected city
* Order type
* Opening hours
* Project description

The opening hours are stored in a Pandas DataFrame.

Example:

```python
opening_hours = pd.DataFrame(
    {
        "Day": ["Monday", "Tuesday"],
        "Opening": ["9:00 AM", "9:00 AM"],
        "Closing": ["11:00 PM", "11:00 PM"]
    }
)
```

The DataFrame is displayed using:

```python
st.dataframe()
```

---

# 📊 Streamlit Concepts Demonstrated

This project covers many important Streamlit concepts.

| Streamlit Function     | Purpose                               |
| ---------------------- | ------------------------------------- |
| `st.set_page_config()` | Configure page title, icon and layout |
| `st.title()`           | Display main title                    |
| `st.header()`          | Display section heading               |
| `st.subheader()`       | Display subsection heading            |
| `st.write()`           | Display text and values               |
| `st.caption()`         | Display small supporting text         |
| `st.info()`            | Display information                   |
| `st.success()`         | Display success message               |
| `st.warning()`         | Display warning message               |
| `st.error()`           | Display error message                 |
| `st.sidebar`           | Create sidebar elements               |
| `st.tabs()`            | Create multiple tabs                  |
| `st.columns()`         | Divide page into columns              |
| `st.expander()`        | Create expandable sections            |
| `st.metric()`          | Display KPIs/metrics                  |
| `st.text_input()`      | Accept text input                     |
| `st.number_input()`    | Accept numerical input                |
| `st.text_area()`       | Accept multi-line text                |
| `st.selectbox()`       | Create dropdown                       |
| `st.radio()`           | Select one option                     |
| `st.checkbox()`        | Create checkbox                       |
| `st.multiselect()`     | Select multiple options               |
| `st.slider()`          | Select a value from a range           |
| `st.button()`          | Create clickable button               |
| `st.dataframe()`       | Display interactive data              |
| `st.divider()`         | Separate sections                     |

---

# 🧠 Concepts Learned

This project demonstrates the following Python and Streamlit concepts.

## Python Concepts

* Variables
* Lists
* Dictionaries
* Conditional statements
* `if`, `elif`, `else`
* Functions
* Importing libraries
* Pandas DataFrames
* String methods
* Boolean conditions

## Streamlit Concepts

* Streamlit application structure
* Page configuration
* Widgets
* Tabs
* Sidebar
* Columns
* Containers
* Expanders
* Metrics
* Forms-like input handling
* User interaction
* Conditional UI
* Data display
* Status messages

---

# 🏗️ Application Architecture

The application follows this general flow:

```text
                    USER
                      |
                      ↓
             STREAMLIT APPLICATION
                      |
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
     Sidebar         Tabs          Layout
        |             |             |
        ↓             ↓             ↓
 Customer Info    Home/Menu      Columns
 City             Order          Expander
 Order Type       Offers         Metrics
        |          About
        |             |
        └──────┬──────┘
               ↓
             Widgets
               |
      ┌────────┼─────────┐
      ↓        ↓         ↓
    Input    Selection   Button
      |        |         |
      └────────┼─────────┘
               ↓
        Conditional Logic
               ↓
      Success / Warning /
       Error / Information
```

---

# 📁 Project Structure

A simple project structure is:

```text
restaurant-menu/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the complete Streamlit application.

### `requirements.txt`

Contains the Python libraries required to run the project.

Example:

```text
streamlit
pandas
```

### `README.md`

Contains documentation about the project.

---

# ⚙️ Installation

## Step 1: Install Python

Make sure Python is installed on your system.

Check the version:

```bash
python --version
```

---

## Step 2: Install Streamlit

Open Command Prompt or PowerShell:

```bash
pip install streamlit
```

---

## Step 3: Install Pandas

```bash
pip install pandas
```

---

# ▶️ Running the Application

Navigate to the project directory:

```bash
cd path/to/restaurant-menu
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will start a local server.

The application can usually be accessed through:

```text
http://localhost:8501
```

or:

```text
http://127.0.0.1:8501
```

---

# 🖥️ Application Workflow

The application works in the following sequence:

```text
1. Open application
       ↓
2. Enter customer information
       ↓
3. Select city
       ↓
4. Select order type
       ↓
5. Open Menu tab
       ↓
6. Select food category
       ↓
7. Select food items
       ↓
8. Open Order tab
       ↓
9. Enter customer details
       ↓
10. Select payment method
       ↓
11. Click Place Order
       ↓
12. Validate information
       ↓
13. Display order confirmation
```

---

# 🎨 User Interface

The application is divided into five main sections:

```text
┌───────────────────────────────────────────────┐
│              🍔 Restaurant Menu               │
├───────────────────────────────────────────────┤
│ 🏠 Home | 🍔 Menu | 🛒 Order | 🎁 Offers | ℹ️ About │
├───────────────────────────────────────────────┤
│                                               │
│              Selected Tab Content              │
│                                               │
└───────────────────────────────────────────────┘
```

The sidebar contains:

```text
Menu
──────────────
Customer Name
City
Order Type
Special Offer
```

---

# 🔧 Technologies Used

## Python

Used as the main programming language.

## Streamlit

Used to create the interactive web application.

## Pandas

Used for creating and displaying the opening-hours DataFrame.

---

# 📦 Libraries Used

```python
import streamlit as st
import pandas as pd
```

---

# 💡 Why Streamlit?

Streamlit was selected because it makes it easy to build interactive applications using Python.

Traditional web development may require:

```text
HTML
CSS
JavaScript
Backend
```

Streamlit allows a Python developer to create an interactive application with much less frontend code.

For example:

```python
st.title("Restaurant Menu")
```

can immediately display a title in the web application.

---

# 🔍 Key Learning: Widgets

A major part of this project is understanding Streamlit widgets.

A widget is an interactive element that allows the user to provide input or perform an action.

Examples used in this project:

```python
st.text_input()
st.number_input()
st.text_area()
st.selectbox()
st.radio()
st.checkbox()
st.multiselect()
st.slider()
st.button()
```

The general concept is:

```text
User Input
     ↓
Streamlit Widget
     ↓
Python Variable
     ↓
Conditional Logic
     ↓
Output
```

Example:

```python
name = st.text_input("Enter Name")

if name:
    st.success("Name entered successfully!")
```

---

# 🔄 Conditional Logic

The application uses Python conditional statements to control what appears on the page.

Example:

```python
if category == "Burgers":
    # Show burgers

elif category == "Fries":
    # Show fries

elif category == "Beverages":
    # Show beverages

else:
    # Show desserts
```

This creates a dynamic application.

The content changes according to the user's selection.

---

# 📈 Future Improvements

This project can be extended into a more advanced restaurant application.

Possible improvements include:

## 1. Shopping Cart

Add a proper cart where users can:

* Add products
* Remove products
* Change quantity
* Calculate total price

---

## 2. Total Bill Calculation

Automatically calculate:

```text
Subtotal
+ Taxes
+ Delivery Charges
- Discount
= Final Amount
```

---

## 3. Database Integration

Connect the application to:

* MySQL
* SQLite
* PostgreSQL

Customer orders could then be stored permanently.

---

## 4. FastAPI Backend

A FastAPI backend can be added.

Architecture:

```text
User
 ↓
Streamlit
 ↓
FastAPI
 ↓
Database
```

---

## 5. User Authentication

Add:

* Login
* Signup
* Admin login
* Customer accounts

---

## 6. Order Tracking

Add order statuses such as:

```text
Order Placed
     ↓
Preparing
     ↓
Ready
     ↓
Out for Delivery
     ↓
Delivered
```

---

## 7. Machine Learning

Machine learning can be added for:

* Food recommendation
* Customer segmentation
* Sales prediction
* Demand forecasting
* Personalized recommendations

For example:

```text
Customer History
       ↓
ML Model
       ↓
Recommended Items
```

---

## 8. Payment Integration

A real application could integrate a payment gateway.

This project does not process real payments.

---

# 🧪 Testing

The following scenarios can be tested:

### Test 1: Empty Name

Expected result:

```text
Please enter your name.
```

### Test 2: No Item Selected

Expected result:

```text
Please select at least one item.
```

### Test 3: Valid Order

Expected result:

```text
Order placed successfully!
```

### Test 4: Valid Coupon

Coupon:

```text
MCD50
```

Expected result:

```text
Coupon applied! ₹50 discount.
```

### Test 5: Invalid Coupon

Expected result:

```text
Invalid coupon code.
```

---

# 📚 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python
* Streamlit
* Pandas
* Interactive UI development
* Data handling
* User input handling
* Conditional logic
* Dashboard development
* Web application development
* Basic application validation
* UI layout design

---

# 🎓 Learning Outcome

After completing this project, you should understand:

1. What Streamlit is.
2. How to create a Streamlit application.
3. How to run a Streamlit application.
4. How to create titles and headings.
5. How to display text.
6. How to create interactive widgets.
7. How to collect user input.
8. How to use buttons.
9. How to create tabs.
10. How to create sidebars.
11. How to use columns.
12. How to use expanders.
13. How to display metrics.
14. How to display DataFrames.
15. How to display success/error/warning messages.
16. How to use conditional logic in Streamlit.
17. How to build a basic interactive business application.

---

# 💼 Resume Description

### Restaurant Outlet Menu – Streamlit

Developed an interactive restaurant outlet menu web application using Python and Streamlit. Implemented multi-tab navigation, sidebar controls, interactive widgets, menu categories, customer order forms, coupon validation, metrics, expandable sections, conditional logic, and Pandas-based data display. Designed the application to demonstrate practical Streamlit concepts and interactive UI development.

---

# 🚀 Conclusion

This project demonstrates how **Streamlit can be used to convert Python code into an interactive web application**.

The application combines:

```text
Python
   +
Streamlit
   +
Pandas
   +
Interactive Widgets
   +
Conditional Logic
   =
Interactive Restaurant Application
```

It also provides a strong foundation for building more advanced applications such as:

* ML prediction apps
* Data dashboards
* Business analytics applications
* Recommendation systems
* FastAPI + Streamlit applications
* Database-connected applications

---

# 👩‍💻 Author

**Aakansha Saxena**

GitHub: `github.com/aakanshasaxena05`

---

# ⭐ Project Status

**Status:** Completed – Learning/Portfolio Project

Future versions can include database integration, authentication, shopping cart functionality, real-time order tracking, FastAPI backend integration, and machine-learning-based recommendations.
