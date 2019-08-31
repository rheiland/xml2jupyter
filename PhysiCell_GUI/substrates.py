# substrates  Tab

import os, math
from ipywidgets import Layout, Label, Text, Checkbox, Button, BoundedIntText, HBox, VBox, Box, \
    FloatText, Dropdown, interactive
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.colors as mplc
import scipy.io
import xml.etree.ElementTree as ET  # https://docs.python.org/2/library/xml.etree.elementtree.html
import glob
import platform
import zipfile
from debug import debug_view 

hublib_flag = True
if platform.system() != 'Windows':
    try:
#        print("Trying to import hublib.ui")
        from hublib.ui import Download
    except:
        hublib_flag = False
else:
    hublib_flag = False


class SubstrateTab(object):

    def __init__(self):
        
        self.output_dir = '.'
#        self.output_dir = 'tmpdir'

        # self.fig = plt.figure(figsize=(7.2,6))  # this strange figsize results in a ~square contour plot

        # initial value
        self.field_index = 4
        # self.field_index = self.mcds_field.value + 4

        # define dummy size of mesh (set in the tool's primary module)
        self.numx = 0
        self.numy = 0

        tab_height = '500px'
        constWidth = '180px'
        constWidth2 = '150px'
        tab_layout = Layout(width='900px',   # border='2px solid black',
                            height=tab_height, ) #overflow_y='scroll')

        max_frames = 1   
        self.mcds_plot = interactive(self.plot_substrate, frame=(0, max_frames), continuous_update=False)  
        svg_plot_size = '500px'  # small: controls the size of the tab height, not the plot (rf. figsize for that)
        svg_plot_size = '800px'  # medium
        svg_plot_size = '750px'  # medium
        self.mcds_plot.layout.width = svg_plot_size
        self.mcds_plot.layout.height = svg_plot_size

        self.max_frames = BoundedIntText(
            min=0, max=99999, value=max_frames,
            description='Max',
           layout=Layout(width='160px'),
        )
        self.max_frames.observe(self.update_max_frames)

        self.field_min_max = {'dummy': [0., 1.]}
        # hacky I know, but make a dict that's got (key,value) reversed from the dict in the Dropdown below
        self.field_dict = {0:'dummy'}

        self.mcds_field = Dropdown(
            options={'dummy': 0},
            value=0,
            #     description='Field',
           layout=Layout(width=constWidth)
        )
        # print("substrate __init__: self.mcds_field.value=",self.mcds_field.value)
#        self.mcds_field.observe(self.mcds_field_cb)
        self.mcds_field.observe(self.mcds_field_changed_cb)

        # self.field_cmap = Text(
        #     value='viridis',
        #     description='Colormap',
        #     disabled=True,
        #     layout=Layout(width=constWidth),
        # )
        self.field_cmap = Dropdown(
            options=['viridis', 'jet', 'YlOrRd'],
            value='viridis',
            #     description='Field',
           layout=Layout(width=constWidth)
        )
        #self.field_cmap.observe(self.plot_substrate)
#        self.field_cmap.observe(self.plot_substrate)
        self.field_cmap.observe(self.mcds_field_cb)

        self.cmap_fixed = Checkbox(
            description='Fix',
            disabled=False,
#           layout=Layout(width=constWidth2),
        )

        self.save_min_max= Button(
            description='Save', #style={'description_width': 'initial'},
            button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Save min/max for this substrate',
            disabled=True,
           layout=Layout(width='90px')
        )

        def save_min_max_cb(b):
#            field_name = self.mcds_field.options[]
#            field_name = next(key for key, value in self.mcds_field.options.items() if value == self.mcds_field.value)
            field_name = self.field_dict[self.mcds_field.value]
#            print(field_name)
#            self.field_min_max = {'oxygen': [0., 30.], 'glucose': [0., 1.], 'H+ ions': [0., 1.], 'ECM': [0., 1.], 'NP1': [0., 1.], 'NP2': [0., 1.]}
            self.field_min_max[field_name][0] = self.cmap_min.value
            self.field_min_max[field_name][1] = self.cmap_max.value
