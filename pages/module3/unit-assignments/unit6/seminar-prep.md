---
layout: page
permalink: /pages/module3/unit-assignments/unit6/seminar-prep.html
---

⬅️[Back](/pages/module3/unit-assignments/unit6/m3u6.html)

## Unit 6: Seminar Preperation

### 🤔 My Reflections

It is first worth noting that linting is such a common practice that I did not even think to mention it in the [Coding Output assignment](/pages/module3/assignment2/m3a2.html) for this Module. Unfortunately, I'm writing this post-submission, but the video walkthrough as part of that assignment clearly shows that the project was built using flake8 in vscode. In fact, at one point I commented out some code that was underlined because of it.

### Assignment Requirements

These questions are provided in the Codio workspace – Testing with Python – where the activities should be completed.

#### Question 1
- Run `styleLint.py` in Codio.
- What happens when the code is run? Can you modify this code for a more favourable outcome? What amendments have you made to the code?

#### Question 1: Answer

The code was run, and it returns the following:

codio@kansaslegacy-diagramsantana:~/workspace$ python styleLint.py 
```
  File "styleLint.py", line 5
    """ Return factorial of n """
                                ^
IndentationError: expected an indented block
```

The original code is as follows:

```python
def factorial(n):
"""Return factorial of n"""
if n == 0:
return 1
else:
return n*factorial(n-1)
```

I corrected the code (and the lint error) by indenting the code as such, which returns without error:

```python
def factorial(n):
    """Return factorial of n"""
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
```


#### Question 2
- `pip install pylint`
- Run `pylint` on pylintTest.py
- Review each of the code errors returned. Can you correct each of the errors identified by pylint?
- Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).

#### Question 2: Answer

Unfortunately, the Codio "box" or "environment" seems to be broken. I tried resetting the whole environment as well, which did not resolve the issue. The instructions clearly say to run `pip install pylint`, but when I do that, I get the following error:

```
      File "/home/codio/.local/lib/python2.7/site-packages/setuptools/sandbox.py", line 250, in run_setup
        _execfile(setup_script, ns)
      File "/home/codio/.local/lib/python2.7/site-packages/setuptools/sandbox.py", line 44, in _execfile
        code = compile(script, filename, 'exec')
      File "/tmp/easy_install-jVI6Od/setuptools_scm-7.1.0/setup.py", line 20
        def scm_version() -> str:
                          ^
    SyntaxError: invalid syntax
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-Wi3Ouv/lazy-object-proxy/
```

```
codio@kansaslegacy-diagramsantana:~/workspace$ pylint
-bash: pylint: command not found
codio@kansaslegacy-diagramsantana:~/workspace$ pylint pylintTest.py 
-bash: pylint: command not found
```

Which, by the way, let me point out that this Codio environment is using Python 2.7, an extremely outdated Python version that has been end of life for over 3 years (January 1 2020), and had its EOL pushed several times before that. This is pretty disappointing to see in a graduate-level course; it was the same in Module 2 as well. It's really not acceptable.

```
codio@kansaslegacy-diagramsantana:~/workspace$ python --version
Python 2.7.17
```

Regardless, here is the corrected code:

```python

# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

import string
 
shift = 3
choice = raw_input("would you like to encode or decode?")
word = (raw_input("Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) - shift
            encoded = encoded + letters[x]

print encoded
```


#### Question 3
- `pip install flake8`
- Run `flake8` on pylintTest.py
- Review the errors returned. In what way does this error message differ from the error message returned by pylint?
- Run flake8 on metricTest.py. Can you correct each of the errors returned by flake8? What amendments have you made to the code?

#### Question 3: Answer

Thankfully, this pip install actually went okay. I installed flake8 and ran `flake8 pylintTest.py` and got the following output:

