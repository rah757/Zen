from flask import Flask, redirect, url_for, render_template, request, session, flash 
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.secret_key = "chickenfry"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')
