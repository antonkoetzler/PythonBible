# Binary search tree in python
class BST:
  def __init__(self, data = None):
    self.data = data
    self.left = None
    self.right = None
  def add(self, data):
    print("Adding a node, ", data)
