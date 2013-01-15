'''
Created on 04/01/2013

@author: rafael.cunha
'''
from flask import Flask, render_template, make_response, Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

print __name__

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
        '''

@app.route('/index')
def index():
    if 'username' in session:
        user = session['username']
        return render_template('loggedin.html', user=user)
        #return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'    

if __name__ == '__main__':
    app.run(debug=True)

