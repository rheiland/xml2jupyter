#
# Parse a PhysiCell configuration file (XML) and generate a Jupyter (Python) module (user_params.py)
# containing associated widgets for user parameters.
#
# Authors: Randy Heiland, Daniel Mishler, Tyler Zhang, Eric Bower, and Paul Macklin
#
import sys
import math
import xml.etree.ElementTree as ET

num_args = len(sys.argv)
print("num_args=",num_args)
if ( num_args < 2):
    print("Usage: python " + sys.argv[0] + " <config-file.xml> [<gui-file.py>]")
    sys.exit(1)
config_file = sys.argv[1]

if ( num_args == 3):
    gui_file = sys.argv[2]


# First, let's use this config file name in the (main) mygui.py module:
# f_main = open('mygui.py', 'r')
# for line in f_main:
#     if 'full_xml_filename' in line:
#         print(line)
# #        break
#         sys.exit(1)
if (num_args == 3):
#    with open('mygui.py') as f:
    with open(gui_file) as f:
    #  newText = f.read().replace('myconfig.xml', config_file) # rwh todo: don't assume this string; find line
        file_str = f.read()
        idx = file_str.find('main_xml_filename')  # verify > -1
        file_pre = file_str[:idx] 
        idx2 = file_str[idx:].find('\n')
        file_post = file_str[idx+idx2:] 

#    with open('mygui.py', "w") as f:
    with open(gui_file, "w") as f:
        f.write(file_pre)
        f.write("main_xml_filename = '" + config_file + "'")
        f.write(file_post)

user_tab_header = """ 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}
"""

"""
        self.therapy_activation_time = BoundedFloatText(
            min=0.,
            max=100000000,
            step=stepsize,
            description='therapy_activation_time',
            style=style, layout=layout,
            # layout=Layout(width=constWidth),
        )
        self.save_interval_after_therapy_start = BoundedFloatText(
            min=0.,
            max=100000000,
            step=stepsize,
            description='save_interval_after_therapy_start',
            style=style, layout=layout,
        )

        label_blankline = Label('')

        self.tab = VBox([HBox([self.therapy_activation_time, Label('min')]), 
                         HBox([self.save_interval_after_therapy_start, Label('min')]), 
                         ])  
"""

fill_gui_str= """

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
"""

fill_xml_str= """

    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
"""

# Now parse a configuration file (.xml) and map the user parameters into GUI widgets
#tree = ET.parse('../config/PhysiCell_settings.xml')
tree = ET.parse(config_file)
root = tree.getroot()
uep = root.find('.//user_parameters')  # find unique entry point (uep) to user params
indent = "        "
indent2 = "          "
widgets = {"double":"FloatText", "int":"IntText", "bool":"Checkbox", "string":"Text"}
type_cast = {"double":"float", "int":"int", "bool":"bool", "string":""}
vbox_str = "\n" + indent + "self.tab = VBox([\n"

# TODO: cast attributes to lower case before doing equality tests; perform more testing!

italicize_flag = False
tag_list = []
for child in uep:
    print(child.tag, child.attrib)
    if child.tag in tag_list:
        print("-------> Warning: duplicate tag!  ", child.tag)
        continue
    else:
        tag_list.append(child.tag)
    units_str = ""
    describe_str = ""
    if 'hidden' in child.attrib.keys() and (child.attrib['hidden'].lower() == "true"):   # do we want to hide this from the user?
        print("  HIDE this parameter from the GUI: ", child.tag)
        continue

    describe_str = ''
    if 'description' in child.attrib.keys():
        if italicize_flag:
            describe_str = child.attrib['description'] 
            describe_str = describe_str.replace(" ","\ ")
        else:
            describe_str = ' (' + child.attrib['description'] + ')'
    if 'units' in child.attrib.keys():
        if child.attrib['units'] != "dimensionless" and child.attrib['units'] != "none":
            units_str = child.attrib['units']
    if 'type' in child.attrib.keys():
