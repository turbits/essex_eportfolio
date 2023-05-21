# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import math
import copy


# +============= CLASSES AND OBJECTS =============+
class Point:
  """Represents a point in 2-D space.
  attributes: x, y.
  """
  x = 0
  y = 0
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
# As an exercise, write a function called distance_between_points that takes two Points as arguments and returns the distance between them.

_p1 = [5.0, 6.0]
_p2 = [9.0, 15.0]
def distance_between_points(p1, p2):
  return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print "---- distance_between_points() ----"
print "takes two Points as arguments and returns the distance between them"
print "distance_between_points([5.0, 6.0], [9.0, 15.0]) = ", distance_between_points(_p1, _p2)
print "\n"

# As an exercise, write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy. It should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.
class Rectangle:
  """Represents a rectangle.
  attributes: width, height, corner.
  """
  width = 0
  height = 0
  corner = Point(0, 0)
  
  def __init__(self, width, height, corner):
    self.width = width
    self.height = height
    self.corner = corner
_rectangle = Rectangle(100, 200, Point(50, 50))

def move_rectangle(rectangle, dx, dy):
  rectangle.corner.x += dx
  rectangle.corner.y += dy
  return rectangle
_r1 = move_rectangle(_rectangle, 10, 10)
print "---- move_rectangle() ----"
print "changes the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner"
print "move_rectangle(Rectangle(100, 200, Point(50, 50)), 10, 10) = width:{}, height:{}, corner.x:{}, corner.y:{}".format(_r1.width, _r1.height, _r1.corner.x, _r1.corner.y)
print "\n"

# As an exercise, write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.
_rectangle = Rectangle(100, 200, Point(50, 50))
def move_rectangle_copy(rect, dx, dy):
  _new_rectangle = copy.deepcopy(rect)
  _new_rectangle.corner.x += dx
  _new_rectangle.corner.y += dy
  return _new_rectangle
_r2 = move_rectangle_copy(_rectangle, 10, 10)
print "---- move_rectangle_copy() ----"
print "returns a new Rectangle instead of modifying the old one"
print "original rectangle = width:{}, height:{}, corner.x:{}, corner.y:{}".format(_rectangle.width, _rectangle.height, _rectangle.corner.x, _rectangle.corner.y)
print "move_rectangle_copy(Rectangle(100, 200, Point(50, 50)), 10, 10) = width:{}, height:{}, corner.x:{}, corner.y:{}".format(_r2.width, _r2.height, _r2.corner.x, _r2.corner.y)
print "original rectangle (again) = width:{}, height:{}, corner.x:{}, corner.y:{}".format(_rectangle.width, _rectangle.height, _rectangle.corner.x, _rectangle.corner.y)
print "\n"

# +============= EXERCISES: CLASSES AND OBJECTS =============+
class Circle:
  """Represents a circle.
  attributes: center, radius.
  """
  center = Point(0, 0)
  radius = 0
  
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius
_circle = Circle(Point(150, 100), 75)

# Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.
def point_in_circle(circle, point):
  return distance_between_points([circle.center.x, circle.center.y], [point.x, point.y]) <= circle.radius
print "---- point_in_circle() ----"
print "returns True if the Point lies in or on the boundary of the circle"
print "point_in_circle(Circle(Point(150, 100), 75), Point(100, 75)) = ", point_in_circle(_circle, Point(100, 75))
print "\n"

# Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.
def rect_in_circle(circle, rect):
  _rect = Rectangle(rect.width, rect.height, Point(rect.corner.x, rect.corner.y))
  _rect.corner.x += rect.width
  _rect.corner.y += rect.height
  return point_in_circle(circle, rect.corner) and point_in_circle(circle, _rect.corner)
print "---- rect_in_circle() ----"
print "returns True if the Rectangle lies entirely in or on the boundary of the circle"
print "rect_in_circle(Circle(Point(150, 100), 75), Rectangle(50, 100, Point(100, 50))) = ", rect_in_circle(_circle, Rectangle(50, 100, Point(100, 50)))
print "\n"

# Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.
def rect_circle_overlap(circle, rect):
  _rect = Rectangle(rect.width, rect.height, Point(rect.corner.x, rect.corner.y))
  _rect.corner.x += rect.width
  _rect.corner.y += rect.height
  return point_in_circle(circle, rect.corner) or point_in_circle(circle, _rect.corner)
print "---- rect_circle_overlap() ----"
print "returns True if any of the corners of the Rectangle fall inside the circle"
print "rect_circle_overlap(Circle(Point(150, 100), 75), Rectangle(50, 100, Point(100, 50))) = ", rect_circle_overlap(_circle, Rectangle(50, 100, Point(100, 50)))
print "\n"

# Write a function draw_rect that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.
import turtle
def draw_rect(turtle, rect):
  turtle.up()
  turtle.goto(rect.corner.x, rect.corner.y)
  turtle.down()
  for i in range(2):
    turtle.forward(rect.width)
    turtle.left(90)
    turtle.forward(rect.height)
    turtle.left(90)
draw_rect(turtle, Rectangle(50, 100, Point(100, 50)))

# Write a function draw_circle that takes a Turtle and a Circle and draws the Circle.
def draw_circle(turtle, circle):
  turtle.up()
  turtle.goto(circle.center.x, circle.center.y)
  turtle.down()
  turtle.circle(circle.radius)
draw_circle(turtle, Circle(Point(150, 100), 75))

