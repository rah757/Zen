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
    UserDatastore,
)
# from flask_security.UserDatastore import create_user

from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

from database import db_session, init_db
from models import User, Role

app = Flask(__name__)

app.config['TESTING'] = True
app.config['DEBUG'] = True

app.config['SECRET_KEY'] = "chickenfry"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite3"

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

# Registering views using app.route
# See https://flask.palletsprojects.com/en/2.3.x/api/#flask.Flask.route
@app.route('/')
def index():
    return render_template('index.html')       

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form["uname"]
        if not app.security.datastore.find_user(username=uname):
            if request.form["passwd"] == request.form["passwdr"]:
                password=hash_password(request.form["passwd"])
                user = app.security.datastore.create_user(username=uname, password=password)
                return redirect('/')
            else:
                flash("Passwords do not match")
                return redirect('/register')
        else:
            flash("Username already exists")
            return redirect('/register')
    else:
        return render_template("register.html")

@app.route('/questions', methods=["GET", "POST"])
@login_required
def questions():
    pass

# To remove database session at end of requests/app shutdown
# See https://flask.palletsprojects.com/en/2.3.x/patterns/sqlalchemy/
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
