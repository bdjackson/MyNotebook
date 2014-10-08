BASENAME = BinomialUncertainty

default: pdflatex

pdflatex:
	echo ${BASENAME}
	pdflatex ${BASENAME}
	pdflatex ${BASENAME}

clean:
	rm -f *.aux *.log *.bbl *.blg *.brf *.cb *.ind *.idx *.ilg  \
	      *.inx *.dvi *.toc *.out *~ ~* spellTmp *.pdf
