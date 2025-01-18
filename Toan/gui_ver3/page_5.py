from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from extend import *

class PAGE5:
    def __init__(self):
        self.is_on = False
    def create_layout(self,l5):
        self.layout3 = Frame(l5,bg='white')
        self.layout3.place(x=0,y=0,width=512,height=704)

        self.layout4 = Frame(l5,bg='white')
        self.layout4.place(x=512,y=0,width=512,height=704)

        # layout5 chứa class SIGNAL
        self.layout5 = Frame(self.layout3,bg='white')
        self.layout5.place(x=0,y=540,width=512,height=160)

        # self.label_power_set()
        self.tab_button()
        self.label_power()
        self.resistor()
        self.emergency()
        # self.alarm_setting()

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


   
    def tab_button(self):
        fontb = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD )
        self.btn_logging = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='SAVE',fg='#8B2252').place(x=30,y=470,width=170,height=65)

    def label_power(self):
        fontrun = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_running = Label(self.layout4,bg='white',font=fontrun,text='Running',fg='black').place(x=412,y=0,width=100,height=40)

        self.photola = Image.open(get_path_img()+'lamp.png')
        self.picla = ImageTk.PhotoImage(self.photola)
        self.lb_lamp_run = Label(self.layout4,bg='white',image=self.picla).place(x=378,y=2,width=40,height=40)

        fontt = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_temp = Label(self.layout4,bg='white',font=fontt,text='35.2 ºC',fg='black').place(x=410,y=31,width=100,height=40)
        
        # label logo
        fonlogo = tkFont.Font(family='Helvetica', size=50, weight=tkFont.BOLD )
        self.label_logo = Label(self.layout4, bg='white',text='LOGO',font=fonlogo,fg='black').place(x=220, y=458,width=270,height=170)
   
    
    def button_fan(self):
        a1 = Image.open(get_path_img()+'fan_on.png').resize((170,170))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open(get_path_img()+'fan_off.png').resize((170,170))
        self.off = ImageTk.PhotoImage(a2)

        self.btn_on = Button(self.layout4,image=self.on,bg='white', bd=0,command=lambda:self.button_fan())
        self.btn_on.place(x=30,y=460,width=170,height=170)

        if self.is_on:
            self.btn_on.config(image=self.off)
            self.is_on = False 
        else:
            self.btn_on.config(image=self.on)
            self.is_on = True

    def resistor(self):
        self.lb_resistors = Label(self.layout3,bg='white',font=('Arial Bold',18),text='RESISTOR SETUP (Ohms):',fg='red').place(x=30,y=80,width=310,height=23)
        self.lb_resistors_line = Label(self.layout3,bg='red').place(x=30,y=105,width=309,height=2)

        self.lb_r1 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R1:',fg='black').place(x=30,y=130,width=40,height=19)
        self.entry_r1 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=74,y=130,width=65,height=20)

        self.lb_r2 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R2:',fg='black').place(x=160,y=130,width=40,height=19)
        self.entry_r2 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=204,y=130,width=65,height=20)

        self.lb_r3 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R3:',fg='black').place(x=297,y=130,width=40,height=19)
        self.entry_r3 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=341,y=130,width=65,height=20)

        self.lb_line1 = Label(self.layout3,bg='black').place(x=33,y=148,width=479,height=2)
        self.lb_line2 = Label(self.layout3,bg='black').place(x=33,y=210,width=479,height=2)
        self.lb_line3 = Label(self.layout3,bg='black').place(x=33,y=271,width=479,height=2)

        self.lb_r4 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R4:',fg='black').place(x=30,y=191,width=40,height=19)
        self.entry_r4 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=74,y=190,width=65,height=20)

        self.lb_r5 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R5:',fg='black').place(x=160,y=191,width=40,height=19)
        self.entry_r5 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=204,y=190,width=65,height=20)

        self.lb_r6 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R6:',fg='black').place(x=297,y=191,width=40,height=19)
        self.entry_r6 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=341,y=190,width=65,height=20)

        self.lb_r7 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R7:',fg='black').place(x=30,y=252,width=40,height=19)
        self.entry_r7 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=74,y=251,width=65,height=20)

        self.lb_r8 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R8:',fg='black').place(x=160,y=252,width=40,height=19)
        self.entry_r8 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=204,y=251,width=65,height=20)

        self.lb_r9 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R9:',fg='black').place(x=297,y=252,width=40,height=19)
        self.entry_r9 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=341,y=251,width=65,height=20)

        self.lb_r10 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R10:',fg='black').place(x=32,y=313,width=48,height=19)
        self.entry_r10 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=84,y=313,width=65,height=21)

        self.lb_r11 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R11:',fg='black').place(x=162,y=313,width=48,height=19)
        self.entry_r11 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=214,y=313,width=65,height=21)

        self.lb_r12 = Label(self.layout3,bg='white',font=('Arial Bold',16),text='R12:',fg='black').place(x=299,y=313,width=48,height=19)
        self.entry_r12 = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=351,y=313,width=65,height=21)

        self.lb_res_thres = Label(self.layout3,bg='white',font=('Arial Bold',17),text='Resistor threshold (%):',fg='black').place(x=30,y=373,width=260,height=23)
        self.entry_res_thres = Entry(self.layout3,bg='#E0EEEE',font=('Arial Bold',17),fg='black').place(x=295,y=373,width=65,height=23)

    def emergency(self):
        self.lb_emergency = Label(self.layout4,bg='white',fg='red',font=('Arial Bold',18),text='EMERGENCY SETTING:').place(x=30,y=80,width=280,height=23)
        self.lb_emergency_line = Label(self.layout4,bg='red').place(x=32,y=105,width=273,height=2)

        self.lb_power = Label(self.layout4,bg='white',font=('Arial Bold',16),text='POWER LIMIT (KW):').place(x=30,y=130,width=210,height=20)
        self.entry_power = Entry(self.layout4,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=247,y=130,width=65,height=20)
        self.lb_power_line = Label(self.layout4,bg='black').place(x=0,y=148,width=420,height=2)

        self.lb_voltage = Label(self.layout4,bg='white',font=('Arial Bold',16),text='VOLTAGE L-N LIMIT (V):').place(x=30,y=191,width=250,height=20)
        self.entry_voltage = Entry(self.layout4,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=285,y=191,width=65,height=20)
        self.lb_voltage_line = Label(self.layout4,bg='black').place(x=0,y=210,width=420,height=2)

        self.lb_temperature = Label(self.layout4,bg='white',font=('Arial Bold',16),text='TEMPERATURE LIMIT (C):').place(x=30,y=252,width=259,height=20)
        self.entry_temperature = Entry(self.layout4,bg='#E0EEEE',font=('Arial Bold',16),fg='black').place(x=301,y=252,width=65,height=20)
        self.lb_temp_line = Label(self.layout4,bg='black').place(x=0,y=271,width=420,height=2)

class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,layout5,text, x_offset=0):
        self.layout =  Frame(layout5,bg='white')
        self.layout.place(x=x_offset,y=13, width=28,height=114)

        self.photol = Image.open(get_path_img()+'lamp.png')
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout, bg='white',image=self.picl).place(x=1.5,y=38.4,width=24,height=38)

        fontr = tkFont.Font(family='Helvetica', size=8)
        self.lb_relay = Label(self.layout, bg='white',font=fontr,fg='black',text=text).place(x=0,y=7,width=28,height=33)

        fontreva = tkFont.Font(family='Helvetica', size=9)
        self.relay_text_value = StringVar()
        self.lb_relay_val = Label(self.layout, bg='white',font=fontreva,text='20.2',fg='black',textvariable=self.relay_text_value).place(x=0,y=71.4,width=28,height=33)

    def set_relay_value(self,text):
        self.relay_text_value.set(text)
        pass


