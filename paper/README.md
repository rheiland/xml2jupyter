# Build (on *nix) the paper to produce a JOSS-like pdf

Run this script:
```
$ bash gen_pdf.sh
```
It requires `make, pandoc, sed, and pdflatex` and should generate	the `paper.pdf` from the `paper.md`.

However, the preferred method when preparing an actual JOSS submission is to run their command `@whedon generate pdf`
