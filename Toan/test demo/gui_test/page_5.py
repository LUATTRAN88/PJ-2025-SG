#!/usr/bin/python3

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
from config.config_service import *
import json
from extend import *
from time import strftime
from threading import Thread
from time import sleep
class PAGE5:
    def __init__(self):
        self.adruino=None
        self.origin_data = None
        # self.is_on = False
        # self.is_test = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
        self.config_service = ConfigService()
        self.valueResArr=[]
        
    def create_layout(self,lay5):
        self.layout1 = Frame(lay5,bg='red')                   
        self.layout1.place(x=0,y=0,width=1024,height=378)       #   y=0

        self.layout2 = Frame(lay5,bg='pink')                        
        self.layout2.place(x=0,y=378,width=1024,height=162)     #   y=378
        
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
        self.r_emer_setting()
        self.tab_button()
        self.button_fan()
        self.button_testmode()
        self.logo()
        self.timeset()
        
           
        self.signal_list = []
        for i in range(16):
            x_space = i * 32
            
            signal = SIGNAL()
            signal.create_layout(self.lay_button_relay,x=x_space,y=106,text ='RL'+str(i+1))
            self.signal_list.append(signal)
            
            if i==12:
                signal.text_relay.set('Fan')
            elif i==13:
                signal.text_relay.set('Alar')
            elif i==14:
                signal.text_relay.set('Spar')
            elif i==15:
                signal.text_relay.set('Spar')
            elif i==3 or i==4 or i==5:
                signal.text_relay.set('10.2')
            elif i==6 or i==7 or i==8:
                signal.text_relay.set('5.2')
            elif i==9 or i==10:
                signal.text_relay.set('2.2')
            elif i==11:
                signal.text_relay.set('1.2')
            else:
                signal.text_relay.set('20.2')
                
        
    def label_run_temp(self):
        # self.run_lamp = Image.open(get_path_img()+'running_on.png').resize((122,44))
        # self.run = ImageTk.PhotoImage(self.run_lamp)
        # self.lb_running = Label(self.layout1,bg='white',image=self.run).place(x=906,y=0,width=101,height=40)
        self.lb_running = Label(self.layout1,bg='white',text='Running',font=('arial bold',15)).place(x=894,y=7,width=80,height=20)
        self.lb_run_on = Label(self.layout1,bg='#00FF00').place(x=982,y=7,width=18,height=18)
        
        
            
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

        self.time_string = StringVar()
        self.lb_time=Label(self.layout1,font=('arial', 15),bg='white',textvariable=self.time_string)
        self.lb_time.place(x=150,y=7,width=210,height=20)
          
    def timeset(self):
        time_string = strftime('%H:%M:%S %p   %x') # time format 
        self.time_string.set(time_string)
        self.lb_time.after(1000,self.timeset) # time delay of 1000 milliseconds     
             
    def line(self):
        self.line_1n = Label(self.board,bg='black').place(x=0,y=0,width=1024,height=1)
        self.line_2n = Label(self.board,bg='black').place(x=0,y=54,width=1024,height=1)
        self.line_3n = Label(self.board,bg='black').place(x=0,y=108,width=1024,height=1)
        self.line_4n = Label(self.board,bg='black').place(x=0,y=162,width=1024,height=1)
        self.line_5n = Label(self.board,bg='black').place(x=0,y=216,width=1024,height=1)
        self.line_6n = Label(self.board,bg='black').place(x=0,y=270,width=1024,height=1)
        self.line_7n = Label(self.board,bg='black').place(x=0,y=323,width=1024,height=1)
        
        self.line_1d = Label(self.board,bg='black').place(x=85,y=54,width=1,height=216)
        self.line_2d = Label(self.board,bg='black').place(x=170,y=54,width=1,height=216)
        self.line_3d = Label(self.board,bg='black').place(x=255,y=54,width=1,height=216)
        self.line_4d = Label(self.board,bg='black').place(x=340,y=54,width=1,height=270)
        self.line_5d = Label(self.board,bg='black').place(x=425,y=54,width=1,height=270)
        
        self.line_6d = Label(self.board,bg='black').place(x=512,y=0,width=1,height=324)
        self.line_7d = Label(self.board,bg='black').place(x=896,y=54,width=1,height=270)
        
        self.line_8d = Label(self.lay_button_relay,bg='black').place(x=512,y=0,width=1,height=162)
        
    def r_emer_setting(self):
        self.lb_r_setting = Label(self.board,bg='white',font=('arial bold',20),text='R SETTING (Ω):',anchor="w",fg='orange',padx=10).place(x=0,y=1,width=383,height=52)
        self.lb_emer_setting = Label(self.board,bg='white',font=('arial bold',20),text='EMER. SETTING (STOP):',anchor="w",fg='orange',padx=10).place(x=513,y=1,width=383,height=52)
        
        self.lb_r1 = Label(self.board,bg='white',font=('arial',16),text='R1:',anchor="w",fg='orange',padx=10).place(x=0,y=55,width=85,height=53)
        self.lb_r4 = Label(self.board,bg='white',font=('arial',16),text='R4:',anchor="w",fg='orange',padx=10).place(x=0,y=109,width=85,height=53)
        self.lb_r7 = Label(self.board,bg='white',font=('arial',16),text='R7:',anchor="w",fg='orange',padx=10).place(x=0,y=163,width=85,height=53) 
        self.lb_r10 = Label(self.board,bg='white',font=('arial',16),text='R10:',anchor="w",fg='orange',padx=10).place(x=0,y=217,width=85,height=53) 
        self.lb_r2 = Label(self.board,bg='white',font=('arial',16),text='R2:',anchor="w",fg='orange',padx=10).place(x=171,y=55,width=84,height=53)
        self.lb_r5 = Label(self.board,bg='white',font=('arial',16),text='R5:',anchor="w",fg='orange',padx=10).place(x=171,y=109,width=84,height=53)
        self.lb_r8 = Label(self.board,bg='white',font=('arial',16),text='R8:',anchor="w",fg='orange',padx=10).place(x=171,y=163,width=84,height=53)
        self.lb_r11 = Label(self.board,bg='white',font=('arial',16),text='R11:',anchor="w",fg='orange',padx=10).place(x=171,y=217,width=84,height=53)
        self.lb_r3 = Label(self.board,bg='white',font=('arial',16),text='R3:',anchor="w",fg='orange',padx=10).place(x=341,y=55,width=84,height=53)
        self.lb_r6 = Label(self.board,bg='white',font=('arial',16),text='R6:',anchor="w",fg='orange',padx=10).place(x=341,y=109,width=84,height=53)
        self.lb_r9 = Label(self.board,bg='white',font=('arial',16),text='R9:',anchor="w",fg='orange',padx=10).place(x=341,y=163,width=84,height=53)
        self.lb_r12 = Label(self.board,bg='white',font=('arial',16),text='R12:',anchor="w",fg='orange',padx=10).place(x=341,y=217,width=84,height=53)
        self.lb_resistor = Label(self.board,bg='white',font=('arial',16),text='Resistor threshold allow (%):',anchor="w",fg='orange',padx=10).place(x=0,y=271,width=340,height=52) 
        
        self.lb_current = Label(self.board,bg='white',font=('arial',16),text='Current limit (A):',anchor="w",fg='orange',padx=10).place(x=513,y=55,width=383,height=53)
        self.lb_voltage = Label(self.board,bg='white',font=('arial',16),text='Voltage L-N limit (V):',anchor="w",fg='orange',padx=10).place(x=513,y=109,width=383,height=53)
        self.lb_temperature = Label(self.board,bg='white',font=('arial',16),text='Temperature limit (°C):',anchor="w",fg='orange',padx=10).place(x=513,y=163,width=383,height=53)
       
        self.resistor_threshold_minus_input = StringVar()
        self.resistor_threshold_plus_input = StringVar()
        
        self.r1_input = StringVar()
        self.r2_input = StringVar()
        self.r3_input = StringVar()
        self.r4_input = StringVar()
        self.r5_input = StringVar()
        self.r6_input = StringVar()
        self.r7_input = StringVar()
        self.r8_input = StringVar()
        self.r9_input = StringVar()
        self.r10_input = StringVar()
        self.r11_input = StringVar()
        self.r12_input = StringVar()

        self.current_input = StringVar()
        self.voltage_input = StringVar()
        self.temperature_input = StringVar()
        
        
        try:
            (r1, r2, r3, r4, r5, r6,
            r7, r8, r9, r10, r11, r12,
            mn, mx, current, voltage, 
            temperature) = self.read_file()
            
            self.r1_input.set(r1)
            self.r2_input.set(r2)
            self.r3_input.set(r3)
            self.r4_input.set(r4)
            self.r5_input.set(r5)
            self.r6_input.set(r6)
            self.r7_input.set(r7)
            self.r8_input.set(r8)
            self.r9_input.set(r9)
            self.r10_input.set(r10)
            self.r11_input.set(r11)
            self.r12_input.set(r12)
            
            self.resistor_threshold_minus_input.set(mn)
            self.resistor_threshold_plus_input.set(mx)
            
            self.current_input.set(current)
            self.voltage_input.set(voltage)
            self.temperature_input.set(temperature)
            
        except:
            tk.messagebox.showinfo('Warning',"Read Data Configure Failed")  

        self.resistor_threshold_minus = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.resistor_threshold_minus_input).place(x=341,y=271,width=84,height=52)
        self.resistor_threshold_plus = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.resistor_threshold_plus_input).place(x=426,y=271,width=85,height=52)
       
        self.r1_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r1_input).place(x=86,y=55,width=84,height=53)
        self.r4_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r4_input).place(x=86,y=109,width=84,height=53)
        self.r7_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r7_input).place(x=86,y=163,width=84,height=53) 
        self.r10_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r10_input).place(x=86,y=217,width=84,height=53)
        self.r2_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r2_input).place(x=256,y=55,width=84,height=53)
        self.r5_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r5_input).place(x=256,y=109,width=84,height=53)
        self.r8_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r8_input).place(x=256,y=163,width=84,height=53)
        self.r11_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r11_input).place(x=256,y=217,width=84,height=53)
        self.r3_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r3_input).place(x=426,y=55,width=85,height=53)
        self.r6_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r6_input).place(x=426,y=109,width=85,height=53)
        self.r9_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r9_input).place(x=426,y=163,width=85,height=53)
        self.r12_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.r12_input).place(x=426,y=217,width=85,height=53)
       
        self.current_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.current_input).place(x=897,y=55,width=127,height=53)
        self.voltage_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.voltage_input).place(x=897,y=109,width=127,height=53)
        self.temperature_value = Entry(self.board,bg='white',font=('arial',16),justify='center',textvariable=self.temperature_input).place(x=897,y=163,width=127,height=53)
        
    def tab_button(self):
        self.btn_apply = Button(self.lay_button_relay,bd=3,bg='#191970',font=('arial bold',12),text='SAVE',fg='white',command=self.write_file)
        self.btn_apply.place(x=21,y=48,width=150,height=48)
        
        self.btn_apply = Button(self.lay_button_relay,bd=3,bg='#191970',font=('arial bold',12),text='EXIT',fg='white',command=self.exitapp)
        self.btn_apply.place(x=182,y=48,width=150,height=48)
    def exitapp(self):
        closeapp(self.adruino,5);  
    
    def button_fan(self):
        # img_fan_on = Image.open(get_path_img()+'sw_on.png').resize((139,65))
        # self.fan_on = ImageTk.PhotoImage(img_fan_on)
        # img_fan_off = Image.open(get_path_img()+'sw_auto.png').resize((139,65))
        # self.fan_off = ImageTk.PhotoImage(img_fan_off)

        self.btn_on_fan = Button(self.lay_logo_switch,text='ON',bg='#00FF00',font=('arial bold',22), bd=3,command=lambda:self.clickfan(),state=DISABLED)
        self.btn_on_fan.place(x=14,y=28,width=139,height=70)
        self.is_fan_on = True

    def clickfan(self):
        ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
        if self.is_fan_on:
            self.btn_on_fan.config(text='OFF',bg='grey')
            self.is_fan_on = False 
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_ON;
        else :
            self.btn_on_fan.config(text='ON',bg='#00FF00')
            self.is_fan_on = True
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
        self.adruino.write_port(ADRUINO_PORT_CTRL_FAN,ADRUINO_REQ_STATUS_PORT);
    
    def setvalue_fan(self,val):
        if val:
            self.btn_on_fan.config(image=self.fan_on)
            self.is_fan_on = False 
        else :
            self.btn_on_fan.config(image=self.fan_off)
            self.is_fan_on = True

    def button_testmode(self):
        # test_phase1 = Image.open(get_path_img()+'sw_1p.png').resize((139,65))
        # self.img_test_phase1 = ImageTk.PhotoImage(test_phase1)
        # test_phase3 = Image.open(get_path_img()+'sw_3p.png').resize((139,65))
        # self.img_test_phase3 = ImageTk.PhotoImage(test_phase3)

        self.btn_testmode_on = Button(self.lay_logo_switch,text='1P',bg='#00FF00',font=('arial bold',22), bd=3,command=lambda:self.clickphase())
        self.btn_testmode_on.place(x=170,y=28,width=139,height=70)
        self.is_test_phase1 = True

    def clickphase(self):
        ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
        if self.is_test_phase1:
            self.btn_testmode_on.config(text='3P',bg='grey')
            self.is_test_phase1 = False 
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_ON;
        else :
            self.btn_testmode_on.config(text='1P',bg='#00FF00')
            self.is_test_phase1 = True
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
        self.adruino.write_port(ADRUINO_PORT_CTRL_PHASE,ADRUINO_REQ_STATUS_PORT);
    def setvalue_phase(self,val):  
        if val:
            self.btn_testmode_on.config(image=self.img_test_phase3)
            self.test_phase2 = False 
        else :
            self.btn_testmode_on.config(image=self.img_test_phase1)
            self.test_phase2 = True        
    def logo(self):
        logo = Image.open(get_path_img()+'logo.jpg').resize((117,117))
        self.piclo = ImageTk.PhotoImage(logo)
        self.label_logo = Label(self.lay_logo_switch, bg='red',image=self.piclo).place(x=349, y=4,width=117,height=117)
        
        self.lb_fan_control = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='FAN CONTROL').place(x=28,y=132,width=110,height=15)
        self.lb_test_mode = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='TEST MODE').place(x=184,y=132,width=110,height=15)
        self.lb_logo_name = Label(self.lay_logo_switch, bg='white',fg='black',font=('arial bold',10),text='TLC ENGINEERING SOLUTIONS').place(x=307,y=132,width=198,height=15)
        
        
    def read_file(self):
        return self.config_service.read_file()
    
    def write_file(self):
        r1 = self.r1_input.get()
        r2 = self.r2_input.get()
        r3 = self.r3_input.get()
        r4 = self.r4_input.get()
        r5 = self.r5_input.get()
        r6 = self.r6_input.get()
        r7 = self.r7_input.get()
        r8 = self.r8_input.get()
        r9 = self.r9_input.get()
        r10 = self.r10_input.get()
        r11 = self.r11_input.get()
        r12 = self.r12_input.get()
        
        mn = self.resistor_threshold_minus_input.get()
        mx = self.resistor_threshold_plus_input.get()
        
        current = self.current_input.get()
        voltage = self.voltage_input.get()
        temperature = self.temperature_input.get()
        
        self.config_service.write_file(r1, r2, r3, r4, r5, r6,
                                       r7, r8, r9, r10, r11, r12, 
                                       mn, mx, current, voltage, temperature)
        self.valueResArr = self.config_service.read_file2();
    def createThreadAdruino(self):
        #self.threading_req = Thread(target=self.requestdata, args=()); 
        self.valueResArr = self.config_service.read_file2();
        if self.adruino.serial_con is not None:
            if self.adruino.serial_con.is_open ==True:
                threading_rep = Thread(target=self.loadingdata, args=());          
                self.flag_thread_req_rep = True;
                #self.threading_req.start();
                threading_rep.start();  
    def stopThreadAdruino(self):
        self.flag_thread_req_rep=False;
    def loadingdata(self):
        while self.flag_thread_req_rep:
            try:
                try:
                    item =self.adruino.getdatanewline(5)  
                    data = json.loads(item); 
                except :
                    continue
                self.origin_data = data['info']
                self.tempcc.set(str(self.origin_data['tempc']))
                self.rl_array = data['rls']
                index=0;
                for i in self.rl_array:
                    
                    if i==1:
                        self.signal_list[index].setonoff(1);

                    else:
                        self.signal_list[index].setonoff(0);

                    index+=1;
                index=0;
                for r in self.valueResArr:
                    if index<12:
                        vln_val=self.origin_data['vln'];
                        kwr=(vln_val*vln_val )/r;
                        kwr=round(kwr, 2);
                        self.signal_list[index].set_relay_value(str(kwr));
                    else: 
                            break;
                    index+=1;
                sleep(0.5)
            except :
                print("Connect Server Abnormal Page 5")
                sleep(1)   
        
