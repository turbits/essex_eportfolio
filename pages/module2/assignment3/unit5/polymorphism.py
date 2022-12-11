# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

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
