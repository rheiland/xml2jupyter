# SVG  Tab

import os
from ipywidgets import Layout, Label, Text, Checkbox, Button, HBox, VBox, Box, \
    FloatText, BoundedIntText, BoundedFloatText, HTMLMath, Dropdown, interactive, Output
from collections import deque
import xml.etree.ElementTree as ET
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import numpy as np
# from hublib.ui import Download
import zipfile
import glob

#mpl.rcParams['figure.max_open_warning'] = 100

debug_view = Output(layout={'border': '1px solid black'})

class SVGTab(object):

#    myplot = None

    def __init__(self):
        tab_height = '520px'
        tab_height = '550px'
        tab_layout = Layout(width='900px',   # border='2px solid black',
                            height=tab_height)  #, overflow_y='scroll')

        self.output_dir = '.'
#        self.output_dir = 'tmpdir'

        max_frames = 1 
        self.svg_plot = interactive(self.plot_svg, frame=(0, max_frames), continuous_update=False)
        svg_plot_size = '500px'
        self.svg_plot.layout.width = svg_plot_size
        self.svg_plot.layout.height = svg_plot_size
        self.use_defaults = True


        self.show_nucleus = 0  # 0->False, 1->True in Checkbox!
        self.show_edge = 1  # 0->False, 1->True in Checkbox!
        self.scale_radius = 1.0
        self.axes_min = 0.0
        self.axes_max = 2000   # hmm, this can change (TODO?)
        self.fig = plt.figure(figsize=(6, 6))
#        self.tab = HBox([svg_plot], layout=tab_layout)

        self.max_frames = BoundedIntText(
            min=0, max=99999, value=max_frames,
            description='Max', 
            # layout=Layout(flex='0 1 auto', width='auto'),  #Layout(width='160px'),
        )
        self.max_frames.observe(self.update_max_frames)

        self.show_nucleus_checkbox= Checkbox(
            description='nucleus', value=False, disabled=False,
            # layout=Layout(flex='1 1 auto', width='auto'),  #Layout(width='160px'),
        )
        self.show_nucleus_checkbox.observe(self.show_nucleus_cb)

        self.show_edge_checkbox= Checkbox(
            description='edge', value=True, disabled=False,
            # layout=Layout(flex='1 1 auto', width='auto'),  #Layout(width='160px'),
        )
        self.show_edge_checkbox.observe(self.show_edge_cb)

#        row1 = HBox([Label('(select slider: drag or left/right arrows)'), 
#            self.max_frames, VBox([self.show_nucleus_checkbox, self.show_edge_checkbox])])
#            self.max_frames, self.show_nucleus_checkbox], layout=Layout(width='500px'))

#        self.tab = VBox([row1,self.svg_plot], layout=tab_layout)

        self.help_label = Label('select slider: drag or left/right arrows', 
                                    layout=Layout(flex='0 1 auto', width='auto'))
#                                    layout=Layout(flex='3 1 auto', width='auto'))
        items_auto = [self.help_label, 
            self.max_frames, 
            self.show_nucleus_checkbox,  
            self.show_edge_checkbox, 
         ]
#row1 = HBox([Label('(select slider: drag or left/right arrows)'), 
#            max_frames, show_nucleus_checkbox, show_edge_checkbox], 
#            layout=Layout(width='800px'))
        box_layout = Layout(display='flex',
                    flex_flow='row',
                    align_items='stretch', 
                    width='90%')
        # row1 = Box(children=items_auto, layout=box_layout)
        #row1 = Box(children=items_auto)
        row1=Box([self.help_label, Box([self.max_frames, self.show_nucleus_checkbox, self.show_edge_checkbox] , layout=Layout(border='0px solid black',
                    width='60%',
                    height='',
                    align_items='stretch',
                    flex_direction='row',
                    display='flex'))] )

        # self.download_button = Download('svg.zip', style='warning', icon='cloud-download', tooltip='Download results', cb=self.download_cb)
        #self.download_button = Download('svg.zip', style='warning', icon='cloud-download', tooltip='Download results')

#        self.tab = VBox([row1, self.svg_plot], layout=tab_layout)
#        self.tab = VBox([row1, self.svg_plot, self.download_button.w], layout=tab_layout)
        self.tab = VBox([row1, self.svg_plot ], layout=tab_layout)

 #       self.output_dir_str = os.getenv('RESULTSDIR') + "/pc4nanobio/"

    def update_max_frames_expected(self, value):  # called when beginning an interactive Run
       with debug_view:
        print("update_max_frames_expected: SVG UPDATE", rdir)
        self.max_frames.value = value  # assumes naming scheme: "snapshot%08d.svg"
        self.svg_plot.children[0].max = self.max_frames.value
