# xml2jupyter

[![Build Status](https://travis-ci.com/rheiland/xml2jupyter.svg?branch=master)](https://travis-ci.com/rheiland/xml2jupyter) 

To see an example application that has been generated with xml2jupyter, click the binder badge [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rheiland/xml2jupyter/master?filepath=PhysiCell_GUI%2Fmygui.ipynb)
(You can also launch an Azure notebook [![Azure Notebooks](https://notebooks.azure.com/launch.svg)](https://notebooks.azure.com/randy-heiland/projects/xml2jupyter), but from there, you will need to click on `demo_gui.ipynb`).

<!-- [![Azure Notebooks](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/import/gh/randy-heiland/xml2jupyter) -->

## Overview
Using an XML configuration file, generate a graphical user interface (GUI) consisting of [Jupyter widgets](https://ipywidgets.readthedocs.io/en/stable/index.html). This project is primarily in support of the [PhysiCell](http://physicell.mathcancer.org/) simulator and its configuration files, however, the basic idea can be extended to other text-based configuration files. The ```xml2jupyter.py``` Python script provides the core functionality for dynamically creating widgets from XML. The other Python scripts are static and provide a self-contained Jupyter GUI consisting of multiple tabs.

<!--
If you simply want to try the notebook, without downloading anything, try clicking on this Binder badge [![Binder](https://img.shields.io/badge/PhysiCell-JupyterGUI-E66581.svg)](https://mybinder.org/v2/gh/rheiland/xml2gui/master?filepath=PhysiCell.ipynb) to run it from your browser.
-->

<!--
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/rheiland/xml2gui/master?filepath=PhysiCell.ipynb) Click the binder badge to play with the notebook from your browser without installing anything.
-->

## Dependencies
1. Minimally, this project just requires Python (we recommend Python 3.x). A standard distribution of Python will let you convert sample XML configuration files into Jupyter widgets. 
2. If you install [Jupyter](https://jupyter.org/install), you will be able to display the widgets in a notebook (in your web browser) and modify the XML via the widgets.
3. If you install some additional Python modules (matplotlib and scipy), not available in the standard library, you will be able to display a GUI notebook for PhysiCell. 


We recommend installing the [Anaconda Python 3.x](https://www.anaconda.com/download/) distribution to provide all dependencies. 
However, an alternative, requiring less disk space, is to install [Miniconda Python 3.x](https://conda.io/miniconda.html) and then:
```
conda install matplotlib
conda install scipy
conda install jupyter
```

## Sample Usage

From the root directory of xml2jupyter (we demonstrate using Unix-style shell commands):
```
$ cp config_samples/config_biorobots.xml .
$ python xml2jupyter.py config_biorobots.xml test_user_params.py 
$ jupyter notebook test_gui.ipynb
```
When the notebook starts in your browser, in the "Cell" menu, click "Run All". This should display the minimal notebook that will let you update your XML after changing values in widgets and cicking the 'Write' button.

![alt text](https://github.com/rheiland/xml2jupyter/blob/master/paper/images/test_biorobots_params.png)

<!--
After you have the desired Python modules:
- Copy your project's configuration file (.xml) to this directory, calling it "myconfig.xml"
- Copy your project's executable to this directory, e.g., ```heterogeneity```, in the example below.
- Generate the Python module of widgets for your user params (a "tab" in the Notebook GUI). From a Terminal/Command Prompt window, run:

```python gen_user_tab.py myconfig.xml```

Then run the notebook:

```jupyter notebook PhysiCell.ipynb```

If you don't have your current working directory in your PATH, you will need to be more explicit, e.g.:
```
./heterogeneity myconfig.xml     # on Unix
.\heterogeneity myconfig.xml     # on Windows
```
-->


## Contributions

We welcome users' feedback and contributions. Please use the Issues feature for comments related to this repository and project.

For questions related to PhysiCell, please join us at https://groups.google.com/forum/#!forum/physicell-users.
