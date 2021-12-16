# Parent class
class Parent:
  def __init__(self):
    self.data = 5

  def print(self):
    print("Prining information from class Parent")
    print(self.data)

  def parentFunc(self):
    print("Hello world")

# Child class
class Child1(Parent):
  # Overrides Parent's __init__ function
  def __init__(self):
    self.moreData = 10

  def print(self):
    print("Printing information from class Child1")

    # We cannot print Parent's data here
    print("moreData: ", self.moreData)

# Child class
class Child2(Parent):
  def __init__(self):
    self.moreData = 10

    # Parent's class information is now inherited.
    # We may now, for example, call parentFunc(self)
    Parent.__init__(self)

  def print(self):
    print("Printing information from class Child2")

    # We can print Parent's data now
    print(self.data)

    print(self.moreData)

class Child4(Parent):
  def __init__(self):
    self.moreData = 10

    # Will also inherited all of Parent's information
    super().__init__()

  def print(self):
    print("Printing information from class Child3")
    print(self.data)
    print(self.moreData)
