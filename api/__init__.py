from flask import Flask
from api.urls import routes
from flask_restful import Api
from api.models import db 
from flask_migrate import Migrate
from api.config import DATABASE_URL

def sql_alchemy(app):
  return db.init_app(app)

def flask_instance(flask=Flask):
  app = flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
  return app

def flask_restful(app):
  api = Api(app)
  api.prefix = '/api'
  return api

def application():
  app = flask_instance()
  api = flask_restful(app)
  sql_alchemy(app)
  routes(api)
  return app