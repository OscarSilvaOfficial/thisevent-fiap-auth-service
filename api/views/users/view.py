from flask import request
from api.models.user import User
from flask.views import MethodView
from api.utils.request import parse_request
from api.utils.auth import encode_password
from api.views.users.parser import parser


class UserView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    request['password'] = encode_password(
      password=request['password'],
      email=request['email']
    ) 
    user = User(**request)
    user.save()
    return user.to_dict() 