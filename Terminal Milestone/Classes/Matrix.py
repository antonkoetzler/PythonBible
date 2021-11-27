class Matrix:
  def __init__(self, n = None):
    self.matrix = []
    self.n = n

    if n != None:
      for x in range(self.n):
        row = []

        for y in range(self.n):
          row.append(None)

        self.matrix.append(row)

  def print(self):
    if self.n == None:
      print("Empty matrix")
    else:
      for x in range(self.n):
        for y in range(self.n):
          print(self.matrix[x][y], " ", end="", flush=True)
        print()