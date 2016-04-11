from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_webpack import Webpack
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask('mycontactapp')
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

webpack = Webpack()
webpack.init_app(app)

import mycontactapp.views
