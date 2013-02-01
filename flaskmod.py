'''
Created on 04/01/2013

@author: kalunga
'''
from flask import Flask, render_template, make_response, Flask, session, redirect, url_for, escape, request
from model import *
from appController import *

app = Flask(__name__)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username <> None:
            user = SessionManager.check_credentials(username)
            if user <> None:
                session['username'] = username
                return redirect(url_for('index'))
            return render_template('loginform.html', message='INVALID CREDENTIALS! Try again.')
    return render_template('loginform.html', message='')

@app.route('/index')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', user=username)
    return 'NOT Logged in'

if __name__ == '__main__':
    app.run(debug=True)

