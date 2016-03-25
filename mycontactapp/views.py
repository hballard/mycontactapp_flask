from flask import render_template, abort, redirect, request
from .models import Contacts, db
from . import app
from .forms import MyForm


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def landing():
    all_contacts = Contacts.query\
        .add_columns(Contacts.id, Contacts.first_name, Contacts.last_name)\
        .order_by(Contacts.first_name)\
        .first()
    return redirect('/{}'.format(all_contacts[0].id))


@app.route('/add_new_contact', methods=['POST'])
def add_new_contact():
    new_contact_form = MyForm(request.form)
    if new_contact_form.validate_on_submit():
        del new_contact_form.id
        new_contact = Contacts(**new_contact_form.data)
        db.session.add(new_contact)
        db.session.commit()
        return redirect('/')


@app.route('/<int:contact_id>', methods=['POST'])
def edit_contact(contact_id):
    edit_contact_form = MyForm(request.form)
    if edit_contact_form.validate_on_submit():
        contact = Contacts.query.get(contact_id)
        edit_contact_form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        return redirect('/')


@app.route('/<int:contact_id>')
def index(contact_id=1):
    all_contacts = Contacts.query\
        .add_columns(Contacts.id, Contacts.first_name, Contacts.last_name)\
        .filter_by(active_status=True)\
        .order_by(Contacts.first_name)\
        .all()
    if contact_id > len(all_contacts) or contact_id == 0:
        abort(404)
    else:
        contact = Contacts.query.get(contact_id)
        return render_template('index.html',
                               contact=contact,
                               all_contacts=all_contacts,
                               edit_form=MyForm(obj=contact),
                               new_form=MyForm())
