class Drink:

  def __init__(self, soda, size, price):
    self.soda = soda
    self.size = size
    self.price = price

  def show_info(self):
    print(self.soda)
    print(self.size)
    print(self.price)
ss = Drink("Soda", "0,5L", "2$")
ss.show_info()


class Soda(Drink):
  def __init__(self, name, production):
    self.name = name
    self.production = production

a = Soda("Juice", "USA")
a.show_info()
