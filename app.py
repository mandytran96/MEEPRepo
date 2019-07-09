from flask import Flask, request, url_for, render_template, redirect
from secure_passwords import VaultKeeper, Grab
app = Flask('__name__',static_url_path='/static/')

@app.route('/')
def MeepFront():
    return render_template('MeepFront.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user = VaultKeeper(request.form['password'])
        if user.findUser(request.form['username']):
            return redirect("signin.html")
        user.addUser(str(request.form['username']))
    return render_template('signup.html')

@app.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        test = Grab()
        if test.findUser(request.form['username']):
            if test.decrypt(request.form['username'],request.form['password']):
                print("IT WORKED!!!!")
    return render_template("signin.html")

if __name__ == '__main__':
    app.run(debug=True)
