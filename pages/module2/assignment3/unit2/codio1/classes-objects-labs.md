---
layout: page
permalink: /pages/module2/assignment3/unit2/codio1/classes-objects-labs.html
---

⬅️[Back](/pages/module2/assignment3/unit2/codio1/codio1.html)

## Module 2: Assignment 3: Unit 2: Codio Activity 1: Classes and Objects Labs

### Code

```python
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
```

### Output:

```
Tutorial Lab 1 - Creating a Class:
<type 'classobj'>
Tutorial Lab 2 - Instantiate a Class:
Tom Thumb weighs 150 lbs and is 78 inches tall.
Tutorial Lab 3 - Modify Instance Data Members:
George Thumb weighs 150 lbs and is 78 inches tall.
Module 9 Challenge:
Tom
George
Jimmy
Sally
Jane
```
