from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont

class PAGE3:
    def __init__(self):
        pass
    def create_layout(self,l4):
        self.layout = Frame(l4, bg='#C1CDCD',width=640,height=420 )
        self.layout.place(x=0,y=61)
        
        self.layout1 = Frame(l4, bg='#C1CDCD',width=438,height=417 )
        self.layout1.place(x=0,y=61)
        
        self.layout2 = Frame(l4, bg='#C1CDCD',width=200,height=417 )
        self.layout2.place(x=438,y=61)
        
        self.Progressbar()
        self.create_label()
        
    def Progressbar(self):
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar")
        hel1 = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD )
        self.name1 = Label(self.layout1, bg='#C1CDCD', width=5,height=2, text='Vol',font=hel1,fg='#FF6103').place(x=5,y=46)
        self.name2 = Label(self.layout1, bg='#C1CDCD', width=5,height=2, text='Ampe',font=hel1,fg='#FF6103').place(x=167,y=46)
        self.name3 = Label(self.layout1, bg='#C1CDCD', width=7,height=2, text='Setpoint',font=hel1,fg='#FF6103').place(x=313,y=46)
      
        self.scale1 = Scale(self.layout1, from_=0, to=100, orient='vertical',length=200,bg='#C1CDCD').place(x=21, y=100)
        self.scale2 = Scale(self.layout1, from_=0, to=100, orient='vertical',length=200,bg='#C1CDCD').place(x=181, y=100)
        self.scale3 = Scale(self.layout1, from_=0, to=100, orient='vertical',length=200,bg='#C1CDCD').place(x=341, y=100)
       
    def create_label(self):
        hel1 = tkFont.Font(family='Helvetica', size=21, weight=tkFont.BOLD )
        label1 = Label(self.layout2, bg='#303030',text='....',font=hel1,fg='white')
        label1.place(x=0,y=0,width=200,height=37)

        helv367 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label2 = Label(self.layout2, bg='#303030',text='Test Values',fg='white',font=helv367)
        label2.place(x=0, y=38,width=200,height=37)
    
        helv366 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label8 = Label(self.layout2, bg='#303030',text='Limits [Warn/Stop]',font=helv366,fg='white')
        label8.place(x=0, y=266,width=200,height=37)
        ########################   
    
        helv_font = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        label3 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label3.place(x=0, y=76,width=200,height=37)
            
        label4 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label4.place(x=0, y=114,width=200,height=37)
            
        label5 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label5.place(x=0, y=152,width=200,height=37)

        label6 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label6.place(x=0, y=190,width=200,height=37)
            
        label7 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label7.place(x=0, y=228,width=200,height=37)
            
        label9 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label9.place(x=0, y=304,width=200,height=37)
            
        label10 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label10.place(x=0, y=342,width=200,height=37)
            
        label11 = Label(self.layout2, bg='#A6A6A6',font=helv_font)
        label11.place(x=0, y=380,width=200,height=37)
        