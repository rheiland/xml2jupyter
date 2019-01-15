make
sed 's/]{}}/]{joss-logo.png}}/' < paper.tex >foo.tex
cp paper.tex paper-bkup.tex 
mv foo.tex paper.tex
pdflatex paper
