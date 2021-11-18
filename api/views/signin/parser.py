from flask_restful import abort


def parser(request):
  """
  Parse the request to get the username and password
  """
  if not request.json.get('email'):
    return abort('Missing email field', 400)

  if not request.json.get('password'):
    return abort('Missing password field', 400)

  return {
    'email': request.json.get('email'),
    'password': request.json.get('password')
  }