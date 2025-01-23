import tkinter as tk
from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
# import threading
# from time import sleep
# import client as clientCall
# import json
from extend import *

class PAGE2:
    def __init__(self):
        self.origin_data = None
        self.is_on = False
        self.is_test = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
    def create_layout(self,lay2):
        self.layout1 = Frame(lay2,bg='white')                   
        self.layout1.place(x=0,y=60,width=512,height=540)

        self.layout2 = Frame(lay2,bg='white')                        
        self.layout2.place(x=512,y=60,width=512,height=540)
        
        self.lay_power_set = Frame(self.layout1,bg='white')
        self.lay_power_set.place(x=0,y=0,width=512,height=180)
        
        self.lay_timer_set = Frame(self.layout1,bg='white')
        self.lay_timer_set.place(x=0,y=180,width=512,height=180)
        
        self.lay_button_load = Frame(self.layout1,bg='white')
        self.lay_button_load.place(x=0,y=360,width=512,height=180)
        
        self.lay_power = Frame(self.layout2,bg='white')
        self.lay_power.place(x=0,y=0,width=512,height=180)
        
        self.lay_parameter = Frame(self.layout2,bg='white')
        self.lay_parameter.place(x=0,y=180,width=512,height=180)
        
        self.lay_logo_switch = Frame(self.layout2,bg='white')
        self.lay_logo_switch.place(x=0,y=360,width=512,height=180)
        
        self.label_powtime()
        self.tab_button()
        self.label_power()
        self.parameter()
        self.button_fan()
        self.button_test()
        self.logo()
        self.line()
        
        self.signal_object = []
        for i in range(16):
            x_spacing= i * 32
            self.display1 = SIGNAL()
            self.display1.create_layout(self.lay_button_load,x=x_spacing,y=124,text='RL' + str(i+1))
            self.signal_object.append(self.display1)
            if i==12:
                self.display1.text_relay.set('Fan')
            elif i==13:
                self.display1.text_relay.set('Alar')
            elif i==14 or i==15:
                self.display1.text_relay.set('Spar')
            elif i==11:
                self.display1.text_relay.set('1.2')
            elif i==10 or i==9:
                self.display1.text_relay.set('2.2')
            elif i==8 or i==7 or i==6:
                self.display1.text_relay.set('5.2')
            elif i==5 or i==4 or i==3:
                self.display1.text_relay.set('10.2')   
            else:
                self.display1.text_relay.set('20.2')
                
        self.relay_object = []
        for i in range(12):
            row= i // 6             # chia làm 2 hàng
            col= i % 6              # mỗi hàng có 6 (cột) đối tượng
            x_space= col * 74       # khoảng cách giữa các (cột) đối tượng
            y_space= row * 85       # khoảng cách giữa 2 hàng
            self.relay_signal = RELAY_POWER()
            self.relay_signal.create_layout(self.lay_timer_set, x=x_space,y=y_space,text = 'RL'+ str(i+1))
            self.relay_object.append(self.relay_signal)
            
            
      
      
    def label_power(self):
        self.run_on = Image.open(get_path_img()+'running_on.png').resize((122,44))
        self.picrun = ImageTk.PhotoImage(self.run_on)
        self.lb_running = Label(self.lay_power,bg='white',image=self.picrun).place(x=394,y=0,width=101,height=40)
       
        # self.lamp = Image.open(get_path_img()+'lamp_on.png').resize((17,17))
        # self.piclamp = ImageTk.PhotoImage(self.lamp)
        # self.lb_lamp_run = Label(self.lay_power,bg='white',image=self.piclamp).place(x=460,y=0,width=40,height=40)
        
        self.tempcc = StringVar()
        self.lb_temp = Label(self.lay_power,bg='white',font=('arial',13),textvariable=self.tempcc).place(x=423,y=33,width=46,height=22)  
        self.lb_temp_c = Label(self.lay_power,bg='white',font=('arial',13),text='ºC').place(x=468,y=33,width=23,height=22) 
        
        self.lb_hour = Label(self.lay_power,bg='white',font=('arial',15),text='22').place(x=195,y=0,width=29,height=38)  
        self.lb_2c = Label(self.lay_power,bg='white',font=('arial',15),text=':').place(x=221,y=0,width=5,height=38)  
        self.lb_mins = Label(self.lay_power,bg='white',font=('arial',15),text='44').place(x=226,y=0,width=29,height=38)  
        
        self.lb_day = Label(self.lay_power,bg='white',font=('arial',15),text='20').place(x=267,y=0,width=26,height=38)     
        self.lb_x1 = Label(self.lay_power,bg='white',font=('arial',15),text='/').place(x=294,y=0,width=7,height=38)  
        self.lb_month = Label(self.lay_power,bg='white',font=('arial',15),text='01').place(x=302,y=0,width=23,height=38) 
        self.lb_x2 = Label(self.lay_power,bg='white',font=('arial',15),text='/').place(x=325,y=0,width=7,height=38) 
        self.lb_year = Label(self.lay_power,bg='white',font=('arial',15),text='2025').place(x=332,y=0,width=50,height=38) 
        
        self.lb_power = Label(self.lay_power,bg='white',font=('arial bold',30),text='POWER',fg='red').place(x=25,y=75,width=150,height=30)
        self.tkw = StringVar()
        self.lb_power_val = Label(self.lay_power,bg='white',font=('arial bold',49),textvariable=self.tkw,fg='red').place(x=190,y=65,width=165,height=48)
        self.lb_power_kw = Label(self.lay_power,bg='white',font=('arial bold',49),text='KW',fg='red').place(x=370,y=65,width=110,height=48)
        
    def line(self):
        self.lb_line_dt1 = Label(self.lay_power,bg='black').place(x=0,y=0,width=1,height=180)
        self.lb_line_dt2 = Label(self.lay_logo_switch,bg='black').place(x=0,y=0,width=1,height=180)
        # self.lb_line_dt3 = Label(self.lay_timer_set,bg='black').place(x=0,y=0,width=512,height=1)
        self.lb_line_dt4 = Label(self.lay_timer_set,bg='black').place(x=0,y=179,width=512,height=1)
        
    def parameter(self):
        # hàng line
        self.lb_line1n = Label(self.lay_parameter,bg='black').place(x=0, y=0,width=512,height=1)
        self.lb_line2n = Label(self.lay_parameter,bg='black').place(x=0, y=36,width=512,height=1)
        self.lb_line3n = Label(self.lay_parameter,bg='black').place(x=0, y=72,width=512,height=1)
        self.lb_line4n = Label(self.lay_parameter,bg='black').place(x=0, y=108,width=512,height=1)
        self.lb_line5n = Label(self.lay_parameter,bg='black').place(x=0, y=144,width=512,height=1)
        self.lb_line6n = Label(self.lay_parameter,bg='black').place(x=0, y=179,width=512,height=1)  
        
        self.lb_line1d = Label(self.lay_parameter,bg='black').place(x=0, y=0,width=1,height=180)     
        self.lb_line2d = Label(self.lay_parameter,bg='black').place(x=85, y=0,width=1,height=180)  
        self.lb_line3d = Label(self.lay_parameter,bg='black').place(x=170, y=0,width=1,height=180)
        self.lb_line4d = Label(self.lay_parameter,bg='black').place(x=255, y=0,width=1,height=180)
        self.lb_line5d = Label(self.lay_parameter,bg='black').place(x=340, y=0,width=1,height=180)
        self.lb_line6d = Label(self.lay_parameter,bg='black').place(x=425, y=0,width=1,height=180)
        self.lb_line7d = Label(self.lay_parameter,bg='black').place(x=511, y=0,width=1,height=180)
        
        
         # hàng đàu tiên, hàng đơn vị
        self.lb_none1 = Label(self.lay_parameter,bg='white').place(x=1, y=1,width=83,height=34)
        self.lb_pow = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='(KW)',fg='black').place(x=86, y=1,width=83,height=34)
        self.lb_ln_v = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L-N (V)',fg='black').place(x=171, y=1,width=83,height=34)
        self.lb_A = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='(A)',fg='black').place(x=256, y=1,width=83,height=34)
        self.lb_none5 = Label(self.lay_parameter,bg='white').place(x=341, y=1,width=83,height=34)
        self.lb_ll_V = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L-L (V)',fg='black').place(x=426, y=1,width=84,height=34)
        
        # hàng L1
        self.lb_L1 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L1',fg='red').place(x=1,y=37,width=83,height=34)
        self.lb_L1_none5 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L1 - L2',fg='red').place(x=341,y=37,width=83,height=34)

        self.kw1 = StringVar()
        self.lb_L1_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.kw1,fg='red').place(x=86,y=37,width=83,height=34)
        self.vln1 = StringVar()
        self.lb_L1_Ln_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.vln1,fg='red').place(x=171,y=37,width=83,height=34)
        self.a1 = StringVar()
        self.lb_L1_A = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.a1,fg='red').place(x=256,y=37,width=83,height=34)
        self.v12 = StringVar()
        self.lb_L1_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.v12,fg='red').place(x=426,y=37,width=84,height=34)
        
         # hàng L2
        self.lb_L2 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L2',fg='orange').place(x=1,y=73,width=83,height=34)
        self.lb_L2_none5 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L2 - L3',fg='orange').place(x=341,y=73,width=83,height=34)

        self.kw2 = StringVar()
        self.lb_L2_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.kw2,fg='orange').place(x=86,y=73,width=83,height=34)
        self.vln2 = StringVar()
        self.lb_L2_ln_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.vln2,fg='orange').place(x=171,y=73,width=83,height=34)
        self.a2 = StringVar()
        self.lb_L2_A = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.a2,fg='orange').place(x=256,y=73,width=83,height=34)
        self.v23 = StringVar()
        self.lb_L2_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.v23,fg='orange').place(x=426,y=73,width=84,height=34)

        # hàng L3  
        self.lb_L3 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L3',fg='blue').place(x=1,y=109,width=83,height=34)
        self.lb_L3_none5 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L3 - L1',fg='blue').place(x=341,y=109,width=83,height=34)

        self.kw3 = StringVar()
        self.lb_L3_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.kw3,fg='blue').place(x=86,y=109,width=83,height=34)
        self.vln3 = StringVar()
        self.lb_L3_ln_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.vln3,fg='blue').place(x=171,y=109,width=83,height=34)
        self.a3 = StringVar()
        self.lb_L3_A = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.a3,fg='blue').place(x=256,y=109,width=83,height=34)
        self.v31 = StringVar()
        self.lb_L3_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.v31,fg='blue').place(x=426,y=109,width=84,height=34)
        
        # hàng FRE.
        self.lb_freq = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='FRE.',fg='black').place(x=1,y=145,width=83,height=33)
        self.freqq = StringVar()
        self.lb_fre_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.freqq,fg='black').place(x=86,y=145,width=83,height=33)
        self.lb_fre_ln_v = Label(self.lay_parameter,bg='white',font=('arial BOLD',15),text='A.LN',fg='black').place(x=171,y=145,width=83,height=33)
        self.lb_fre_A = Label(self.lay_parameter,bg='white',font=('arial',15),text='232.4',fg='black').place(x=256,y=145,width=83,height=33)
        self.lb_fre_none5 = Label(self.lay_parameter,bg='white',font=('arial BOLD',15),text='A.PF',fg='black').place(x=341,y=145,width=83,height=33)
        self.lb_fre_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),text='0.99',fg='black').place(x=426,y=145,width=84,height=34)
         
    def button_fan(self):
        a1 = Image.open(get_path_img()+'sw_on.png').resize((139,65))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open(get_path_img()+'sw_auto.png').resize((139,65))
        self.off = ImageTk.PhotoImage(a2)

        self.btn_on = Button(self.lay_logo_switch,image=self.on,bg='white', bd=0,command=lambda:self.button_fan())
        self.btn_on.place(x=15,y=46,width=139,height=70)

        if self.is_on:
            self.btn_on.config(image=self.off)
            self.is_on = False 
        else :
            self.btn_on.config(image=self.on)
            self.is_on = True
            
    def button_test(self):
        test1 = Image.open(get_path_img()+'sw_1p.png').resize((139,65))
        self.ont = ImageTk.PhotoImage(test1)
        test2 = Image.open(get_path_img()+'sw_3p.png').resize((139,65))
        self.offt = ImageTk.PhotoImage(test2)

        self.btn_on = Button(self.lay_logo_switch,image=self.ont,bg='white', bd=0,command=lambda:self.button_test())
        self.btn_on.place(x=171,y=46,width=139,height=70)

        if self.is_test:
            self.btn_on.config(image=self.offt)
            self.is_test = False 
        else :
            self.btn_on.config(image=self.ont)
            self.is_test = True
            
    def logo(self):
        logo = Image.open(get_path_img()+'logo.jpg').resize((117,117))
        self.piclo = ImageTk.PhotoImage(logo)
        self.label_logo = Label(self.lay_logo_switch, bg='red',image=self.piclo).place(x=350, y=22,width=117,height=117)
        
        self.lb_fan_control = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='FAN CONTROL').place(x=29,y=150,width=110,height=15)
        self.lb_test_mode = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='TEST MODE').place(x=185,y=150,width=110,height=15)
        self.lb_logo_name = Label(self.lay_logo_switch, bg='white',fg='black',font=('arial bold',10),text='TLC ENGINEERING SOLUTIONS').place(x=308,y=150,width=198,height=15)
        
    def label_powtime(self):
        self.lb_powset = Label(self.lay_power_set,bg='white',font=('arial bold',30),text='POWER\n SET',fg='orange').place(x=70,y=48,width=150,height=75)
        self.lb_powset_kw = Label(self.lay_power_set,bg='white',font=('arial bold',45),text='KW',fg='orange').place(x=350,y=69,width=100,height=45)
        
        self.lb_powset_val = Label(self.lay_power_set,bg='white',font=('arial bold',45),text='0',fg='orange').place(x=230,y=69,width=105,height=45)

        self.lb_available = Label(self.lay_power_set,bg='white',font=('arial bold',15),text='AVAILABLE POWER').place(x=85,y=145,width=197,height=20)
        self.lb_available_val = Label(self.lay_power_set,bg='white',font=('arial bold',15),text='99.8').place(x=305,y=145,width=65,height=20)
        self.lb_available_val = Label(self.lay_power_set,bg='white',font=('arial bold',15),text='KW').place(x=375,y=145,width=45,height=20)


      
      
    def tab_button(self):
       
        
        self.btn_apply = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD APPLY',fg='white')
        self.btn_apply.place(x=21,y=6,width=150,height=48)
        self.btn_stop = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD STOP',fg='white')
        self.btn_stop.place(x=182,y=6,width=150,height=48)
        self.btn_drop = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD DROP',fg='white')
        self.btn_drop.place(x=343,y=6,width=150,height=48)
        self.btn_logging = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD LOGGING',fg='white')
        self.btn_logging.place(x=21,y=66,width=150,height=48)
        
   
