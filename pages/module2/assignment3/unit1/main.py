# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

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
