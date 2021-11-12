from flask_restful import Api
from api.views import UserView

def routes(app: Api):
  app.add_resource(UserView, '/')