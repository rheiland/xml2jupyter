 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='elastic_coefficient', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'red'

        self.elastic_coefficient = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name2 = Button(description='worker_motility_persistence_time', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'green'

        self.worker_motility_persistence_time = FloatText(
          value=5.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='worker_migration_speed', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'red'

        self.worker_migration_speed = FloatText(
          value=5.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='attached_worker_migration_bias', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'green'

        self.attached_worker_migration_bias = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='unattached_worker_migration_bias', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'red'

        self.unattached_worker_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='number_of_directors', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'green'

        self.number_of_directors = IntText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='number_of_cargo_clusters', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'red'

        self.number_of_cargo_clusters = IntText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name8 = Button(description='number_of_workers', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'green'

        self.number_of_workers = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='drop_threshold', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'red'

        self.drop_threshold = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='worker_color', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'green'

        self.worker_color = Text(
          value='red',
          style=style, layout=widget_layout)

        param_name11 = Button(description='cargo_color', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'red'

        self.cargo_color = Text(
          value='blue',
          style=style, layout=widget_layout)

        param_name12 = Button(description='director_color', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'green'

        self.director_color = Text(
          value='limegreen',
          style=style, layout=widget_layout)

        units_button1 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'red'
        units_button2 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'green'
        units_button3 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'red'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'green'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'red'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'green'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'red'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'green'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'red'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'green'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'red'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'green'

        desc_button1 = Button(description='elastic coefficient of cells', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'red'
        desc_button2 = Button(description='persistance time for worker motility', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'green'
        desc_button3 = Button(description='speed of worker cells', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'red'
        desc_button4 = Button(description='migration bias of attached workers', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'green'
        desc_button5 = Button(description='migration bias of unattached workers', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'red'
        desc_button6 = Button(description='# of director cells', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'green'
        desc_button7 = Button(description='# of cargo clusters', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'red'
        desc_button8 = Button(description='# of worker cells', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'green'
        desc_button9 = Button(description='threshold to drop cargo', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'red'
        desc_button10 = Button(description='color of worker cells', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'green'
        desc_button11 = Button(description='color of cargo cells', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'red'
        desc_button12 = Button(description='color of director cells', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'green'

        row1 = [param_name1, self.elastic_coefficient, units_button1, desc_button1] 
        row2 = [param_name2, self.worker_motility_persistence_time, units_button2, desc_button2] 
        row3 = [param_name3, self.worker_migration_speed, units_button3, desc_button3] 
        row4 = [param_name4, self.attached_worker_migration_bias, units_button4, desc_button4] 
        row5 = [param_name5, self.unattached_worker_migration_bias, units_button5, desc_button5] 
        row6 = [param_name6, self.number_of_directors, units_button6, desc_button6] 
        row7 = [param_name7, self.number_of_cargo_clusters, units_button7, desc_button7] 
        row8 = [param_name8, self.number_of_workers, units_button8, desc_button8] 
        row9 = [param_name9, self.drop_threshold, units_button9, desc_button9] 
        row10 = [param_name10, self.worker_color, units_button10, desc_button10] 
        row11 = [param_name11, self.cargo_color, units_button11, desc_button11] 
        row12 = [param_name12, self.director_color, units_button12, desc_button12] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.elastic_coefficient.value = float(uep.find('.//elastic_coefficient').text)
        self.worker_motility_persistence_time.value = float(uep.find('.//worker_motility_persistence_time').text)
        self.worker_migration_speed.value = float(uep.find('.//worker_migration_speed').text)
        self.attached_worker_migration_bias.value = float(uep.find('.//attached_worker_migration_bias').text)
        self.unattached_worker_migration_bias.value = float(uep.find('.//unattached_worker_migration_bias').text)
        self.number_of_directors.value = int(uep.find('.//number_of_directors').text)
        self.number_of_cargo_clusters.value = int(uep.find('.//number_of_cargo_clusters').text)
        self.number_of_workers.value = int(uep.find('.//number_of_workers').text)
        self.drop_threshold.value = float(uep.find('.//drop_threshold').text)
        self.worker_color.value = (uep.find('.//worker_color').text)
        self.cargo_color.value = (uep.find('.//cargo_color').text)
        self.director_color.value = (uep.find('.//director_color').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//elastic_coefficient').text = str(self.elastic_coefficient.value)
        uep.find('.//worker_motility_persistence_time').text = str(self.worker_motility_persistence_time.value)
        uep.find('.//worker_migration_speed').text = str(self.worker_migration_speed.value)
        uep.find('.//attached_worker_migration_bias').text = str(self.attached_worker_migration_bias.value)
        uep.find('.//unattached_worker_migration_bias').text = str(self.unattached_worker_migration_bias.value)
        uep.find('.//number_of_directors').text = str(self.number_of_directors.value)
        uep.find('.//number_of_cargo_clusters').text = str(self.number_of_cargo_clusters.value)
        uep.find('.//number_of_workers').text = str(self.number_of_workers.value)
        uep.find('.//drop_threshold').text = str(self.drop_threshold.value)
        uep.find('.//worker_color').text = str(self.worker_color.value)
        uep.find('.//cargo_color').text = str(self.cargo_color.value)
        uep.find('.//director_color').text = str(self.director_color.value)
