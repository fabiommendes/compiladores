pandoc prova1.md  -o prova1.pdf --mathjax --latex-engine=xelatex
pandoc prova1-gabarito.md  -o prova1-gabarito.pdf --mathjax --latex-engine=xelatex
evince prova1.pdf 
