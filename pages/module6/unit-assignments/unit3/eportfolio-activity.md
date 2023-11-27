---
layout: page
permalink: /pages/module6/unit-assignments/unit3/eportfolio-activity.html
---

⬅️[Back](/pages/module6/unit-assignments/unit3/m6u3.html)

# Unit 3 - ePortfolio Activity: Data Structures Reflection

> Read Dicheva & Hodge (2018). Think about an online system which you use on a daily basis. Consider how it might operate at the back-end using data structures. This will inform our discussion during next week’s seminar.


## My Response

Let's consider a platform such as GitHub; I will briefly preface by saying I have never looked at any articles on how GitHub does this and the engineering team is most likely cleverer than I am. This platform has social elements, code repositories, project wikis, project issue trackers, and more. The platform is used by millions of users, and is a great example of a system that would use various data structures to store and retrieve data in the most efficient manner.

For example, if we take a look at the profile page, we can see that there are several public and private fields such as real name, username, email(s), social link(s), etc. Some of these, such as emails or social links, could be stored using lists or arrays. Repositories could be stored in tree structures or linked lists. The issues in the issue tracker could be stored in a graph structure with a reference to the repository, the issue identifier, the title, description, and whatever else you would want in an issue. The wiki could be stored in a tree structure, although using a database would probably be much more efficient.

All of these data structures would of course be stored in one or more databases and tables, which would be data structures themselves. This matroyshka doll of data structures is what would make up the back-end of a platform such as GitHub, or really any sufficiently complex software.
