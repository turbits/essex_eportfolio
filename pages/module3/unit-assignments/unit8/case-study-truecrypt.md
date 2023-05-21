---
layout: page
permalink: /pages/module3/unit-assignments/unit8/case-study-truecrypt.html
---

⬅️[Back](/pages/module3/unit-assignments/unit8/m3u8.html)

# Unit 8: Cryptography Case Study: TrueCrypt

My answer to follow.

## Requirements


This discussion will last for 3 weeks covering units 8, 9 and 10. Ensure you include appropriate citations and references in all your posts (this is not included in the word count for each week's post/submission).

### Discussion Topic

TrueCrypt was a popular and well-respected operating system add-on that could create encrypted volumes on a Windows and/or Linux system. In addition, it was also designed to create a complete, bootable volume that could encrypt the entire operating system and data for a Windows XP system. It was discontinued in 2014.

Case Study: Read the TrueCrypt cryptanalysis by Junestam & Guigo (2014) (link is in the reading list) and then answer the following questions:
- The (anonymous) TrueCrypt authors have said “Using TrueCrypt is not secure as it may contain unfixed security issues” (http://truecrypt.sourceforge.net/, 2014). Does the cryptanalysis provided above prove or disprove this assumption?
- Would you be prepared to recommend TrueCrypt to a friend as a secure storage environment? What caveats (if any) would you add?

Remember to save this to your e-portfolio.

Present an ontology design which captures the weaknesses of TrueCrypt, and organise them according to their severity. Expand the ontology design by considering the factors which will cause each weakness to become an issue from a user's perspective. For example, if a user wishes to encrypt a disk storing bank details using TrueCrypt, which weakness of the software might cause this specific user goal to be negatively impacted? 

### Learning Outcomes
- Identify and manage security risks as part of a software development project.
- Critically analyse development problems and determine appropriate methodologies, tools and techniques (including program design and development) to solve them.
- Design and develop/adapt computer programs and to produce a solution that meets the design brief and critically evaluate solutions that are produced.

### Assignment Guidance
- Your initial posting should respond to the question and be at least 200 words long.  This should be labelled as 'Initial Post'
- You will then respond to at least 2 of your peers' posts in unit 2 (each labelled as 'Peer Response').  To guide your responses, look at the guidelines for the peer review process on the Department’s homepage. Focus on the possible measures that could have been put in place in order to prevent the incidents highlighted by your peers.  Please try to limit your response posts to 200-300 words maximum, so that others may be encouraged to reflect on, and respond to your ideas. 
- In Unit 3, you should provide a summary post based on your initial post, the feedback from your peers and the content of the three units. Please label this as ‘Summary Post’. It should be 300 words.
- Referencing: When you have referred to other authors thoughts, ideas and opinions in your posts, you must reference the author as you would in an academic assignment using the UoEO Harvard reference style.
- You will be not be assessed on your contribution to this forum throughout the module, but the tutor will post group feedback via a module announcement.
- This activity forms a component of your e-portfolio which you will submit in unit 12. All e-portfolio activities are intended to demonstrate your ability and strengths through evidence and reflection.

---

## Reflection/Answer

1. The (anonymous) TrueCrypt authors have said “Using TrueCrypt is not secure as it may contain unfixed security issues” (http://truecrypt.sourceforge.net/, 2014). Does the cryptanalysis provided above prove or disprove this assumption?
- According to the cryptanalysis by Junestam & Guigo (2014), TrueCrypt is still secure enough to be used, regardless of what the authors claim. This is, or at least was, a point of contention at the time. Another team, VeraCrypt, picked up where TrueCrypt left off and has continued to develop the software.

2. Would you be prepared to recommend TrueCrypt to a friend as a secure storage environment? What caveats (if any) would you add?
- I would not recommend TrueCrypt when something like [VeraCrypt](https://www.veracrypt.fr/en/Home.html) exists, a more mature and secure version of TrueCrypt.

3. Present an ontology design which captures the weaknesses of TrueCrypt, and organise them according to their severity. Expand the ontology design by considering the factors which will cause each weakness to become an issue from a user's perspective. For example, if a user wishes to encrypt a disk storing bank details using TrueCrypt, which weakness of the software might cause this specific user goal to be negatively impacted?
- The ontology I have designed is outlined below:

**TrueCrypt Weakness**
- Security Concerns
    - High Severity
        - Unpatched Vulnerabilities
            - Factors: Discontinued development, lack of security updates, known exploits
            - Impact: Potential unauthorised access to encrypted disk containing user details
    - Medium Severity
        - Weak Encryption Algorithms
            - Factors: Outdated or improperly implemented algorithms, faster hardware, improved attack methods, improved cryptanalysis techniques
            - Impact: Reduced protection level of user details, potential unauthorised access in the future
    - Low Severity
        - Insecure Random Number Generation
            - Factors: Potential for weak entropy source(s), predictable random number generation
            - Impact: Increased risk of unauthorized access to due weak encryption keys
- Usability Concerns
    - High Severity
        - Complex User Interface
            - Factors: Non-intuitive design, steep learning curve, requires existing technical knowledge
            - Impact: Increased risk of misconfiguration or errors in the encrypted disk, reduced encryption effectiveness
    - Medium Severity
        - Lack of Features
            - Factors: Lack of support for modern operating systems, lack of support for modern hardware, lack of support for modern encryption algorithms
            - Impact: Reduced ability to encrypt modern systems, reduced encryption effectiveness
    - Low Severity
        - Lack of Documentation
            - Factors: Discontinued development, lack of documentation, lack of community support
            - Impact: Reduced ability to troubleshoot issues, increased risk of misconfiguration

This ontology outlines some of the key weaknesses of TrueCrypt, and the severity of each weakness. It also outlines some of the factors and impact that may cause a weakness to become an issue from a user's perspective. By using an ontology such as this one, user's can make an informed decision on whether the software is suitable for their needs or if they should seek an alternative software.
