---
layout: page
permalink: /pages/module2/assignment3/unit2/codio2/class-methods.html
---

⬅️[Back](/pages/module2/assignment3/unit2/codio2/codio2.html)

## Module 2: Assignment 3: Unit 2: Codio Activity 2: Class Methods

### Code

```python
class Time:
  """Represents the time of day.

  attributes: hour, minute, second
  """
  hour = 0
  minute = 0
  second = 0

  # ==== 17.2 - Printing objects ====
  # As an exercise, rewrite time_to_int (from Section 16.4) as a method. You might be tempted to rewrite int_to_time as a method, too, but that doesnt really make sense because there would be no object to invoke it on.
  def time_to_int(self):
    minutes = self.hour * 60 + self.minute
    seconds = minutes * 60 + self.second
    return seconds

  # ==== 17.4 - A more complicated example ====
  def is_after(self, other):
    return self.time_to_int() > other.time_to_int()

def print_time(time):
  print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

def is_after(t1, t2):
  return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

# as an exercise, write a "pure" version of increment that creates and returns a new Time object rather than modifying the parameter.
def increment(time, seconds):
  _time = copy.deepcopy(time)
  _time.second += seconds
  if _time.second >= 60:
    _time.minute += 1
    _time.second -= 60
  if _time.minute >= 60:
    _time.hour += 1
    _time.minute -= 60

def time_to_int(time):
  minutes = time.hour * 60 + time.minute
  seconds = minutes * 60 + time.second
  return seconds


# ==== 17.5 - The init method ====
# As an exercise, write an init method for the Point class that takes x and y as optional parameters and assigns them to the corresponding attributes.
class Point:
  """Represents a point in 2-D space.

  attributes: x, y.
  """
  x = 0
  y = 0

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return "({self.x}, {self.y})".format(self=self)

  # ==== 17.7 - Operator overloading ====
  # As an exercise, write an add method for the Point class.
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  # ==== 17.8 - Type-based dispatch ====
  # As an exercise, write an add method for Point that works with either a Point object or a tuple
  def __add__(self, other):
    if isinstance(other, Point):
      return Point(self.x + other.x, self.y + other.y)
    elif isinstance(other, tuple):
      return Point(self.x + other[0], self.y + other[1])

# ==== 17.6 - The __str__ method ====
# As an exercise, write a str method for the Point class. Create a Point object and print it.
_point = Point(1, 2)
print(_point)
```

### Output

```
(1, 2)
```

This one wasn't really about the output, but about the code.
