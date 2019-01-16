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

Jupyter Notebooks [@Kluyver:2016aa] provide executable documents (in a variety of programming languages) that can be run in a web browser. 
When a notebook contains
graphical widgets, it becomes an easy-to-use graphical user interface (GUI).
Many scientific simulation packages use
text-based configuration files (hopefully in some standard format) to provide parameter values.
<!-- For many users, especially novice users, editing such a configuration file can be burdensome. -->
Xml2jupyter is a Python package that bridges this gap. It provides a mapping between configuration files, formatted in 
the Extensible Markup Language (XML), and Jupyter widgets. Widgets are automatically generated from the XML
file and these can, optionally, be incorporated into a larger GUI for a simulation package. 
Users modify parameter values via the widgets 
and the values are written to the XML configuration file. 
Xml2jupyter has been tested using the PhysiCell [@PhysiCell:2018] simulation software
and will be used by students for classroom and research projects.

```xml
<user_parameters>
  <random_seed type="int" units="dimensionless">0</random_seed> 

  <!-- for microenvironment setup --> 
  <cargo_signal_D type="double" units="micron/min^2">1e3</cargo_signal_D>
  <cargo_signal_decay type="double" units="1/min">.4</cargo_signal_decay>
  <director_signal_D type="double" units="micron/min^2">1e3</director_signal_D>
  <director_signal_decay type="double" units="1/min">.1</director_signal_decay>
  
  <!-- for cell definitions -->
  <elastic_coefficient type="double" units="1/min">0.05</elastic_coefficient>
  ... 
</user_parameters>
```
A portion of a sample XML configuration file.


![](images/test_screen.png)

The resulting Jupyter notebook containing the widgets for the above XML.

# PhysiCell Jupyter GUI

Our ultimate goal is to generate a functional GUI for PhysiCell users. Xml2jupyter provides one
important piece of this - dynamically generating widgets for custom user parameters for a model.
With the addition of static components (tabs) of the GUI, a user can also visualize output results
from simulations.
This additional functionality requires modules not available in the Python
standard library, e.g., Matplotlib [@Hunter:2007]
to display plots, and SciPy to parse PhysiCell output data. We provide instructions for installing these additional dependencies on
`github link`.

![](images/biorobots_cells.png)
![](images/biorobots_substrates.png)

Additional tabs used by the PhysiCell Jupyter GUI.

<!-- 
-![](images/heterogeneity_params.png)
The images above show hetero...  -->


# Acknowledgements

We thank the National Science Foundation for providing funding via NSF EEC-1720625.
We acknowledge support from our collaborators at Purdue University, especially Martin Hunt, who 
contributed to our `pc4nanobio` tool on nanoHUB.

# References

