from ipywidgets import Output
from IPython.display import display, HTML

class AboutTab(object):

    def __init__(self):
        self.tab = Output(layout={'height': '350px'})  # Doesn't change the html window!
        # self.tab = Output(layout={'height': 'auto'})
        self.tab.append_display_data(HTML(filename='doc/about.html'))
        
