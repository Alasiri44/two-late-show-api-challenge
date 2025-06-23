from __init__ import db
from flask import Flask

class Episode(db.Model):
    __tablename__ ='episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    number = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Episode {self.id} {self.username}>'
    
    