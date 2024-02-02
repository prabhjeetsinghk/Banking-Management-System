# app.py
import streamlit as st

from login import LOGIN
from signup import user_signup
from update import user_update

def my_python_function():
    # Replace this with your actual Python function logic
    return "Hello from Python function!"

# def main():
#     st.title("Streamlit App")

#     # Add a button to trigger the Python function
#     if st.button("Click me"):
#         result = my_python_function()
#         st.write(result)

def main_login():
    d1 = LOGIN()
    adminType, login_status, user_email = d1.user_login()
    if login_status:
        selection_after_login(adminType, user_email)
    else:
        main_login()

def selection_after_login(adminType, user_email):
    adminType = adminType
    email = user_email
    if adminType == 0:
        print("\t\t\t*******Select the o2peration to perform******\n")
        option = int(input("1. Credit\n2. Debit\n3. Update User Profile\n\n"))
        if option == 3:
            d3 = user_update()
            d3.update_user(email)
        else:
            print("Please select only from given options\n")
            selection_after_login(email)
    else:
        print("Hello Admin, Choose below operations")
        option = int(input("1. Add new user\n2. Update existing user"))
        signup()

def signup():
    d2 = user_signup()
    d2.add_user_details()
    selectoption()


def selectoption():
    # st.text("Select the operation below:\n1. Login\n2. Signup\n")
    if st.button("Login"):
        main_login()
    elif st.button("Signup"):
        signup_page = user_signup()
        signup_page.render()
        # signup()


if __name__ == '__main__':
    st.title("Welcome to Python Bank")
    # print("\n\n\n\t\t\t*******Welcome to Python Bank******\n")
    selectoption()

