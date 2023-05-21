---
layout: page
permalink: /pages/module2/assignment3/unit6/encapsulation-2.html
---

⬅️[Back](/pages/module2/assignment3/unit6/m2a3u6.html)

## Module 2: Assignment 3: Unit 6: Encapsulation 2

### Code

```python
class Phone:
  def __init__(self, model, storage, megapixels):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
    self._carrier = "AT&T"

  def _private_method(self):
    print "I am a private method"

phone = Phone("iPhone", 256, 12)
print phone.__dict__
phone._private_method()
```

### Output:

```
{'_model': 'iPhone', '_megapixels': 12, '_storage': 256, '_carrier': 'AT&T'}
I am a private method
```
