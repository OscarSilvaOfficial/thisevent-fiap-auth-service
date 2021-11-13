from flask import Flask
from api.urls import routes
from flask_restful import Api
from api.models import db
from flask_migrate import Migrate

def sql_alchemy(app):
  return db.init_app(app)

def flask_restful(flask=Flask):
  app = flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/db?charset=utf8mb4'
  return app

def application():
  app = flask_restful()
  db = sql_alchemy(app)
  Migrate(app, db)
  api = Api(app)
  api.prefix = '/api'
  routes(api)
  return app