---
layout: page
permalink: /pages/module2/assignment3/unit8/formative-assessment-2.html
---

## Module 2: Assignment 3: Unit 8: Formative Assessment 2

"Assume you want to write a recursive function that multiplies each element in a list by the number 5. What should the base case be?"

Answer (Incorrect): When the lenght of the list is 0
Wrong answer because I did not take into account that the function would not run again (base case) if the list was empty.

Feedback:
The program should keep recursing until the length of the list is 1. A length of 1 means there is only one element left in the list. There is no reason to keep calling the function when once the list is empty.
