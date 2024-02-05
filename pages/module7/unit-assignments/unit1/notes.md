Blakely et all 2002
risk: "the possibility of an event which would reduce the value of the business were it to occur. such an event is called an 'adverse event'"
- also define a measure of risk as "annualised loss expectation" (ALE)

Stoneburner et al 2002
risk: "the net negative impact of the exercise of a vulnerability, considering both the probability and the impact of occurrence." 
risk management: "risk management is the process of identifying risk, assessing risk, and taking steps to reduce risk to an acceptable level."

hubbard 2009
risk: a state of uncertainty where some of the possibilities involve a loss, injury, catastrophe, or other undesirable outcome (i.e., something bad could happen)."
uncertainty: "uncertainty[..] is the existence of more than one possibility. The 'true' outcome/state/result/value is not known."
measurement of uncertainty: "measurement of uncertainty [is by] a set of probabilities assigned to a set of possibilities. For example: there is a 60% chance it will rain tomorrow, and a 40% chance it won't."

josey et al 2014
"the Open FAIR Body of Knowledge defines risk as the probably frequency and magnitude of future loss."
risk derived from the combination of threat event frequency, vulnerability, and asset value and liability characteristics

sutton
information risk is a subset of business risk and relates to the confidentiality, integrity, and availability of business information assets and the information management [...] the general principles of business risk management still apply."

---

main concepts that underpin information security management (three tenets of security, Campbell 2016):
- confidentiality
- integrity
- availability

more sources also adding "non-repudiation" to the list

## confidentiality
defined by ISO/IEC 27000:2012 as where "information is not made available or disclosed to unauthorized individuals and entities or processes."

## integrity
defined by ISO/IEC 27000:2012 as "the property of accuracy and completeness of assets"

## availability
defined by ISO/IEC 27000:2012 as "the property of being accessible and usable upon demand by an authorized entity."

## non-repudiation
defined by ISO/IEC 27000:2012 as "ability to prove the occurrence of a claimed event or action and its originating entities."

---

## threat
ISO/IEC 27000:2012 defines a threat as "the potential cause of an unwanted incident, which may result in harm to a system or organization"

## vulnerability
ISO/IEC 27000:2012 defines a vulnerability as "a weakness of an asset or control that can be exploited by one or more threats"

risk-assessment process - threat modelling
physical threats - buildings/people
technical threats - hardware/software

---

risk management process

information risk key element
risk management system - implementation as a programme, proper governance, buy in, and contribution from senior management. all approp standards and certs are known, compliant with legal and regulatory requirements, and are aligned with the business strategy.

Hoffman et al (2016) recommends treating the org as a system of 5 parts:
1. the strategy system - supplies tasks and objectives
2. the intellectual resource - consisting of people's efforts and behaviours
3. the technology system - consisting of materials and technical equipment
4. the structure system - supplying formal structures and procedures
5. the management system - supplies, monitors, and drives the attainment of goals

The Information Security Management System (ISMS)
hoffman and course recommend that risk mgmt process are tightly coupled to other existing mgmt systems such as quality and the isms

must also follow PDCA mandate - plan, do, check, act

---

# Controls and Procedures

Campbell (2016) recommends production of a risk register that collects and collates risks from as wide a variety of sources as possible, and recommends gathering from:
1. risk notification mailboxes
    - where anyone is free to submit a risk. caveat being that submissions may not be categories or require additional work
2. threat workshops
    - use of scenarios with subject matter experts to explore possible risks and vulns. e.g. how would a sysadmin hack into their system, how would a security guard bypass cctv
3. business impact assessments
    - focusing on how business owners of key resources/apps evaluate the business impact of losing their resource/system
4. gap analysis
    - using audit framework to evaluate existing systems/solutions looking for gaps/omissions that constitute a risk
5. security audits
    - pentests where third parties eval systems against best practice, auditing/exploitation toolkits to investigate possible weaknesses

## analysing the risks

