---
layout: page
permalink: /pages/module6/assignment1/m6a1-project-report.html
---

⬅️[Module 6](/pages/module6.html)

# Unit 6: Assignment 1: Project Report

This is a markdown version of the (prettier) submitted document, available for download (.docx) [here](/pages/module6/assignment1/SEPM_A1_TeamProjectReport.docx).

# Synputer Project Report

<ins>Software Engineering Project Management - PCOM7E - Group 1 - Assignment 1</ins>

Authors: Nassar Al-Naimi, Charles Kuyayama, Abdulahi Alihu Ngamjeh, Trevor Woodman

## Introduction
Amidst the fervour of the computing revolution, we embark on a mission - the creation of a ground-breaking computing system: the Synputer. In this proposal, we take a step through the looking glass, and see up-close the design, development, and testing processes, and a thorough deep dive into the materials and pricing structure that will position the Synputer as a must-have premium product.

## Methodology Section
### Development Methodologies Overview
In software and hardware development, choosing the right methodology is pivotal. Two prominent methodologies, Waterfall and Agile, offer distinct approaches.

#### Waterfall
A structured, sequential approach suitable for projects with stable requirements (Lientz & Swanson, 1980).
- Advantages: Clear documentation, defined milestones.
- Disadvantages: Limited flexibility for changing requirements, late-stage surprises.

#### Agile
An iterative, adaptable approach emphasizing customer collaboration (Beck et al., 2001).
- Advantages: Adaptability to changing requirements, frequent deliveries, stakeholder engagement.
- Disadvantages: Requires active collaboration, not suitable for all projects.

### Justification for Agile Approach
We choose Agile for the Synputer Development Project due to its adaptability to evolving technology and changing requirements (Highsmith & Cockburn, 2001).

## Gherkin Specifications
See **APPENDIX A**

These Gherkin specifications provide a clear and structured way to define the expected behaviour of the system based on the identified key requirements. THey will assist in development, testing, and valdiation phases of key feature sets in the Synputer.

## Requirements Gathering

| Component | Requirement | Assumption |
| --- | --- | --- |
| CPU | Motorola 68K | Readily available |
| RAM | 1024KB | Compatibility with 68K, speed |
| Storage | Multiple options (disk, cartridge) | Adequate default storage for user needs |
| Graphics | 2D, portable | Can match software demands |
| Connectivity | Serial port(s), joystick port, keyboard port | Industry standards |
| GUI | X-Windows, PTR/E, GEM | User-friendly, meets expectations |

## Project Plan
### Budget Allocation
The Synputer Development Project operates within a strict budget of £500,000, with no exceeding until income is generated from machine sales. Budget allocation is as follows:
- Materials (£250,000): Procurement of components, software licenses, and materials essential for Synputer development.
- Labour (£200,000): Salaries for the development team and QA personnel, ensuring top talent for the project.
- Overhead (£50,000): Covers additional expenses such as utilities, facility costs, and administration to support the project.

Remaining Budget: £0 (Strict adherence to budget constraints)

### Milestones and Constraints
- First Major Prototype: Scheduled for completion one year before the product release, allowing ample time for testing and refinement.
- EDC Purchase (2,000 Unit	s): EDC's commitment to purchase 2,000 units before the product release, a significant opportunity and constraint.
- Product Release by January 1984: Firm deadline set by Syn, ensuring the project's maximum timeline of approximately 13 months.

### Pricing Strategy and Revenue Generation
Detailed pricing strategies and considerations, as well as revenue generation projections, are provided in the Appendix B and Appendix C respectively.

The order to EDC will be for the agreed upon amount of 2000 units at £250 each.

Given requirements, component cost, salaries, and licenses, the projected initial unit cost of the Synputer will be approximately £200.

The Commodore 64’s rough price tag of £300-£350 set it up as a viable personal computer that many households could afford. We believe a similar aggressive pricing strategy will be beneficial to the Synputer, and so our initial unit price will be set at £300. This target may fluctuate before release based on our pricing strategy including price testing as well as the industry and economy closer to date.

## Testing Strategy
### Testing Times Allocation
Testing times have been allocated to various phases based on their complexity and criticality:
- Longer testing cycles (2-week sprints) for hardware development due to assembly intricacies.
- Shorter cycles (1-week sprints) for software development to facilitate rapid prototyping and testing.

### Types of Testing
Multiple types of testing will be conducted to ensure product quality:
- Unit testing to validate software components in isolation.
- Integration testing to identify issues when integrating system parts.
- System testing to verify the entire system's performance.
- User acceptance testing to confirm alignment with user needs and requirements.

## Conclusion
The Synputer project represents a fusion of innovation and sound project management principles. Our choice of Agile-based methodology for software development aligns with industry trends, ensuring adaptability and responsiveness (Kerzner, 2017; Lock, 2019). 

Requirements gathering, grounded in stakeholder dialogue and Gherkin specifications, sets the stage for user-centric development (Schwalbe, 2018).

Our project plan, constrained by budget and deadlines, emphasizes resource allocation and efficiency (Phillips & Phillips, 2017).

Testing, a cornerstone of quality assurance, will strike a balance between hardware and software quality. Our pricing strategy and revenue generation plans, included in the appendices, promise long-term success.