#        self.svg_plot.update()

    def update(self, rdir):
        with debug_view:
            print("svg.py: update(): rdir (->self.output_dir)=", rdir)
        self.output_dir = rdir

        if rdir == '':
            # self.max_frames.value = 0
            tmpdir = os.path.abspath('tmpdir')
            # with debug_view:
            #     print("svg.py: update(): tmpdir=", tmpdir)
            self.output_dir = tmpdir
            all_files = sorted(glob.glob(os.path.join(tmpdir, 'snapshot*.svg')))
            # with debug_view:
            #     print("svg.py: update(): len(all_files)=", len(all_files))
            if len(all_files) > 0:
                last_file = all_files[-1]
                self.max_frames.value = int(last_file[-12:-4])  # assumes naming scheme: "snapshot%08d.svg"
                self.svg_plot.update()
            return

        all_files = sorted(glob.glob(os.path.join(rdir, 'snapshot*.svg')))
        with debug_view:
            print("svg.py: update(): rdir != blank; len(all_files)=", len(all_files))
        if len(all_files) > 0:
            last_file = all_files[-1]
            self.max_frames.value = int(last_file[-12:-4])  # assumes naming scheme: "snapshot%08d.svg"
            self.svg_plot.update()


    def download_cb(self):
        file_str = os.path.join(self.output_dir,'*.svg')
        # print('zip up all ',file_str)
        with zipfile.ZipFile('svg.zip','w') as myzip:
            for f in glob.glob(file_str):
                myzip.write(f, os.path.basename(f))   # 2nd arg avoids full filename path in the archive

    def show_nucleus_cb(self, b):
        global current_frame
        if (self.show_nucleus_checkbox.value):
            self.show_nucleus = 1
        else:
            self.show_nucleus = 0
#        self.plot_svg(self,current_frame)
        self.svg_plot.update()

    def show_edge_cb(self, b):
        if (self.show_edge_checkbox.value):
            self.show_edge = 1
        else:
            self.show_edge = 0
        self.svg_plot.update()


    def update_max_frames(self,_b):
        self.svg_plot.children[0].max = self.max_frames.value

    def plot_svg(self, frame):
        # global current_idx, axes_max
        global current_frame
        current_frame = frame
        fname = "snapshot%08d.svg" % frame

#        fullname = self.output_dir_str + fname
#        fullname = fname  # do this for nanoHUB! (data appears in root dir?)
        full_fname = os.path.join(self.output_dir, fname)
        if not os.path.isfile(full_fname):
            # print("File does not exist: ", fname)
            # print("File does not exist: ", full_fname)
            #print("No: ", full_fname)
            print("Missing output file")   #  No:  snapshot00000000.svg
            return

        xlist = deque()
        ylist = deque()
        rlist = deque()
        rgb_list = deque()

        #  print('\n---- ' + fname + ':')
#        tree = ET.parse(fname)
        tree = ET.parse(full_fname)
        root = tree.getroot()
        #  print('--- root.tag ---')
        #  print(root.tag)
        #  print('--- root.attrib ---')
        #  print(root.attrib)
        #  print('--- child.tag, child.attrib ---')
        numChildren = 0
        for child in root:
            #    print(child.tag, child.attrib)
            #    print("keys=",child.attrib.keys())
            if self.use_defaults and ('width' in child.attrib.keys()):
                self.axes_max = float(child.attrib['width'])
                # print("debug> found width --> axes_max =", axes_max)
            if child.text and "Current time" in child.text:
                svals = child.text.split()
                # title_str = "(" + str(current_idx) + ") Current time: " + svals[2] + "d, " + svals[4] + "h, " + svals[7] + "m"
                # title_str = "Current time: " + svals[2] + "d, " + svals[4] + "h, " + svals[7] + "m"
                title_str = svals[2] + "d, " + svals[4] + "h, " + svals[7] + "m"

            # print("width ",child.attrib['width'])
            # print('attrib=',child.attrib)
            # if (child.attrib['id'] == 'tissue'):
            if ('id' in child.attrib.keys()):
                # print('-------- found tissue!!')
                tissue_parent = child
                break

        # print('------ search tissue')
        cells_parent = None

        for child in tissue_parent:
            # print('attrib=',child.attrib)
            if (child.attrib['id'] == 'cells'):
                # print('-------- found cells, setting cells_parent')
                cells_parent = child
                break
            numChildren += 1

        num_cells = 0
        #  print('------ search cells')
        for child in cells_parent:
            #    print(child.tag, child.attrib)
            #    print('attrib=',child.attrib)
            for circle in child:  # two circles in each child: outer + nucleus
                #  circle.attrib={'cx': '1085.59','cy': '1225.24','fill': 'rgb(159,159,96)','r': '6.67717','stroke': 'rgb(159,159,96)','stroke-width': '0.5'}
                #      print('  --- cx,cy=',circle.attrib['cx'],circle.attrib['cy'])
                xval = float(circle.attrib['cx'])

                s = circle.attrib['fill']
                # print("s=",s)
                # print("type(s)=",type(s))
                if (s[0:3] == "rgb"):  # if an rgb string, e.g. "rgb(175,175,80)" 
                    rgb = list(map(int, s[4:-1].split(",")))  
                    rgb[:] = [x / 255. for x in rgb]
                else:     # otherwise, must be a color name
                    rgb_tuple = mplc.to_rgb(mplc.cnames[s])  # a tuple
                    rgb = [x for x in rgb_tuple]

                # test for bogus x,y locations (rwh TODO: use max of domain?)
                too_large_val = 10000.
                if (np.fabs(xval) > too_large_val):
                    print("bogus xval=", xval)
                    break
                yval = float(circle.attrib['cy'])
                if (np.fabs(yval) > too_large_val):
                    print("bogus xval=", xval)
                    break

                rval = float(circle.attrib['r'])
                # if (rgb[0] > rgb[1]):
                #     print(num_cells,rgb, rval)
                xlist.append(xval)
                ylist.append(yval)
                rlist.append(rval)
                rgb_list.append(rgb)

                # For .svg files with cells that *have* a nucleus, there will be a 2nd
                if (self.show_nucleus == 0):
                #if (not self.show_nucleus):
                    break

            num_cells += 1

            # if num_cells > 3:   # for debugging
            #   print(fname,':  num_cells= ',num_cells," --- debug exit.")
            #   sys.exit(1)
            #   break

            # print(fname,':  num_cells= ',num_cells)

        xvals = np.array(xlist)
        yvals = np.array(ylist)
        rvals = np.array(rlist)
        rgbs = np.array(rgb_list)
        # print("xvals[0:5]=",xvals[0:5])
        # print("rvals[0:5]=",rvals[0:5])
        # print("rvals.min, max=",rvals.min(),rvals.max())

        # rwh - is this where I change size of render window?? (YES - yipeee!)
        #   plt.figure(figsize=(6, 6))
        #   plt.cla()
        title_str += " (" + str(num_cells) + " agents)"
        #   plt.title(title_str)
        #   plt.xlim(axes_min,axes_max)
        #   plt.ylim(axes_min,axes_max)
        #   plt.scatter(xvals,yvals, s=rvals*scale_radius, c=rgbs)
