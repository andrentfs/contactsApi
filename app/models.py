from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
    
    def compare_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f"<User: {self.username}"

class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    cellphone = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, name, cellphone):
        self.name = name
        self.cellphone = cellphone
    
    def __repr__(self):
        return f"<Contact: {self.name}"