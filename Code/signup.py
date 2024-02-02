from Code.CreateDatabase import UserDatabase
from encdecString import encdec
from datetime import datetime
import re
import streamlit as st

def render_signup_page():  
    with st.form(key='signup_form'):              
        st.title('Register your account here!')
        user_name = st.text_input("Enter your name")
        user_email = st.text_input("Enter your email")
        user_pwd = st.text_input("Enter your password", type="password")
        confirm_pwd = st.text_input("Re-enter your password", type="password")            
        submitted = st.form_submit_button('Register User')
        st.write(user_email)
        if submitted:
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if re.match(email_regex, user_email) is not None:
                st.write('Email is valid')  

                if user_pwd == confirm_pwd:
                    db = UserDatabase()
                    cursor = db.getkeyvalue("select keyValue from keytable")
                    rows = cursor.fetchall()
                    st.write(rows)
                    key = rows[0][0]                        
                    st.write(key)    

                    enc = encdec(key=key)

                    hashed = enc.strEncoder(user_pwd)
                    print('Encoded password: ', hashed)
                    admin_type = 0
                    sql_query = "INSERT INTO user_data (user_id, user_name, user_pwd, admin_type) VALUES (?, ?, ?, ?)"
                    params = (user_email, user_name, hashed, admin_type)
                    result = db.add_user_details(query=sql_query,param=params)                        
                    if result.rowcount > 0:
                        balance = 0.0
                        add_balance_sql_query = "INSERT INTO account_balance (user_id, balance) VALUES (?,?)"
                        params = (user_email,balance)
                        db.update_balance(query=add_balance_sql_query, param=params)                            
                        current_datetime = datetime.now()
                        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        add_transaction_sql_query = "INSERT INTO transactions (user_id, transaction_time) VALUES (?, ?)"
                        params = (user_email, formatted_datetime)
                        db.update_trasaction(query=add_transaction_sql_query, param=params)
                    else:
                        st.write("Error occurred while adding user account")
                else:
                    st.error("Passwords do not match.")
            else:
                st.write("Invalid email format. Please enter a valid email address.") 
                st.error("Invalid email format. Please enter a valid email address.")

if __name__ == "__main__":
    render_signup_page()