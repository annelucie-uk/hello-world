from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('user_preferences.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, date_of_birth TEXT, interests TEXT, daily_agenda TEXT)''')

conn.commit()

@app.route('/')
def index():
    return redirect(url_for('sign_in'))


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()

        if user is None:
            return "No user found for username and password", 401

        return f"Welcome back, {username}!"
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            date_of_birth = request.form['date_of_birth']
            interests = request.form['interests']
            daily_agenda = request.form['daily_agenda']

            if not username or not password:
                return "Username and password are required", 400

            c.execute("SELECT * FROM users WHERE username=?", (username,))
            if c.fetchone() is not None:
                return f"The username {username} is already taken. Please choose a different username.", 400

            c.execute("INSERT INTO users VALUES (?,?,?,?,?)", (username, password, date_of_birth, interests, daily_agenda))
            conn.commit()

            return f"User {username} created successfully!", 201

        return render_template('signup.html')
    except sqlite3.DatabaseError as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
