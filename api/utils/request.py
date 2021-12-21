def parse_request(request, parser):
  """
  Get request and parse it.
  """
  def real_decorator(function):
    def wrapper(self, *args):
      response = parser(request)
      return function(self, response)
    return wrapper
  return real_decorator