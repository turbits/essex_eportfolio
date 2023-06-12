---
layout: page
permalink: /pages/module4/unit-assignments/unit4/collab-log4j.html
---

⬅️[Back](/pages/module4/unit-assignments/unit4/m4u4.html)

# Unit 4: Collaborative Discussion 2: The Pros and Cons of Logging - The Impact of log4j

## Table of Contents

- 👉[My Reflection](#my-reflection)
- 👉[Initial Post](#initial-post)

## Activity Description

## Discussion Topic

Read Berger (2021) and Ekelhart et al (2019) and then post your thoughts on the issues of logging for security analysis versus the issues of log-related exploits. You should support your arguments with appropriate academic references.

**Learning Outcomes**
- Identify and analyse security threats and vulnerabilities in network systems and determine appropriate methodologies, tools and techniques to manage and/or solve them.
- Design and critically appraise computer programs and systems to produce solutions that help manage and audit risk and security issues.
- Gather and synthesise information from multiple sources (including internet security alerts and warning sites) to aid in the systematic analysis of security breaches and issues.

**Discussion Guidance**
- Your initial posting should respond to the question and be at least 200 words long. This should be labelled as 'Initial Post'
- You will then respond to at least 2 of your peers' posts in unit 5 (each labelled as 'Peer Response'). To guide your responses, look at the guidelines for the peer review process on the Department’s homepage. Focus on the possible measures that could have been put in place in order to prevent the incidents highlighted by your peers. Please try to limit your response posts to 200-300 words maximum, so that others may be encouraged to reflect on, and respond to your ideas. 
- Referencing: When you have referred to other authors thoughts, ideas and opinions in your posts, you must reference the author as you would in an academic assignment using the UoEO Harvard reference style.
- You will not be assessed on your contribution to this forum throughout the module, but the tutor will post group feedback via a module announcement.
- This activity forms a component of your e-portfolio which you should continue to build throughout your programme. All e-portfolio activities are intended to demonstrate your ability and strengths through evidence and reflection.


## My Reflection

***This reflection is simply my thoughts, the "initial post" to follow.***

I have no doubt mentioned this previously, but the ambiguous "read AuthorX (<date>)" with no reference link in the assignment page is both absurdly unhelpful and a violation of the University's own referencing guidelines. There is a separate area of the learning platform for "reading material" per unit, but this too does not contain actual links, merely a list of authors, the title of the material, and sometimes a chapter or page where applicable. The reading list this time around did not even include one of the author's cited in-line: Berger (2021) does not appear in the reading list. Unbelievable hypocracy and/or laziness throughout the course material in this entire program, not just this course, thus far. Very disappointing.

Regardless, I believe I was able to extrapolate what material "Berger (2021)" was referring to; there is a result that appears to only have been published in 2023 according to the article, but Wikipedia marks it as published in 2021. This article: [What is Log4Shell? The Log4j vulnerability explained (and what to do about it)](https://www.dynatrace.com/news/blog/what-is-log4shell/) appears to be the most relevant, so I will be continuing under the assumption that this is the correct article.


## Initial Post

Logging in general is an indisposable tool for security analysis, debugging, monitoring, and more, but it is not without its own risks. The log4j vulnerability, dubbed "Log4Shell", is a excellent example of a good thing gone bad. Developers using log4j probably never considered that a logging library they were using to catch bad code would (or could) be utilised to deliver malicious payloads. The Log4Shell vulnerability was such that a remote attacker could assume control of a device running infected versions of log4j.

The fact is, logging is a necessary component of any system. This naturally introduces one or more attack vectors based on what software and dependencies are used of course, but the benefits of logging *should* outweigh the risks, as long as the software and any dependencies are being tested and kept up-to-date (in most circumstances). In log4j's case, this didn't matter. The exploit was considered zero-day, in other words, it was unknown to the public or the vendor, Apache in this case, and was most likely being actively exploited in the wild previous to its discovery. Apache released four patches in quick succession in December of 2021 to patch the vulnerability: [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228), [CVE-2021-45046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45046), [CVE-2021-45105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45105), and [CVE-2021-44832](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832) (Berger, 2021).

Regardless of the Log4Shell exploit, logging remains as necessary as it always was. As detailed by Ekelhart et al. in the article "Taming the logs - Vocabularies for semantic security analysis", logging for the purpose of analysis can be extremely complex. Often, logging components have permissive access to a system for the purposes of logging. This introduces a rather inticing attack vector that, if not properly secured, may lead to similar instances of this exploit elsewhere.

Speaking from experience, it is often the case that IT departments are woefully understaffed. This leads to an overall significantly reduced level of visibility into the environment. Few administrators cannot possibly monitor all systems, let alone keep pace with updates, patching, and tickets. Much of the time there is not sufficient logging in place to begin with, leading to security patching and updates falling by the wayside as attention is drawn to "putting out fires" among continuous project deliveries and other day-to-day tasks. This is a recipe for disaster, one that is becoming commonplace as companies grow in size and IT complexity increases. The demand on IT departments and growth of a company outpaces the growth of the IT department by multitudes; the result: a bomb that adheres only to the theory of chaos. At some point the bomb will explode and the result is, increasingly, catastrophic.

**References**

- Berger, A. (2023). What is Log4Shell? The Log4j vulnerability explained (and what to do about it). Available here: https://www.dynatrace.com/news/blog/what-is-log4shell/ [Accessed 11 June 2023]
- Ekelhart et al. (2018). Taming the logs - Vocabularies for semantic security analysis. Available here: https://www.researchgate.net/publication/328376303_Taming_the_logs_-_Vocabularies_for_semantic_security_analysis [Accessed 11 June 2023]
