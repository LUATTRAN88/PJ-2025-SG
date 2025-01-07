from tkinter import *
from PIL import ImageTk, Image
from tkinter import font as tkFont
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from page_2 import *

class PAGE1:
    def __init__(self):
        pass
    def create_layout(self,l1):
        self.layout3 = Frame(l1, bg='#DCDCDC',width=200,height=417)
        self.layout3.place(x=438,y=61)
        # self.layout4 = Frame(l1, bg='yellow',width=438,height=360)
        self.layout4 = Frame(l1, bg='yellow',width=436,height=254)
        self.layout4.place(x=2,y=61)
        
        self.layout5 = Frame(l1, bg='#A6A6A6',width=436,height=162)
        self.layout5.place(x=2,y=316)
       
       
        self.create_label(self.layout3)
        self.chart(self.layout4)
        self.button_stop(self.layout3)

    def hide(self):
        self.layout3.pack();
        self.layout4.pack();
    def show(self):
        self.layout3.pack_forget();
        self.layout4.pack_forget();
    


    def create_label(self, layout3):
        hel1 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label1 = Label(layout3, bg='#303030',text='Test Values',font=hel1,fg='white')
        label1.place(x=0,y=0,width=200,height=37)

        helv367 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label2 = Label(layout3, bg='#A6A6A6',fg='white',font=helv367)
        label2.place(x=0, y=38,width=200,height=37)
    
        helv366 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label8 = Label(layout3, bg='#303030',text='Emergency',font=helv366,fg='white')
        label8.place(x=0, y=266,width=200,height=37)
        
        helv_font = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label3 = Label(layout3, bg='#A6A6A6',font=helv_font)
        label3.place(x=0, y=76,width=200,height=37)
            
        label4 = Label(layout3, bg='#A6A6A6',font=helv_font)
        label4.place(x=0, y=114,width=200,height=37)
            
        label5 = Label(layout3, bg='#A6A6A6',font=helv_font)
        label5.place(x=0, y=152,width=200,height=37)

        label6 = Label(layout3, bg='#A6A6A6',font=helv_font)
        label6.place(x=0, y=190,width=200,height=37)
            
        label7 = Label(layout3, bg='#A6A6A6',font=helv_font)
        label7.place(x=0, y=228,width=200,height=37)
               
    def button_stop(self,layout3):
        photo = Image.open('stop.png');
        resize = photo.resize((125,130));
        self.pic = ImageTk.PhotoImage(resize);
        self.stop = Button(layout3,bg='#A6A6A6',image=self.pic,bd=3).place(x=0, y=304,width=200,height=113)
            
    def chart(self,layout4):

        data = { 'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3] }  
        dataframe = pd.DataFrame(data)

        figure = plt.Figure(figsize=(4.36, 4.13), dpi=100)
        figure_plot = figure.add_subplot(2, 1, 1)
        figure_plot.set_ylabel('Unemployment Rate')
        
        line = FigureCanvasTkAgg(figure, layout4)
        line.get_tk_widget().pack(side=LEFT, fill=BOTH)
    
        dataframe = dataframe[['year', 'unemployment_rate']].groupby('year').sum()
        dataframe.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)
        figure_plot.set_title('Year Vs. Unemployment Rate')
        
        
        
        # figure = plt.Figure(figsize=(4.36, 4.17), dpi=100)   dòng 85