### qualitative assessment
may consist of asking pertinent staff to eval a risk as minor/med/major. can be assigned a numerical value later if desired

### quantitative assessment
use statistical or historical data to eval and assign a weighing to a risk

### risk classification
- eliminate: should be removed or avoided completely
- tolerate: risk is recorded but no action taken, usually due to cost-benefit analysis
- reduce: impact of risk is minimized by preventative action
- transfer: cost of mitigation and/or impact of a risk is shared between multiple stakeholders

## mitigating mechanisms
### physical controls
security guards, alarm systems, locks, cctv, etc

### procedural controls
such as new processes or procedures that affect staff as part of their induction, annual training, or even changes to their employment contracts

### technical controls
involving adding or modifying the technical components used as part of the security stack, such as new or improved firewalls, IDS systems, or SIEM (security information and event management) solutions

together these controls can be used to provide:
- preventative controls: by blocking threats or removing vulns
- directive controls: informing staff of their duties and/or responsibilities
- detective controls: to detect and report unauthorised or undesired incidents
- corrective controls: to respond to and fix incidents

---

Risk = Threat x Vulnerability x Asset

based on OPEN Fair definition

## qualitative assessment
It is used for lower value assets or when the people performing the assessment do not have the appropriate training or skills to perform a quantitative assessment, or where the necessary amount of data is not available.


Threats and/or vulnerabilities are assigned to categories such as  high / medium / low - even if numerical values are assigned at a later date to ease with cost calculations or attribution. 


Once categorisation has been made then the calculation discussed previously can still be performed so that a numerical, or even financial risk can be assigned to each potential threat.  We will discuss the validity of this value later.

## quantitative assessment
It is a well defined, mathematical calculation. It often involves the use of probabilities and game theory and is widely used by insurance companies when creating indemnities against certain risks occurring.


Hubbard (Hubbard, 2009) discusses quantitative assessment in great detail and categorises the types of people that he believes can perform these calculations into four areas – his so called '4 horsemen', which we will explore further in the next section.

# the four horsemen - quantitative assessments
hubbard (2009) categorises the types of people that he believes can perform these calculations into four areas:
- actuaries
- war quants: some term he coined for ww2 scientists
- economist
- management consultant

---


# Open FAIR
standard produced by The Open Group, a consortium of companies that produce open standards for IT. unix trademark, togaf, archimate

## Factor Analysis Information Risk
- Open Risk Taxonomy (O-RT)
- Open Risk Analysis (O-RA)

according to open group (josey et al 2014) reasons to use open fair are:
- emphasis on risk: as opposed to emphasis on controls or instrumentation
- logical and rational framework: providing guidance on how to do analysis
- quantitative: focus on data and probabilities whenever possible
- flexible: adaptable according to availability of resources and data
- rigorous: designed to avoid gaps and errors caused by heuristics and bias

Open FAIR designed to work with/be compatible with other standards such as:
- ISO 31000
- ISO 27001
- ISO 27005
- COSO ERM
- SABSA (Sherwood Applied Business Security Architecture)
- COBIT (Control Objectives for Information Technology)
- OCTAVE
- NIST 800-30

## Open FAIR Diagram
Risk
- Loss Event Frequency (LEF)
    - Threat Event Frequency (TEF)
        - Contact Frequency (CF)
        - Probability of Action (PoA)
    - Vulnerability (Vuln)
        - Threat Capability (TCap)
        - Resistance Strength (RS)
- Loss Magnitude (LM)
    - Primary Loss (PL)
    - Secondary Loss (SL)
        - Secondary Loss Event Frequency (SLEF)
        - Secondary Loss Magnitude

## OCTAVE
Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE) framework created at Carnegie Mellon in 1999

OCTAVE mix of 3 programs:
- information security evaluation (ISE) - was a vulnerability evaluation system focusing on computing infrastructure
- CMUs software engineering institute (SEI) - risk program software risk management expertise
- information security risk management (ISRM) - survey and research

