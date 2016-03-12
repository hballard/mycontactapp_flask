from . import app
from flask import render_template
from .models import Contacts


@app.route('/')
@app.route('/<int:contact_id>')
def index(contact_id=1):
    contacts = Contacts.query.all()
    contact = contacts[contact_id - 1]
    return render_template('index.html', contact=contact, contacts=contacts)
