"""Recreate the compact primer notebook using Python's standard library."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
cells = []

def md(text):
    cells.append(dict(cell_type='markdown', metadata={}, source=text.strip().splitlines(True)))

def slide(title, body, notes, source):
    md(f'## {title}\n\n{body}\n\n::: {{.source}}\n{source}\n:::\n\n::: {{.notes}}\n{notes}\n:::')

md('''---
title: "Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations"
author: "Sander Greenland · Stephen J. Senn · Kenneth J. Rothman · John B. Carlin · Charles Poole · Steven N. Goodman · Douglas G. Altman (2016)"
format:
  revealjs:
    theme: simple
    css: slides.css
    slide-number: c/t
    progress: true
    transition: none
    center: false
    width: 1280
    height: 800
    margin: 0.07
    embed-resources: true
    html-math-method: mathml
    navigation-mode: linear
    controls: true
    history: true
    title-slide-attributes:
      data-background-color: "#102f3a"
execute:
  enabled: false
  echo: false
  warning: false
---
''')

slide('Models, hypotheses, and statistical tests', r'''**Model → test hypothesis → discrepancy statistic → P value**

- A **model** mathematically describes data variability, assuming how data were collected, analyzed, and selected for reporting.
- A **test hypothesis** specifies an effect, e.g. $H:\theta=0$ for no difference in mean growth.
- A **test statistic** measures discrepancy between the data and the hypothesis.

> “The P value is then the probability that the chosen test statistic would have been at least as large as its observed value if every model assumption were correct, including the test hypothesis.”
>
> — Greenland et al., p. 339

The probability includes the observed discrepancy **and more extreme discrepancies**.''', r'Introduce the whole testing chain before discussing its interpretation. Every method of statistical inference depends on assumptions, even nonparametric methods. The model includes sampling, allocation, dependence, missingness, and selection of analyses. Optional normal example: $Z=(\widehat\theta-\theta_0)/s$, with known standard error s; under the point hypothesis and normal model Z is standard normal. For a two-sided test use absolute Z as the discrepancy statistic. Standard error describes variability of the estimate across studies. Formally, $P=\Pr\{T(D^*)\geq T(D_{\mathrm{obs}})\mid H,A\}$, where D star is hypothetical repeated data, H the specified hypothesis, and A other assumptions. This is not a probability that H is true. Composite hypotheses need appropriate calibration.', 'Greenland et al. (2016), pp. 338–339; quotation p. 339.')

slide('A little notation: what varies, and what is assumed?', r'''Let D be the data, θ the effect, and A the other model assumptions.
A point hypothesis specifies $H:\theta=\theta_0$.

$$P=\Pr\!\left\{T(D^*)\ge T(D_{\mathrm{obs}})\mid\theta=\theta_0,A\right\}.$$

- **Dobs:** the observed data; **D*:** hypothetical data under H and A.
- **T:** a discrepancy statistic; larger values mean less agreement.
- Probability is over **hypothetical data**, with θ₀ and A held fixed.

For an exactly normal estimate $\widehat\theta$ with known standard error s:

$$Z=\frac{\widehat\theta-\theta_0}{s},\qquad
P=\Pr\{|Z^*|\ge|Z_{\mathrm{obs}}|\}\quad (Z^*\sim N(0,1)).$$

The absolute values make this example a **two-sided** test.''', 'Use this as a translation of the opening verbal definition. Theta is fixed but unknown; theta zero is the candidate value being tested. Other candidate values can be tested with the same construction. The reference distribution of Z star assumes the point hypothesis and A. Known standard error and exact normality are illustrative assumptions, not universal properties of estimators; estimated SEs may require a t distribution or an asymptotic approximation. A is not limited to the distributional assumptions written in a formula: it includes design and reporting assumptions. The definition includes the observed discrepancy and more extreme discrepancies; it is not the probability of exactly the observed data. Composite one-sided hypotheses need appropriate calibration.', 'Greenland et al. (2016), pp. 338–339. Notation and normal-model example added.')

slide('The natural question: how certain is the hypothesis?', r'''> “It is natural to express such certainty in terms of ‘probabilities’ of hypotheses.”
>
> — Greenland et al., p. 339

**We want to learn the effect size and assess how uncertain our estimate is.**

It is natural to want probabilities for possible effect sizes—but conventional frequentist calculations provide **probabilities of data patterns under assumed effect sizes and other model assumptions**.

$$\Pr(\text{data pattern}\mid H,A)\quad\neq\quad\Pr(H\mid\text{data}).$$

These are different questions. A probability calculated assuming H does not, by itself, supply a probability for H.''', 'Read the quote as the motivation for statistical analysis, not a dismissal of probabilities of hypotheses. The distinction is what the conventional frequentist calculation provides. The display contrasts conditioning directions; it is not an equation defining a P value, which additionally involves a tail event. H is a specified hypothesis and A denotes other assumptions. The quoted source uses double quotation marks around probabilities; single marks here distinguish the inner quotation. Biological example and notation added.', 'Greenland et al. (2016), “Uncertainty, probability, and statistical significance,” p. 339; quotation p. 339.')

slide('The assumptions quietly treated as known', r'''Traditional definitions emphasize the null hypothesis while

> “treating all other assumptions used to compute the P value as if they were known to be correct.”
>
> — Greenland et al., p. 339

> “this statistical model often incorporates unrealistic or at best unjustified assumptions.”
>
> — Greenland et al., p. 338

The full model is **H together with the other assumptions A**, including:

- Sampling, allocation, and dependence among observations.
- Measurement, missing data, and selection of analyses for reporting.

**The calculation assumes these conditions are satisfied; it does not establish that they are.** If repeated measurements from one animal are treated as independent animals, a small P could reflect that mistake rather than a treatment effect.''', 'This is the central move in the primer: enlarge the object being checked from the targeted hypothesis to the entire model underlying the probability calculation. Assumptions are design-specific; not every study uses random sampling or random allocation. Randomization addresses allocation but cannot guarantee correct measurement, missing-data assumptions, or nonselective reporting. A is shorthand for a web of assumptions, not simply normality of regression residuals. The next slide develops the compatibility interpretation. The repeated-measurements example is added to explain what can go wrong when a calculation assumes independence that the study does not supply.', 'Greenland et al. (2016), “Statistical models, hypotheses, and tests,” p. 338; “Uncertainty, probability, and statistical significance,” p. 339; quotation p. 339.')

slide('P values: compatibility with the entire model', r'''> “Recognizing that these other assumptions are often questionable if not unwarranted, we will adopt a more general view of the P value as a statistical summary of the compatibility between the observed data and what we would predict or expect to see if we knew the entire statistical model (all the assumptions used to compute the P value) were correct.”
>
> — Greenland et al., p. 339

**The reference is the entire model: H together with A.**

A small P flags a discrepancy with that joint model. It cannot distinguish a false test hypothesis from a failure of another assumption.''', 'This quotation follows immediately after the warning about treating other assumptions as known. Read the conditional ending carefully: compatibility is assessed against what the model would predict if all its assumptions were correct. The statistic does not validate those assumptions. A small P may arise from a false test hypothesis, violated protocols, or selection for a small result. A large P does not establish the model either. Compatibility here is not a posterior probability of a hypothesis.', 'Greenland et al. (2016), “Uncertainty, probability, and statistical significance,” p. 339; quotation p. 339.')

slide('Statistical significance and surprisal', r'''“Statistically significant” conventionally means **P ≤ α**, usually α = 0.05.

> “the arbitrary classification of results into ‘significant’ and ‘non-significant’ is unnecessary for and often damaging to valid interpretation of data”
>
> — Greenland et al., p. 338 (in most scientific settings)

An added way to express P continuously is **surprisal**, in bits:

$$S=-\log_2(P).$$

| P | 0.50 | 0.05 | 0.01 |
|---|---:|---:|---:|
| S (bits) | 1 | 4.32 | 6.64 |

**Coin calibration:** s bits corresponds to the probability of **all heads in s specified independent fair-coin flips**: $P=2^{-s}$.
For example, **P = 1/32 gives S = 5 bits**, like five heads in five flips.

Larger S means greater surprise under the **joint model**; it is not a probability that the hypothesis is true.''', 'The significance critique is from the 2016 paper; surprisal is an explicitly added connection to later work by Rafi and Greenland (2020). Alpha is fixed in advance, whereas P is computed from the observed data. S is a monotonic re-expression of P and inherits its model and selection assumptions. Under a properly calibrated P value, the bits provide a scale for the surprise of the tail event, not a posterior probability or a Bayes factor. The coin analogy concerns a specified sequence in a fixed number of flips, not the waiting time until a run of heads. For noninteger S, such as 4.32, interpret it as a position on a continuous information scale, between the integer-flip examples. The analogy calibrates the probability of the tail event, not the exact observed data. S is not a count of observed flips and adds no information beyond P. The P=.05 threshold has no special discontinuity on this scale. Do not interpret the transform as evidence exclusively against H rather than against the joint assumptions.', 'Greenland et al. (2016), pp. 338–339. Added connection: [Rafi & Greenland (2020), “Semantic and cognitive tools…”](https://pmc.ncbi.nlm.nih.gov/articles/PMC7528258/), BMC Medical Research Methodology 20:244.')

slide('From tests to estimates and confidence intervals', r'''Test a range of candidate effects, rather than only θ = 0. Inverting corresponding two-sided tests gives a **95% confidence interval**:

$$C_{0.95}(D)=\{\theta_0:p_{\theta_0}(D)>0.05\}.$$

For a normal estimate with known standard error s: $\widehat\theta\pm1.96s$.
An estimate of 3 with s = 2 gives **−0.92 to 6.92**.

**Read the range:** the null and substantial increases are both compatible with these data at this level, under the model. Effects outside the interval are less compatible by the corresponding test—not impossible.

**Why “95%”?** Across repeated valid applications, this procedure produces intervals covering the true effect 95% of the time. It does not assign a 95% probability to the effect lying in this particular interval.''', 'The main point is the move from testing only zero to displaying a range of effect sizes. The illustrative normal calculation assumes an exactly normal estimate with known SE; in other settings coverage may be approximate or conservative. The inversion display follows the source’s P greater than .05 convention; including boundary points in the conventional normal interval makes no substantive difference here. Three units and SE two match trial A in misconception 16, p. 343, not biological observations. “Substantial” depends on scientific context: the example permits increases up to nearly seven outcome units. Compatibility is conditional on assumptions and is not a posterior probability. The repeated-application coverage concerns the varying intervals and a fixed true parameter. Effects just outside an endpoint are almost as compatible as those just inside, so the endpoint is not a scientific cliff. This slide uses direct explanation rather than the unrelated null-focus quotation.', 'Greenland et al. (2016), “Moving from tests to estimates,” p. 340; interval interpretation, pp. 343–345. Normal illustration added.')

nb = dict(cells=cells, metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}, 'language_info':{'name':'python','version':'3'}}, nbformat=4, nbformat_minor=5)
for i, cell in enumerate(cells):
    cell['id'] = f'cell-{i:03}'
(ROOT / 'greenland_2016_slides.ipynb').write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n')
print(f'Wrote {len(cells)} cells: title and {len(cells)-1} primer slides.')
