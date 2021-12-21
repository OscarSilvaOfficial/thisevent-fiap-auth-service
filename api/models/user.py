from flask import abort
from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from api.models import db

class User(db.Model, SerializerMixin):

  __tablename__ = 'users'
  serialize_only = ('id', 'name', 'email')

  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False, unique=True)
  password = Column(String(255), nullable=False)
  
  @staticmethod
  def get(filter_by):
    user = User.query.filter_by(**filter_by).first()

    if not user:
      return abort(500, '')

    return user

  @staticmethod
  def delete(user):
    db.session.delete(user)
    db.session.commit()

  def save(self):
    db.session.add(self)
    try:
      db.session.commit()
    except Exception:
      raise {'message': 'User duplicated'}
    return self