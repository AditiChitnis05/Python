'''
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(self.name, self.salary)


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language=language
    def code(self):
        print(self.name, "writes", self.language, "code")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def manage(self):
        print(self.name, "manages", self.team_size, "people")

d1=Developer("Aditi", 7000000, "Python")
d1.display()
d1.code()

d2= Manager("Aditya", 70000000, 100)
d2.display()
d2.manage()


class Vehicle:
    def hello(self):
        print("This is a vehicle")
    def stop(self):
        print("vehicle stopped")

class Car(Vehicle):
    def cars(self):
        print("Hi i am a car")

c=Car()

c.hello()
c.stop()
c.cars()




class Grandfather():
    def land(self):
        print("Grandpa owns land")
    
class Father(Grandfather):
    def house(self):
        print("Father built house on grandpas land")

    def car(self):
        print("I own car")

class Son(Father):
    def Bike(self):
        print("Son inherited land and house he sold it to get a bike")

c=Son()

c.land()
c.house()
c.Bike()
c.car()

'''

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()