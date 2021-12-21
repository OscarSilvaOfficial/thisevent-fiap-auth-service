from flask import abort


def parser(request):
  """
  Parse the request to get the username and password
  """
  if not request.json.get('email'):
    return abort(400, 'Missing email field')

  if not request.json.get('password'):
    return abort(400, 'Missing password field')

  return {
    'email': request.json.get('email'),
    'password': request.json.get('password')
  }