#            print(self.field_min_max)

        self.save_min_max.on_click(save_min_max_cb)

        self.cmap_min = FloatText(
            description='Min',
            value=0,
            step = 0.1,
            disabled=True,
            layout=Layout(width=constWidth2),
        )
        self.cmap_min.observe(self.mcds_field_cb)

        self.cmap_max = FloatText(
            description='Max',
            value=38,
            step = 0.1,
            disabled=True,
            layout=Layout(width=constWidth2),
        )
        self.cmap_max.observe(self.mcds_field_cb)

        def cmap_fixed_cb(b):
            if (self.cmap_fixed.value):
                self.cmap_min.disabled = False
                self.cmap_max.disabled = False
                self.save_min_max.disabled = False
            else:
                self.cmap_min.disabled = True
                self.cmap_max.disabled = True
                self.save_min_max.disabled = True
#            self.mcds_field_cb()

        self.cmap_fixed.observe(cmap_fixed_cb)

        field_cmap_row2 = HBox([self.field_cmap, self.cmap_fixed])

#        field_cmap_row3 = HBox([self.save_min_max, self.cmap_min, self.cmap_max])
        items_auto = [
            self.save_min_max, #layout=Layout(flex='3 1 auto', width='auto'),
            self.cmap_min, 
            self.cmap_max,  
         ]
        box_layout = Layout(display='flex',
                    flex_flow='row',
                    align_items='stretch',
                    width='80%')
        field_cmap_row3 = Box(children=items_auto, layout=box_layout)

#        field_cmap_row3 = Box([self.save_min_max, self.cmap_min, self.cmap_max])

        # mcds_tab = widgets.VBox([mcds_dir, mcds_plot, mcds_play], layout=tab_layout)
        mcds_params = VBox([self.mcds_field, field_cmap_row2, field_cmap_row3, self.max_frames])  # mcds_dir
#        mcds_params = VBox([self.mcds_field, field_cmap_row2, field_cmap_row3,])  # mcds_dir

#        self.tab = HBox([mcds_params, self.mcds_plot], layout=tab_layout)
#        self.tab = HBox([mcds_params, self.mcds_plot])

        help_label = Label('select slider: drag or left/right arrows')
        row1 = Box([help_label, Box( [self.max_frames, self.mcds_field, self.field_cmap], layout=Layout(border='0px solid black',
                            width='50%',
                            height='',
                            align_items='stretch',
                            flex_direction='row',
                            display='flex'))] )
        row2 = Box([self.cmap_fixed, self.cmap_min, self.cmap_max], layout=Layout(border='0px solid black',
                            width='50%',
                            height='',
                            align_items='stretch',
                            flex_direction='row',
                            display='flex'))
        if (hublib_flag):
            self.download_button = Download('mcds.zip', style='warning', icon='cloud-download', 
                                                tooltip='Download data', cb=self.download_cb)
            download_row = HBox([self.download_button.w, Label("Download all substrate data (browser must allow pop-ups).")])

    #        self.tab = VBox([row1, row2, self.mcds_plot])
            self.tab = VBox([row1, row2, self.mcds_plot, download_row])
        else:
            # self.tab = VBox([row1, row2])
            self.tab = VBox([row1, row2, self.mcds_plot])

    #---------------------------------------------------
    def update_dropdown_fields(self, data_dir):
        # print('update_dropdown_fields called --------')
        self.output_dir = data_dir
        tree = None
        try:
            fname = os.path.join(self.output_dir, "initial.xml")
            tree = ET.parse(fname)
            xml_root = tree.getroot()
        except:
            print("Cannot open ",fname," to read info, e.g., names of substrate fields.")
            return

        xml_root = tree.getroot()
        self.field_min_max = {}
        self.field_dict = {}
        dropdown_options = {}
        uep = xml_root.find('.//variables')
        comment_str = ""
        field_idx = 0
        if (uep):
            for elm in uep.findall('variable'):
                # print("-----> ",elm.attrib['name'])
                self.field_min_max[elm.attrib['name']] = [0., 1.]
                self.field_dict[field_idx] = elm.attrib['name']
                dropdown_options[elm.attrib['name']] = field_idx
                field_idx += 1

