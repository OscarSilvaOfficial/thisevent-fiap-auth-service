from flask import abort

def parser(request):
  """
  Parse the request to get the token
  """
  if not request.headers.get('authentication-token'):
      return abort('Token is required', 401)

  return {
    'authentication-token': request.headers.get('authentication-token')
  }