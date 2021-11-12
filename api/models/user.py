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

  def save(self):
    db.session.add(self)
    db.session.commit()
    return self