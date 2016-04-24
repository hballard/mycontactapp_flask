from flask_wtf import Form
from wtforms.fields.core import StringField, BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.fields.html5 import EmailField, TelField, IntegerField
from wtforms.validators import Email, Length, Optional, Regexp


class MyForm(Form):
    first_name = StringField('First Name', validators=[Length(max=80),
        Optional()])
    last_name = StringField('Last Name', validators=[Length(max=80),
        Optional()])
    job_title = StringField('Job Title', validators=[Length(max=120),
        Optional()])
    company = StringField('Company', validators=[Length(max=120), Optional()])
    phone_number = TelField('Phone Number', validators=[Regexp('^(?:(?:\+?1\s*'
        '(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1'
        '|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8]'
        '[02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]'
        '{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)'
        '\s*(\d+))?$'),Optional()])
    email = EmailField('Email', validators=[Email(), Optional()])
    address1 = StringField('Address', validators=[Length(max=120), Optional()])
    city = StringField('City', validators=[Length(max=120), Optional()])
    state = StringField('State', validators=[Length(max=80), Optional()])
    zipcode = StringField('Zip Code', validators=[Length(max=80),
        Regexp('^\d{5}(?:[-\s]\d{4})?$'), Optional()])
    comments = TextAreaField('Comments', validators=[Length(max=250),
        Optional()])
    active_status = BooleanField('Un-check to Delete', default='Checked')
