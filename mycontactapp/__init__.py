from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_webpack import Webpack

app = Flask('mycontactapp')
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

webpack = Webpack()
webpack.init_app(app)

import mycontactapp.views