# 16 relay
# class SIGNAL:
#     def __init__(self):
#         pass
#     def create_layout(self,lay_button_load,x,y,text):
#         self.layout =  Frame(lay_button_load,bg='white')
#         self.layout.place(x=x+2,y=124, width=28,height=46)

#         self.photol = Image.open(get_path_img()+'lamp_on.png').resize((17,17))
#         self.picl = ImageTk.PhotoImage(self.photol)
#         self.lb_lamp = Label(self.layout, bg='white',image=self.picl)
#         self.lb_lamp.place(x=0,y=12,width=28,height=23)
        
        
#         self.lb_relay = Label(self.layout, bg='white',font=('arial bold',8),fg='black',text=text).place(x=0,y=0,width=28,height=11)

#         self.text_relay_val = StringVar()
#         self.lb_relay_val = Label(self.layout, bg='white',font=('arial bold',8),fg='black',textvariable=self.text_relay_val).place(x=0,y=36,width=28,height=11)

# 12 relay
class RELAY_POWER:
    def __init__(self):
        self.lamp_relay = False
    def create_layout(self,lay_timer_set, x,y,text):
        self.layout = Frame(lay_timer_set,bg='white')
        self.layout.place(x=x+48,y=y+8,width=48,height=66)

        
        self.lb_relay1 = Label(self.layout,bg='white',font=('arial',12),text=text).place(x=0,y=0,width=55,height=14)
        
        self.lamp_signal_relay()

    def lamp_signal_relay(self):
        i1 = Image.open(get_path_img()+'relay_s.png').resize((48,47))
        self.onr = ImageTk.PhotoImage(i1)
        a2 = Image.open(get_path_img()+'relay_off.png').resize((48,47))
        self.offr = ImageTk.PhotoImage(a2)
        
        self.btn_on = Button(self.layout,image=self.onr,bg='white',font=('arial',13),text='19.2',fg='black',compound="center", bd=0,command=lambda:self.lamp_signal_relay())
        self.btn_on.place(x=0,y=18,width=48,height=47)

        if self.lamp_relay:
            self.btn_on.config(image=self.offr)
            self.lamp_relay = False 
        else:
            self.btn_on.config(image=self.onr)
            self.lamp_relay = True