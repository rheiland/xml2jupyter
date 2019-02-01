 
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

        self.resource_D = FloatText(
          description='resource_D',
          value=100000,
          step=10000,
          style=style, layout=layout)

        self.resource_lambda = FloatText(
          description='resource_lambda',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.quorum_D = FloatText(
          description='quorum_D',
          value=100000,
          step=10000,
          style=style, layout=layout)

        self.quorum_lambda = FloatText(
          description='quorum_lambda',
          value=10,
          step=1,
          style=style, layout=layout)

        self.death_signal_D = FloatText(
          description='death_signal_D',
          value=40000,
          step=1000,
          style=style, layout=layout)

        self.death_signal_lambda = FloatText(
          description='death_signal_lambda',
          value=1,
          step=0.1,
          style=style, layout=layout)

        self.signal_D = FloatText(
          description='signal_D',
          value=25000,
          step=1000,
          style=style, layout=layout)

        self.signal_lambda = FloatText(
          description='signal_lambda',
          value=.1,
          step=0.01,
          style=style, layout=layout)

        self.poison_D = FloatText(
          description='poison_D',
          value=50000,
          step=1000,
          style=style, layout=layout)

        self.poison_lambda = FloatText(
          description='poison_lambda',
          value=20,
          step=1,
          style=style, layout=layout)

        self.number_of_invaders = IntText(
          description='number_of_invaders',
          value=15,
          step=1,
          style=style, layout=layout)

        self.number_of_suppliers = IntText(
          description='number_of_suppliers',
          value=50,
          step=1,
          style=style, layout=layout)

        self.number_of_scouts = IntText(
          description='number_of_scouts',
          value=10,
          step=1,
          style=style, layout=layout)

        self.number_of_attackers = IntText(
          description='number_of_attackers',
          value=50,
          step=1,
          style=style, layout=layout)

        self.invader_max_birth_rate = FloatText(
          description='invader_max_birth_rate',
          value=0.0028,
          step=0.0001,
          style=style, layout=layout)

        self.invader_max_death_rate = FloatText(
          description='invader_max_death_rate',
          value=0.001,
          step=0.0001,
          style=style, layout=layout)

        self.invader_persistence_time = FloatText(
          description='invader_persistence_time',
          value=15,
          step=1,
          style=style, layout=layout)

        self.invader_migration_speed = FloatText(
          description='invader_migration_speed',
          value=0.25,
          step=0.01,
          style=style, layout=layout)

        self.invader_migration_bias = FloatText(
          description='invader_migration_bias',
          value=0.5,
          step=0.1,
          style=style, layout=layout)

        self.invader_secretion_rate = FloatText(
          description='invader_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.invader_quorum_weight = FloatText(
          description='invader_quorum_weight',
          value=.1,
          step=0.01,
          style=style, layout=layout)

        self.scout_persistence_time = FloatText(
          description='scout_persistence_time',
          value=15,
          step=1,
          style=style, layout=layout)

        self.scout_migration_speed = FloatText(
          description='scout_migration_speed',
          value=.5,
          step=0.1,
          style=style, layout=layout)

        self.scout_migration_bias = FloatText(
          description='scout_migration_bias',
          value=0.125,
          step=0.01,
          style=style, layout=layout)

        self.scout_secretion_rate = FloatText(
          description='scout_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.scout_signal_threshold = FloatText(
          description='scout_signal_threshold',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.attacker_max_birth_rate = FloatText(
          description='attacker_max_birth_rate',
          value=0.0005,
          step=0.0001,
          style=style, layout=layout)

        self.attacker_max_death_rate = FloatText(
          description='attacker_max_death_rate',
          value=0.0001,
          step=1e-05,
          style=style, layout=layout)

        self.attacker_persistence_time = FloatText(
          description='attacker_persistence_time',
          value=15,
          step=1,
          style=style, layout=layout)

        self.attacker_migration_speed = FloatText(
          description='attacker_migration_speed',
          value=1,
          step=0.1,
          style=style, layout=layout)

        self.attacker_migration_bias = FloatText(
          description='attacker_migration_bias',
          value=0.25,
          step=0.01,
          style=style, layout=layout)

        self.attacker_secretion_rate = FloatText(
          description='attacker_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.attacker_signal_threshold = FloatText(
          description='attacker_signal_threshold',
          value=0.1,
          step=0.01,
          style=style, layout=layout)

        self.supplier_secretion_rate = FloatText(
          description='supplier_secretion_rate',
          value=100,
          step=10,
          style=style, layout=layout)

        self.tab = VBox([
          HBox([self.resource_D, Label('micron^2/min (resource diffusion coefficient)')]), 
          HBox([self.resource_lambda, Label('1/min (resource decay rate)')]), 
          HBox([self.quorum_D, Label('micron^2/min (quorum diffusion coefficient)')]), 
          HBox([self.quorum_lambda, Label('1/min (quorum decay rate)')]), 
          HBox([self.death_signal_D, Label('micron^2/min (death signal diffusion coefficient)')]), 
          HBox([self.death_signal_lambda, Label('1/min (death signal decay rate)')]), 
          HBox([self.signal_D, Label('micron^2/min (attack signal diffusion coefficient)')]), 
          HBox([self.signal_lambda, Label('1/min (attack signal decay rate)')]), 
          HBox([self.poison_D, Label('micron^2/min (poison diffusion coefficient)')]), 
          HBox([self.poison_lambda, Label('1/min (poison decay rate)')]), 
          HBox([self.number_of_invaders, Label(' (number of randomly placed invaders)')]), 
          HBox([self.number_of_suppliers, Label(' (number of randomly placed suppliers)')]), 
          HBox([self.number_of_scouts, Label(' (number of randomly placed scouts)')]), 
          HBox([self.number_of_attackers, Label(' (number of randomly placed attackers)')]), 
          HBox([self.invader_max_birth_rate, Label('1/min (max birth rate for invaders)')]), 
          HBox([self.invader_max_death_rate, Label('1/min (max death rate for invaders)')]), 
          HBox([self.invader_persistence_time, Label('min (persistence time for invader migration)')]), 
          HBox([self.invader_migration_speed, Label('micron/min (speed of invader cells)')]), 
          HBox([self.invader_migration_bias, Label(' (invader migration bias)')]), 
          HBox([self.invader_secretion_rate, Label('1/min (rate invaders secrete their signals)')]), 
          HBox([self.invader_quorum_weight, Label(' (motile direction = w*grad(Q) - (1-w)*grad(D))')]), 
          HBox([self.scout_persistence_time, Label('min (persistence time for scout migration)')]), 
          HBox([self.scout_migration_speed, Label('micron/min (speed of scout cells)')]), 
          HBox([self.scout_migration_bias, Label(' (scout migration bias)')]), 
          HBox([self.scout_secretion_rate, Label('1/min (rate scouts secrete their signals)')]), 
          HBox([self.scout_signal_threshold, Label(' (scouts release S if Q > threshold)')]), 
          HBox([self.attacker_max_birth_rate, Label('1/min (max birth rate for attackers)')]), 
          HBox([self.attacker_max_death_rate, Label('1/min (max death rate for attackers)')]), 
          HBox([self.attacker_persistence_time, Label('min (persistence time for attacker migration)')]), 
          HBox([self.attacker_migration_speed, Label('micron/min (speed of attacker cells)')]), 
          HBox([self.attacker_migration_bias, Label(' (attacker migration bias)')]), 
          HBox([self.attacker_secretion_rate, Label('1/min (rate attackers secrete their signals)')]), 
          HBox([self.attacker_signal_threshold, Label(' (attackers release P if S > threshold)')]), 
          HBox([self.supplier_secretion_rate, Label('1/min (rate suppliers release resource)')]), 
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.resource_D.value = float(uep.find('.//resource_D').text)
        self.resource_lambda.value = float(uep.find('.//resource_lambda').text)
        self.quorum_D.value = float(uep.find('.//quorum_D').text)
        self.quorum_lambda.value = float(uep.find('.//quorum_lambda').text)
        self.death_signal_D.value = float(uep.find('.//death_signal_D').text)
        self.death_signal_lambda.value = float(uep.find('.//death_signal_lambda').text)
        self.signal_D.value = float(uep.find('.//signal_D').text)
        self.signal_lambda.value = float(uep.find('.//signal_lambda').text)
        self.poison_D.value = float(uep.find('.//poison_D').text)
        self.poison_lambda.value = float(uep.find('.//poison_lambda').text)
        self.number_of_invaders.value = int(uep.find('.//number_of_invaders').text)
        self.number_of_suppliers.value = int(uep.find('.//number_of_suppliers').text)
        self.number_of_scouts.value = int(uep.find('.//number_of_scouts').text)
        self.number_of_attackers.value = int(uep.find('.//number_of_attackers').text)
        self.invader_max_birth_rate.value = float(uep.find('.//invader_max_birth_rate').text)
        self.invader_max_death_rate.value = float(uep.find('.//invader_max_death_rate').text)
        self.invader_persistence_time.value = float(uep.find('.//invader_persistence_time').text)
        self.invader_migration_speed.value = float(uep.find('.//invader_migration_speed').text)
        self.invader_migration_bias.value = float(uep.find('.//invader_migration_bias').text)
        self.invader_secretion_rate.value = float(uep.find('.//invader_secretion_rate').text)
        self.invader_quorum_weight.value = float(uep.find('.//invader_quorum_weight').text)
        self.scout_persistence_time.value = float(uep.find('.//scout_persistence_time').text)
        self.scout_migration_speed.value = float(uep.find('.//scout_migration_speed').text)
        self.scout_migration_bias.value = float(uep.find('.//scout_migration_bias').text)
        self.scout_secretion_rate.value = float(uep.find('.//scout_secretion_rate').text)
        self.scout_signal_threshold.value = float(uep.find('.//scout_signal_threshold').text)
        self.attacker_max_birth_rate.value = float(uep.find('.//attacker_max_birth_rate').text)
        self.attacker_max_death_rate.value = float(uep.find('.//attacker_max_death_rate').text)
        self.attacker_persistence_time.value = float(uep.find('.//attacker_persistence_time').text)
        self.attacker_migration_speed.value = float(uep.find('.//attacker_migration_speed').text)
        self.attacker_migration_bias.value = float(uep.find('.//attacker_migration_bias').text)
        self.attacker_secretion_rate.value = float(uep.find('.//attacker_secretion_rate').text)
        self.attacker_signal_threshold.value = float(uep.find('.//attacker_signal_threshold').text)
        self.supplier_secretion_rate.value = float(uep.find('.//supplier_secretion_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//resource_D').text = str(self.resource_D.value)
        uep.find('.//resource_lambda').text = str(self.resource_lambda.value)
        uep.find('.//quorum_D').text = str(self.quorum_D.value)
        uep.find('.//quorum_lambda').text = str(self.quorum_lambda.value)
        uep.find('.//death_signal_D').text = str(self.death_signal_D.value)
        uep.find('.//death_signal_lambda').text = str(self.death_signal_lambda.value)
        uep.find('.//signal_D').text = str(self.signal_D.value)
        uep.find('.//signal_lambda').text = str(self.signal_lambda.value)
        uep.find('.//poison_D').text = str(self.poison_D.value)
        uep.find('.//poison_lambda').text = str(self.poison_lambda.value)
        uep.find('.//number_of_invaders').text = str(self.number_of_invaders.value)
        uep.find('.//number_of_suppliers').text = str(self.number_of_suppliers.value)
        uep.find('.//number_of_scouts').text = str(self.number_of_scouts.value)
        uep.find('.//number_of_attackers').text = str(self.number_of_attackers.value)
        uep.find('.//invader_max_birth_rate').text = str(self.invader_max_birth_rate.value)
        uep.find('.//invader_max_death_rate').text = str(self.invader_max_death_rate.value)
        uep.find('.//invader_persistence_time').text = str(self.invader_persistence_time.value)
        uep.find('.//invader_migration_speed').text = str(self.invader_migration_speed.value)
        uep.find('.//invader_migration_bias').text = str(self.invader_migration_bias.value)
        uep.find('.//invader_secretion_rate').text = str(self.invader_secretion_rate.value)
        uep.find('.//invader_quorum_weight').text = str(self.invader_quorum_weight.value)
        uep.find('.//scout_persistence_time').text = str(self.scout_persistence_time.value)
        uep.find('.//scout_migration_speed').text = str(self.scout_migration_speed.value)
        uep.find('.//scout_migration_bias').text = str(self.scout_migration_bias.value)
        uep.find('.//scout_secretion_rate').text = str(self.scout_secretion_rate.value)
        uep.find('.//scout_signal_threshold').text = str(self.scout_signal_threshold.value)
        uep.find('.//attacker_max_birth_rate').text = str(self.attacker_max_birth_rate.value)
        uep.find('.//attacker_max_death_rate').text = str(self.attacker_max_death_rate.value)
        uep.find('.//attacker_persistence_time').text = str(self.attacker_persistence_time.value)
        uep.find('.//attacker_migration_speed').text = str(self.attacker_migration_speed.value)
        uep.find('.//attacker_migration_bias').text = str(self.attacker_migration_bias.value)
        uep.find('.//attacker_secretion_rate').text = str(self.attacker_secretion_rate.value)
        uep.find('.//attacker_signal_threshold').text = str(self.attacker_signal_threshold.value)
        uep.find('.//supplier_secretion_rate').text = str(self.supplier_secretion_rate.value)
