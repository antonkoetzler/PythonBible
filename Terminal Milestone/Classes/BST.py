# Binary search tree in python
class BST:
  def __init__(self, data = None):
    self.data = data
    self.left = None
    self.right = None

  def add(self, data):
    if self.data == None:
      self.data = data

    if self.data > data:
      if self.left == None:
        self.left = BST(data)
      else:
        self.left.add(data)
    else:
      if self.right == None:
        self.right = BST(data)
      else:
        self.right.add(data)
