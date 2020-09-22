import re

class Doggo:
  """
  A class representing a guard dog.

  name: str 
    Name of the dog
    Cannot be empty (Raises ValueError)
    Can be only alphabetic characters, dots and spaces (Raises ValueError)
    Is read only (raises Error)

  sound: str ("Bark!")
    Sound of the dog barking
    Cannot be empty (Raises ValueError)

  num_legs: int (4)
    The number of legs the dog has
    Cannot be less then 0 (Raises ValueError)
  
  bark(): void
    Prints the name of the dog and the sound it makes in the following format:
    '<name> barks: <sound>!'
  """

  def __init__(self, name, num_legs = 4):
    if name == "":
      raise ValueError("Should not be empty")

    # for character in name:
    #   if re.search("[A-Za-z]", character):
    #     continue
    #   else:
    #     raise ValueError("Should be alphabetic")
    if re.search("[^A-Za-z. ]", name) :
      raise ValueError("Should be alphabetic")
      
    self.__name = name
    self.sound = "Bark!"
    self.num_legs = num_legs

  @property
  def name(self):
    return self.__name

  @property
  def sound(self):
    return self.__sound

  @sound.setter
  def sound(self, new_sound):
    if new_sound == "":
      raise ValueError("Sound can not be empty")
    self.__sound = new_sound


  