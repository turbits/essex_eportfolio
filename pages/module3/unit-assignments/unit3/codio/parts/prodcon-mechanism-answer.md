---
layout: page
permalink: /pages/module3/unit-assignments/unit3/codio/parts/prodcon-mechanism-answer.html
---

⬅️[Back](/pages/module3/unit-assignments/unit3/codio/the-producer-consumer-mechanism.html)

## Module 3: Unit 3: Codio Acitivty 3: Producer Consumer Mechanism

### The Code

```python
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

### The Questions and Answers

1. How is the queue data structure used to achieve the purpose of the code?
    - A: The queue data structure is used to store the numbers that are produced. The consumer thread consumes the numbers from the queue. The queue is used to synchronise the producer and consumer threads.
2. What is the purpose of `q.put(i)`?
    - A: The purpose of `q.put(i)` is to put the current number, `i`, into the queue. In this code, the `producer()` function is used to put numbers into the queue, 0 through 99, inclusive.
3. What is achieved by `q.get()`?
    - A: `q.get()` is used to get the current number in the queue. In this code, it is stored in the local variable `number` in the `consumer()` function.
4. What functionality is provided by `q.join()`?
    - A: The functionality provided by `q.join()` is to block the main thread (the main program, in this case) until the queue is empty, at which point the program will continue. In this program's case, the main thread will be blocked until the queue fully processes, at which point it will print the final results.
5. Extend this producer-consumer code to make the producer-consumer scenario available in a secure way. What technique(s) would be appropriate to apply?
    - A: From a thread safety perspective and with Python specifically, queue.Queue is thread-safe and does not require any lock management. In other programming languages, this may or may not be true and could require extensive thread management. If this producer-consumer mechanism was to be used with sensitive data, it would be appropriate to properly control access and perhaps encrypt the data passing through it.
