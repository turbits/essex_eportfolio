# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class Car:
  def __init__(self, make, model, year, engine):
    self.make = make
    self.model = model
    self.year = year
    self.engine = engine
    
  def describe(self):
    print('This is a {} {}, from {}. The engine is a {}L {} with {} horsepower. It runs on {}.'.format(self.make, self.model, self.year, self.engine.displacement, self.engine.configuration, self.engine.horsepower, self.engine.fuel_type))
  
  def start(self):
    self.engine.ignite()

class Engine:
  def __init__(self, configuration, displacement, horsepower, fuel_type):
    self.configuration = configuration
    self.displacement = displacement
    self.horsepower = horsepower
    self.fuel_type = fuel_type

  def ignite(self):
    print('Zippy!')


my_engine = Engine("V6", 2.6, 301, "gasoline")
my_car = Car("Nissan", "Skyline GT-R", 1993, my_engine)
my_car.describe()
# my_car.engine.ignite()

# Reading Question
"""
Fill in the blanks below with the words from the dropdown menu.

X should be used to add functionality if there is a "is a" relationship.
Answer (Correct): Inheritance

X should be used to add functionality if there is a "has a" relationship.
Answer (Correct): Composition

Feedback:
Use inheritance when you have a “is a” relationship; e.g. a car is a vehicle.
Use composition when you have a “has a” relationship; e.g. a car has an engine.
"""
