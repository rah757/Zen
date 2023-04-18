from flask import Flask, redirect, url_for, render_template, request, session, flash 
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "chickenfry"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class user(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = password


@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        username = None  # add this line to define the variable
        return redirect(url_for('login'))
    

@app.route("/view")
def view():
    return render_template("view.html", values=user.query.all())


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["uname"]
        password = request.form["passw"]
        
        login_user = user.query.filter_by(username=username, password=password).first()

        print(login_user) # Add this line for debugging purposes

        if login_user:
            session['username'] = username
            flash('logged in successfully')
            return redirect(url_for("home"))
        else:
             flash('err')
             return render_template('login.html', error='Invalid username or password')
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("login2.html")

@app.route('/logout')
def logout():
    username = session["username"]
    flash(f"You have been logged out successfully, {username}", "info")
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/questions')
def questions():
    return render_template('questions.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)