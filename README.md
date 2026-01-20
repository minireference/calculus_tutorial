Calculus tutorial
=================

- **Download PDF**: https://minireference.com/static/tutorials/calculus_tutorial.pdf [2MB, 25 pages]
- **Interactive computational notebooks:** https://bit.ly/calctut3 


## Why?

I want people to have access to a free learning materials on calculus.
I can't give my books for free yet,
but I *can* offer the condensed guide to the main ideas
so that interested readers print on their own and benefit from this knowledge and explanations.

This tutorial serves as promotional material for my book,
the [No Bullshit Guide to Math and Physics](https://minireference.com/#noBSmathphys)
and also appears as Appendix F in the [No Bullshit Guide to Statistics](https://gum.co/noBSstats).


## How?

I've prepared a informationally-dense condensed tutorial that explains key ideas using multiple modalities:
- Text descriptions without jargon
- Math formulas
- Visualizations (graphs and diagrams)
- Code examples of symbolic calculations using SymPy
- Code examples numerical procedures from scratch (only basic Python)
- Code examples that leverage high-performance NumPy and SciPy routines

Presenting the material from multiple perspectives makes it easy to understand what's going on.



## What?

A condensed guide to the core ideas of calculus ideas: limits, derivatives, integrals, plus sequences and series
in the form of a (relatively) short printable tutorial.
Basically, I took the essential definitions and simple examples from my [Math & Physics book](https://minireference.com/#noBSmathphys)
and condensed the into a single document that you can read in one sitting. 


## Contents

Here is what you'll learn:

- Review of math prerequisites (sets; functions and their graphs; basic geometry and trigonometry)
- Limits (limits at infinity, continuity; computing limits using SymPy)
- Derivatives (derivative formulas; higher derivatives; computing derivatives numerically; optimization)
- Integrals (integrals as areas; numerical integration; integrals as functions; FTC; applications)
- Sequences and series (convergence; Taylor series; using SymPy for series)
- Minimal introduction to multivariable and vector calculus (partial derivatives; gradient; multiple integrals)
- Practice problems (with answers and [solutions](https://raw.githubusercontent.com/minireference/calculus_tutorial/refs/heads/main/calcproblems/calculus_tutorial_problems_and_solutions.pdf))
- Links to further learning resources and plug of the [**No Bullshit Guide to Math & Physics**](https://minireference.com/#noBSmathphys)




## License


CC BY 4.0  Attribution 4.0 International. See [LICENSE.txt][./LICENSE.txt] for details.

<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" alt="Creative Commons Attribution (CC BY)" width="88" height="31">




## Contributing

I'm open to feedback and pull requests with improvements to any of the text.
Here is a structure of the source code:

- [`calculus_tutorial.tex`](./calculus_tutorial.tex) — main LaTeX entry point
- [`sections/`](./sections/) — LaTeX source files for each section
- [`figures/`](./figures/) — figures used in the PDF
- [`calcproblems/`](./calcproblems/) — problems and solutions

To rebuild the PDF from the source files, clone this repo and run:

```bash
pdflatex calculus_tutorial.tex
pdflatex calculus_tutorial.tex

```




## Citation

If you would like to cite this tutorial in your work, please use

```bibtex
@article{savov_calculus_tutorial_2026,
  title = {Calculus explained in 25 pages},
  author = {Ivan Savov},
  publisher = {Minireference Co.},
  year = {2026},
  note = {\url{https://minireference.com/static/tutorials/calculus_tutorial.pdf}}
}

```


## Links

- Announcement blog post: https://minireference.com/blog/calculus-tutorial-shipped/
- Announcement video: [COMING SOON]
- Outline gdoc: https://docs.google.com/document/d/14Y9LO4W3MkLgf8aYjhGZjWnnXDTJrhckYGDx9ijjr_A
- Backup link: https://raw.githubusercontent.com/minireference/calculus_tutorial/refs/heads/main/calculus_tutorial.pdf

