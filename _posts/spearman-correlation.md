 
I feel obliged to discuss how at least one non-parametric rank-based statistic is useful.

	\begin{tcolorbox}[colframe=blue!50!black, title=Quotation (Galen Seilis)]
	[...] estimators such as Spearman's correlation tell us about comonotonicity of pairs of variables without the difficulties that come with modeling.
	\end{tcolorbox}
	
	Dustin expressed that ``comonotonicity" is a difficult term to pronounce\footnote{The site \href{https://www.pronouncekiwi.com/Comonotonic}{pronouncewiki} gives some examples.}, which is an attidue I am sympathetic to as someone who took an undergraduate course in metabolism. "Phosphoribosylformimino-5-aminoimidazole-4-carboxamide ribonucleotide isomerase", anyone? Dustin did not make any further comment on whether he agreed or disagreed that Spearman's rank correlation quantifies comonotonicity. I think the point I was making about comonotonicity is worth unpacking and emphasizing further.\\
	
	Comonotonicity is a description of a pair (or collection) of variables which go up and down together. Similarly, antimonotonicity is a description a pair of variables in which one increasing implies that the other is decreasing, and vice versa. Well, these are informal descriptions anyway. For further reading on more precisely-defined notions of comonotonicity see \href{https://www.parisschoolofeconomics.eu/IMG/pdf/MED090320-Scarsini.pdf}{Puccetti \& Scarsini 2009}, but I will continue here with a less precise and more intuitive exposition.
	
	\begin{figure}[H]
		\centering
		\includegraphics[scale=1]{perm_grid.pdf}
		\caption{All $4!=24$ possible arrangments of ranks for a bijection $\{1, 2, 3, 4\} \mapsto \{1, 2, 3, 4\}$. Yellow squares indicate a pair is a member of the relation, otherwise it is not a member of the relation.}
	\end{figure}	
