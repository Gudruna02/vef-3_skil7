from flask import Flask, render_template, session, url_for, request, redirect, escape
import os
from pymysql import *

app = Flask(__name__)
app.secret_key = os.urandom(69)

pwd = "popcorn3002"
connection = connect(host='tsuts.tskoli.is', port=3306, user='1805023780', password=pwd, database='1805023780_verk7', autocommit=True)


#with connection.cursor() as cursor:
#        cursor.execute("SELECT * FROM users")
#        users = cursor.fetchall()

#INSERT INTO User (user, pass, nafn) VALUES 
#('Kleina13', 'admin', 'Ragnar Helgi B. Unnþórsson');


#        cursor.execute("INSERT INTO User (user, pass, nafn) VALUES ('Kleina13', 'admin', 'Ragnar Helgi B. Unnþórsson');")

@app.route("/")
def index():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

    if 'user' in session:
        user = session['user']
    else: 
        user = {"username":"none", "password":"none", "name":"none"}

    return render_template('main.tpl', user=user)


@app.route("/innskraning", methods=['GET', 'POST'])
def innskraning():
    error = False
    if 'user' in session:
        return redirect(url_for('index'))

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

    if request.method == 'POST':
        error = True
        for u in users:
            if request.form['username'] == u[0]:
                if request.form['password'] == u[1]:
                    session['user'] = {"username":u[0], "password":u[1], "name":u[2]}
                    return redirect(url_for('index'))
    return render_template('login.tpl', error=error)

@app.route('/sida')
def sida():
    if 'user' in session:
        user = session['user']
    else:
        return redirect(url_for('innskraning'))

    return render_template('sida.tpl', user=user)

@app.route('/utskraning')
def utskraning():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('index'))

@app.route('/nyrnotandi', methods=['GET', 'POST'])
def nyrnotandi():
    error = False
    if 'user' in session:
        return redirect(url_for('index'))

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

    if request.method == 'POST':
        for u in users:
            if u[0] == request.form['username']:
                return render_template('nyrnotandi.tpl', error=True)

        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO users (user, pass, nafn) VALUES
                               ('{request.form['username']}', '{request.form['password']}', '{request.form['name']}');""")
        return redirect(url_for('innskraning'))

    return render_template('nyrnotandi.tpl', error=error)



@app.errorhandler(404)
def not_found(error):
    return render_template("not_found.tpl"),404

@app.errorhandler(405)
def not_allowed(error):
    return render_template("not_allowed.tpl"),405

if __name__ == '__main__':
    app.run(debug=True)