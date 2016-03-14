from . import db


class Contacts(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    job_title = db.Column(db.String(120))
    company = db.Column(db.String(120))
    phone_number = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    address1 = db.Column(db.String(250))
    city = db.Column(db.String(120))
    state = db.Column(db.String(80))
    zipcode = db.Column(db.Integer)
    comments = db.Column(db.Text)
    active_status = db.Column(db.Boolean)

    def __init__(self, first_name, last_name, **kwargs):

        super(Contacts, self).__init__(**kwargs)
        # do custom initialization here
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Contact %r: %r>' % (self.id, self.first_name)