```
codio@kansaslegacy-diagramsantana:~/workspace$ flake8 pylintTest.py 
pylintTest.py:5:1: W293 blank line contains whitespace
pylintTest.py:12:3: E111 indentation is not a multiple of 4
pylintTest.py:14:7: E111 indentation is not a multiple of 4
pylintTest.py:16:7: E111 indentation is not a multiple of 4
pylintTest.py:17:7: E111 indentation is not a multiple of 4
pylintTest.py:17:14: E225 missing whitespace around operator
pylintTest.py:19:7: E111 indentation is not a multiple of 4
pylintTest.py:23:11: E111 indentation is not a multiple of 4
pylintTest.py:24:11: E111 indentation is not a multiple of 4
pylintTest.py:26:14: W292 no newline at end of file
```

Unfortunately, I can't answer the second part of this question as pylint was not able to be installed, see Question 2.

The third part of this question asks to run flake8 on `metricTest.py`. I did so and it returned the following output:

```
metricTest.py:2:1: E265 block comment should start with '# '
metricTest.py:2:48: W291 trailing whitespace
metricTest.py:13:8: E999 SyntaxError: invalid syntax
metricTest.py:16:1: E112 expected an indented block
metricTest.py:20:1: E128 continuation line under-indented for visual indent
metricTest.py:21:1: E128 continuation line under-indented for visual indent
metricTest.py:22:1: E128 continuation line under-indented for visual indent
metricTest.py:23:1: E112 expected an indented block
metricTest.py:27:8: E225 missing whitespace around operator
metricTest.py:28:1: E112 expected an indented block
metricTest.py:30:3: E261 at least two spaces before inline comment
metricTest.py:31:8: E225 missing whitespace around operator
metricTest.py:31:17: E225 missing whitespace around operator
metricTest.py:32:1: E112 expected an indented block
metricTest.py:34:3: E261 at least two spaces before inline comment
metricTest.py:34:80: E501 line too long (83 > 79 characters)
metricTest.py:35:2: E201 whitespace after '['
metricTest.py:35:5: E202 whitespace before ']'
metricTest.py:36:8: E225 missing whitespace around operator
metricTest.py:37:1: E112 expected an indented block
metricTest.py:37:8: E225 missing whitespace around operator
metricTest.py:38:1: E112 expected an indented block
metricTest.py:38:3: E261 at least two spaces before inline comment
metricTest.py:39:22: E231 missing whitespace after ','
metricTest.py:40:10: E225 missing whitespace around operator
metricTest.py:41:1: E112 expected an indented block
metricTest.py:41:3: E261 at least two spaces before inline comment
metricTest.py:42:35: E231 missing whitespace after ','
metricTest.py:42:45: E231 missing whitespace after ','
metricTest.py:43:1: E128 continuation line under-indented for visual indent
metricTest.py:44:1: E128 continuation line under-indented for visual indent
metricTest.py:45:10: E225 missing whitespace around operator
metricTest.py:46:1: E112 expected an indented block
metricTest.py:46:3: E261 at least two spaces before inline comment
metricTest.py:48:1: E128 continuation line under-indented for visual indent
metricTest.py:52:1: E112 expected an indented block
metricTest.py:54:24: E231 missing whitespace after ','
metricTest.py:55:1: E112 expected an indented block
metricTest.py:59:1: E112 expected an indented block
metricTest.py:62:1: E112 expected an indented block
metricTest.py:63:13: E225 missing whitespace around operator
metricTest.py:64:1: E112 expected an indented block
metricTest.py:65:10: E225 missing whitespace around operator
metricTest.py:66:1: E112 expected an indented block
metricTest.py:66:12: E225 missing whitespace around operator
metricTest.py:69:1: E112 expected an indented block
metricTest.py:72:1: E112 expected an indented block
metricTest.py:74:17: E231 missing whitespace after ','
metricTest.py:75:1: E112 expected an indented block
metricTest.py:75:8: E225 missing whitespace around operator
metricTest.py:76:1: E112 expected an indented block
metricTest.py:77:8: E231 missing whitespace after ':'
metricTest.py:78:2: E201 whitespace after '['
metricTest.py:78:5: E202 whitespace before ']'
metricTest.py:82:1: E112 expected an indented block
metricTest.py:83:13: E225 missing whitespace around operator
metricTest.py:84:1: E112 expected an indented block
metricTest.py:86:1: E112 expected an indented block
metricTest.py:86:19: W292 no newline at end of file
```