#             self.therapy_activation_time = BoundedFloatText(
#            min=0., max=100000000, step=stepsize,
        full_name = "self." + child.tag
        if child.attrib['type'] not in widgets.keys():
            print("    *** Warning - Invalid type: " + child.attrib['type'])
        else:    
            # self.default_cell_speed = FloatText(
            #   description='default_cell_speed',
            #   step=0.02,
            #   style=style, layout=layout)
            user_tab_header += "\n" + indent + full_name + " = " + widgets[child.attrib['type']] + "(\n"
            user_tab_header += indent2 + "description='" + child.tag + "',\n"

            # Try to calculate and provide a "good" delta step (for the tiny "up/down" arrows on a numeric widget)
            if child.attrib['type'] == "double":
                fval_abs = abs(float(child.text))
                if (fval_abs > 0.0):
                    if (fval_abs > 1.0):  # crop
                        delta_val = pow(10, int(math.log10(abs(float(child.text)))) - 1)
                    else:   # round
                        delta_val = pow(10, round(math.log10(abs(float(child.text)))) - 1)
                else:
                    delta_val = 0.01  # if initial value=0.0, we're totally guessing at what a good delta is
                print('double: ',float(child.text),', delta_val=',delta_val)

                user_tab_header += indent2 + "value=" + child.text + ",\n"
                # Note: "step" values will advance the value to the nearest multiple of the step value itself :-/
                user_tab_header += indent2 + "step=" + str(delta_val) + ",\n"

            # Integers
            elif child.attrib['type'] == "int":  # warning: math.log(1000,10)=2.99..., math.log10(1000)=3  
                if (abs(int(child.text)) > 0):
                    delta_val = pow(10,int(math.log10(abs(int(child.text)))) - 1)
                else:
                    delta_val = 1  # if initial value=0, we're totally guessing at what a good delta is
                print('int: ',int(child.text),', delta_val=',delta_val)

                user_tab_header += indent2 + "value=" + child.text + ",\n"
                user_tab_header += indent2 + "step=" + str(delta_val) + ",\n"

            # Booleans
            elif child.attrib['type'] == "bool":
                user_tab_header += indent2 + "value=" + child.text + ",\n"
            
            # Strings
            elif child.attrib['type'] == "string":
                user_tab_header += indent2 + "value='" + child.text + "',\n"


            # Finally, append the info at the end of this widget
            user_tab_header += indent2 + "style=style, layout=layout)\n"

            if italicize_flag:
                if len(describe_str) > 0:
                    vbox_str += indent2 + "HBox([" + full_name + ", Label('" + units_str + "'), " + " Label(r'\((" + describe_str + "\))')]), \n"
                else:
                    vbox_str += indent2 + "HBox([" + full_name + ", Label('" + units_str + "'), ]), \n"
            else:
                vbox_str += indent2 + "HBox([" + full_name + ", Label('" + units_str + describe_str + "')]), \n"

            # float, int, bool
            fill_gui_str += indent + full_name + ".value = " + type_cast[child.attrib['type']] + "(uep.find('.//" + child.tag + "').text)\n"

            fill_xml_str += indent + "uep.find('.//" + child.tag + "').text = str("+ full_name + ".value)\n"

vbox_str += indent + "])"

# Write the beginning of the Python module for the user parameters tab in the GUI
user_tab_file = "user_params.py"
print("\n --------------------------------- ")
print("Generated a new: ", user_tab_file)
print()
#print("If this is your first time:")
#print("Run the GUI via:  jupyter notebook mygui.ipynb")
print("Test the minimal GUI via:  jupyter notebook test_gui.ipynb")
print("run the Jupyter menu item:  Cell -> Run All")
print()
print("(or, if you already have a previous GUI running and want to see new params:")
print("run the Jupyter menu item:  Kernel -> Restart & Run All)")
print()
fp= open(user_tab_file, 'w')
fp.write(user_tab_header)
fp.write(vbox_str)
fp.write(fill_gui_str)
fp.write(fill_xml_str)
fp.close()
