from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

database_name = os.getenv('DATABASE_NAME')


app = Flask(__name__)

@app.route('/home/<email>', methods=['GET', 'POST'])
def home(email):
    conn = sqlite3.connect(database_name)
    cursor = conn.execute('''
            select user_name, user_email, user_phone, user_address, balance from user_data where user_email = (?)
        ''', (email, ))
    rows = cursor.fetchall()

    if not rows:
        # Handle the case when the user with the provided email is not found
        return render_template('error.html', message="User not found.")

    # Fetch user details from the user_data table (replace with your logic)
    user_details = {
        'user_name': rows[0][0],
        'user_email': rows[0][1],
        'user_phone': rows[0][2],
        'user_address': rows[0][3],
        'balance': rows[0][4]
    }

    return render_template('home.html', **user_details)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout/<email>',methods=['POST'])
def logout(email):
    conn = sqlite3.connect(database_name)
    cursor = conn.execute('''
            UPDATE user_data SET logged_in = 0 WHERE user_email = (?)
        ''', (email, ))
    rows = cursor.fetchall()

    if not rows:
        # Handle the case when the user with the provided email is not found
        return render_template('error.html', message="Please try again")

    conn.commit()    
    conn.close()

    return render_template('index.html')

@app.route('/view_transactions')
def view_transactions():
    return render_template('index.html')

@app.route('/make_transaction/<email>',methods=['GET', 'POST'])
def debit():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Extract data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']


        conn = sqlite3.connect(database_name)
        conn.execute('''
            INSERT INTO user_data (user_email, user_name, user_pwd, user_phone, user_address)
            VALUES (?, ?, ?, ?, ?)
        ''', (email, fullname, password, phone, address))
        conn.commit()
        conn.close()

        # return render_template('success.html', fullname=fullname)
        fullname = request.form['fullname']
        return jsonify({'success': True, 'fullname': fullname})
       
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(database_name)
        cursor = conn.execute('''
            SELECT user_pwd FROM user_data WHERE user_email = (?)
        ''', (email, ))
        rows = cursor.fetchall()
        user_pwd = rows[0][0]
        
        if user_pwd == password:
            now = datetime.now()
            timeValue = now.strftime("%Y-%m-%d %H:%M:%S")
            cursor = conn.execute('''
            UPDATE user_data SET logged_in = 1, last_logged_time = (?) WHERE user_email = (?)
        ''', (timeValue,email))
            conn.commit()
            conn.close()
            
            return  redirect(url_for('home', email=email))
        else:
            return jsonify({'success': False, 'message': 'Invalid email or password!'})

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)