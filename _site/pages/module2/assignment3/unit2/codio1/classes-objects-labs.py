# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# +============= TUTORIAL LAB 1: CREATING A CLASS =============+
print "Tutorial Lab 1 - Creating a Class:"
class Person:
  """Represents a generic person."""

  def __init__(self, first, last, weight, height):
    self.first_name = first
    self.last_name = last
    self.weight_in_lbs = weight
    self.height_in_inches = height
print(type(Person))

# +============= TUTORIAL LAB 2: INSTANTIATE A CLASS =============+
print "Tutorial Lab 2 - Instantiate a Class:"
_p = Person("Tom", "Thumb", 150, 78)
print("{} {} weighs {} lbs and is {} inches tall.".format(_p.first_name, _p.last_name, _p.weight_in_lbs, _p.height_in_inches))

# +============= TUTORIAL LAB 3: MODIFY INSTANCE DATA MEMBERS =============+
print "Tutorial Lab 3 - Modify Instance Data Members:"
_p.first_name = "George"
print("{} {} weighs {} lbs and is {} inches tall.".format(_p.first_name, _p.last_name, _p.weight_in_lbs, _p.height_in_inches))

# +============= MODULE 9 CHALLENGE =============+
print "Module 9 Challenge:"
person1 = Person("Tom", "Thumb", 150, 70)
person2 = Person("George", "Thumb", 180, 75)
person3 = Person("Jimmy", "Thumb", 250, 85)
person4 = Person("Sally", "Thumb", 120, 65)
person5 = Person("Jane", "Thumb", 130, 60)
person_list = [person1, person2, person3, person4, person5]
for person in person_list:
  print("{}".format(person.first_name))
