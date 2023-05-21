---
layout: page
permalink: /pages/module2/assignment3/unit1/code.html
---

⬅️[Back](/pages/module2/assignment3/unit1/m2a3u1.html)

# Module 2: Unit 1: Code

## Code

```python
# (main.py)
class Item:
  _id = 0
  name = 0

  def __init__(self, _id, name):
    self._id = _id
    self.name = name

  def __str__(self):
    return "Item Details\nID: {}\nName: {}".format(self._id, self.name)

  def get_id(self):
    return self._id

  def set_id(self, id):
    self._id = id

def main():
  item = Item(1, "Iron Ore")

  print "\nOn creation, item ID is 1..."
  def print_item_details():
    print item
  print_item_details()

  print "\nSetting item ID to 4 using public setter..."
  item.set_id(4)
  print_item_details()

if __name__ == "__main__":
  main()
```

## Output:

```
On creation, item ID is 1...
Item Details
ID: 1
Name: Iron Ore

Setting item ID to 4 using public setter...
Item Details
ID: 4
Name: Iron Ore
```
