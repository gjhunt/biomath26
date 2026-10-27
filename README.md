# Greenland (2016) biomathematics lunch

The current deck contains **a title and seven content slides**, organized around the primer on pp. 338–340. Further sections can be added as requested; length is currently unconstrained.

1. Models, hypotheses, and statistical tests (including the quoted P-value definition).
2. A little notation: what varies, and what is assumed?
3. The natural question: how certain is the hypothesis?
4. The assumptions quietly treated as known.
5. P values: compatibility with the entire model.
6. Statistical significance and surprisal, including a fair-coin calibration.
7. From tests to estimates and confidence intervals.

Page-cited quotations organize the primer summary. A notation slide gives the conditional tail probability and a two-sided normal Z example. The surprisal transform is an explicitly labeled addition from Rafi & Greenland (2020), [Semantic and cognitive tools to aid statistical science](https://pmc.ncbi.nlm.nih.gov/articles/PMC7528258/), rather than a claim about the 2016 primer. The CI slide explains the range of compatible effects and repeated-study coverage directly.

## Files

- `greenland_2016_slides.ipynb`: editable Quarto notebook.
- `greenland_2016_slides.html`: self-contained Reveal.js slides.
- `slides.css`: styling.
- `SUMMARY.md`: separate summary of the entire paper, retained as reference.
- `scripts/create_notebook.py`: standard-library Python generator for the current notebook.

## Build and present

With Quarto installed (tested with 1.6.39):

```sh
make               # build HTML
make preview       # preview server
make clean         # remove generated HTML
```

Open the HTML in a current browser with MathML support. Press **S** for presenter view and **O** for overview. Scripts, styles, and native math are included in the HTML; no Python packages or Jupyter kernel are required to render it.

`make regenerate` recreates the notebook using Python 3 and **overwrites notebook edits**. Normal builds preserve edits. The original `codex_container` make target remains available. Quarto cache/data are kept under the project’s `.cache` and `.local/share` directories for container compatibility.

## Source

Greenland S, Senn SJ, Rothman KJ, Carlin JB, Poole C, Goodman SN, Altman DG. (2016). *Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations.* European Journal of Epidemiology 31:337–350. DOI: 10.1007/s10654-016-0149-3. Based on the supplied `greenland_2016.pdf`.

The build and slide structure were checked. Browser-based visual inspection was not available in this environment.
