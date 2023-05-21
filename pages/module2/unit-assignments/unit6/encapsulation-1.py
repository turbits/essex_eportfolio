# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

# 2. What is encapsulation?

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

# Reading Question
# Select the best definition of encapsulation from the choices below.
# Answer: Encapsulation occurs when you group together related data and methods, and when you hide or restrict access to data.
# (Correct)
# Feedback: There are two main ideas behind encapsulation: grouping together related data and restricting this data. Each idea on its own can be an example of encapsulation. However, the best definition is one that includes the grouping of data and restricting the data.
