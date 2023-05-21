---
layout: page
permalink: /pages/module2/assignment3/unit6/encapsulation-3.html
---

⬅️[Back](/pages/module2/assignment3/unit6/m2a3u6.html)

## Module 2: Assignment 3: Unit 6: Encapsulation 3

### Code

```python
class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"

  def __private_method(self):
    return "I am a private method"

  def helper_method(self):
    return self.__private_method()

obj = PrivateClass()
# print(obj.__private_method())
print(obj.helper_method())
```

### Output:

```
I am a private method
```
