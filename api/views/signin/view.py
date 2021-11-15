from flask import request
from flask.views import MethodView
from api.models.user import User
from api.utils.auth import encode_password, encode_token
from api.utils.request import parse_request
from api.views.signin.parser import parser


class SignInView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    email = request.get('email')
    user = User.get({ 'email': email })

    password = encode_password(**request)

    if password != user.password:
      return {'message': 'Wrong password'}, 401

    return encode_token({
      'id': user.id,
      'email': user.email,
      'name': user.name,
      'password': user.password
    })