The following is the original code in the `metricTest.py` file. For whatever reason, the files lines are prefixed with what appear to be line numbers. I have a feeling that this was not intended, considering the lack of quality seen elsewhere in the Codio environment and the assignment instructions. Again, pretty disappointing. If this was intended, it's not clear as to why, this teaches nothing except how to use the backspace key.

```python

#CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

"""
2 Module metricTest.py
3
4 Metric example - Module which is used as a testbed for static
checkers.
5 This is a mix of different functions and classes doing
different things.
6
7 """
8 import random
9
10 def fn(x, y):
11 """ A function which performs a sum """
12 return x + y
13
14 def find_optimal_route_to_my_office_from_home(start_time,
15 expected_time,
16 favorite_route='SBS1K',
17 favorite_option='bus'):
18
19
20 d = (expected_time – start_time).total_seconds()/60.0
21
22 if d<=30:
23 return 'car'
24
25 # If d>30 but <45, first drive then take metro
26 if d>30 and d<45:
27 return ('car', 'metro')
28
29 # If d>45 there are a combination of optionsWriting Modifiable and Readable Code
[ 68 ]
30 if d>45:
31 if d<60:
32 # First volvo,then connecting bus
33 return ('bus:335E','bus:connector')
34 elif d>80:
35 # Might as well go by normal bus
36 return random.choice(('bus:330','bus:331',':'.
join((favorite_option,
37 favorite_route))))
38 elif d>90:
39 # Relax and choose favorite route
40 return ':'.join((favorite_option,
41 favorite_route))
42
43
44 class C(object):
45 """ A class which does almost nothing """
46
47 def __init__(self, x,y):
48 self.x = x
49 self.y = y
50
51 def f(self):
52 pass
53
54 def g(self, x, y):
55
56 if self.x>x:
57 return self.x+self.y
58 elif x>self.x:
59 return x+ self.y
60
61 class D(C):
62 """ D class """
63
64 def __init__(self, x):
65 self.x = x
66
67 def f(self, x,y):
68 if x>y:
69 return x-y
70 else:Chapter 2
[ 69 ]
71 return x+y
72
73 def g(self, y):
74
75 if self.x>y:
76 return self.x+y
77 else:
78 return y-self.x
```

This is the code without the line numbers as I have a feeling that is what the assignment was asking to run the linter against:

```python

#CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

"""
Module metricTest.py

Metric example - Module which is used as a testbed for static
checkers.
This is a mix of different functions and classes doing
different things.

"""
import random

def fn(x, y):
""" A function which performs a sum """
return x + y

def find_optimal_route_to_my_office_from_home(start_time,
expected_time,
favorite_route='SBS1K',
favorite_option='bus'):


d = (expected_time – start_time).total_seconds()/60.0

if d<=30:
return 'car'

# If d>30 but <45, first drive then take metro
if d>30 and d<45:
return ('car', 'metro')

# If d>45 there are a combination of optionsWriting Modifiable and Readable Code
[ 68 ]
if d>45:
if d<60:
# First volvo,then connecting bus
return ('bus:335E','bus:connector')
elif d>80:
# Might as well go by normal bus
return random.choice(('bus:330','bus:331',':'.
join((favorite_option,
favorite_route))))
elif d>90:
# Relax and choose favorite route
return ':'.join((favorite_option,
favorite_route))


class C(object):
""" A class which does almost nothing """

def __init__(self, x,y):
self.x = x
self.y = y

def f(self):
pass

def g(self, x, y):

if self.x>x:
return self.x+self.y
elif x>self.x:
return x+ self.y

class D(C):
 """ D class """

def __init__(self, x):
self.x = x

def f(self, x,y):
if x>y:
return x-y
else:Chapter 2
[ 69 ]
 return x+y

 def g(self, y):

if self.x>y:
return self.x+y
else:
return y-self.x
```

This is the output from flake8 after running it against the code, sans line-numbers:

