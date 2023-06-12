---
layout: page
permalink: /pages/module4/unit-assignments/unit3/scanning-activity.html
---

⬅️[Back](/pages/module4/unit-assignments/unit3/m4u3.html)

# Unit 3: Scanning Activity

## Table of Contents

- 👉[My Reflection](#my-reflection)

## Activity Description

Using the website(s) assigned to you in Unit 1, carry out the following exercises and answer the questions listed below. Ideally, you should complete this task before the next seminar, where it will be discussed further. Your findings/results from this exercise will be utilised specifically for the preparation of the 'Vulnerability Audit and Assessment - Results and Executive Summary' assessment in Unit 6.

**Instructions**

Perform a basic scan using standard tools such as traceroute, dig and nslookup. Instructions on using traceroute, etc can be found on this website. Refer to this week's reading for further assistance. Do not use ping as it will cause confusion because of shared addresses.

Use these basic tools and make a list that details the following information:
- How many hops from your machine to your assigned website?
- Which step causes the biggest delay in the route? What is the average duration of that delay?
- What are the main nameservers for the website?
- Who is the registered contact?
- What is the MX record for the website?
- Where is the website hosted?

**Learning Outcomes**
- Identify and analyse security threats and vulnerabilities in network systems and determine appropriate methodologies, tools and techniques to manage and/or solve them.
- Design and critically appraise computer programs and systems to produce solutions that help manage and audit risk and security issues.
- Gather and synthesise information from multiple sources (including internet security alerts and warning sites) to aid in the systematic analysis of security breaches and issues.

**Reflection**

Reflect on this activity by answering the following questions:
- Did you have any issues or challenges with the scans?
- How did you overcome them?
- How will they affect your final report?

**Record all reflections in your e-portfolio.**


## My Reflection

The website I was assigned (that I chose) was https://copperplate.org.uk. As directed, I completed several scans on the domain, using traceroute, dig, and nslookup. My findings are as follows:

>Q: How many hops from your machine to your assigned website?

A: Using `traceroute copperplate.org.uk`, there were 16 hops from my machine to the website before the route began to time out on the next hop:

```bash
$ traceroute copperplate.org.uk
traceroute to copperplate.org.uk (68.66.247.187), 64 hops max, 52 byte packets
 1  192.168.1.1 (192.168.1.1)  3.324 ms  3.556 ms  2.048 ms
 2  10.131.127.254 (10.131.127.254)  14.519 ms  14.317 ms  19.872 ms
 3  10.11.64.25 (10.11.64.25)  17.769 ms  15.505 ms  14.968 ms
 4  10.1.2.105 (10.1.2.105)  36.857 ms  35.737 ms  38.094 ms
 5  207.35.49.125 (207.35.49.125)  34.774 ms  40.637 ms  36.018 ms
 6  tcore4-edmonton_bundle-ether1.net.bell.ca (64.230.119.234)  59.740 ms
    tcore3-edmonton_be1.net.bell.ca (64.230.119.232)  61.645 ms
    tcore4-edmonton_bundle-ether1.net.bell.ca (64.230.119.234)  57.480 ms
 7  * tcore4-vancouver_tengige0-15-0-5.net.bell.ca (64.230.77.109)  64.601 ms *
 8  bx6-seattle_et-0/0/13_ae1.net.bell.ca (64.230.76.157)  60.656 ms  90.761 ms  56.519 ms
 9  * * *
10  chi-b23-link.ip.twelve99.net (62.115.132.154)  116.376 ms  105.568 ms  133.235 ms
11  nyk-bb1-link.ip.twelve99.net (80.91.246.163)  149.674 ms
    nyk-bb2-link.ip.twelve99.net (62.115.137.58)  120.343 ms
    nyk-bb1-link.ip.twelve99.net (80.91.246.163)  127.334 ms
12  * ldn-bb1-link.ip.twelve99.net (62.115.113.21)  185.672 ms *
13  adm-bb1-link.ip.twelve99.net (213.155.136.99)  200.437 ms  197.538 ms
    adm-bb4-link.ip.twelve99.net (62.115.140.43)  186.552 ms
14  adm-b10-link.ip.twelve99.net (62.115.120.227)  202.920 ms
    adm-b10-link.ip.twelve99.net (62.115.120.229)  187.961 ms  236.231 ms
15  a2hosting-ic-370345.ip.twelve99-cust.net (62.115.145.217)  193.504 ms  273.148 ms  307.188 ms
16  v401.nl1-c2-040101_0209-38.a2webhosting.com (209.124.94.237)  202.298 ms  191.469 ms  192.932 ms
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
```

>Q: Which step causes the biggest delay in the route? What is the average duration of that delay?

A: It appears that the largest delay in the route is between hops 14 and 15 for me, in northwest Canada: `a2hosting-ic-370345.ip.twelve99-cust.net (62.115.145.217)`. The average duration of the delay is 257.947ms:

```bash
$traceroute copperplate.org.uk
<...>
15  a2hosting-ic-370345.ip.twelve99-cust.net (62.115.145.217)  193.504 ms  273.148 ms  307.188 ms
<...>
```

>Q: What are the main nameservers for the website?

A: To find the nameservers for the website `copperplate.org.uk` I used `dig` with the following parameters: `dig @1.1.1.1 NS +short copperplate.org.uk`. The results were as follows:
```bash
$ dig @1.1.1.1 +short NS copperplate.org.uk
ns4.a2hosting.com.
ns1.a2hosting.com.
ns2.a2hosting.com.
ns3.a2hosting.com.
```

>Q: Who is the registered contact?

A: Using `whois`, I found the following registered contact information. This would indicate that the website is registered to a company called Nominet UK, which is located in the United Kingdom. Likely this is just the whois privacy service and not the actual owner of the website.

```bash
$ whois copperplate.org.uk
<...>
organisation: Nominet UK
address:      Minerva House
address:      Edmund Halley Road
address:      Oxford Science Park
address:      Oxford OX4 4DQ
address:      United Kingdom of Great Britain and Northern Ireland (the)

contact:      administrative
name:         TLD Registry Services Management
organisation: Nominet UK
address:      Minerva House
address:      Edmund Halley Road
address:      Oxford Science Park
address:      Oxford OX4 4DQ
address:      United Kingdom of Great Britain and Northern Ireland (the)
phone:        +44 1865 332211
e-mail:       registrymanagement@nominet.uk

contact:      technical
name:         TLD Registry Services Technical
organisation: Nominet UK
address:      Minerva House
address:      Edmund Halley Road
address:      Oxford Science Park
address:      Oxford OX4 4DQ
address:      United Kingdom of Great Britain and Northern Ireland (the)
phone:        +44 1865 332211
e-mail:       registrytechnical@nominet.uk
<...>
```

>Q: What is the MX record for the website?

A: Using the `dig` command with the following parameters, `dig copperplate.org.uk MX +short`, I found the following MX record:

```bash
$ dig copperplate.org.uk MX +short
0 mail.copperplate.org.uk.
```

>Q: Where is the website hosted?

A: Per the nameservers, the website is hosted by A2 Hosting, which according to their website has datacentres in Michigan, Arizona, Amsterdam, and Singapore, so technically could be physically hosted in any one of these locations.

>"Reflect on this activity by answering the following questions:
>1. Did you have any issues or challenges with the scans?
>2. How did you overcome them?
>3. How will they affect your final report?"

1. I had no issues with the scans or the tools, I use these tools often and am familiar with the output.
2. N/A
3. N/A
