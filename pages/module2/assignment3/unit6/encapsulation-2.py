# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# 3. Encapsulation Through Convention

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

# Reading Question
# Assume the following code:
# ---
# class ExampleClass:
#    def __init__(self, attr1, attr2):
#        self.attr1 = attr1
#        self._attr2 = attr2
# ---
# Select all of the true statements about the instance variables `attr1` and `attr2`
# Answer: `_attr2` is assumed to be a private instance variable
# Answer: Both `attr1` and `attr2` are public instance variables
# (Correct)
# Feedback: The single underscore is only a convention. In reality both attr1 and _attr2 are public instance variables. Python programmers will assume that _attr2 is private because of the single underscore. However, there is no such thing as a truly private instance variable.
