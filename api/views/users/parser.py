from flask import abort

def parser(request):
  if not request.json.get('name'):
    return abort('Missing name field', 400)

  if not request.json.get('email'):
    return abort('Missing email field', 400)

  if not request.json.get('password'):
    return abort('Missing password field', 400)

  return {
    'email': request.json.get('email'),
    'password': request.json.get('password'),
    'name': request.json.get('name')
  }