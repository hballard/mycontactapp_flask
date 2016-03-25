from flask_wtf import Form
from wtforms.fields.core import StringField, BooleanField
from wtforms.fields.simple import TextAreaField, HiddenField
from wtforms.fields.html5 import EmailField, TelField, IntegerField
from wtforms.validators import Email, Length, Regexp, Optional


class MyForm(Form):
    id = HiddenField()
    first_name = StringField('First Name', validators=[Length(max=80),
        Optional()])
    last_name = StringField('Last Name', validators=[Length(max=80),
        Optional()])
    job_title = StringField('Job Title', validators=[Length(max=120),
        Optional()])
    company = StringField('Company', validators=[Length(max=120), Optional()])
    phone_number = TelField('Phone Number', validators=[Optional()])
    email = EmailField('Email', validators=[Email(), Optional()])
    address1 = StringField('Address', validators=[Length(max=120), Optional()])
    city = StringField('City', validators=[Length(max=120), Optional()])
    state = StringField('State', validators=[Length(max=80), Optional()])
    zipcode = IntegerField('Zip Code')
    comments = TextAreaField('Comments', validators=[Length(max=250),
        Optional()])
    active_status = BooleanField('Un-check to Delete', default='Checked')
