---
layout: page
permalink: /pages/module2/assignment3/unit5/polymorphism.html
---

⬅️[Back](/pages/module2/assignment3/unit5/m2a3u5.html)

## Module 2: Assignment 3: Unit 5: Polymorphism

### Code

```python
class Vehicle(object):
  def __init__(self, make, color):
    self.make = make
    self.color = color

  def info(self):
    print("The make of the car is {}, the color is {}.".format(self.make, self.color))

class DriverlessCar(Vehicle):
  def __init__(self, make, color, top_speed, detection_distance):
    super(DriverlessCar, self).__init__(make, color)
    self.top_speed = top_speed
    self.detection_distance = detection_distance

  def drive(self):
    print ("The car is driving at {}km/h, and it can detect objects {} metres away.".format(self.top_speed, self.detection_distance))

car = DriverlessCar("Subaru", "world rally blue", 180, 50)

car.info()
car.drive()
```

### Output:

```
The make of the car is Subaru, the color is world rally blue.
The car is driving at 180km/h, and it can detect objects 50 metres away.
```