```
metricTestCorrected.py:1:1: E265 block comment should start with '# '
metricTestCorrected.py:1:48: W291 trailing whitespace
metricTestCorrected.py:14:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:15:1: E305 expected 2 blank lines after class or function definition, found 0
metricTestCorrected.py:15:1: E112 expected an indented block
metricTestCorrected.py:15:39: E999 IndentationError: expected an indented block
metricTestCorrected.py:18:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:19:1: E128 continuation line under-indented for visual indent
metricTestCorrected.py:20:1: E128 continuation line under-indented for visual indent
metricTestCorrected.py:21:1: E128 continuation line under-indented for visual indent
metricTestCorrected.py:24:1: E112 expected an indented block
metricTestCorrected.py:26:5: E225 missing whitespace around operator
metricTestCorrected.py:27:1: E112 expected an indented block
metricTestCorrected.py:30:5: E225 missing whitespace around operator
metricTestCorrected.py:30:14: E225 missing whitespace around operator
metricTestCorrected.py:31:1: E112 expected an indented block
metricTestCorrected.py:33:80: E501 line too long (80 > 79 characters)
metricTestCorrected.py:34:2: E201 whitespace after '['
metricTestCorrected.py:34:5: E202 whitespace before ']'
metricTestCorrected.py:35:5: E225 missing whitespace around operator
metricTestCorrected.py:36:1: E112 expected an indented block
metricTestCorrected.py:36:5: E225 missing whitespace around operator
metricTestCorrected.py:37:1: E115 expected an indented block (comment)
metricTestCorrected.py:38:1: E112 expected an indented block
metricTestCorrected.py:38:19: E231 missing whitespace after ','
metricTestCorrected.py:39:7: E225 missing whitespace around operator
metricTestCorrected.py:40:1: E115 expected an indented block (comment)
metricTestCorrected.py:41:1: E112 expected an indented block
metricTestCorrected.py:41:32: E231 missing whitespace after ','
metricTestCorrected.py:41:42: E231 missing whitespace after ','
metricTestCorrected.py:42:1: E128 continuation line under-indented for visual indent
metricTestCorrected.py:43:1: E128 continuation line under-indented for visual indent
metricTestCorrected.py:44:7: E225 missing whitespace around operator
metricTestCorrected.py:45:1: E115 expected an indented block (comment)
metricTestCorrected.py:46:1: E112 expected an indented block
metricTestCorrected.py:47:1: E128 continuation line under-indented for visual indent
metricTestCorrected.py:51:1: E305 expected 2 blank lines after class or function definition, found 0
metricTestCorrected.py:51:1: E112 expected an indented block
metricTestCorrected.py:53:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:53:21: E231 missing whitespace after ','
metricTestCorrected.py:54:1: E305 expected 2 blank lines after class or function definition, found 0
metricTestCorrected.py:54:1: E112 expected an indented block
metricTestCorrected.py:57:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:58:1: E305 expected 2 blank lines after class or function definition, found 0
metricTestCorrected.py:58:1: E112 expected an indented block
metricTestCorrected.py:60:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:62:1: E305 expected 2 blank lines after class or function definition, found 1
metricTestCorrected.py:62:1: E112 expected an indented block
metricTestCorrected.py:62:10: E225 missing whitespace around operator
metricTestCorrected.py:63:1: E112 expected an indented block
metricTestCorrected.py:64:7: E225 missing whitespace around operator
metricTestCorrected.py:65:1: E112 expected an indented block
metricTestCorrected.py:65:9: E225 missing whitespace around operator
metricTestCorrected.py:67:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:68:2: E111 indentation is not a multiple of 4
metricTestCorrected.py:70:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:71:1: E305 expected 2 blank lines after class or function definition, found 0
metricTestCorrected.py:71:1: E112 expected an indented block
metricTestCorrected.py:73:1: E302 expected 2 blank lines, found 1
metricTestCorrected.py:73:14: E231 missing whitespace after ','
metricTestCorrected.py:74:1: E305 expected 2 blank lines after class or function definition, found 0
metricTestCorrected.py:74:1: E112 expected an indented block
metricTestCorrected.py:74:5: E225 missing whitespace around operator
metricTestCorrected.py:75:1: E112 expected an indented block
metricTestCorrected.py:76:5: E231 missing whitespace after ':'
metricTestCorrected.py:76:5: E701 multiple statements on one line (colon)
metricTestCorrected.py:77:2: E201 whitespace after '['
metricTestCorrected.py:77:5: E202 whitespace before ']'
metricTestCorrected.py:78:2: E111 indentation is not a multiple of 4
metricTestCorrected.py:78:2: E113 unexpected indentation
metricTestCorrected.py:80:2: E111 indentation is not a multiple of 4
metricTestCorrected.py:82:1: E112 expected an indented block
metricTestCorrected.py:82:10: E225 missing whitespace around operator
metricTestCorrected.py:83:1: E112 expected an indented block
metricTestCorrected.py:85:1: E112 expected an indented block
metricTestCorrected.py:85:16: W292 no newline at end of file
```

