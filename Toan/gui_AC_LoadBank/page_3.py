import tkinter as tk
from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
# import threading
# from time import sleep
# import client as clientCall
# import json
from extend import *
from time import strftime
from config.config_setting import *

class PAGE3:
    def __init__(self):
        self.origin_data = None
        # self.is_on = False
        # self.is_test = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
        self.config_setting = ConfigSetting()
        # self.power_input = self.read_file()[0]
        # self.voltage_input = self.read_file()[1]
        # self.temp_input = self.read_file()[2]
        
    def create_layout(self,lay3):
        self.layout1 = Frame(lay3,bg='red')                   
        self.layout1.place(x=0,y=60,width=1024,height=378)

        self.layout2 = Frame(lay3,bg='pink')                        
        self.layout2.place(x=0,y=438,width=1024,height=162)
        
        self.lay_run_temp = Frame(self.layout1,bg='white')
        self.lay_run_temp.place(x=0,y=0,width=1024,height=54)
        
        self.board = Frame(self.layout1,bg='white')
        self.board.place(x=0,y=54,width=1024,height=324)
        
        self.lay_button_relay = Frame(self.layout2,bg='white')
        self.lay_button_relay.place(x=0,y=0,width=513,height=162)
        
        self.lay_logo_switch = Frame(self.layout2,bg='white')
        self.lay_logo_switch.place(x=513,y=0,width=511,height=162)
        
        self.label_run_temp()
        self.line()
        self.alarm_setting()
        self.tab_button()
        self.button_fan()
        self.button_testmode()
        self.logo()
        self.timeset()
        
           
        self.signal_list = []
        for i in range(16):
            x_space = i * 32
            
            display_relay = SIGNAL()
            display_relay.create_layout(self.lay_button_relay,x=x_space,y=106,text ='RL'+str(i+1))
            self.signal_list.append(display_relay)
            
            if i==12:
                display_relay.text_relay.set('Fan')
            elif i==13:
                display_relay.text_relay.set('Alar')
            elif i==14:
                display_relay.text_relay.set('Spar')
            elif i==15:
                display_relay.text_relay.set('Spar')
            elif i==3 or i==4 or i==5:
                display_relay.text_relay.set('10.2')
            elif i==6 or i==7 or i==8:
                display_relay.text_relay.set('5.2')
            elif i==9 or i==10:
                display_relay.text_relay.set('2.2')
            elif i==11:
                display_relay.text_relay.set('1.2')
            else:
                display_relay.text_relay.set('20.2')
                
        
    def label_run_temp(self):
        self.run_lamp = Image.open(get_path_img()+'running_on.png').resize((122,44))
        self.run = ImageTk.PhotoImage(self.run_lamp)
        self.lb_running = Label(self.layout1,bg='white',image=self.run).place(x=906,y=0,width=101,height=40)
            
        self.tempcc = StringVar()
        self.lb_temp = Label(self.layout1,bg='white',font=('arial',13),textvariable=self.tempcc).place(x=930,y=34,width=46,height=20)  
        self.lb_temp_c = Label(self.layout1,bg='white',font=('arial',13),text='ºC').place(x=980,y=34,width=23,height=20) 
            
        # self.lb_hour = Label(self.layout1,bg='white',font=('arial',15),text='22').place(x=707,y=0,width=29,height=38)  
        # self.lb_2c = Label(self.layout1,bg='white',font=('arial',15),text=':').place(x=733,y=0,width=5,height=38)  
        # self.lb_mins = Label(self.layout1,bg='white',font=('arial',15),text='44').place(x=738,y=0,width=29,height=38)  
            
        # self.lb_day = Label(self.layout1,bg='white',font=('arial',15),text='20').place(x=779,y=0,width=26,height=38)     
        # self.lb_x1 = Label(self.layout1,bg='white',font=('arial',15),text='/').place(x=806,y=0,width=7,height=38)  
        # self.lb_month = Label(self.layout1,bg='white',font=('arial',15),text='01').place(x=814,y=0,width=23,height=38) 
        # self.lb_x2 = Label(self.layout1,bg='white',font=('arial',15),text='/').place(x=837,y=0,width=7,height=38) 
        # self.lb_year = Label(self.layout1,bg='white',font=('arial',15),text='2025').place(x=844,y=0,width=50,height=38) 
    
    def timeset(self):
        l1=Label(self.layout1,font=('arial', 15),bg='white')
        l1.place(x=692,y=7,width=210,height=20)
        time_string = strftime('%H:%M:%S %p %x') # time format 
        l1.config(text=time_string)
        l1.after(1000,self.timeset) # time delay of 1000 milliseconds 
             
    def line(self):
        self.line_1n = Label(self.board,bg='black').place(x=0,y=0,width=1024,height=1)
        self.line_2n = Label(self.board,bg='black').place(x=0,y=54,width=1024,height=1)
        self.line_3n = Label(self.board,bg='black').place(x=0,y=108,width=1024,height=1)
        self.line_4n = Label(self.board,bg='black').place(x=0,y=162,width=1024,height=1)
        self.line_5n = Label(self.board,bg='black').place(x=0,y=216,width=1024,height=1)
        self.line_6n = Label(self.board,bg='black').place(x=0,y=270,width=1024,height=1)
        self.line_7n = Label(self.board,bg='black').place(x=0,y=323,width=1024,height=1)
        
        self.line_1d = Label(self.board,bg='black').place(x=384,y=54,width=1,height=270)
        self.line_2d = Label(self.board,bg='black').place(x=512,y=0,width=1,height=324)
        self.line_3d = Label(self.board,bg='black').place(x=896,y=0,width=1,height=324)
        
        self.line_4d = Label(self.lay_button_relay,bg='black').place(x=512,y=0,width=1,height=162)
        
    def alarm_setting(self):
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial bold',20),text='ALARM SETTING:',anchor="w",fg='orange',padx=10).place(x=0,y=1,width=383,height=52)
        self.lb_power = Label(self.board,bg='white',font=('arial',16),text='Power limit (kW):',anchor="w",fg='orange',padx=10).place(x=0,y=55,width=383,height=52)
        self.lb_voltage = Label(self.board,bg='white',font=('arial',16),text='Voltage L-N limit (V):',anchor="w",fg='orange',padx=10).place(x=0,y=109,width=383,height=52)
        self.lb_temp = Label(self.board,bg='white',font=('arial',16),text='Temperature limit (°C):',anchor="w",fg='orange',padx=10).place(x=0,y=163,width=383,height=52) 
        
        # self.power_value = Label(self.board,bg='white',font=('arial',16),text='80').place(x=385,y=55,width=126,height=52)
        # self.voltage_value = Label(self.board,bg='white',font=('arial',16),text='240').place(x=385,y=109,width=126,height=52)
        # self.temp_value = Label(self.board,bg='white',font=('arial',16),text='80').place(x=385,y=163,width=126,height=52)
        
        self.power_input = StringVar()
        self.voltage_input = StringVar()
        self.temp_input = StringVar()
        
        
        try:
            power, voltage, temp = self.read_file()
            self.power_input.set(power)
            self.voltage_input.set(voltage)
            self.temp_input.set(temp)
        except:
             tk.messagebox.showinfo('Warning',"Read Data Configure Failed")  
        
        self.power_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.power_input).place(x=385,y=55,width=127,height=53)
        self.voltage_value = Entry(self.board,bg='white',font=('arial',16),justify='center', textvariable=self.voltage_input).place(x=385,y=109,width=127,height=53)
        self.temp_value = Entry(self.board,bg='white',font=('arial',16),justify='center', textvariable=self.temp_input).place(x=385,y=163,width=127,height=53)
        
        
    def tab_button(self):
        self.btn_apply = Button(self.lay_button_relay,bd=3,bg='#191970',font=('arial bold',12),text='SAVE',fg='white',command=self.write_file)
        self.btn_apply.place(x=21,y=48,width=150,height=48)
        
        self.btn_apply = Button(self.lay_button_relay,bd=3,bg='#191970',font=('arial bold',12),text='CANCEL',fg='white')
        self.btn_apply.place(x=182,y=48,width=150,height=48)
        
    def button_fan(self):
        img_fan_on = Image.open(get_path_img()+'sw_on.png').resize((139,65))
        self.fan_on = ImageTk.PhotoImage(img_fan_on)
        img_fan_off = Image.open(get_path_img()+'sw_auto.png').resize((139,65))
        self.fan_off = ImageTk.PhotoImage(img_fan_off)

        self.btn_on_fan = Button(self.lay_logo_switch,image=self.fan_on,bg='white', bd=0,command=lambda:self.clickfan())
        self.btn_on_fan.place(x=15,y=28,width=139,height=70)
        self.is_fan_on = True
        
    def clickfan(self):
        if self.is_fan_on:
            self.btn_on_fan.config(image=self.fan_off)
            self.is_fan_on = False 
            control_relay(req='300',id='14',status='0')
        else :
            self.btn_on_fan.config(image=self.fan_on)
            self.is_fan_on = True
            control_relay(req='300',id='14',status='1')
            
    def button_testmode(self):
        test_phase1 = Image.open(get_path_img()+'sw_1p.png').resize((139,65))
        self.img_test_phase1 = ImageTk.PhotoImage(test_phase1)
        test_phase2 = Image.open(get_path_img()+'sw_3p.png').resize((139,65))
        self.img_test_phase2 = ImageTk.PhotoImage(test_phase2)

        self.btn_testmode_on = Button(self.lay_logo_switch,image=self.img_test_phase1,bg='white', bd=0,command=lambda:self.clickphase())
        self.btn_testmode_on.place(x=171,y=28,width=139,height=70)
        self.test_phase1 = True
        
    def clickphase(self):
        if self.test_phase1:
            self.btn_testmode_on.config(image=self.img_test_phase1)
            self.test_phase1 = False 
            control_relay(req='300',id='15',status='0')
        else :
            self.btn_testmode_on.config(image=self.img_test_phase2)
            self.test_phase1 = True
            control_relay(req='300',id='15',status='1')
            
    def logo(self):
        logo = Image.open(get_path_img()+'logo.jpg').resize((117,117))
        self.piclo = ImageTk.PhotoImage(logo)
        self.label_logo = Label(self.lay_logo_switch, bg='red',image=self.piclo).place(x=350, y=4,width=117,height=117)
        
        self.lb_fan_control = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='FAN CONTROL').place(x=29,y=132,width=110,height=15)
        self.lb_test_mode = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='TEST MODE').place(x=185,y=132,width=110,height=15)
        self.lb_logo_name = Label(self.lay_logo_switch, bg='white',fg='black',font=('arial bold',10),text='TLC ENGINEERING SOLUTIONS').place(x=308,y=132,width=198,height=15)
        
    def read_file(self):
        return self.config_setting.read_file()
        
    def write_file(self):
        power = self.power_input.get()
        voltage = self.voltage_input.get()
        temp = self.temp_input.get()
        # print(power, '')
        # print('tYpe ', type(power))
        self.config_setting.write_file(power=power, voltage=voltage, temperature=temp)    