## References
- Beck, K., et al. (2001). Manifesto for Agile Software Development. Retrieved from https://agilemanifesto.org/
- Highsmith, J., & Cockburn, A. (2001). Agile software development: The business of innovation. Computer, 34(9), 120-127.
- Kerzner, H. (2017). Project Management: A Systems Approach to Planning, Scheduling, and Controlling. John Wiley & Sons.
- Lientz, B. P., & Swanson, E. B. (1980). Software maintenance management: A study of the maintenance of computer application software in 487 data processing organizations. ACM.
- Lock, D. (2019). Project Management. Gower Publishing, Ltd.
- Phillips, J., & Phillips, P. P. (2017). PMP Project Management Professional Study Guide. Sybex.
- Schwalbe, K. (2018). Information Technology Project Management. Cengage Learning.
- Simpson, D. & Hinkle, G. (2023) An Introduction to MAHD: Modified Agile for Hardware Development Framework. Available at: https://agileforhardware.org/wp-content/uploads/2018/07/An-Intro-to-MAHD-Ebook-Final-7_25_18.pdf [Accessed 25 October 2023]
- Ullman, D. (2019) Scrum for Hardware and Systems Development. Available at: https://www.researchgate.net/publication/335819562_Scrum_for_Hardware_and_Systems_Development [Accessed 25 October 2023]

## APPENDIX A: GHERKIN SPECIFICATIONS
**Scenario: Joystick Use**
- Given the Synputer is powered off.
- When the user connects a joystick
- And the user presses the power button.
- And the computer finishes boot sequence.
- Then the joystick is available for use

**Scenario: Storage expansion with native or third-party cartridges**
- Given the Synputer storage expansion is empty.
- When the user inserts a third-party storage cartridge
- And the user attempts to save a file.
- Then the drive is available for storing the file

**Scenario: Multi-tasking in HB/OS**
- Given the Synputer is on
- And the Synputer has available RAM.
- When the user opens a second program
- Then the Synputer is multitasking both programs

**Scenario: TeleBasic to HyperBasic transpilation and execution**
- Given the program to run is written in TeleBasic
- And the user has tried to run the program.
- Then the Synputer transpiles the TeleBasic program to HyperBasic
- Then the Synputer compiles the HyperBasic program
- Then the Synputer starts the program
- Then the program opens

**Scenario: Backwards-compatible emulation of software**
- Given the program to run was made for an older Syn-built machine.
- And the user has tried to run the program.
- Then the Synputer starts an emulator
- Then the Synputer starts the program in the emulator
- Then the program opens

**Scenario: Keyboard is connected to Synputer**
- Given the Synputer is powered off.
- And the user has connected a keyboard via PS/2 port.
- And the user presses the power button.
- And the computer finishes the boot sequence.
- Then the keyboard is available for use

**Scenario: 512kb RAM Overflow**
- Given the Synputer is using the limit of the 512kb RAM.
- And another process is opened by the user or the Synputer.
- Then the Synputer will crash with a stack overflow error
- Then the Synputer will power cycle

**Scenario: Power outage while Synputer powered on and connected to outlet**
- Given the Synputer is plugged into a wall outlet.
- And the Synputer is powered on.
- And a power cut occurs to the wall outlet.
- Then the Synputer will continue to operate until battery is depleted

**Scenario: Serial RS-485 device attached**
- Given the Synputer is powered off.
- And a RS-485 device is attached via the RS-485 port.
- And the user presses the power button.
- And the Synputer finishes the boot sequence.
- Then the serial device is available for use

**Scenario: EZ-SUITE Business productivity suite use outside HB/OS**
- Given the user runs an EZ-SUITE program
- And the OS being used is not HB/OS
- Then the program crashes with an unsupported OS error

## APPENDIX B: PRICING STRATEGY
### Pricing Strategies and Considerations
The pricing strategy for the Synputer machine is carefully crafted to balance competitiveness and profitability. It considers various factors and considerations:

1. **Production Cost**: Pricing considers the total cost of production, including materials, labour, and overhead. We aim to ensure that the selling price covers these costs while leaving room for profit.
2. **Market Analysis**: Thorough market research is conducted to understand customer expectations, demand elasticity, and competitive pricing in the computing industry.
3. **Competitive Positioning**: The Synputer will be positioned competitively within the market. Pricing will be set to offer value to customers while maintaining a competitive edge.
4. **Segmentation**: Different pricing strategies may be employed for various customer segments. Tailoring pricing to meet the needs of different customer groups is a consideration.
5. **Promotions and Discounts**: Consideration of promotional pricing and discounts to stimulate initial sales and market penetration.
6. **Long-term Sustainability**: Pricing is not just for immediate profitability but also for long-term sustainability. It considers the potential for recurring revenue through accessories, software, and support services.
7. **Price Testing**: Ongoing evaluation and adjustment of pricing strategies based on market feedback and performance.

## APPENDIX C: REVENUE GENERATION
### Projections and Plans for Income Generation
The income generation plan for the Synputer project is structured to maximize revenue while ensuring product quality and customer satisfaction:

1. **Product Sales**: Income generation begins with the sale of Synputer machines. Revenue projections are based on anticipated sales volumes and pricing strategies.
2. **Accessories and Upgrades**: Additional revenue streams will be created through the sale of accessories and hardware upgrades compatible with the Synputer.
3. **Software Licensing**: Revenue will also be generated through software licensing, including proprietary software bundled with the Synputer.
4. **Maintenance and Support Services**: Offering maintenance contracts and support services to customers will provide ongoing revenue while enhancing customer loyalty.
5. **Market Expansion**: Plans for expanding into new markets and exploring partnerships to increase sales and revenue.
6. **Cost Management**: Continuous cost management to optimize profit margins and ensure profitability.
