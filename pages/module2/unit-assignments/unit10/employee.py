# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class Employee:
  def __init__(self, name, title, salary):
    self.name = name
    self.title = title
    self.salary = salary

  def display(self):
    print('Employee: {}\nTitle: {}\nSalary: {}'.format(self.name, self.title, self.salary))

def greeting():
  print('Hello from the employee module')
