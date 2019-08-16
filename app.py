from flask import Flask, request, url_for, render_template, redirect, session
#from flask-session import Session
from secure_passwords import VaultKeeper, Grab
import requests

app = Flask('__name__',static_url_path='/static/')
grab = Grab()
#sess = Session()


@app.route('/')
def MeepFront():
    return render_template('MeepFront.html')


@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user = VaultKeeper(request.form['password'])
        if user.findUser(request.form['username']):
            print(user.findUser(request.form['username']))
            return redirect("FrankOcean_html.html")
        user.addUser(str(request.form['username']))
    return render_template('Signup_page.html')


@app.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        if grab.findUser(request.form['username']):
            if grab.decrypt(request.form['username'],request.form['password']):
                session["username"] = request.form["username"]
                return render_template("SampleHTML.html")
    return render_template("Signin_page.html")


@app.route('/profile')
def profile():
    if grab.has_profile(session['username']):
        return render_template("SampleHTML.html")
    else:
        return render_template("SampleHTML.html")


if __name__ == '__main__':
    app.secret_key = "meepIsNotSpongebob"
    app.config['SESSION_TYPE'] = "mongodb"
    app.run(debug=True)

