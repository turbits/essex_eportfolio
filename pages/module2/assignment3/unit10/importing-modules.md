---
layout: page
permalink: /pages/module2/assignment3/unit10/importing-modules.html
---

## Module 2: Assignment 3: Unit 10: Importing Modules

### Code

(employee.py)

```python
class Employee:
  def __init__(self, name, title, salary):
    self.name = name
    self.title = title
    self.salary = salary

  def display(self):
    print('Employee: {}\nTitle: {}\nSalary: {}'.format(self.name, self.title, self.salary))

def greeting():
  print('Hello from the employee module')
```

(program.py)

```python
# import employee
from employee import Employee, greeting

# emp = employee.Employee('Trevor Woodman', 'Student', 10)
emp = Employee('Trevor Woodman', 'Student', 10)
emp.display()

greeting()
```

### Output

```
Employee: Trevor Woodman
Title: Student
Salary: 10
Hello from the employee module
```

### Reading Question

"Select all of the ways you should import a module. Hint, there is more than one correct answer."

Answer (Correct): import my_module
Answer (Correct): from my_module import MyClass

Feedback:
The correct answers are import my_module and from my_module import MyClass.

While from my_module import \* is technically valid Python code, programmers are encourage to avoid the wildcard when importing from modules.

When importing, you always start with the the module name. Either import the entire module, import my_module or indicate the module then import the item, from my_module import MyClass. Do not start with the item name.
