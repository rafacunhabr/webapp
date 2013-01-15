'''
Created on 04/01/2013

@author: kalunga
'''
from flask import Flask, render_template, make_response, Flask, session, redirect, url_for, escape, request
from model import *

app = Flask(__name__)

print __name__

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('loginform.html')

@app.route('/index')
def index():
    if 'username' in session:
        username = session['username']
        user1 = ''
        app.logger.warning('esta inicializado? ' + str(Core.is_initialized()))
        Core.initialize()
        for user in User.objects(first_name = username):
            user1 = user
            break 
        return render_template('index.html', user=user1)
        #return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'    


if __name__ == '__main__':
    app.run(debug=True)

