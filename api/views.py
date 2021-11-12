from flask import request
from flask.views import MethodView

from api.models.user import User
from api.utils.auth import encode_password


class UserView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  def get(self, request=request):
    pass

  def post(self, request=request):
    username = request.json.get('name')
    password = request.json.get('password')
    email = request.json.get('email')
    user = User(
      name=username,
      password=encode_password(email, password),
      email=email
    )
    user.save()
    return user.to_dict()