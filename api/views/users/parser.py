def parser(request):
  if not request.json.get('name'):
    return {'message': 'Missing name field'}, 400

  if not request.json.get('email'):
    return {'message': 'Missing email field'}, 400

  if not request.json.get('password'):
    return {'message': 'Missing password field'}, 400

  return {
    'email': request.json.get('email'),
    'password': request.json.get('password'),
    'name': request.json.get('name')
  }