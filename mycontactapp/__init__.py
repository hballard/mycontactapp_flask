from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('mycontactapp')
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

import mycontactapp.views
