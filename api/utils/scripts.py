from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from api.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)  

def create_databases():
  if not database_exists(engine.url):
    create_database(engine.url)

def create_tables():
  meta = MetaData()
  users = Table(
    'users', meta, 
    Column('id', Integer, primary_key = True), 
    Column('name', String(255)), 
    Column('email', String(255), unique=True),
    Column('password', String(255))
  )
  meta.create_all(engine)