---
layout: page
permalink: /pages/module6/unit-assignments/unit9/m6u9-eportfolio-activity.html
---

⬅️[Back](/pages/module6/unit-assignments/unit9/m6u9.html)

# Unit 9 - ePortfolio Activity: Improving Code Quality

This activity had us implement "at least 3" of the srategies presented in the Writing Clean and Pythonic Code seminar by James Mertz (Mertz, 2019). The presentation included (summed up) the following strategies:
- Use tools to help you
    - IDEs
        - PyCharm
        - VS Code
    - Linters
        - PyLint
    - Formatters
        - black.py
- Properly structure your project
    - Notebook structure
    - One off script structure
    - Package structure
- Follow a style guide
    - PEP8
- Document all the things
    - Comments & docstrings
    - Project documentation
    - Documentation Generators
        - Sphinx

I will be using my "autonomous vehicle system" project from a previous course in this program, Object Oriented Programming, way back in module 2, almost a year ago! Back then, we were required to use a platform called "codio", which is a web-based IDE. This time around, I will be using the JetBrain's PyCharm IDE, a fully featured and python-focused IDE. Unfortunately, the Python version installed in the codio environment was 2.7.15 and I was unable to upgrade, if I am remembering correctly.

So, the first order of business is to convert this Python 2.7.15 code to Python 3.11. I believe this would conform to the "use tools to help you" and "follow a style guide" strategies - I am using a modern and focused Python IDE, I am using the latest version of Python, and PyCharm will assist me with PEP8 compliance. For now, I won't touch the structure of the project or add/remove any comments or docstrings, I'll leave that for after I finish converting the code.

Some things that were first apparent when beginning to convert the code were:
- Any "print" statements needed to be converted to "print()" functions
- It appears I did not originally follow PEP8, as the files did not have an indentation of 4 spaces, but rather 2 spaces
- Some parameters and variables had to be type hinted to conform to various PEP8 warnings
- Some parameters shadowed built-in names, so had to be renamed. An example of this is in the utility.py file, in the "get_choice" function, where the "list" parameter is a list of choices the user can select. List is a built-in name in Python, so it was renamed to "choice_list".

The program was built hastily and was not finished before, so there were some existing bugs. That being said, it at least presented a workable menu. After conversion, the program technically runs without error, but the main menu is printed in a loop! I do remember some weird menu bugs on the first attempt a year ago, so they are most likely related. I won't be fixing these bugs, but I will be adding some comments and docstrings to the code to explain some oddities I came across when converting.

There is a line in the `utility.py` file that reads `if not str.isalnum(user_input):`. At first glance I had forgotten what "isalnum" meant, so had to look it up. It's clear to me now that this means "is alphanumeric", but I've added a comment to explain it. I added docstrings to the `c_err` function in `utility.py` as well (this is terribly named). In `backend.py` I added a docstring to the `traffic_emerg_stop` class method, as it is not immediately clear what exactly this would do. One would probably think this stops all traffic immediately, which shows how badly named it is. Instead, this function runs every "tick" of the program, and has a _chance_ to stop traffic. I've also added a similar docstring to the `traffic_speed_change` method, also in this file. Similarly, it too sounds like it would immediately change the traffic speed, but instead is a chance every tick.

I think these changes and conversion count towards at least three of the strategies presented in the seminar. I've used a tool to help me (PyCharm), I've followed a style guide (PEP8, with the help of PyCharm), and I've added comments and docstrings to the code where appropriate. I've also done very minor refactoring and fixed some conversion bugs from 2.7.15 to 3.11.

For reference, you can view:
- The original code: https://github.com/turbits/essex-m2a2
- The updated code: https://github.com/turbits/essex_eportfolio/tree/main/pages/module6/unit-assignments/unit9/avs_m2a2_repo


**References**
- Mertz, J. (2019). Writing Clean and Pythonic Code. Available at: https://dataverse.jpl.nasa.gov/file.xhtml?fileId=63890&version=1.0 [Accessed 27 November, 2023]
