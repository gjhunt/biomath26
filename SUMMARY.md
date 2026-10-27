# Greenland et al. (2016): reading summary

**Paper:** Sander Greenland, Stephen J. Senn, Kenneth J. Rothman, John B. Carlin, Charles Poole, Steven N. Goodman, and Douglas G. Altman. *Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations.* European Journal of Epidemiology 31:337–350. DOI: 10.1007/s10654-016-0149-3. This summary is based on the supplied `greenland_2016.pdf`; page references below are printed journal pages.

## Central argument

This is a methodological essay, not an empirical study. The authors explain statistical tests and estimation, catalogue 25 common misinterpretations, and recommend better interpretation and reporting. Their organizing claim is that inference depends on a full web of assumptions about study design, data collection, analysis, and reporting. The fitted regression equation is only one part of that model. Interpreting a statistical result requires attention to the process that produced and selected it.

## P values (pp. 338–343)

A P value is a tail probability for a chosen discrepancy statistic under the test hypothesis **and all the other model assumptions**. It includes outcomes at least as extreme as the observed result, rather than just the observed data. A small value identifies incompatibility between the data and the joint model; it does not isolate which assumption failed. A large value does not establish the hypothesis, because many other hypotheses can also be compatible with the data.

The authors reject interpreting P as the probability that the hypothesis is true, that chance caused the result, or that an individual significant finding is false. Type-I error control describes performance across repeated applications under specified assumptions; it does not directly give the fraction of discoveries that are false.

Significance also does not measure effect size or biological importance. A precise estimate of a tiny effect can yield a small P value, while an imprecise estimate can leave large effects unresolved. Exact P values retain information lost by reporting only which side of 0.05 a result occupies.

## Confidence intervals (pp. 339–340, 343–345)

A 95% confidence procedure covers the fixed true effect in 95% of repeated valid applications (with qualifications for approximate or conservative procedures). The nominal confidence level is not, by itself, a posterior probability that the effect lies in a particular observed interval. A confidence interval is also not a prediction interval for estimates in future studies.

Intervals help shift attention toward effect size and precision. Through inversion of corresponding tests, they identify a range of candidate effects with P values above a chosen cutoff. But their endpoints are not sharp boundaries between possible and impossible effects. Values just inside and outside an endpoint can be nearly equally compatible. Intervals also inherit the model and selection assumptions behind the analysis; they need not capture uncertainty about bias.

## Comparing and synthesizing studies (pp. 342–344)

Different significance labels do not establish different effects, and identical P values do not establish agreement. In one example, two trials estimate exactly the same difference, 3, but have standard errors 2 and 1, yielding P values about 0.13 and 0.003. Their observed effect contrast is zero. Conversely, estimates 3 and 12 with standard errors 1 and 4 have identical individual P values but a direct contrast with P about 0.03. Comparisons require estimation and testing of the contrast itself, including covariance where appropriate. Overlap between individual confidence intervals is not a general test of that contrast.

Counting significant studies is not evidence synthesis. Appropriate pooled analysis or meta-analysis should consider study biases and heterogeneity, as well as sampling uncertainty.

## Power and replication (p. 345)

Power is a design’s pre-study probability of rejecting a test hypothesis at a specified alternative. It does not give the probability that a particular nonsignificant result is correct. Plug-in observed power in the usual fixed-design setting is a transformation of the observed test result and adds no independent information. Even high planned power plus nonsignificance does not necessarily favor the null over the alternative; assess both hypotheses against the actual data.

For two independent studies each with actual power 80% at the same true alternative, the chance both are significant is 64%, while the chance their significance labels disagree is 32%. Label disagreement alone therefore provides a poor definition of failed replication.

## Selection and practical recommendations (pp. 345–348)

Selecting analyses or publications on their results breaks ordinary interpretations of unadjusted P values and intervals. Selection can favor significance or nonsignificance. Residual diagnostics cannot validate the entire study and reporting process.

Report effect estimates, intervals, precise P values, and substantive context together. Describe design, assumptions, analysis plans, exclusions, and the analyses actually performed. Compare meaningful alternatives directly and assess the totality of evidence. Bayesian methods can express hypothesis probabilities with additional assumptions, including priors, but also require scrutiny of their models and analysis process.

The paper offers interpretive guidance rather than a universal decision procedure. Useful lunch questions are how to define meaningful effects, how to act when evidence remains uncertain, and how to represent uncertainty about bias as well as sampling error.
