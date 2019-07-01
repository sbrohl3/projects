from classes.validator import Validator

class Person(Validator):
  """A simple person class"""

  def __init__(self, name, email):
      self.name = name
      self.email = email