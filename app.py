from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/reset_password', methods=['POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form.get('email')
        new_password = request.form.get('new_password')
        try:
            response = dbo.update_password(email, new_password)
            if response:
                return render_template("forgot_password.html", message="Password updated successfully. You can now log in.")
            else:
                return render_template("forgot_password.html", message="Failed to update password. Please try again later.")
            
        except Exception as e:
            print("Error:", e)
            return render_template('forgot_password.html', message="An error occurred. Please try again later.")

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        response = dbo.insert(name, email, password)
        if response:
            return redirect('/login')  
        else:
            return render_template('register.html', message="Email already exists")
    except Exception as e:
        return render_template('register.html', message="An error occurred while registering")

@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        response = dbo.search(email, password)
        if response:
            session['logged_in'] = True  
            return redirect('/profile')
        else:
            return render_template('login.html', message='Incorrect email/password')
    except Exception as e:
        return render_template('login.html', message='An error occurred while logging in')

@app.route('/profile')
def profile():
    if session.get('logged_in'):
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session.get('logged_in'):
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    if session.get('logged_in'):
        text = request.form.get('ner_text')
        try:
            response = api.ner(text)
            return render_template('ner.html', response=response)
        except Exception as e:
            return render_template('ner.html', message='An error occurred while performing NER')
    else:
        return redirect('/')
    


if __name__ == '__main__':
    app.run(debug=True)
