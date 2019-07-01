## Importing the Validator class so the Person class can inherit it
from classes.validator import Validator

class Person(Validator):
  """A simple person class"""

  def __init__(self, name, email):
      ## A constructor for instantiating common variables to be inherited by the Instructor and Student classes
      self.name = name
      self.email = email