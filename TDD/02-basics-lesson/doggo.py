class Doggo:
  """
  A class representing a guard dog.

  name: str 
    Name of the dog
    Cannot be empty (Raises ValueError)
    Can be only alphanumeric characters (Raises ValueError)

  sound: str
    Sound of the dog barking
    Cannot be empty (Raises ValueError)

  num_legs: int (4)
    The number of legs the dog has
    Cannot be less then 0 (Raises ValueError)
  
  bark(): str
    Returns the name of the dog and the sound it makes in the following format:
    '<name> barks: <sound>!'
  """

  def __init__(self, name):
    if name == "":
      raise ValueError("Should not be empty")
    self.name = name
