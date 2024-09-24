import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Niv@123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/AI_QUIZ_APP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'JWT123NIV'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db = SQLAlchemy(app)
