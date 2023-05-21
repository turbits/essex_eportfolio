---
layout: page
permalink: /pages/module3/unit-assignments/unit4/seminar-prep/seminar-preparation.html
---

⬅️[Back](/pages/module3/unit-assignments/unit4/m3u4.html)

# Unit 4: Seminar Preparation

## Requirements

### Recursion

One of the classic programming problems that is often solved by recursion is the towers of Hanoi problem. A good explanation and walkthrough are provided by Cormen & Balkcom (n.d.) - the link is in the reading list. (the code they used for their visual example is provided on their website as well).

1. Read the explanation, study the code and then create your own version using Python (if you want to make it more interesting you can use asterisks to represent the disks). Create a version that asks for the number of disks and then executes the moves, and then finally displays the number of moves executed.
2. What is the (theoretical) maximum number of disks that your program can move without generating an error?
3. What limits the number of iterations? What is the implication for application and system security?

### Regex

The second language concept we will look at is regular expressions (regex). We have already presented some studies on their use, and potential problems, above. The lecturecast also contains a useful link to a tutorial on creating regex. Re-read the provided links and tutorial (Jaiswal, 2020) and then attempt the problem presented below:

1. The UK postcode system consists of a string that contains a number of characters and numbers – a typical example is ST7 9HV (this is not valid – see below for why). The rules for the pattern are available from idealpostcodes (2020).
Create a python program that implements a regex that complies with the rules provided above – test it against the examples provided.
    - Examples:
      - M1 1AA
      - M60 1NW
      - CR2 6XH
      - DN55 1PT
      - W1A 1HQ
      - EC1A 1BB
2. How do you ensure your solution is not subject to an evil regex attack?


## Reflection

### Recursion

1. See the following links for this unit assignment:
- 🧑‍💻[Python program for Tower of Hanoi problem - download .py file](tower-of-hanoi.py)
- 📃[Markdown version](/pages/module3/unit-assignments/unit4/tower-of-hanoi.html)

2. As my program mentions, the recursion limit for Python 3.11 is, as of writing, 1000. We can also get the recursion limit by calling `sys.getrecursionlimit()`. It is also possible to set the recursion limit (`sys.setrecursionlimit()`), but this is not recommended as it can cause a stack overflow.

3. The number of iterations are limited by the recursion limit. The implication for application and systems security is that if the recursion limit is too low, and the program relies on deep recursion, it will crash. If the recursion limit is too high or not set, the program may crash due to a stack overflow. The recursion limit can be exploited by a malicious actor to intentionally crash a program, or to cause a denial of service attack. Stack overflows can also be exploited to do various things, including code injection due to memory corruption.

### Regex

1. See the following links for this unit assignment:
- 🧑‍💻[Python program for UK postcode regex - download .py file](uk-postcode-regex.py)
- 📃[Markdown version](/pages/module3/unit-assignments/unit4/uk-postcode-regex.html)

2. The function that I wrote, while I believe it is compliant with the postcode specification provided, does not implement a timeout exception, which would be the main way of preventing an 'evil regex' or 'regex bomb' attack. This would be a solid addition to the function.

Unfortunately the re.match() function doesn't seem to timeout, nor can you set a domain-like property, such as in .NET: `domain.SetData("REGEX_DEFAULT_MATCH_TIMEOUT", TimeSpan.FromSeconds(1));`. In Python, you could write a custom exception and decorator, which there is an example of in [this StackOverflow answer](https://stackoverflow.com/a/11901541), although this appears to now either not work at all, or only work for Unix. I'm not sure of other ways to implement a timeout exception but I'm sure there are several. At this point though the explanation above should suffice as a reflection on the topic and what I would do in a real-world scenario.

