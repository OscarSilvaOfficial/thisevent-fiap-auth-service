from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from api.models import db

class User(db.Model, SerializerMixin):

  __tablename__ = 'users'
  serialize_only = ('id', 'name', 'email')

  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)
  
  @staticmethod
  def get(filter_by):
    try:
      user = User.query.filter_by(**filter_by).first()
    except User.DoesNotExist:
      return {'message': 'User does not exist'}, 404
    return user

  def save(self):
    db.session.add(self)
    try:
      db.session.commit()
    except Exception:
      raise {'message': 'User duplicated'}
    return self