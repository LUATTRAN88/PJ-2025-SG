import tkinter as tk
from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
# import threading
# from time import sleep
# import client as clientCall
# import json
from extend import *

class PAGE3:
    def __init__(self):
        self.origin_data = None
        self.is_on = False
        self.is_test = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
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
        self.button_test()
        self.logo()
        
       
        # self.display_relay = SIGNAL()
        # self.display_relay.create_layout(self.lay_button_relay)
        
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
            
        self.lb_hour = Label(self.layout1,bg='white',font=('arial',15),text='22').place(x=707,y=0,width=29,height=38)  
        self.lb_2c = Label(self.layout1,bg='white',font=('arial',15),text=':').place(x=733,y=0,width=5,height=38)  
        self.lb_mins = Label(self.layout1,bg='white',font=('arial',15),text='44').place(x=738,y=0,width=29,height=38)  
            
        self.lb_day = Label(self.layout1,bg='white',font=('arial',15),text='20').place(x=779,y=0,width=26,height=38)     
        self.lb_x1 = Label(self.layout1,bg='white',font=('arial',15),text='/').place(x=806,y=0,width=7,height=38)  
        self.lb_month = Label(self.layout1,bg='white',font=('arial',15),text='01').place(x=814,y=0,width=23,height=38) 
        self.lb_x2 = Label(self.layout1,bg='white',font=('arial',15),text='/').place(x=837,y=0,width=7,height=38) 
        self.lb_year = Label(self.layout1,bg='white',font=('arial',15),text='2025').place(x=844,y=0,width=50,height=38) 
        
        
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
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial',16),text='Power limit (kW):',anchor="w",fg='orange',padx=10).place(x=0,y=55,width=383,height=52)
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial',16),text='Voltage L-N limit (V):',anchor="w",fg='orange',padx=10).place(x=0,y=109,width=383,height=52)
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial',16),text='Temperature limit (°C):',anchor="w",fg='orange',padx=10).place(x=0,y=163,width=383,height=52) 
        
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial',16),text='80',fg='orange').place(x=385,y=55,width=126,height=52)
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial',16),text='240',fg='orange').place(x=385,y=109,width=126,height=52)
        self.lb_alarm_setting = Label(self.board,bg='white',font=('arial',16),text='80',fg='orange').place(x=385,y=163,width=126,height=52)
        
    def tab_button(self):
        self.btn_apply = Button(self.lay_button_relay,bd=3,bg='#191970',font=('arial bold',12),text='SAVE',fg='white')
        self.btn_apply.place(x=21,y=48,width=150,height=48)
        
        self.btn_apply = Button(self.lay_button_relay,bd=3,bg='#191970',font=('arial bold',12),text='CANCEL',fg='white')
        self.btn_apply.place(x=182,y=48,width=150,height=48)
        
    
    def button_fan(self):
        a1 = Image.open(get_path_img()+'sw_on.png').resize((139,65))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open(get_path_img()+'sw_auto.png').resize((139,65))
        self.off = ImageTk.PhotoImage(a2)

        self.btn_on = Button(self.lay_logo_switch,image=self.on,bg='white', bd=0,command=lambda:self.button_fan())
        self.btn_on.place(x=15,y=28,width=139,height=70)

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
        self.btn_on.place(x=171,y=28,width=139,height=70)

        if self.is_test:
            self.btn_on.config(image=self.offt)
            self.is_test = False 
        else :
            self.btn_on.config(image=self.ont)
            self.is_test = True
            
    def logo(self):
        logo = Image.open(get_path_img()+'logo.jpg').resize((117,117))
        self.piclo = ImageTk.PhotoImage(logo)
        self.label_logo = Label(self.lay_logo_switch, bg='red',image=self.piclo).place(x=350, y=4,width=117,height=117)
        
        self.lb_fan_control = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='FAN CONTROL').place(x=29,y=132,width=110,height=15)
        self.lb_test_mode = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='TEST MODE').place(x=185,y=132,width=110,height=15)
        self.lb_logo_name = Label(self.lay_logo_switch, bg='white',fg='black',font=('arial bold',10),text='TLC ENGINEERING SOLUTIONS').place(x=308,y=132,width=198,height=15)
        
        
        
        
# class SIGNAL:
#     def __init__(self):
#         pass
#     def create_layout(self,lay_button_relay,x,text):
#         self.layout =  Frame(lay_button_relay,bg='white')
#         self.layout.place(x=x+1,y=100, width=28,height=46)

#         self.photol = Image.open(get_path_img()+'lamp_on.png').resize((17,17))
#         self.picl = ImageTk.PhotoImage(self.photol)
#         self.lb_lamp = Label(self.layout, bg='white',image=self.picl)
#         self.lb_lamp.place(x=0,y=12,width=28,height=23)
        
        
#         self.lb_relay = Label(self.layout, bg='white',font=('arial bold',8),fg='black',text=text).place(x=0,y=0,width=28,height=11)

#         self.text_relay = StringVar()
#         self.lb_relay_val = Label(self.layout, bg='white',font=('arial bold',8),fg='black',textvariable=self.text_relay).place(x=0,y=36,width=28,height=11)
