 
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

        self.random_seed = IntText(
          description='random_seed',
          value=0,
          step=1,
          style=style, layout=layout)

        self.cargo_signal_D = FloatText(
          description='cargo_signal_D',
          value=1600.0,
          step=100,
          style=style, layout=layout)

        self.cargo_signal_decay = FloatText(
          description='cargo_signal_decay',
          value=0.8,
          step=0.1,
          style=style, layout=layout)

        self.director_signal_D = FloatText(
          description='director_signal_D',
          value=1300.0,
          step=100,
          style=style, layout=layout)

        self.director_signal_decay = FloatText(
          description='director_signal_decay',
          value=0.19,
          step=0.01,
          style=style, layout=layout)

        self.elastic_coefficient = FloatText(
          description='elastic_coefficient',
          value=0.12,
          step=0.01,
          style=style, layout=layout)

        self.worker_motility_persistence_time = FloatText(
          description='worker_motility_persistence_time',
          value=5.9,
          step=0.1,
          style=style, layout=layout)

        self.worker_migration_speed = FloatText(
          description='worker_migration_speed',
          value=5.9,
          step=0.1,
          style=style, layout=layout)

        self.attached_worker_migration_bias = FloatText(
          description='attached_worker_migration_bias',
          value=1.5,
          step=0.1,
          style=style, layout=layout)

        self.unattached_worker_migration_bias = FloatText(
          description='unattached_worker_migration_bias',
          value=1.0,
          step=0.1,
          style=style, layout=layout)

        self.number_of_directors = IntText(
          description='number_of_directors',
          value=20,
          step=1,
          style=style, layout=layout)

        self.number_of_cargo_clusters = IntText(
          description='number_of_cargo_clusters',
          value=110,
          step=10,
          style=style, layout=layout)

        self.number_of_workers = IntText(
          description='number_of_workers',
          value=35,
          step=1,
          style=style, layout=layout)

        self.drop_threshold = FloatText(
          description='drop_threshold',
          value=0.4,
          step=0.1,
          style=style, layout=layout)

        self.worker_color = Text(
          description='worker_color',
          style=style, layout=layout)

        self.cargo_color = Text(
          description='cargo_color',
          style=style, layout=layout)

        self.director_color = Text(
          description='director_color',
          style=style, layout=layout)

        self.tab = VBox([
          HBox([self.random_seed, Label('')]), 
          HBox([self.cargo_signal_D, Label('micron/min^2')]), 
          HBox([self.cargo_signal_decay, Label('1/min')]), 
          HBox([self.director_signal_D, Label('micron/min^2')]), 
          HBox([self.director_signal_decay, Label('1/min')]), 
          HBox([self.elastic_coefficient, Label('1/min')]), 
          HBox([self.worker_motility_persistence_time, Label('min')]), 
          HBox([self.worker_migration_speed, Label('micron/min')]), 
          HBox([self.attached_worker_migration_bias, Label('min')]), 
          HBox([self.unattached_worker_migration_bias, Label('min')]), 
          HBox([self.number_of_directors, Label('')]), 
          HBox([self.number_of_cargo_clusters, Label('')]), 
          HBox([self.number_of_workers, Label('')]), 
          HBox([self.drop_threshold, Label('')]), 
          HBox([self.worker_color, Label('')]), 
          HBox([self.cargo_color, Label('')]), 
          HBox([self.director_color, Label('')]), 
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.cargo_signal_D.value = float(uep.find('.//cargo_signal_D').text)
        self.cargo_signal_decay.value = float(uep.find('.//cargo_signal_decay').text)
        self.director_signal_D.value = float(uep.find('.//director_signal_D').text)
        self.director_signal_decay.value = float(uep.find('.//director_signal_decay').text)
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
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//cargo_signal_D').text = str(self.cargo_signal_D.value)
        uep.find('.//cargo_signal_decay').text = str(self.cargo_signal_decay.value)
        uep.find('.//director_signal_D').text = str(self.director_signal_D.value)
        uep.find('.//director_signal_decay').text = str(self.director_signal_decay.value)
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
