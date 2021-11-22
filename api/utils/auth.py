from api.models.user import User
from api.config import SECRET
from jwt import decode, encode

def encode_password(email, password , *args, **kwargs):
  """
  Encode a password using the SECRET key
  """
  payload = {
    'email': email,
    'password': password
  }
  return encode(payload, SECRET, algorithm='HS256')

def decode_password(password):
  """
  Decode a password using the SECRET key
  """
  return decode(password, SECRET, algorithms=['HS256'])

def encode_token(payload):
  """
  Encode a token using the SECRET key
  """
  return encode(payload, SECRET, algorithm='HS256')

def validate_token(token):
  """
  Validate a token using the SECRET key
  """
  token = decode(token, SECRET, algorithms=['HS256'])

  user = User.get({'email': token['email']})

  if user.password != token['password']:
    return False
  
  return user