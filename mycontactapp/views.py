from flask import render_template, abort
from mycontactapp.models import Contacts
from mycontactapp import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/<int:contact_id>')
def index(contact_id=1):
    all_contacts = Contacts.query.all()
    if contact_id > len(all_contacts) or contact_id == 0:
        abort(404)
    else:
        contact = all_contacts[contact_id - 1]
        return render_template('index.html', contact=contact, all_contacts=all_contacts)