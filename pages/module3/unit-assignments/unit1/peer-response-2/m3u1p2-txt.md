---
layout: page
permalink: /pages/module3/unit-assignments/unit1/peer-response-2/m3u1p2-txt.html
---

⬅️[Back](/pages/module3/unit-assignments/unit1/m3u1.html)

## Module 3: Unit 1: Peer Response 2

This is a unit assignment component of [Secure Software Development](/pages/module3.html) - [Unit 1](/pages/module3/unit-assignments/unit1/m3u1.html).

- [Image Version](/pages/module3/unit-assignments/unit1/peer-response-2/m3u1p2.html)

#### Daud Abassi's Initial Post

> ##### Initial Post - Using Components With Known Vulnerabilities
>
> ###### by Daud Abassi - Sunday, 12 February 2023, 10:45 AM
>
> "Using Components with Known Vulnerabilities" is a security risk that refers to the practice of incorporating third-party software libraries, frameworks, or modules into a web application without adequately checking for vulnerabilities. These components can often contain security flaws that have been discovered and documented by the security community, and attackers can leverage these vulnerabilities to compromise the security of the application.
>
> One of the primary reasons this security risk is so prevalent is because of the ease with which developers can obtain and integrate components into their applications. With the rise of open-source software, developers can access a wide range of high-quality components, but these components may also have known vulnerabilities that have not yet been fixed.
>
> Furthermore, even when a vulnerability is discovered, the component author may not have released a patch to fix the issue. In such cases, the only way to mitigate the risk is to either stop using the component altogether or to perform a thorough security audit to assess the impact of the vulnerability and implement mitigation strategies.
>
> To reduce the risk of using components with known vulnerabilities, it is important for organizations to adopt a software development lifecycle that includes regular security assessments and to implement processes to regularly monitor and update components used in applications. This includes establishing a component inventory, regularly checking for new vulnerabilities in those components, and having a plan in place to remediate any vulnerabilities that are discovered.
>
> In conclusion, using components with known vulnerabilities is a common security risk that can have serious consequences for organizations. By following best practices and implementing proper security measures, organizations can reduce the risk and protect their web applications from potential attacks.
>
> In the following flowchart diagram while logging into a online shopping website such known vulnerable components can be exploited during multiple processes.
>
> https://documents.lucid.app/documents/e31d7181-7ce8-46b1-9b38-266d5226eec7/pages/0_0?a=1836&x=534&y=-88&w=1008&h=1496&store=1&accept=image%2F*&auth=LCA%2019314cb42003411bded7504ac967a6350489805e-ts%3D1676195191
>
> (Trevor - Note: The link above is broken and a flowchart was not visible in the post.)

#### My Peer Response

> ##### Re: Initial Post - Using Components With Known Vulnerabilities
>
> ###### by Trevor Woodman - Tuesday, 14 February 2023, 10:52 PM
>
> Hi Daud,
>
> Your subject matter is clearly explained, and it is true that it is quite easy to use insecure components if one isn’t careful, especially libraries. It is worth noting that your OWASP category is out of date. It’s now known as A06:2021-Vulnerable and Outdated Components (OWASP, 2021). It also appears you've had an issue with including your flowchart here as I only see part of what looks like a URL.
>
> Some notable examples of insecure components that come to mind are npm (https://npmjs.com) and PyPi (https://pypi.org), both public library repositories for JavaScript and Python, respectively. Anyone can create and publish a package to these repositories which could, and has, introduced significant security issues to new and existing projects. A package in use by many could theoretically be compromised and have malicious code injected, which if developers were not careful by using validated versions of the libraries (and sub-dependent libraries) that they use in their projects, they could have a security issue on hand.
>
> A high-profile example of something similar, while nothing as malicious as code injection but still affected a significant number of developers using the component directly or indirectly, was the sudden removal of a specific library back in 2016 when a developer, Azer Koçulu, removed all 272 of their packages from npm in protest to corporate pressure. One of the packages, called left-pad, was in use by an incalculable number of packages either as direct dependencies or sub-dependencies, breaking thousands of builds by developers all over the world (Schlueter, I. 2016).
>
> In summary, an interesting topic and one that has many facets. The importance of validating one’s dependencies at the general component level, only using the version(s) of the validated component, and validating any sub-dependencies cannot be overstated.
>
> References:
> Schlueter, I. (2016). kik, left-pad, and npm. Available at https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm [Accessed 14 February 2023]
> OWASP (2021). OWASP Top Ten. Available at https://owasp.org/www-project-top-ten/ [Accessed 14 February 2023]
