from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

class PAGE3:
    def __init__(self):
        self.is_on = False
    def create_layout(self,l1):
        self.layout3 = Frame(l1,bg='#C1CDCD')
        self.layout3.place(x=0,y=64,width=512,height=704)

        self.layout4 = Frame(l1,bg='#C1CDCD')
        self.layout4.place(x=512,y=64,width=512,height=704)

        # layout5 chứa class SIGNAL
        self.layout5 = Frame(self.layout3,bg='#C1CDCD')
        self.layout5.place(x=0,y=540,width=512,height=160)

        # self.label_power_set()
        self.tab_button()
        self.label_power()
        self.alarm_setting()

        #   Mảng chứa các đối tượng SIGNAL
        self.signal_objects = []
        # Khoảng cách giữa các đối tượng SIGNAL / Chiều rộng mỗi khung là 28, cộng thêm khoảng cách 10 pixel giữa chúng/ spacing = 38  (là khoảng cách giữa các đối tượng) 

        #Tạo và sắp xếp 16 đối tượng SIGNAL
        for i in range(16):
            signal = SIGNAL()
            signal.create_layout(self.layout5, x_offset=i * 32.2, text ='RL' + str(i+1) )
            
            if i==12:
                signal.set_relay_value('Fan')
            elif i==13:
                signal.set_relay_value('Alrm')
            elif i==14:
                signal.set_relay_value('Spar')
            elif i==15:
                signal.set_relay_value('Spar')
            else:
                signal.set_relay_value('20.0')

            self.signal_objects.append(signal)

            self.button_fan()


    def alarm_setting(self):
        self.photoa = Image.open('alarm_setting.png').resize((210,50))
        self.pica = ImageTk.PhotoImage(self.photoa)
        self.lb_alarm_setting = Label(self.layout3,bg='#C1CDCD',image=self.pica).place(x=30,y=20,width=200,height=40)
        
        font = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD )
        self.lb_power_limit = Label(self.layout3,bg='#C1CDCD',font=font,text='POWER LIMIT (KW):').place(x=30,y=65,width=170,height=35)
        self.lb_power_data = Label(self.layout3,bg='#C1CDCD',font=font,text='120').place(x=190,y=65,width=40,height=35)

        self.lb_voltage = Label(self.layout3,bg='#C1CDCD',font=font,text='VOLTAGE L-N LIMIT (V):').place(x=30,y=105,width=200,height=35)
        self.lb_voltage_data = Label(self.layout3,bg='#C1CDCD',font=font,text='250').place(x=221,y=105,width=40,height=35)

        self.lb_temperature = Label(self.layout3,bg='#C1CDCD',font=font,text='TEMPERATURE LIMIT (C):').place(x=30,y=145,width=210,height=35)
        self.lb_temp_data = Label(self.layout3,bg='#C1CDCD',font=font,text='80').place(x=235,y=145,width=40,height=35)



    def tab_button(self):
        fontb = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD )
        self.btn_logging = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='SAVE',fg='#8B2252').place(x=0,y=470,width=170,height=65)

    def label_power(self):
        fontrun = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_running = Label(self.layout4,bg='#C1CDCD',font=fontrun,text='Running',fg='black').place(x=412,y=0,width=100,height=40)

        self.photola = Image.open('lamp.png')
        self.picla = ImageTk.PhotoImage(self.photola)
        self.lb_lamp_run = Label(self.layout4,bg='#C1CDCD',image=self.picla).place(x=378,y=2,width=40,height=40)

        fontt = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_temp = Label(self.layout4,bg='#C1CDCD',font=fontt,text='35.2 ºC',fg='black').place(x=410,y=31,width=100,height=40)
        
        # label logo
        fonlogo = tkFont.Font(family='Helvetica', size=50, weight=tkFont.BOLD )
        self.label_logo = Label(self.layout4, bg='#C1CDCD',text='LOGO',font=fonlogo,fg='black').place(x=220, y=458,width=270,height=170)
   
    
    def button_fan(self):
        a1 = Image.open('fan_on.png').resize((170,170))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('fan_off.png').resize((170,170))
        self.off = ImageTk.PhotoImage(a2)

        self.btn_on = Button(self.layout4,image=self.on,bg='#C1CDCD', bd=0,command=lambda:self.button_fan())
        self.btn_on.place(x=30,y=460,width=170,height=170)

        if self.is_on:
            self.btn_on.config(image=self.off)
            self.is_on = False 
        else:
            self.btn_on.config(image=self.on)
            self.is_on = True


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
        self.relay_text_value = StringVar()
        self.lb_relay_val = Label(self.layout, bg='#C1CDCD',font=fontreva,text='20.2',fg='black',textvariable=self.relay_text_value).place(x=0,y=71.4,width=28,height=33)

    def set_relay_value(self,text):
        self.relay_text_value.set(text)
        pass


