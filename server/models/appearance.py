from __init__ import db
from flask import Flask

class Appearance(db.Model):
    __tablename__ ='appearance'
    
    id = db.Column(db.Integer, primary_key=True)
    rating= db.Column(db.Integer)
    guest_id = db.Column(db.Integer)
    episode_id = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<User {self.id} {self.username}>'
    
    