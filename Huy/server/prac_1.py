from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
import threading

class PAGE1:
    def __init__(self):
        self.running = True
        self.is_on = True
    def create_layout(self,l1):
        
        self.layout = Frame(l1,bg='#C1CDCD',width=161,height=415)
        self.layout.place(x=477,y=64)
        
        self.layout1 = Frame(l1,bg='#C1CDCD',width=475,height=303)
        self.layout1.place(x=2,y=65)

        self.layout2 = Frame(l1,bg='#C1CDCD',width=475,height=108)
        self.layout2.place(x=2,y=369)

        self.create_label()
        # self.button_stop()
        # self.button_play()
        self.chart(self.layout1)
        self.button_power()
        self.button_parameter()

    def create_label(self):
        hel1 = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD )
        self.label1_text = StringVar()
        self.label1 = Label(self.layout,bg='#303030',font=hel1,text='Điện áp trung bình',fg='white',textvariable=self.label1_text).place(x=0,y=0,width=161,height=37)   
        self.label2_text = StringVar()
        self.label2 = Label(self.layout,bg='#303030',font=hel1,text='Dòng trung bình',fg='white',textvariable=self.label2_text).place(x=0,y=38,width=161,height=37)   
        self.label3 = Label(self.layout,bg='#303030',font=hel1,text='Ampe',fg='white').place(x=0,y=76,width=161,height=37)   
        self.label4 = Label(self.layout,bg='#303030',font=hel1,text='Tần số',fg='white').place(x=0,y=114,width=161,height=37) 
        self.label5 = Label(self.layout,bg='#303030',font=hel1,fg='white').place(x=0,y=152,width=161,height=37) 
        self.label6 = Label(self.layout,bg='#303030',font=hel1,fg='white').place(x=0,y=190,width=161,height=37) 
        self.label7 = Label(self.layout,bg='#303030',font=hel1,fg='white').place(x=0,y=228,width=161,height=37) 
        self.label8 = Label(self.layout,bg='#303030',font=hel1,text='Emergency',fg='white').place(x=0,y=266,width=161,height=37) 

    # def button_stop(self):
    #     photos = Image.open('stop.png')
    #     self.pics = ImageTk.PhotoImage(photos)
    #     self.stop = Button(self.layout,bg='#C1CDCD',bd=4,image=self.pics).place(x=0,y=306,width=161,height=109)
    # def button_play(self):
    #     photop = Image.open('play.png')
    #     self.picp = ImageTk.PhotoImage(photop)
    #     self.play = Button(self.layout,bg='#C1CDCD',bd=4,image=self.picp,command=lambda:self.start_chart()).place(x=0,y=360,width=161,height=54)

        
    # def button_stop(self):
    #     if(self.onoff==1):
    #         self.onoff=0;
    #         photos = Image.open('pause.png')
    #         self.pics = ImageTk.PhotoImage(photos)
    #         self.stop = Button(self.layout,bg='#C1CDCD',bd=4,image=self.pics,command=lambda:self.stop_chart()).place(x=0,y=306,width=161,height=54)
    #     else:
    #         self.onoff=1;
    #         photos = Image.open('play.png')
    #         self.pics = ImageTk.PhotoImage(photos)
    #         self.stop = Button(self.layout,bg='#C1CDCD',bd=4,image=self.pics,command=lambda:self.stop_chart()).place(x=0,y=306,width=161,height=54)

    def button_power(self):
        a1 = Image.open('play.png')
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('pause.png')
        self.off = ImageTk.PhotoImage(a2)

        self.button_on = Button(self.layout,image=self.on,bg='#66CDAA', bd=3,command= self.button_power)
        self.button_on.place(x=0,y=305,width=161,height=109)

        if self.is_on:
            self.button_on.config(image=self.on)
            self.stop_chart()
            self.is_on = False 
        else:
            self.button_on.config(image=self.off)
            self.start_chart()
            self.is_on = True

    
    def chart(self,layout1):
        # def chart(self,layout1):
        self.fig, self.ax = plt.subplots(figsize=(4.77, 3.04), dpi=100)
        self.ax.set_title("Real-Time Data Chart")
        # self.ax.set_xlabel("Time (seconds)")
        self.ax.set_ylabel("Random Values")
        self.x_data, self.y_data = [], []

        self.canvas = FigureCanvasTkAgg(self.fig, master=layout1)
        self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
        
        threading.Thread(target=self.update_chart, daemon=True).start()
        
    def update_chart(self):
        counter = 0
        while self.running:
            counter += 1
            self.x_data.append(counter)
            self.y_data.append(random.randint(0, 100))

            self.ax.clear()
            self.ax.plot(self.x_data, self.y_data, color='blue', marker='o')
            self.ax.set_title("Real-Time Data Chart")
            # self.ax.set_xlabel("Time (seconds)")
            self.ax.set_ylabel("Random Values")
            self.label1_text.set('điện áp: '+str(random.randint(0, 100)) + ' V')
            self.label2_text.set('Dòng:  ' + str(counter)+' A')
            self.canvas.draw()
     
            time.sleep(0.3)
            
    def start_chart(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.update_chart, daemon=True).start()  

    def stop_chart(self):
        self.running = False
        
    
    def button_parameter(self):
        help = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD )
        self.button1 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='V1N').place(x=1,y=0,width=119,height=54)
        self.button2 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='V2N').place(x=120,y=0,width=118,height=54)
        self.button3 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='V3N').place(x=238,y=0,width=118,height=54)
        self.button4 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='VLN').place(x=357,y=0,width=119,height=54)

        self.button5 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='L1').place(x=0,y=55,width=95,height=55)
        self.button6 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='L2').place(x=95,y=55,width=95,height=55)
        self.button7 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='L3').place(x=190,y=55,width=95,height=55)
        self.button8 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='AVI').place(x=285,y=55,width=95,height=55)
        self.button9 = Button(self.layout2,bg='#66CDAA',fg='#27408B',bd=3,font=help,text='Feq').place(x=380,y=55,width=95,height=55)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # data = { 'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
        #         'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3] }  
        # dataframe = pd.DataFrame(data)

        # figure = plt.Figure(figsize=(4.77, 4), dpi=100)
        # figure_plot = figure.add_subplot(2, 1, 1)
        # figure_plot.set_ylabel('Unemployment Rate')
        
        # line = FigureCanvasTkAgg(figure, layout1)
        # line.get_tk_widget().pack(side=LEFT, fill=BOTH)
    
        # dataframe = dataframe[['year', 'unemployment_rate']].groupby('year').sum()
        # dataframe.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)
        # figure_plot.set_title('Year Vs. Unemployment Rate')

    
