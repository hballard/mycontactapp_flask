from flask import render_template, abort, redirect, request
from .models import Contacts, db
from . import app
from .forms import MyForm
from .utilities import flash_errors


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def landing():
    all_contacts = Contacts.query\
        .filter_by(active_status=True)\
        .order_by(Contacts.first_name)\
        .first()
    return redirect('/{}'.format(all_contacts.id))


@app.route('/add_new_contact', methods=['POST'])
def add_new_contact():
    new_contact_form = MyForm(request.form)
    if new_contact_form.validate_on_submit():
        new_contact = Contacts(**new_contact_form.data)
        db.session.add(new_contact)
        db.session.commit()
        new_contact = Contacts.query\
                              .order_by(Contacts.id.desc())\
                              .first()
        return redirect('/{}'.format(new_contact.id))
    flash_errors(new_contact_form)
    return redirect('/')


@app.route('/<int:contact_id>', methods=['POST'])
def edit_contact(contact_id):
    edit_contact_form = MyForm(request.form)
    if edit_contact_form.validate_on_submit():
        contact = Contacts.query.get(contact_id)
        edit_contact_form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        if edit_contact_form.data.get('active_status') is True:
            return redirect('/{}'.format(contact_id))
        return redirect('/')
    flash_errors(edit_contact_form)
    return redirect('/{}'.format(contact_id))


@app.route('/<int:contact_id>')
def index(contact_id=1):
    all_contacts = Contacts.query\
        .with_entities(Contacts.id, Contacts.first_name, Contacts.last_name)\
        .filter_by(active_status=True)\
        .order_by(Contacts.first_name)\
        .all()
    if contact_id not in [contact[0] for contact in all_contacts]:
        abort(404)
    else:
        contact = Contacts.query.get(contact_id)
        return render_template('index.html',
                               contact=contact,
                               all_contacts=all_contacts,
                               edit_form=MyForm(obj=contact),
                               new_form=MyForm())
