from flask import request
from flask.views import MethodView
from api.models.user import User
from api.utils.auth import encode_password, encode_token, validate_token


class TokenView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  def post(self, request: request=request):
    token = request.headers.get('authentication-token')

    if not token:
      return {'message': 'Token is required'}, 401

    if not validate_token(token):
      return {'message': 'Invalid token'}, 401

    return {'valid_token': True}
    