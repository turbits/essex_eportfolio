---
layout: page
permalink: /pages/module5/unit-assignments/unit8/m5u8-worksheets.html
---

⬅️[Back](/pages/module5/unit-assignments/unit8/m5u8.html)

# Unit 8: Summary Measures and Hypothesis Testing Worksheets

Unfortunately, this unit had exceptionally confusing naming for the activities and the files, apologies for any readability issues.

Excel files are provided for each exercise in their respective sections.

See the [description](/pages/module5/unit-assignments/unit8/worksheets/m5u8-worksheets-activity-desc.html) page for the activity description.

## Table of Contents
- 👉 [Unit 8: Summary Measures and Hypothesis Testing Activity Description](/pages/module5/unit-assignments/unit8/worksheets/m5u8-worksheets-activity-desc.html)
- 👉 [Unit 8: Activity: Summary Measures Worksheet (docx)](/pages/module5/unit-assignments/unit8/worksheets/m5u8-worksheet1-summary.docx)
- 👉 [Unit 8: Activity: Hypothesis Testing Worksheet (docx)](/pages/module5/unit-assignments/unit8/worksheets/m5u8-worksheet2-hypothesis.docx)
- 👉 [Unit 8: Activity: Summary Measures Answers](#summary-measures-answers)
- 👉 [Unit 8: Activity: Hypothesis Testing Answers](#hypothesis-testing-answers)


## Summary Measures Answers

### Summary Measures Exercise 8.1

[Unit 8: Activity: Summary Measures Exercise 8.1 - Exe 8.1B.xlsx](/pages/module5/unit-assignments/unit8/exercises/Exe%208.1B.xlsx)

***Briefly interpret your findings. What do these results tell you about the relative effectiveness of the two weight-reducing diets?***

The results indicate that diet A is more effective than diet B. The mean weight loss for diet A is 5.341kg, while the mean weight loss for diet B is 3.710kg. Furthermore, the standard deviation is 2.536 for diet A and 2.769 for diet B, showing that diet B had slightly more varied results.

### Summary Measures Exercise 8.2

[Unit 8: Activity: Summary Measures Exercise 8.2 - Exe 8.2B.xlsx](/pages/module5/unit-assignments/unit8/exercises/Exe%208.2B.xlsx)

***Briefly interpret your findings. What do these results tell you about the relative effectiveness of the two weight-reducing diets?***

In diet A, the mean is slightly lower than the median, indicating a slight negative skew. In diet B, it is similar, but the mean has a comparitively smaller deviation from the median, indicating a more symmetrical distribution of results.

### Summary Measures Exercise 8.3

[Unit 8: Activity: Summary Measures Exercise 8.3 - Exe 8.3D.xlsx](/pages/module5/unit-assignments/unit8/exercises/Exe%208.3D.xlsx)

***Briefly interpret your findings. What do these results tell you about the patterns of brand preferences for each of the two demographic areas?***

Area 1 greatly prefers "Other" brand, comparitive to A or B. Area 2 has a comparitively more distributed preference, but still favours "Other". Brand A is the least popular in both areas.

## Hypothesis Testing Answers

### Exercise 8.4

[Unit 8: Activity: Hypothesis Testing Exercise 8.4 - Exe 8.4G.xlsx](/pages/module5/unit-assignments/unit8/exercises/Exe%208.4G.xlsx)

Agent1 and Agent2 are air filters, the values in these columns represent the impurity of the air after filtration per batch.

***Assuming the data to be suitably distributed, complete a two-tailed test of whether the population mean impurity differs between the two filtration agents, and interpret your findings.***

The t-value is -3.26 with 11 df, and a p value of 0.003. The magnitude of the t-value indicates that there is a substantial difference between the two agents' mean impurity. Since the p-value is less than the conventional significance level of 0.05, we can reject the null hypothesis that the two agents are equally effective.

### Exercise 8.5

[Unit 8: Activity: Hypothesis Testing Exercise 8.5 - Exe 8.4G.xlsx (uses same sheet)](/pages/module5/unit-assignments/unit8/exercises/Exe%208.4G.xlsx)

***Suppose instead a one-tailed test had been conducted to determine whether Filter Agent 1 was the more effective [agent]. What would your conclusions have been?***

Assuming that we want to test if Agent2 is more effective than Agent1, our null hypothesis (H0) states that there is no difference or that the mean of Agent2 is greater than or equal to that of Agent1. Our alternative hypothesis (H1), would state that the mean of Agent1 is greater than that of Agent2.

H0 = μ2 <= μ1 (Agent2 is as effective or less effective than Agent1)
H1 = μ2 > μ1 (Agent2 is more effective than Agent1)

Given the previous values: t-value = -3.26, df = 11, p-value = 0.003. Given that the t-value is negative, it falls in the left tail. Because the t-value is negative, the one-tailed p-value represents the probability of observing a t-value as extreme as -3.26 or less in the left tail.

The one-tailed p-value is 0.003, which is less than the conventional significance level of 0.05. Ergo, we can reject the null hypothesis that Agent2 is as effective or less than Agent1, and conclude that Agent2 is more effective than Agent1.

### Exercise 8.6

[Unit 8: Activity: Hypothesis Testing Exercise 8.6 - Exe 8.6C.xlsx](/pages/module5/unit-assignments/unit8/exercises/Exe%208.6C.xlsx)

***Assuming the data can be suitably distributed, complete an appropriate test of whether the population mean income for males exceeds that of females and interpret your findings. What assumptions underpin the validity of your analysis, and how could you validate them?***

The dataset is comprised of 120 data points of both male and female incomes, 60 each. Upon running an F-test, we receive the following values:
F-test:
- F = 1.226
- p2 = 0.436

Male:
- mean = 52.913
- variance = 233.129

Female:
- mean = 44.233
- variance = 190.176

Since the data indicates that the sample mean income for males is higher at 52.913 compared to females at 44.233, this would indicate that males have a higher mean income than females. This analysis assumes that the data is normally distributed, and that the variance is equal between the two groups.

To validate our results, we can run a separate t-test to compare. Assuming the following hypotheses:

H0 = μM <= μF (Income for males is the same or less than females)
H1 = μM > μF (Income for males is greater than females)

The t-test yields the following important values:
- tStat = 3.768
- tCritical one-tail = 1.671
- tCritical two-tail = 2.001

Due to the t-statistic being more extreme than the t-critical value(s), we can reject the null hypothesis (H0), indicating that, indeed, the mean income for males is greater than that of females.

