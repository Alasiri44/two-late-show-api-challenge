from models.__init__ import db
from flask import Flask

class User(db.Model):
    __tablename__ ='users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    
    def __repr__(self):
        return f'<User {self.id} {self.username}>'
    