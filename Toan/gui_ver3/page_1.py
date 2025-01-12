from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

class PAGE1:
    def __init__(self):
        pass
    def create_layout(self,l1):
        self.layout3 = Frame(l1,bg='#C1CDCD')
        self.layout3.place(x=0,y=64,width=512,height=536)

        self.layout4 = Frame(l1,bg='#C1CDCD')
        self.layout4.place(x=512,y=64,width=512,height=536)

        self.layout5 = Frame(self.layout3,bg='#C1CDCD')
        self.layout5.place(x=0,y=353,width=512,height=160)
        
        self.label_text()
        self.tab_button()
        # self.display = SIGNAL()
        # self.display.create_layout(self.layout5)

        #   Mảng chứa các đối tượng SIGNAL
        self.signal_objects = []
         # Khoảng cách giữa các đối tượng SIGNAL
        # Chiều rộng mỗi khung là 28, cộng thêm khoảng cách 10 pixel giữa chúng
        #   spacing = 38  (là khoảng cách giữa các đối tượng)

        #Tạo và sắp xếp 16 đối tượng SIGNAL
        for i in range(16):
            signal = SIGNAL()
            signal.create_layout(self.layout5, x_offset=i * 32.2, text ='RL' + str(i+1) )
            
            self.signal_objects.append(signal)
            


    def label_text(self):
        fontp = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD )
        self.lb_powset = Label(self.layout3,bg='#C1CDCD',font=fontp,text='POWER SET',fg='#2E8B57').place(x=20,y=20,width=200,height=100)
        self.lb_powset_val = Label(self.layout3,bg='#C1CDCD',font=fontp,text='57 KW',fg='#8B2252').place(x=240,y=20,width=157,height=100)

        self.lb_time = Label(self.layout3,bg='#C1CDCD',font=fontp,text='TIMER SET',fg='#2E8B57').place(x=20,y=150,width=200,height=100)
        self.lb_time_val = Label(self.layout3,bg='#C1CDCD',font=fontp,text='60 mins',fg='#8B2252').place(x=240,y=150,width=157,height=100)

        fontt = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_temp = Label(self.layout3,bg='#C1CDCD',font=fontt,text='35.2 C',fg='black').place(x=200,y=475,width=100,height=40)

        
        fontrun = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_running = Label(self.layout4,bg='#C1CDCD',font=fontrun,text='Running',fg='black').place(x=412,y=0,width=100,height=40)

        self.photola = Image.open('lamprun.png')
        self.picla = ImageTk.PhotoImage(self.photola)
        self.lb_lamp_run = Label(self.layout4,bg='#C1CDCD',image=self.picla).place(x=378,y=3,width=40,height=40)

        fontpo = tkFont.Font(family='Helvetica', size=31, weight=tkFont.BOLD )
        self.lb_power = Label(self.layout4,bg='#C1CDCD',font=fontpo,text='POWER',fg='RED').place(x=20,y=59,width=220,height=75)
        self.lb_power_val = Label(self.layout4,bg='#C1CDCD',font=fontpo,text='58.1 KW',fg='RED').place(x=242,y=59,width=265,height=75)

    def tab_button(self):
        self.photo1 = Image.open('up.png').resize((50,46))
        self.pic1 = ImageTk.PhotoImage(self.photo1)
        self.btn_powset_up = Button(self.layout3,bd=0, bg='#C1CDCD',image=self.pic1).place(x=427,y=20,width=50,height=46)

        self.photo2 = Image.open('down.png').resize((50,46))
        self.pic2 = ImageTk.PhotoImage(self.photo2)
        self.btn_powset_down = Button(self.layout3,bd=0, bg='#C1CDCD',image=self.pic2).place(x=427,y=75,width=50,height=46)

        self.photo3 = Image.open('up.png').resize((50,46))
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.btn_time_up = Button(self.layout3,bd=0,bg='#C1CDCD',image=self.pic3).place(x=427,y=150,width=50,height=46)

        self.photo4 = Image.open('down.png').resize((50,46))
        self.pic4 = ImageTk.PhotoImage(self.photo4)
        self.btn_time_down = Button(self.layout3,bd=0,bg='#C1CDCD',image=self.pic4).place(x=427,y=205,width=50,height=46)

        fontb = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.btn_apply = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD APPLY',fg='#8B2252').place(x=0,y=295,width=128,height=55)
        self.btn_stop = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD STOP',fg='#8B2252').place(x=128,y=295,width=128,height=55)
        self.btn_drop = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD DROP',fg='#8B2252').place(x=256,y=295,width=128,height=55)
        self.btn_logging = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD LOGGING',fg='#8B2252').place(x=384,y=295,width=128,height=55)

class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,layout5,text, x_offset=0):
        self.layout =  Frame(layout5,bg='#C1CDCD')
        self.layout.place(x=x_offset,y=13, width=28,height=114)

        self.photol = Image.open('lamp.png')
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout, bg='#C1CDCD',image=self.picl).place(x=1.5,y=38.4,width=24,height=38)

        fontr = tkFont.Font(family='Helvetica', size=8)
        self.lb_relay = Label(self.layout, bg='#C1CDCD',font=fontr,fg='black',text=text).place(x=0,y=7,width=28,height=33)

        fontreva = tkFont.Font(family='Helvetica', size=9)
        self.lb_relay_val = Label(self.layout, bg='#C1CDCD',font=fontreva,text='20.2',fg='black').place(x=0,y=71.4,width=28,height=33)









       