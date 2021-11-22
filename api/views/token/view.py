from flask import request
from flask.views import MethodView
from api.utils.auth import validate_token
from api.utils.request import parse_request
from api.views.token.parser import parser
from flask import abort


class TokenView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    token = request.get('authentication-token')

    validation = validate_token(token)

    if validation == False:
      abort(401, 'Invalid authentication token')
    
    return validation.to_dict()
    