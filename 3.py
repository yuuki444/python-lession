class human:
  def __init__(self, firstname, secondname, age):
    self.firstname = firstname
    self.secondname = secondname
    self.age = age
  def show_info(self):
    print(self.firstname)
    print(self.secondname)
    print(self.age)
f = human("ivan", "ivanov", "20")
s = human("George","Georgiev", "30")
a = input("")
if a == "f":
  f.show_info()
  
if a == "s":
  s.show_info()
