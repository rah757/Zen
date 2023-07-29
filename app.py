from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session,
    flash,
)
from flask_security import (
    Security,
    SQLAlchemySessionUserDatastore,
#    auth_required,
    current_user,
    hash_password,
    verify_password,
    login_required,
#    permissions_accepted,
#    permissions_required,
#    roles_accepted,
    UsernameUtil,
    PasswordUtil,
)

from datetime import timedelta

from database import db_session, init_db
from models import User, Role, Entry

from sqlalchemy import select

app = Flask(__name__)

app.config['TESTING'] = True
app.config['DEBUG'] = True

app.config['SECRET_KEY'] = "chickenfry"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Salt for hashing the passwords, change if deploying in production 
app.config['SECURITY_PASSWORD_SALT'] = "146585145368132386173505678016728509634"

# Enabling username in flask_security
app.config['SECURITY_USERNAME_ENABLE'] = True

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)

with app.app_context():
    init_db()

@app.route('/')
@login_required
def home():
    values = []
    for entry in db_session.execute(select(Entry.health).where(Entry.user_id == current_user._id)):
        values.append(entry[0])

    return render_template('index.html', username=current_user.username, values=values)

@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all() ,entries = Entry.query.all(), sleeps = Sleep.query.all())

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form["uname"]
        if not app.security.datastore.find_user(username=uname):
            if request.form["passwd"] == request.form["passwdr"]:
                password=hash_password(request.form["passwd"])
                user = app.security.datastore.create_user(username=uname, password=password)
                db_session.commit()
                return redirect('/')
            else:
                flash("Passwords do not match")
                return redirect('/register')
        else:
            flash("Username already exists")
            return redirect('/register')
    else:
        return render_template("register.html")

@app.route("/questions", methods=["GET","POST"])
@login_required
def questions():
    if request.method == "POST":
        q0 = int(request.form['q0'])
        q1 = int(request.form['q1'])
        q2 = int(request.form['q2'])
        q3 = int(request.form['q3'])
        q4 = int(request.form['q4'])
        q5 = int(request.form['q5'])
        q6 = int(request.form['q6'])
        q7 = int(request.form['q7'])
        q8 = int(request.form['q8'])
        q9 = int(request.form['q9'])

        health = (q0+q1+q2+(100*(1-(q3/100)))+(100*(1-(q4/100)))+(q5*10)+q6+q7+q8+(100*(q9/12)))/10

        # create new entry and add to session
        user_id = current_user._id
        new_entry = Entry(user_id=user_id, health=health)
        db_session.add(new_entry)
        db_session.commit()

        return redirect(url_for("home"))

    return render_template('questions.html')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=True)

        #Entry.query.delete()
        #db.session.commit()
        #Entry.query.filter_by(user_id=1).delete()                                                                                      #deleters
        #db.session.commit()
