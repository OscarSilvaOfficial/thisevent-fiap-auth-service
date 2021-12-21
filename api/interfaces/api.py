from abc import ABC, abstractmethod


class API(ABC):
  
  @abstractmethod
  def add_resource(view, endpoint):
    pass