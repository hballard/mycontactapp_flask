from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('mycontactapp')
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)


# Try to remap 'static' folder to URI of webpack server, so I can use url_for()
# function in jinja templates

# app.url_map._rules.pop()
# app.url_map._rules_by_endpoint.clear()
# # enable host matching and re-add the static route with the desired host
# app.url_map.host_matching = True
# app.add_url_rule('/<filename>',
#                  endpoint='static',
#                  view_func=app.send_static_file,
#                  host='localhost:3000')

import mycontactapp.views
