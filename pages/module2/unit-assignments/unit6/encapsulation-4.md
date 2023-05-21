---
layout: page
permalink: /pages/module2/unit-assignments/unit6/encapsulation-4.html
---

⬅️[Back](/pages/module2/unit-assignments/unit6/m2u6.html)

# 5. Encapsulation Formative Assessment 1

Use the terms Public and Private to fill in the blanks below.

=> Private

- means that an attribute or method can be accessed only from within the class.

=> Public

- means that an attribute or method can be accessed from within the class or outside of the class.

(Correct)
When an attribute or method is public, then it can be accessed from outside and inside of the class. Attributes or methods that are private can only be accessed from within the class.

# 6. Encapsulation Formative Assessment 2

Select all of the code snippets that have “private” attributes. Hint, there is more than one right answer.

Option 1:

```python
class TestClass:
  def __init__(self):
    self.__attr = "I am an attribute"
```

Option 2:

```python
class TestClass:
  def __init__(self):
    self._attr = "I am an attribute"
```

Option 3:

```python
class TestClass:
  def __init__(self):
    self.attr = "I am an attribute"
```

Answers:
Option 1
Option 2
(Correct)

Feedback:
The correct answers are:
Option 1
Option 2

The single underscore is the Python convention for a private attribute. The double underscore is technically used for name mangling, but makes it harder to access the attribute outside of the class.
