# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# import employee
from employee import Employee, greeting

# emp = employee.Employee('Trevor Woodman', 'Student', 10)
emp = Employee('Trevor Woodman', 'Student', 10)
emp.display()
"""
Employee: Trevor Woodman
Title: Student
Salary: 10"""

greeting()
"""
Hello from the employee module"""

# Reading Question
"""
Select all of the ways you should import a module. Hint, there is more than one correct answer.

Answer (Correct): import my_module
Answer (Correct): from my_module import MyClass

Feedback:
The correct answers are import my_module and from my_module import MyClass.

While from my_module import * is technically valid Python code, programmers are encourage to avoid the wildcard when importing from modules.

When importing, you always start with the the module name. Either import the entire module, import my_module or indicate the module then import the item, from my_module import MyClass. Do not start with the item name.
"""
