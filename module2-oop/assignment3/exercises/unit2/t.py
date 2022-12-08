# +===================================================================+
# codio-results.py - showing all results/outputs from the codio
# exercises from Unit 2
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio/tree/main/module2-oop/assignment3
# Project: Module 2 (OOP_PCOM7E), Assignment 3, Unit 2: Codio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import math
import copy

class Point:
  """Represents a point in 2-D space.
  attributes: x, y.
  """
  x = 0
  y = 0

class Rectangle:
  """Represents a rectangle.
  attributes: width, height, corner.
  """
  width = 0
  height = 0
  corner = Point()

class Circle:
  """Represents a circle.
  attributes: center, radius.
  """
  center = Point()
  radius = 0
  
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius
  
  def __init__(self, width, height, corner):
    self.width = width
    self.height = height
    self.corner = corner

def distance_between_points(p1, p2):
  return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def move_rectangle(rectangle, dx, dy):
  rectangle.corner.x += dx
  rectangle.corner.y += dy
  return rectangle

def move_rectangle_copy(rect, dx, dy):
  _new_rectangle = copy.deepcopy(rect)
  _new_rectangle.corner.x += dx
  _new_rectangle.corner.y += dy
  return _new_rectangle

# write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.
def point_in_circle(point, circle):
  return distance_between_points([point.x, point.y], [circle.center.x, circle.center.y]) <= circle.radius


def rect_in_circle(rect, circle):
  _rect = Rectangle()
  _rect.width = rect.width
  _rect.height = rect.height
  _rect.corner = Point()
  _rect.corner.x += rect.width
  _rect.corner.y += rect.height
  return point_in_circle(rect.corner, circle) and point_in_circle(_rect.corner, circle)

def rect_circle_overlap(rect, circle):
  _rect = Rectangle()
  _rect.width = rect.width
  _rect.height = rect.height
  _rect.corner = Point()
  _rect.corner.x += rect.width
  _rect.corner.y += rect.height
  return point_in_circle(rect.corner, circle) or point_in_circle(_rect.corner, circle)

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
