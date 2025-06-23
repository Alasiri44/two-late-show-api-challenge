from __init__ import db
from flask import Flask

class Guest(db.Model):
    __tablename__ ='guests'
    
    id = db.Column(db.Integer, primary_key=True)
    naame = db.Column(db.String)
    occupation = db.Column(db.String)
    
    def __repr__(self):
        return f'<Guest {self.id} {self.name}>'
    
      
    
