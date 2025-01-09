from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from tkinter import ttk

class PAGE3:
    def __init__(self):
        pass
    def create_layout(self,l3):
        self.layout = Frame(l3, bg='#C1CDCD')
        self.layout.place(x=2,y=65,width=636,height=415)

        self.layout1 = Frame(l3, bg='#C1CDCD')
        self.layout1.place(x=2,y=65,width=475,height=413)

        self.layout2 = Frame(l3, bg='#C1CDCD')
        self.layout2.place(x=478,y=65,width=160,height=413)

        self.create_label()
        self.button_stop()
        self.Progressbar()

    def create_label(self):
        hel1 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.label1 =Label(self.layout2,bg='#303030',font=hel1,fg='white').place(x=0, y=0,width=160,height=37)
        self.label2 = Label(self.layout2,bg='#303030',font=hel1).place(x=0,y=38,width=160,height=37)   
        self.label3 = Label(self.layout2,bg='#303030',font=hel1).place(x=0,y=76,width=160,height=37)   
        self.label4 = Label(self.layout2,bg='#303030',font=hel1).place(x=0,y=114,width=160,height=37) 
        self.label5 = Label(self.layout2,bg='#303030',font=hel1).place(x=0,y=152,width=160,height=37) 
        self.label6 = Label(self.layout2,bg='#303030',font=hel1).place(x=0,y=190,width=160,height=37) 
        self.label7 = Label(self.layout2,bg='#303030',font=hel1).place(x=0,y=228,width=160,height=37) 
        self.label8 = Label(self.layout2,bg='#303030',font=hel1,text='Emergency',fg='white').place(x=0,y=266,width=161,height=37) 

    def button_stop(self):
        photos = Image.open('stop.png')
        self.pics = ImageTk.PhotoImage(photos)
        self.stop = Button(self.layout2,bg='#C1CDCD',bd=4,image=self.pics).place(x=0,y=305,width=160,height=109)

    def Progressbar(self):
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar")
        hel1 = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD )
        self.name1 = Label(self.layout1, bg='#C1CDCD', width=5,height=2, text='Vol',font=hel1,fg='#FF6103').place(x=25,y=43)
        self.name2 = Label(self.layout1, bg='#C1CDCD', width=5,height=2, text='Ampe',font=hel1,fg='#FF6103').place(x=187,y=43)
        self.name3 = Label(self.layout1, bg='#C1CDCD', width=7,height=2, text='Setpoint',font=hel1,fg='#FF6103').place(x=334,y=43)
      
        self.scale1 = Scale(self.layout1, from_=0, to=100, orient='vertical',length=200,bg='#C1CDCD').place(x=41, y=100)
        self.scale2 = Scale(self.layout1, from_=0, to=100, orient='vertical',length=200,bg='#C1CDCD').place(x=201, y=100)
        self.scale3 = Scale(self.layout1, from_=0, to=100, orient='vertical',length=200,bg='#C1CDCD').place(x=361, y=100)