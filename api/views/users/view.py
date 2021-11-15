from flask import request
from api.models.user import User
from flask.views import MethodView
from api.utils.request import parse_request
from api.views.users.parser import parser


class UserView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    user = User(**request)
    user.save()
    return user.to_dict() 