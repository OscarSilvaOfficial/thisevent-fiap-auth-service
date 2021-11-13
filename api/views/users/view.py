from flask import request
from flask.views import MethodView
from api.models.user import User
from api.utils.auth import encode_password


class UserView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  def post(self, request=request):
    user = User(**{
      'name': request.json.get('name'),
      'email': request.json.get('email'),
      'password': encode_password(request.json.get('email'), request.json.get('password')),
    })
    user.save()
    return user.to_dict()