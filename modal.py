from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(name='Camilo Italo', email='alpha19ci@gmail.com')
    db.session.add(user)
    db.session.commit()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email")


user_schema = UserSchema()
users_schema = UserSchema(many=True) 
