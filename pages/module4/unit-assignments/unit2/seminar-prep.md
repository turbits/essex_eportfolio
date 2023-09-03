---
layout: page
permalink: /pages/module4/unit-assignments/unit2/seminar-prep.html
---

⬅️[Back](/pages/module4/unit-assignments/unit2/m4u2.html)

# Seminar Activity - The Solar Winds Breach Case Study

[My Case Study](#my-case-study)

## Instructions

Read the Solar Winds article by Temple-Raston (2021) and the description of the Cyber Kill Chain model (Hutchins et al, 2011) and carry out the following activities:
- Create a table that analyses the solar winds exploit using the Cyber Kill Chain. Are there any phases that you cannot identify?
- Create a list of possible mitigations for each phase. Are there any phases you cannot mitigate?
- What tools would you utilise in each phase? Give reasons for your answer.
- Create a slide deck presentation with up to 4 slides that discuss your solution. Be prepared to present it at the seminar this week.

Learning Outcomes
- Identify and analyse security threats and vulnerabilities in network systems and determine appropriate methodologies, tools and techniques to manage and/or solve them.
- Articulate the legal, social, ethical and professional issues faced by information security and risk professionals.


## My Case Study

1. Create a table that analyses the solar winds exploit using the Cyber Kill Chain. Are there any phases that you cannot identify?

*There were no phases that were unidentifiable. The following table was created to analyze the Solar Winds exploit using the Cyber Kill Chain:*


| Phase | Description |
| --- | --- |
| Reconnaissance | Initial attack vectors were multifaceted, involving password brute forcing, security misconfiguration, and stolen secret keys to bypass multi-factor authentication. |
| Weaponization | The weaponization of the attack was extremely sophisticated, involving the reverse engineering of SolarWinds Orion API and a novel system to detect when code would be built and subsequent last-second swap of a temporary file inside the software bundle, resulting in a legitimate SolarWinds-signed software package with an infected binary, `solarwinds.orion.core.businesslayer.dll`. |
| Delivery | The code with malicious payload had to be downloaded, then deployed. The network that the system running the update was deployed on had to also be connected to the internet for the command and control aspect of the attack to function. |
| Exploitation | Once the required delivery parameters were met, the exfiltration began. Due to the nature of Orion, the software often (if not always) had administrative privileges inside a compromised customer's environment. |
| Installation | To maintain persistence, the adversary used multiple mechanisms, including adding tokens and certificates, federation trusts, and backdoors. |
| Command and Control | The payload included a backdoor that uses HTTP to communicate to the adversary C&C servers. It can lay dormant for up to 2 weeks, then begins to retrieve and execute commands that instruct it to do various things to a system, including data collection and exfil, modification of systems, and system actions such as rebooting (Elastic, n.d.). |
| Actions on Objectives | The objectives of the attack were to collect information from compromised environments and exfiltrate it. One method of exfiltration was by compromising the SAML signing certificate to escalate Active Directory privileges and to access resources such as email to exfil (CISA, 2021) |

2. Create a list of possible mitigations for each phase. Are there any phases you cannot mitigate?

| Phase | Mitigation |
| --- | --- |
| Reconnaissance | Hardened security on MFA, hardened password policies such as unguessable passwords and ensuring they are resistant or theoretically impossible to brute force, and ensuring that secret keys are properly secured. |
| Weaponization | Stringent security measures involving the build and deploy process, verification of existing codebase and signatures on build. |
| Delivery | Customer-side verification of signatures. Ideally updates would be tested in a dev environment, although given the sophistication of the adversary and their payload and methods, it's very possible that this would not have been caught. |
| Exploitation | Unsure if the customer could have employed the Principle of Least Privilege here, or if Orion *requires* administrative access, but if so that should have been put in place. |
| Installation | More advanced threat detection tools may have been able to mitigate this issue, but once inside the network the adversary was clearly motivated and knowledgeable enough to persist under the radar. They were employing methods to spoof as legitimate users, fooling typical threat modeling. |
| Command and Control | It would be very difficult to detect the presence of the adversary at this point, which was proven given the length of time this issue had existed in the wild before being found. Unless a mistake was made, or patterns emerged from normal monitoring and threat detection software then I suspect this would be near impossible to mitigate in this particular circumstance without something like an active blue team and perhaps an internal red team working in efficient conjuction to hunt active threats in the environment. |
| Actions on Objectives | For the compromised certificate, it should be ensured that the certificate is configured correctly and securely, so as to not allow self-escalation vulnerabilities to occur. |

3. What tools would you utilise in each phase? Give reasons for your answer.

*I'm not going to go into incredible detail here, but utilising software such as Nessus, a vulnerability assessment tool, would be a start. Having a robust threat detection system in place, such as a SIEM (def) is also a good option, with ideally an in-house team or managed security service provider (MSSP) to monitor and respond to threats real-time, in addition to software that integrates with the SIEM and team(s) monitoring it, such as Crowdstrike and Darktrace. Threat detection and incident response plans are also important, as well as having a robust backup and recovery plan in place.*

4. Create a slide deck presentation with up to 4 slides that discuss your solution. Be prepared to present it at the seminar this week.

*Unfortunately, I can't attend the seminars due to the time they take place. Additionally, I won't be creating a slide deck, but the information contained in the tables above should suffice.*

**References**

CISA (2021). Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure, and Private Sector Organizations. Retrieved from https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a [Accessed 16 May 2023]

Elastic (n.d.). SUNBURST Command and Control Activity. Retrieved from https://www.elastic.co/guide/en/security/current/sunburst-command-and-control-activity.html [Accessed 16 May 2023]