#        constWidth = '180px'
        # print('options=',dropdown_options)
        self.mcds_field.value=0
        self.mcds_field.options=dropdown_options
#         self.mcds_field = Dropdown(
# #            options={'oxygen': 0, 'glucose': 1},
#             options=dropdown_options,
#             value=0,
#             #     description='Field',
#            layout=Layout(width=constWidth)
#         )

    def update_max_frames_expected(self, value):  # called when beginning an interactive Run
        self.max_frames.value = value  # assumes naming scheme: "snapshot%08d.svg"
        self.mcds_plot.children[0].max = self.max_frames.value

#    def update(self, rdir):
    def update(self, rdir=''):
        # with debug_view:
        #     print("substrates: update rdir=", rdir)        

        if rdir:
            self.output_dir = rdir

        all_files = sorted(glob.glob(os.path.join(self.output_dir, 'output*.xml')))
        if len(all_files) > 0:
            last_file = all_files[-1]
            self.max_frames.value = int(last_file[-12:-4])  # assumes naming scheme: "snapshot%08d.svg"

        # with debug_view:
        #     print("substrates: added %s files" % len(all_files))


        # self.output_dir = rdir
        # if rdir == '':
        #     # self.max_frames.value = 0
        #     tmpdir = os.path.abspath('tmpdir')
        #     self.output_dir = tmpdir
        #     all_files = sorted(glob.glob(os.path.join(tmpdir, 'output*.xml')))
        #     if len(all_files) > 0:
        #         last_file = all_files[-1]
        #         self.max_frames.value = int(last_file[-12:-4])  # assumes naming scheme: "output%08d.xml"
        #         self.mcds_plot.update()
        #     return

        # all_files = sorted(glob.glob(os.path.join(rdir, 'output*.xml')))
        # if len(all_files) > 0:
        #     last_file = all_files[-1]
        #     self.max_frames.value = int(last_file[-12:-4])  # assumes naming scheme: "output%08d.xml"
        #     self.mcds_plot.update()

    def download_cb(self):
        file_xml = os.path.join(self.output_dir, '*.xml')
        file_mat = os.path.join(self.output_dir, '*.mat')
        # print('zip up all ',file_str)
        with zipfile.ZipFile('mcds.zip', 'w') as myzip:
            for f in glob.glob(file_xml):
                myzip.write(f, os.path.basename(f)) # 2nd arg avoids full filename path in the archive
            for f in glob.glob(file_mat):
                myzip.write(f, os.path.basename(f))

    def update_max_frames(self,_b):
        self.mcds_plot.children[0].max = self.max_frames.value

    def mcds_field_changed_cb(self, b):
        # print("mcds_field_changed_cb: self.mcds_field.value=",self.mcds_field.value)
        if (self.mcds_field.value == None):
            return
        self.field_index = self.mcds_field.value + 4

        field_name = self.field_dict[self.mcds_field.value]
#        print('mcds_field_cb: '+field_name)
        self.cmap_min.value = self.field_min_max[field_name][0]
        self.cmap_max.value = self.field_min_max[field_name][1]
        self.mcds_plot.update()

    def mcds_field_cb(self, b):
        #self.field_index = self.mcds_field.value
#        self.field_index = self.mcds_field.options.index(self.mcds_field.value) + 4
#        self.field_index = self.mcds_field.options[self.mcds_field.value]
        self.field_index = self.mcds_field.value + 4

        # field_name = self.mcds_field.options[self.mcds_field.value]
        # self.cmap_min.value = self.field_min_max[field_name][0]  # oxygen, etc
        # self.cmap_max.value = self.field_min_max[field_name][1]  # oxygen, etc

#        self.field_index = self.mcds_field.value + 4

#        print('field_index=',self.field_index)
        self.mcds_plot.update()

    def plot_substrate(self, frame):
        # global current_idx, axes_max, gFileId, field_index
        fname = "output%08d_microenvironment0.mat" % frame
        xml_fname = "output%08d.xml" % frame
        # fullname = output_dir_str + fname

#        fullname = fname
        full_fname = os.path.join(self.output_dir, fname)
        full_xml_fname = os.path.join(self.output_dir, xml_fname)
#        self.output_dir = '.'

