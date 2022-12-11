# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex_eportfolio
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

def find_sum(n):
  """Recursively calculate the sum of the first n numbers"""
  if n == 0:
    return 0
  else:
    return n + find_sum(n - 1)

