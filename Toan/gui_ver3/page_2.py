from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

class PAGE2:
    def __init__(self):
        self.is_on = False
        # self.lamp_on = False
    def create_layout(self,l1):
        self.layout3 = Frame(l1,bg='#C1CDCD')
        self.layout3.place(x=0,y=64,width=512,height=704)

        self.layout4 = Frame(l1,bg='#C1CDCD')
        self.layout4.place(x=512,y=64,width=512,height=704)

        # layout5 chứa class SIGNAL
        self.layout5 = Frame(self.layout3,bg='#C1CDCD')
        self.layout5.place(x=0,y=540,width=512,height=160)

        # layout6 chứa class SIGNAL_POWER
        self.layout6 = Frame(self.layout3, bg='#C1CDCD')
        self.layout6.place(x=0,y=83,width=512,height=289)

        self.label_power_set()
        self.tab_button()
        self.label_power()

        # self.display_signal = SIGNAL_POWER()
        # self.display_signal.create_layout(self.layout6)
        

        

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

        # self.display_signal = SIGNAL_POWER()
        # self.display_signal.create_layout(self.layout6)

        self.relay_power_objects = []

        for t in range(12):
            row = t // 6  # Xác định hàng
            col = t % 6   # Xác định cột
            space_x = col * 85.333  # Khoảng cách theo cột
            space_y = row * 150     # Khoảng cách theo hàng (tăng y để không chồng nhau)

            signal_repo = SIGNAL_POWER()
            signal_repo.create_layout(self.layout6, x=space_x,y=space_y, text ='RL' + str(t+1) )
            self.relay_power_objects.append(signal_repo)
        

    def label_power_set(self):
        fontps = tkFont.Font(family='Helvetica', size=37, weight=tkFont.BOLD )
        self.lb_power_set = Label(self.layout3,bg='#C1CDCD',font=fontps,text='POWER SET (KW)',fg='#00CD00').place(x=10,y=18,width=500,height=62)

    def tab_button(self):
        fontb = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.btn_apply = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD APPLY',fg='#8B2252').place(x=0,y=375,width=170,height=65)
        self.btn_stop = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD STOP',fg='#8B2252').place(x=171,y=375,width=170,height=65)
        self.btn_drop = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD DROP',fg='#8B2252').place(x=342,y=375,width=170,height=65)
        self.btn_logging = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD LOGGING',fg='#8B2252').place(x=0,y=470,width=170,height=65)

    def label_power(self):
        fontrun = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_running = Label(self.layout4,bg='#C1CDCD',font=fontrun,text='Running',fg='black').place(x=412,y=0,width=100,height=40)

        self.photola = Image.open('lamp.png')
        self.picla = ImageTk.PhotoImage(self.photola)
        self.lb_lamp_run = Label(self.layout4,bg='#C1CDCD',image=self.picla).place(x=378,y=2,width=40,height=40)

        fontpo = tkFont.Font(family='Helvetica', size=42, weight=tkFont.BOLD )
        self.lb_power = Label(self.layout4,bg='#C1CDCD',font=fontpo,text='POWER',fg='red').place(x=24,y=59,width=220,height=75)
        self.lb_power_val = Label(self.layout4,bg='#C1CDCD',font=fontpo,text='58.1 KW',fg='red').place(x=246,y=59,width=265,height=75)

        fontt = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_temp = Label(self.layout4,bg='#C1CDCD',font=fontt,text='35.2 ºC',fg='black').place(x=410,y=31,width=100,height=40)
        
        # hàng đàu tiên, hàng đơn vị
        fontri = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD )
        self.lb_pow = Label(self.layout4,bg='#C1CDCD',font=fontri,text='POWER\n KW',fg='black').place(x=65, y=150,width=70,height=50)
        self.lb_volt_ln = Label(self.layout4,bg='#C1CDCD',font=fontri,text='VOLT.\n L-N (V)',fg='black').place(x=136, y=150,width=70,height=50)
        self.lb_current = Label(self.layout4,bg='#C1CDCD',font=fontri,text='CURRENT\n (A)',fg='black').place(x=209, y=150,width=70,height=50)
        self.lb_pf = Label(self.layout4,bg='#C1CDCD',font=fontri,text='PF',fg='black').place(x=280, y=150,width=70,height=50)
        self.lb_none = Label(self.layout4,bg='#C1CDCD').place(x=355, y=150,width=70,height=50)
        self.lb_volt_ll = Label(self.layout4,bg='#C1CDCD',font=fontri,text='VOLT.\n L-L (V)',fg='black').place(x=428, y=150,width=70,height=50)

        # các đường line
        self.lb_line1 = Label(self.layout4,bg='black').place(x=135, y=150,width=1,height=210)
        self.lb_line2 = Label(self.layout4,bg='black').place(x=207, y=150,width=1,height=210)
        self.lb_line3 = Label(self.layout4,bg='black').place(x=280, y=150,width=1,height=210)
        self.lb_line4 = Label(self.layout4,bg='black').place(x=351, y=150,width=1,height=210)
        self.lb_line5 = Label(self.layout4,bg='black').place(x=426, y=150,width=1,height=210)
        self.lb_line6 = Label(self.layout4,bg='black').place(x=499, y=150,width=1,height=210)
        self.lb_line7 = Label(self.layout4,bg='black').place(x=65, y=150,width=1,height=210)
        self.lb_line8 = Label(self.layout4,bg='black').place(x=20, y=150,width=1,height=210)
        self.lb_line9n = Label(self.layout4,bg='black').place(x=20, y=150,width=479,height=1)
        self.lb_line10n = Label(self.layout4,bg='black').place(x=20, y=200,width=479,height=1)
        self.lb_line11n = Label(self.layout4,bg='black').place(x=20, y=240,width=479,height=1)
        self.lb_line12n = Label(self.layout4,bg='black').place(x=20, y=280,width=479,height=1)
        self.lb_line13n = Label(self.layout4,bg='black').place(x=20, y=320,width=479,height=1)
        self.lb_line14n = Label(self.layout4,bg='black').place(x=20, y=360,width=479,height=1)

          # hàng L1
        fonl1 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.lb_L1 = Label(self.layout4,bg='#C1CDCD',font=fonl1,text='L1',fg='red').place(x=22,y=201,width=43,height=39)
        self.lb_L1_none = Label(self.layout4,bg='#C1CDCD',font=fonl1,text='L1 - L2',fg='red').place(x=353,y=201,width=72,height=39)

        fonl1t = tkFont.Font(family='Helvetica', size=12 )
        self.lb_L1_power = Label(self.layout4,bg='#C1CDCD',font=fonl1t,text='19.5',fg='red').place(x=66,y=201,width=69,height=39)
        self.lb_L1_volt_Ln = Label(self.layout4,bg='#C1CDCD',font=fonl1t,text='231.8',fg='red').place(x=137,y=201,width=69,height=39)
        self.lb_L1_volt_cur = Label(self.layout4,bg='#C1CDCD',font=fonl1t,text='28.0',fg='red').place(x=209,y=201,width=70,height=39)
        self.lb_L1_volt_pf = Label(self.layout4,bg='#C1CDCD',font=fonl1t,text='0.99',fg='red').place(x=281,y=201,width=70,height=39)
        self.lb_L1_volt_ll = Label(self.layout4,bg='#C1CDCD',font=fonl1t,text='401.5',fg='red').place(x=427,y=201,width=71,height=39)

        # hàng L2
        fonl2 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.lb_L2 = Label(self.layout4,bg='#C1CDCD',font=fonl2,text='L2',fg='orange').place(x=21,y=241,width=44,height=39)
        self.lb_L2_none = Label(self.layout4,bg='#C1CDCD',font=fonl2,text='L2 - L3',fg='orange').place(x=353,y=241,width=72,height=39)

        fonl2t = tkFont.Font(family='Helvetica', size=12)
        self.lb_L2_power = Label(self.layout4,bg='#C1CDCD',font=fonl2t,text='19.2',fg='orange').place(x=66,y=241,width=69,height=39)
        self.lb_L2_volt_ln = Label(self.layout4,bg='#C1CDCD',font=fonl2t,text='232.1',fg='orange').place(x=137,y=241,width=69,height=39)
        self.lb_L2_cur = Label(self.layout4,bg='#C1CDCD',font=fonl2t,text='27.6',fg='orange').place(x=209,y=241,width=70,height=39)
        self.lb_L2_pf = Label(self.layout4,bg='#C1CDCD',font=fonl2t,text='0.98',fg='orange').place(x=282,y=241,width=68,height=39)
        self.lb_L2_volt_ll = Label(self.layout4,bg='#C1CDCD',font=fonl2t,text='402.0',fg='orange').place(x=427,y=241,width=72,height=39)

        # hàng L3  
        fonl3 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.lb_L3 = Label(self.layout4,bg='#C1CDCD',font=fonl3,text='L3',fg='blue').place(x=21,y=281,width=44,height=39)
        self.lb_L3_volt_none = Label(self.layout4,bg='#C1CDCD',font=fonl3,text='L3 - L1',fg='blue').place(x=353,y=281,width=72,height=39)

        fonl3t = tkFont.Font(family='Helvetica', size=12 )
        self.lb_L3_power = Label(self.layout4,bg='#C1CDCD',font=fonl3t,text='19.4',fg='blue').place(x=66,y=281,width=69,height=39)
        self.lb_L3_volt_ln = Label(self.layout4,bg='#C1CDCD',font=fonl3t,text='232.7',fg='blue').place(x=137,y=281,width=69,height=39)
        self.lb_L3_volt_cur = Label(self.layout4,bg='#C1CDCD',font=fonl3t,text='27.8',fg='blue').place(x=209,y=281,width=70,height=39)
        self.lb_L3_volt_pf = Label(self.layout4,bg='#C1CDCD',font=fonl3t,text='1.0',fg='blue').place(x=282,y=281,width=68,height=39)
        self.lb_L3_volt_ll = Label(self.layout4,bg='#C1CDCD',font=fonl3t,text='403.1',fg='blue').place(x=427,y=281,width=72,height=39)

        
        # hàng FREQ
        fonl4 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD )
        self.lb_freq = Label(self.layout4,bg='#C1CDCD',font=fonl4,text='FREQ.',fg='black').place(x=21,y=321,width=44,height=39)
        self.lb_freq_cur = Label(self.layout4,bg='#C1CDCD',font=fonl4,text='TEMP.',fg='black').place(x=209,y=321,width=70,height=39)

        fonl4t = tkFont.Font(family='Helvetica', size=12 )
        self.lb_freq_pow_vol = Label(self.layout4,bg='#C1CDCD',font=fonl4t,text='50.2 Hz',fg='black').place(x=66,y=321,width=141,height=39)
        self.lb_freq_cur = Label(self.layout4,bg='#C1CDCD',font=fonl4t,text='35.2 ºC',fg='black').place(x=282,y=321,width=216,height=39)

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


class SIGNAL_POWER:
    def __init__(self):
        self.lamp_on = False
    def create_layout(self,layout6,text,x,y):
        self.layout = Frame(layout6,bg='#C1CDCD')
        self.layout.place(x=x,y=y,width=85,height=144)

        fonre = tkFont.Font(family='Helvetica', size=16)
        self.lb_relay1 = Label(self.layout,bg='#C1CDCD',font=fonre,text=text).place(x=13,y=9,width=55,height=34)
        
        self.lamp_signal_relay()

    def lamp_signal_relay(self):
        a1 = Image.open('lamp_signal_on.png').resize((70,70))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('lamp_signal_off.png').resize((70,70))
        self.off = ImageTk.PhotoImage(a2)

        self.btn_on = Button(self.layout,image=self.on,bg='#C1CDCD', bd=0,command=lambda:self.lamp_signal_relay())
        self.btn_on.place(x=1,y=40,width=83,height=83)

        if self.lamp_on:
            self.btn_on.config(image=self.off)
            self.lamp_on = False 
        else:
            self.btn_on.config(image=self.on)
            self.lamp_on = True