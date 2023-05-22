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
    entries = db.relationship('Entry', backref='user', lazy=True)

    def __init__(self, user_id, username, email, password):
        self.username = username
        self.email = email
        self.password = password
   


class Entry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    health = db.Column(db.Integer)

    def __init__(self, user_id, health):
        self.user_id = user_id
        self.health = health

class Sleep(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    sleep = db.Column(db.Integer)

    def __init__(self, user_id, sleep):
        self.user_id = user_id
        self.sleep = sleep


@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])


    else:
        username = None  # add this line to define the variable
        return redirect(url_for('login'))
    

@app.route("/view")
def view():
    return render_template("view.html", values=user.query.all() ,entries = Entry.query.all(), sleeps = Sleep.query.all())


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

@app.route("/questions", methods=["GET","POST"])
def questions():
    if request.method == "POST":
        q1 = int(request.form['q1'])
        q2 = int(request.form['q2'])
        q3 = int(request.form['q3'])
        q4 = int(request.form['q4'])
        q5 = int(request.form['q5'])
        q6 = int(request.form['q6'])
        q7 = int(request.form['q7'])
        q8 = int(request.form['q8'])
        q9 = int(request.form['task'])
        q10 = int(request.form['time'])

        health = (q1+q2+q3+q4+(q5//20)+q6+q7+q8+q9+q10)/10

        # create new entry and add to session
        user_id = user.query.filter_by(username=session['username']).first()._id
        new_entry = Entry(user_id=user_id, health=health)
        db.session.add(new_entry)
        db.session.commit()


        return redirect(url_for("home"))

    return render_template('questions.html')

@app.route("/sleep", methods=["GET","POST"])
def sleep():
    if request.method == "POST":
        sleep = int(request.form['sleep'])

        # create new entry and add to session
        user_id = user.query.filter_by(username=session['username']).first()._id
        new_entry = Sleep(user_id=user_id, sleep=sleep)
        db.session.add(new_entry)
        db.session.commit()
        
        return redirect(url_for("home"))
    return render_template('sleep.html')
     

@app.route('/logout')
def logout():
    username = session["username"]
    flash(f"You have been logged out successfully, {username}", "info")
    session.pop('username', None)
    return redirect(url_for('login'))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
















        #Entry.query.delete()
        #db.session.commit()
        #Entry.query.filter_by(user_id=1).delete()                                                                                      #deleters
        #db.session.commit()