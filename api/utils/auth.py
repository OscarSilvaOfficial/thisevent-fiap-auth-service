from config import SECRET
from jwt import decode, encode

def encode_password(email, password):
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