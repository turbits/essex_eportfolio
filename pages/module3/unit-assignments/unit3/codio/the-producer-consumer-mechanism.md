---
layout: page
permalink: /pages/module3/unit-assignments/unit3/codio/the-producer-consumer-mechanism.html
---

⬅️[Back](/pages/module3/unit-assignments/unit3/codio/m3u3-codio.html)

# Module 3: Unit 3: Codio Activity 2: The Producer-Consumer Mechanism

## Table of Contents

- 📃[My Answers to the Questions](/pages/module3/unit-assignments/unit3/codio/parts/prodcon-mechanism-answer.html)

## Assignment Instructions

Producer/Consumer Problem (also known as the ‘bounded buffer’ problem):
- A ‘producer’ is producing items at a particular (unknown and sometimes unpredictable) rate.
- A ‘consumer’ is consuming the items – again, at some rate.

For example, a producer-consumer scenario models an application producing a listing that must be consumed by a printer process, as well as a keyboard handler producing a line of data that will be consumed by an application program. This is shown in the picture below (Shene, 2014).

Items are placed in a buffer when produced, so:
- Consumer should wait if there isn’t an item to consume
- Producer shouldn’t ‘overwrite’ an item in the buffer

![](/pages/module3/unit-assignments/unit3/codio/assets/the_producer_consumer_mechanism.jpg)

Synchronisation is necessary because:
- If the consumer has not taken out the current value in the buffer, then the producer should not replace it with another.
- Similarly, the consumer should not consume the same value twice.


## Task

Run producer-consumer.py in the provided Codio workspace (Producer-Consumer Mechanism), where the queue data structure is used.

A copy of the code is available here for you.

```python
# code source: https://techmonger.github.io/55/producer-consumer-python/
 
from threading import Thread
from queue import Queue
 
q = Queue()
final_results = []
 
def producer():
    for i in range(100):
        q.put(i)
        
 
def consumer():
    while True:
        number = q.get()
        result = (number, number**2)
        final_results.append(result)
        q.task_done()
   
   
for i in range(5):
    t = Thread(target=consumer)
    t.daemon = True
    t.start()
    
producer()
 
q.join()
 
print (final_results)
```

Answer the following questions:
- How is the queue data structure used to achieve the purpose of the code?
- What is the purpose of q.put(I)?
- What is achieved by q.get()?
- What functionality is provided by q.join()?
- Extend this producer-consumer code to make the producer-consumer scenario available in a secure way. What technique(s) would be appropriate to apply?

Remember to record your thoughts and answers in your e-portfolio.
