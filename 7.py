class IterableWithGenerators:
  def __init__(self, data):
      self.data = data

  def __iter__(self):

      for i in self.data:
          yield self.generator(i)

  def generator(self, i):

      for i in range(i):
          yield i

a = IterableWithGenerators([1, 2, 3])

for b in a:

  for value in b:
      print(value)
