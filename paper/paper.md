---
title: 'Xml2jupyter: Mapping parameters between XML and Jupyter widgets'
tags:
  - Jupyter
  - XML
  - Python
  - GUI
authors:
  - name: Randy Heiland
    orcid: 0000-0002-7440-2905
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Daniel Mishler
    orcid: 0000-0001-9450-2850
    affiliation: 1 
  - name: Tyler Zhang
    orcid: 0000-0002-9583-2234
    affiliation: 1 
  - name: Eric Bower
    orcid: 0000-0002-7166-8329
    affiliation: 1 
  - name: Paul Macklin
    orcid: 0000-0002-9925-0151
    affiliation: 1
affiliations:
 - name: Intelligent Systems Engineering, Indiana University
   index: 1
date: 31 January 2019
bibliography: paper.bib
---

# Summary

Jupyter Notebooks provide executable documents (in a variety of programming languages) that can be run in a web browser. 
When a notebook contains
graphical widgets, it becomes an easy-to-use graphical user interface (GUI).
Many scientific simulation packages use
text-based configuration files (hopefully in some standard format) to provide parameter values.
<!-- For many users, especially novice users, editing such a configuration file can be burdensome. -->
Xml2jupyter is a Python package that bridges this gap. It provides a mapping between configuration files formatted in 
the Extensible Markup Language (XML) and Jupyter widgets. Widgets are automatically generated from the XML
file and incorporated into a larger GUI for simulation software. A user changes parameter values via the widgets 
and the values are written back to the XML configuration file. This tool has been tested using PhysiCell [@PhysiCell:2018]
and will be used by students for classroom and research projects.


-![Test widgets](images/test_screen.png)

The image above shows...

# Acknowledgements

We thank the National Science Foundation for providing funding via NSF EEC-1720625.
We acknowledge support and contributions from our collaborators at Purdue University, especially Martin Hunt.

# Funding

# References

