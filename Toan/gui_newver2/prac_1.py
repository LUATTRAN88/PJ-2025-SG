from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PAGE1:
    def __init__(self):
        pass
    def create_layout(self,l1):
        self.layout = Frame(l1,bg='#C1CDCD',width=161,height=415)
        self.layout.place(x=477,y=64)
        
        self.layout1 = Frame(l1,bg='#C1CDCD',width=475,height=303)
        self.layout1.place(x=2,y=65)

        self.layout2 = Frame(l1,bg='#C1CDCD',width=475,height=149)
        self.layout2.place(x=2,y=329)

        self.create_label()
        self.button_stop()
        self.chart(self.layout1)

    def create_label(self):
        hel1 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.label1 = Label(self.layout,bg='#303030',font=hel1,text='Điện áp trung bình',fg='white').place(x=0,y=0,width=161,height=37)   
        self.label2 = Label(self.layout,bg='#303030',font=hel1,text='Dòng trung bình',fg='white').place(x=0,y=38,width=161,height=37)   
        self.label3 = Label(self.layout,bg='#303030',font=hel1,text='Ampe',fg='white').place(x=0,y=76,width=161,height=37)   
        self.label4 = Label(self.layout,bg='#303030',font=hel1,text='Tần số',fg='white').place(x=0,y=114,width=161,height=37) 
        self.label5 = Label(self.layout,bg='#303030',font=hel1,fg='white').place(x=0,y=152,width=161,height=37) 
        self.label6 = Label(self.layout,bg='#303030',font=hel1,fg='white').place(x=0,y=190,width=161,height=37) 
        self.label7 = Label(self.layout,bg='#303030',font=hel1,fg='white').place(x=0,y=228,width=161,height=37) 
        self.label8 = Label(self.layout,bg='#303030',font=hel1,text='Emergency',fg='white').place(x=0,y=266,width=161,height=37) 

    def button_stop(self):
        photos = Image.open('stop.png')
        self.pics = ImageTk.PhotoImage(photos)
        self.stop = Button(self.layout,bg='#C1CDCD',bd=4,image=self.pics).place(x=0,y=306,width=161,height=109)

    def chart(self,layout1):
        data = { 'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3] }  
        dataframe = pd.DataFrame(data)

        figure = plt.Figure(figsize=(4.77, 4), dpi=100)
        figure_plot = figure.add_subplot(2, 1, 1)
        figure_plot.set_ylabel('Unemployment Rate')
        
        line = FigureCanvasTkAgg(figure, layout1)
        line.get_tk_widget().pack(side=LEFT, fill=BOTH)
    
        dataframe = dataframe[['year', 'unemployment_rate']].groupby('year').sum()
        dataframe.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)
        figure_plot.set_title('Year Vs. Unemployment Rate')

    
