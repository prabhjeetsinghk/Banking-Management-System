from login import LOGIN
from signup import user_signup
from update import user_update

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
        print("\t\t\t*******Select the operation to perform******\n")
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
    option = int(input("Select the operation below:\n1. Login\n2. Signup\n"))
    if option == 1:
        main_login()
    elif option == 2:
        signup()
    else:
        print("Please enter correct option\n")
        selectoption()


if __name__ == '__main__':
    print("\n\n\n\t\t\t*******Welcome to Python Bank******\n")
    selectoption()
