from flask import render_template, abort, redirect, url_for
from .models import Contacts
from . import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def landing():
    all_contacts = Contacts.query.add_columns(Contacts.id, Contacts.first_name,
                                              Contacts.last_name)\
                                              .order_by(Contacts.first_name)\
                                              .first()
    return redirect('/{}'.format(all_contacts[0].id))


@app.route('/<int:contact_id>')
def index(contact_id=1):
    all_contacts = Contacts.query.add_columns(Contacts.id, Contacts.first_name,
                                              Contacts.last_name)\
                                              .order_by(Contacts.first_name)\
                                              .all()
    if contact_id > len(all_contacts) or contact_id == 0:
        abort(404)
    else:
        contact = Contacts.query.filter_by(id=contact_id).first()
        return render_template('index.html',
                               contact=contact,
                               all_contacts=all_contacts)
