from models.__init__ import db
from flask import Flask

class Episode(db.Model):
    __tablename__ ='episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    number = db.Column(db.Integer)
    
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Episode {self.id} {self.date} of {self.number}>'
    
    