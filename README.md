# Inequality Zoo for Event Graphs

We provide here a series of numerical results for the e-print: https://arxiv.org/abs/2209.02670

In vertices .txt files we provide the set of all deterministic assignments that define the classical polytope. The vertices represent the V-representation of the polytope, and it is computationally easy to find vertices for some 'small' graphs. One can find the vertices with the following algorithm: find all deterministic assignments, find all cycles in the graph, exclude the assignments that allow for a single 0 in a given cycle. These violate the transitivity of equality, and in terms of probabilities these violate the Boole inequalities.

In facets .txt files we provide the set of facet defining inequalities for the classical polytopes. We find those by using the fact that for a given V-representation one can find a facet representation for the polytope (so-called H-representation) using standard algorithmic tools. The tool we have used was the program PORTA (http://comopt.ifi.uni-heidelberg.de/software/PORTA/) that has the command traf that does the job. We present the full set of inequalities for those.

We have also presented some results found for violations that were searched using simple sampling of quantum states using QuTip (https://qutip.org/). 

# What is included

1) Full set of classical vertices (deterministic edge assignments) for small event graphs.
2) Full set of inequalities for the event graphs W4=K4, W5, W6, W7, K5, K6.
3) An easy Python code for checking if a given point pertains to K5.
4) A large number of quantum violations for the K5 inequalities in 2, 3, and 4 dimensional quantum systems.
5) All deterministic assignments for K7.

# How to cite

Bib.
@article{wagner2022inequalities,
  title={Inequalities witnessing coherence, nonlocality, and contextuality},
  author={Wagner, Rafael and Barbosa, Rui Soares and Galv{\~a}o, Ernesto F.},
  journal={arXiv preprint arXiv:2209.02670},
  year={2022}
}
