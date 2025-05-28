from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/flagged')
def flagged():
    return render_template('flagged.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/random')
def random():
    return render_template('random.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

if __name__ == '__main__':
    app.run(debug=True)