#        if not os.path.isfile(fullname):
        if not os.path.isfile(full_fname):
            print("Once output files are generated, click the slider.")  # No:  output00000000_microenvironment0.mat
            return

#        tree = ET.parse(xml_fname)
        tree = ET.parse(full_xml_fname)
        xml_root = tree.getroot()
        mins= round(int(float(xml_root.find(".//current_time").text)))  # TODO: check units = mins
        hrs = int(mins/60)
        days = int(hrs/24)
        title_str = '%dd, %dh, %dm' % (int(days),(hrs%24), mins - (hrs*60))


        info_dict = {}
#        scipy.io.loadmat(fullname, info_dict)
        scipy.io.loadmat(full_fname, info_dict)
        M = info_dict['multiscale_microenvironment']
        #     global_field_index = int(mcds_field.value)
        #     print('plot_substrate: field_index =',field_index)
        f = M[self.field_index, :]   # 4=tumor cells field, 5=blood vessel density, 6=growth substrate
        # plt.clf()
        # my_plot = plt.imshow(f.reshape(400,400), cmap='jet', extent=[0,20, 0,20])
    
        # self.fig = plt.figure(figsize=(7.2,6))  # this strange figsize results in a ~square contour plot
        self.fig = plt.figure(figsize=(24.0,20))  # this strange figsize results in a ~square contour plot
        # self.fig = plt.figure(figsize=(28.8,24))  # this strange figsize results in a ~square contour plot
        #     fig.set_tight_layout(True)
        #     ax = plt.axes([0, 0.05, 0.9, 0.9 ]) #left, bottom, width, height
        #     ax = plt.axes([0, 0.0, 1, 1 ])
        #     cmap = plt.cm.viridis # Blues, YlOrBr, ...
        #     im = ax.imshow(f.reshape(100,100), interpolation='nearest', cmap=cmap, extent=[0,20, 0,20])
        #     ax.grid(False)

        # print("substrates.py: ------- numx, numy = ", self.numx, self.numy )
        if (self.numx == 0):   # need to parse vals from the config.xml
            fname = os.path.join(self.output_dir, "config.xml")
            tree = ET.parse(fname)
            xml_root = tree.getroot()
            xmin = float(xml_root.find(".//x_min").text)
            xmax = float(xml_root.find(".//x_max").text)
            dx = float(xml_root.find(".//dx").text)
            ymin = float(xml_root.find(".//y_min").text)
            ymax = float(xml_root.find(".//y_max").text)
            dy = float(xml_root.find(".//dy").text)
            self.numx =  math.ceil( (xmax - xmin) / dx)
            self.numy =  math.ceil( (ymax - ymin) / dy)

        xgrid = M[0, :].reshape(self.numy, self.numx)
        ygrid = M[1, :].reshape(self.numy, self.numx)

        num_contours = 15
        levels = MaxNLocator(nbins=num_contours).tick_values(self.cmap_min.value, self.cmap_max.value)
        contour_ok = True
        if (self.cmap_fixed.value):
            try:
                my_plot = plt.contourf(xgrid, ygrid, M[self.field_index, :].reshape(self.numy, self.numx), levels=levels, extend='both', cmap=self.field_cmap.value)
            except:
                contour_ok = False
                # print('got error on contourf 1.')
        else:    
            try:
                my_plot = plt.contourf(xgrid, ygrid, M[self.field_index, :].reshape(self.numy,self.numx), num_contours, cmap=self.field_cmap.value)
            except:
                contour_ok = False
                # print('got error on contourf 2.')

        if (contour_ok):
            plt.title(title_str)
            plt.colorbar(my_plot)
        axes_min = 0
        axes_max = 2000
        # plt.xlim(axes_min, axes_max)
        # plt.ylim(axes_min, axes_max)


# mcds_play = widgets.Play(
# #     interval=10,
#     value=50,
#     min=0,
#     max=100,
#     step=1,
#     description="Press play",
#     disabled=False,
# )
# #mcds_slider = widgets.IntSlider()

# widgets.jslink((mcds_play, 'value'), (mcds_slider, 'value'))
# widgets.HBox([mcds_play, mcds_slider])

