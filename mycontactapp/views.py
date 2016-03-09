from . import app
from flask import render_template
from .models import Contacts


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact_list')
def contact_list():
    contacts = Contacts.query.all()
    return render_template('list.html', contacts=contacts)


@app.route('/get_contact/<int:contact_id>')
def get_contact(contact_id):
    contact = Contacts.query.filter_by(id=contact_id).first()
    return render_template('contact.html', contact=contact)