#        plt.axes().set_aspect('equal', 'datalim')

        self.fig = plt.figure(figsize=(6, 6))   #rwh: move to __init__
#        plt.figure(figsize=(7, 7))

#        axx = plt.axes([0, 0.05, 0.9, 0.9])  # left, bottom, width, height
#        axx = fig.gca()
#        print('fig.dpi=',fig.dpi) # = 72

        #   im = ax.imshow(f.reshape(100,100), interpolation='nearest', cmap=cmap, extent=[0,20, 0,20])
        #   ax.xlim(axes_min,axes_max)
        #   ax.ylim(axes_min,axes_max)

        # convert radii to radii in pixels
#        ax2 = fig.gca()
        ax2 = self.fig.gca()
        N = len(xvals)
        rr_pix = (ax2.transData.transform(np.vstack([rvals, rvals]).T) -
                    ax2.transData.transform(np.vstack([np.zeros(N), np.zeros(N)]).T))
        rpix, _ = rr_pix.T

#        markers_size = (144. * rpix / fig.dpi)**2   # = (2*rpix / fig.dpi * 72)**2
        markers_size = (144. * rpix / self.fig.dpi)**2   # = (2*rpix / fig.dpi * 72)**2
#        markers_size = (2*rpix / fig.dpi * 72)**2
        markers_size = markers_size/4000000.
        #print('markers_size.max()=',markers_size.max())

#        ax.scatter(xvals,yvals, s=rvals*self.scale_radius, c=rgbs)
#        axx.scatter(xvals,yvals, s=markers_size, c=rgbs)

#rwh - temp fix - Ah, error only occurs when "edges" is toggled on
        if (self.show_edge):
            plt.scatter(xvals,yvals, s=markers_size, c=rgbs, edgecolor='black', linewidth=0.5)
        else:
            plt.scatter(xvals,yvals, s=markers_size, c=rgbs)

        plt.xlim(self.axes_min, self.axes_max)
        plt.ylim(self.axes_min, self.axes_max)
        #   ax.grid(False)
#        axx.set_title(title_str)
        plt.title(title_str)

        # plt.close(fig)

# video-style widget - perhaps for future use
# svg_play = widgets.Play(
#     interval=1,
#     value=50,
#     min=0,
#     max=100,
#     step=1,
#     description="Press play",
#     disabled=False,
# )
# def svg_slider_change(change):
#     print('svg_slider_change: type(change)=',type(change),change.new)
#     plot_svg(change.new)
    
#svg_play
# svg_slider = widgets.IntSlider()
# svg_slider.observe(svg_slider_change, names='value')

# widgets.jslink((svg_play, 'value'), (svg_slider,'value')) #  (svg_slider, 'value'), (plot_svg, 'value'))

# svg_slider = widgets.IntSlider()
# widgets.jslink((play, 'value'), (slider, 'value'))
# widgets.HBox([svg_play, svg_slider])

# Using the following generates a new mpl plot; it doesn't use the existing plot!
#svg_anim = widgets.HBox([svg_play, svg_slider])

#svg_tab = widgets.VBox([svg_dir, svg_plot, svg_anim], layout=tab_layout)

#svg_tab = widgets.VBox([svg_dir, svg_anim], layout=tab_layout)
#---------------------
