---
layout: page
permalink: /pages/module2/unit-assignments/unit7/code.html
---

⬅️[Back](/pages/module2/unit-assignments/unit7/m2u7.html)

# Module 2: Unit 7: Code

- Create a nested dictionary of data on cars within a Car class. Extend the program to work with the dictionary by calling the following methods: items(), keys(), values()
  - items()
  - keys()
  - values()

## Code

```python
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
```

## Output:

```
Printing my_car.data
{'color': 'brilliant red', 'make': 'Subaru', 'model': 'WRX', 'year': 2015}

Using items() on data dictionary
[('color', 'brilliant red'), ('make', 'Subaru'), ('model', 'WRX'), ('year', 2015)]

Using keys() on data dictionary
['color', 'make', 'model', 'year']

Using values() on data dictionary
['brilliant red', 'Subaru', 'WRX', 2015]
```
