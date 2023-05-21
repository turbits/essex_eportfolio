---
layout: page
permalink: /pages/module2/assignment3/unit6/encapsulation-1.html
---

⬅️[Back](/pages/module2/assignment3/unit6/m2a3u6.html)

## Module 2: Assignment 3: Unit 6: Encapsulation 1

### Code

```python
class Phone:
  def __init__(self, model, storage, megapixels):
    self.model = model
    self.storage = storage
    self.megapixels = megapixels

my_phone = Phone("iPhone", 256, 12)
print(my_phone.model)
print(my_phone.storage)
print(my_phone.megapixels)

print "Change model to 'True'"
my_phone.model = True
print my_phone.model
print "Change storage to '256GB'"
my_phone.storage = "256GB"
print my_phone.storage
print "Change megapixels to '-32'"
my_phone.megapixels = -32
print my_phone.megapixels
```

### Output:

```
iPhone
256
12
Change model to 'True'
True
Change storage to '256GB'
256GB
Change megapixels to '-32'
-32
```
