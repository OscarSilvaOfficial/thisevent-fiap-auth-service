from flask import request
from flask.views import MethodView
from api.utils.auth import validate_token
from api.utils.request import parse_request
from api.views.token.parser import parser


class TokenView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    token = request.get('authentication-token')

    try:
      validate_token(token)
    except Exception as e:
      return {'message': 'Invalid token'}, 401
      
    return {'valid_token': True}
    