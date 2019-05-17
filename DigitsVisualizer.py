
__author__ = "V. Robles-Bykbaev"
__copyright__ = "GI-IATa - Universidad Politecnica Salesiana"
__credits__ = ["V. Robles-Bykbaev"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "V. Robles-Bykbaev"
__email__ = "vrobles@ups.edu.ec"
__status__ = "Production"

import tkinter
from tkinter import ttk
from Utilities import Utilities


class DigitsVisualizer(tkinter.Frame):
    
    def __init__(self, path = './corpus/digits-database.data'):
        super().__init__()
        self.path = path
        self.utilities = Utilities()
        self.indices = self.utilities.generate_indices()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.initialize()
    
    def initialize(self):
        
        self.canvas = tkinter.Canvas(self, bg = 'white', width = self.WIDTH, height = self.HEIGHT)
        #self.canvas.pack()
        self.canvas.grid(row = 0, column = 0)
        
        self.master.title('Digits Visualizer')
        self.frame = tkinter.Frame(relief = tkinter.RAISED, borderwidth = 2)
        
        lblText = tkinter.Label(self.frame, text = 'Digits')
        lblText.grid(row = 0, column = 0)
        
        self.cbxData = ttk.Combobox(self.frame, values = [str(i) for i in self.indices])
        self.cbxData.grid(row = 0, column = 1)
        self.cbxData.bind('<<ComboboxSelected>>', self.cbx_selection)
        
        #self.frame.grid(row = 0, column = 1)
        self.frame.pack(fill = tkinter.BOTH, expand = True)
        
        self.pack(fill = tkinter.BOTH, expand = True)
        
        print(self.utilities.get_digit(21, 53))
        
        self.generate_grid()
        
    def generate_grid(self):
        self.canvas.delete('all')
        data = self.utilities.get_digit(self.indices[0][1],self.indices[0][2])
        cols = len(data[0])#.lstrip().rstrip())
        rows = len(data)
        print(cols,'===',rows)
        stepx = float(self.WIDTH)/float(cols)
        stepy = float(self.HEIGHT)/float(rows)
        countx = stepx
        county = stepy
        
        while county<float(self.HEIGHT):
            self.canvas.create_line(0.0,county,float(self.WIDTH),county)
            county+=stepy
        
        while countx<float(self.WIDTH):
            self.canvas.create_line(countx,0.0,countx,float(self.HEIGHT))
            countx+=stepx
            
        print(stepx,'@@@',stepy)
        
    def cbx_selection(self, evt):
        self.canvas.delete('all')
        #self.canvas.create_rectangle(30,30,120,120,outline='red',fill='red')
        print('GET: ',self.cbxData.get())
        _id = [int(i) for i in (str(self.cbxData.get()).replace(')','').replace(' ','').replace('(','')).split(',')]
        
        data = self.utilities.get_digit(_id[1],_id[2])
        cols = len(data[0])#.lstrip().rstrip())
        rows = len(data)
        print(cols,'===',rows)
        stepx = float(self.WIDTH)/float(cols)
        stepy = float(self.HEIGHT)/float(rows)
        
        countx = 0.0
        county = 0.0
        i = 0
        j = 0
        
        while county<float(self.HEIGHT):
            while countx<float(self.WIDTH):
                if data[i][j] == 1:
                    self.canvas.create_rectangle(countx,county,countx+stepx,county+stepy,outline='lavender',fill='lavender')
#                    print(countx,' ',(countx+stepx),' ',(county),' ',(county+stepy))
                else:
                    self.canvas.create_rectangle(countx,county,countx+stepx,county+stepy,outline='azure',fill='azure')
                j+=1
                countx+=stepx
            county+=stepy
            j=0
            i+=1
            countx = 0.0
        
    
if __name__=="__main__":
    root = tkinter.Tk()
    dv = DigitsVisualizer()
    root.mainloop()
    
