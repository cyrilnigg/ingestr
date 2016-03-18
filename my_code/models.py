import datetime
from flask import url_for
from my_code import db


class Case(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    description = db.StringField(required=False)
    start_date = db.DateTimeField()
    end_date = db.DateTimeField()

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name

    @property
    def post_type(self):
        return self.__class__.__name__

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class Custodian(Case):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email_address = db.StringField(required=True)
    status = db.StringField()
    mbox_location = db.StringField()
