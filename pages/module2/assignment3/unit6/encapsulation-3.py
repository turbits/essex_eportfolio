# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# 4. Double Underscore

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

# Reading Question
# Assume the following code:
# ---
# class TestClass:
#  def __init__(self):
#    self._attr = 1
#    self.attr = 2
#    self.__attr = 3
#
#  def helper(self):
#    return self.__attr
#
# my_test = TestClass()
# ---
# Which command will print `3`?
# Answer: print(my_test.helper())
# (Correct)
# Feedback:
# The correct answer is: print(my_test.helper())
# The value 3 is stored in __attr. Because of the double underscores, you cannot access it outside of the class. The helper method can access __attr because it is inside the class.
# - print(my_test.attr) will print 2
# - print(my_test._attr) will print 1
# - print(my_test.__attr) will cause an error
