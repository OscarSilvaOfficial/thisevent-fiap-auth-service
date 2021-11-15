def parse_request(request, parser):
  def real_decorator(function):
    def wrapper(self, *args):
      response = parser(request)
      return function(self, response)
    return wrapper
  return real_decorator