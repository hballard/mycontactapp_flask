from . import db


class Contacts(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    job_title = db.Column(db.String(120))
    company = db.Column(db.String(120))
    phone_number = db.Column(db.String(120))
    email = db.Column(db.String(120))
    address1 = db.Column(db.String(250))
    city = db.Column(db.String(120))
    state = db.Column(db.String(80))
    zipcode = db.Column(db.String(120))
    comments = db.Column(db.Text)
    active_status = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):

        super(Contacts, self).__init__(**kwargs)

    def __repr__(self):
        return '<Contact %r: %r>' % (self.id, self.first_name)