This is the fully corrected code, based on flake8 linting:

```python
# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON

"""
Module metricTest.py

Metric example - Module which is used as a testbed for static
checkers.
This is a mix of different functions and classes doing
different things.
"""

import random


def fn(x, y):
    """ A function which performs a sum """
    return x + y


def find_optimal_route_to_my_office_from_home(start_time,
                                              expected_time,
                                              favorite_route="SBS1K",
                                              favorite_option="bus"):
    d = (expected_time - start_time).total_seconds() / 60.0

    if d <= 30:
        return "car"

    # If d>30 but <45, first drive then take metro
    if d > 30 and d < 45:
        return ("car", "metro")

    # If d>45 there are a combination of options
    if d > 45:
        if d < 60:
            # First volvo,then connecting bus
            return ("bus:335E", "bus:connector")
        elif d > 80:
            # Might as well go by normal bus
            return random.choice(("bus:330",
                                  "bus:331",
                                  ":".join((favorite_option,
                                            favorite_route))))

        elif d > 90:
            # Relax and choose favorite route
            return ":".join((favorite_option, favorite_route))


class C(object):
    """ A class which does almost nothing """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self):
        pass

    def g(self, x, y):
        if self.x > x:
            return self.x + self.y
        elif x > self.x:
            return x + self.y


class D(C):
    """ D class """

    def __init__(self, x):
        self.x = x

    def f(self, x, y):
        if x > y:
            return x - y
        else:
            return x + y

    def g(self, y):
        if self.x > y:
            return self.x + y
        else:
            return y - self.x

```


#### Question 4
- pip install mccabe
- Run `mccabe` on sums.py. What is the result?
- Run `mccabe` on sums2.py. What is the result?

#### Question 4: Answer

`pip install mccabe` completed successfully.

The instruction "run `mccabe` on sums.py" is **incorrect** and will not work. To run mccabe on a file we could use it with flake8 if flake8 2.x+ is installed alongside mccabe, for example: `flake8 --max-complexity 10 sums.py`. Alternatively, we can run it with python: `python -m mccabe sums.py`.

The output of `python -m mccabe sums.py` is:

```
("4:0: 'test_sum'", 1)
('If 7', 2)
```

The output of `python -m mccabe sums2.py` is:

```
("7:0: 'test_sum_tuple'", 1)
("4:0: 'test_sum'", 1)
('If 10', 2)
```


#### Question 5
- (Trevor Note: I added this Question header, because the next line was just by itself)
- What are the contributors to the cyclomatic complexity in each piece of code?

#### Question 5: Answer

The contributors to the cyclomatic complexity are the number of linearly independent paths in the logic of the code. This includes but isn't limited to `if` statements, `try`/`except` blocks, `raise` statements, etc.


#### Activity

Select one or more of the tools installed above and use it/them to test the code your team has created as part of the summative assessment. You should demonstrate your tests (and share your results) during the Seminar. Discuss the need to change the code based on the output from the test tools/linters.


#### Activity Answer

For this activity, please see the video walkthrough in [Assignment 2](/pages/module3/assignment2/m3a2.md) where the vscode footage shows that flake8 has been used whilst developing the project code. Unfortunately, it was not mentioned in the walkthrough or in the README as it's just so common. To write code without a linter would be like driving a car without a seatbelt, it's just common sense to use it.
