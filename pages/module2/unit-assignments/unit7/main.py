# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class Car:
  def __init__(self):
    self.data = {
      'make': '',
      'model': '',
      'year': '',
      'color': ''
    }

  def set_make(self, make):
    self.data['make'] = make

  def set_model(self, model):
    self.data['model'] = model

  def set_year(self, year):
    self.data['year'] = year

  def set_color(self, color):
    self.data['color'] = color

# example
my_car = Car()
my_car.set_make('Subaru')
my_car.set_model('WRX')
my_car.set_year(2015)
my_car.set_color('brilliant red')

print "\nPrinting my_car.data"
print(my_car.data)

# using items() to iterate through the dictionary
print "\nUsing items() on my_car.data"
my_car_items = my_car.data.items()
print my_car_items

# using keys() to iterate through the dictionary
print "\nUsing keys() on my_car.data"
my_car_keys = my_car.data.keys()
print my_car_keys

# using values() to iterate through the dictionary
print "\nUsing values() on my_car.data"
my_car_values = my_car.data.values()
print my_car_values
