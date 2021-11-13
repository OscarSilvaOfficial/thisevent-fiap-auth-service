from flask import request
from flask.views import MethodView
from api.models.user import User
from api.utils.auth import encode_password, encode_token


class SignInView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  def post(self, request=request):
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.get({'email': email})

    password = encode_password(email, password)

    if password != user.password:
      return {'message': 'Wrong password'}, 401

    return encode_token({
      'id': user.id,
      'email': user.email,
      'name': user.name,
      'password': user.password
    })