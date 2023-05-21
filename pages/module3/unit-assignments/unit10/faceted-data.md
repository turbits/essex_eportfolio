---
layout: page
permalink: /pages/module3/unit-assignments/unit10/faceted-data.html
---

⬅️[Back](/pages/module3/unit-assignments/unit10/m3u10.html)

# Unit 10: From Distributed Computing to Microarchitectures: Faceted Data

My answers to follow. Unfortunately, the "article" is not in the Unit 10 reading list but I did manage to find it in the module resources reading list link; apparently the "article" is from Unit 12. The article title is "Faceted Dynamic Information Flow via Control and Data Monads" by Schmitz et al (2016), and is available [here](http://kennknowles.com/research/schmitz-rhodes-austin-knowles-flanagan.post.16.faceted.pdf).

## Requirements

Read Schmitz et al (2016) article about faceted data.
- Do you think this is a good approach to protect systems from data leakage? What are the pros and cons?
- Create a basic outline design of how you would create such a system in Python. 

Add your answers to your e-portfolio.

## Reflection/Answers

> Do you think this is a good approach to protect systems from data leakage? What are the pros and cons?

The article outlines an approach of separating the policy enforcement from the code execution and tracks data flow between program and policy variables.

Pros:
- The separation of concerns between policy and code execution appears to be a logical and effective approach
- It allows policy makers to focus solely on policy without worrying about code execution, and vice versa for programmers
- It has the potential to allow for more dynamic and robust policy enforcement

Cons:
- The approach adds significant complexity to the system, which may be difficult to efficiently manage
- This separation, although a good idea in theory, may be difficult to implement in practice
- Developers would be required to be familiar with policy language which may require training
- Given its complexity, it could add significant performance overhead

> Create a basic outline design of how you would create such a system in Python. 

I would define an outline for a system as such:

1. Define the policy language; this should be a language that is easy to understand and implement, and something that both the policy makers and developers could easily understand. This could be as simple as using a language like YAML or XML, or something more complex like creating a domain-specific language (DSL) that is specific to the system.

2. Create policy enforcement; A system to enforce policy during runtime. I would most likely use a set of decorators for this as they are quite familiar to a developer and are easily understood as to their purpose. The decorators would wrap functions and methods, and enforce policy on the data that is being passed to them.

3. Data monad; A system that tracks the data flow throughout the program.

4. Control monad; A system that tracks the control flow of the program.

5. Testing; The system would require extensive, robust, and ideally automated testing to ensure that the policies are being correctly enforced in the system.
