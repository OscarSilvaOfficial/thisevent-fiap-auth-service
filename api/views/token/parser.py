def parser(request):
  """
  Parse the request to get the token
  """
  if not request.headers.get('authentication-token'):
      return {'message': 'Token is required'}, 401

  return {
    'authentication-token': request.headers.get('authentication-token')
  }