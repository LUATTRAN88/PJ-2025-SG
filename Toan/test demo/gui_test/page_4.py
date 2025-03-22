#!/usr/bin/python3

import tkinter as tk
from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
import tkinter.messagebox 
import client as clientCall
from extend import *
from page_5 import *
import json
from extend import *
from time import strftime
from threading import Thread
from time import sleep
from config.config_service import *
class PAGE4:
    def __init__(self):
        self.adruino=None
        self.origin_data = None
        # self.is_on = False
        # self.is_test = False
        
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
        self.code = '5959'
        self.valuerelay_fan_phase=None;
        self.display5=None
        self.config_service = ConfigService()
        self.valueResArr=[]
        
    def create_layout(self,lay4):
        self.layout = Frame(lay4,bg='orange')
        self.layout.place(x=0,y=60,width=1024,height=540)
        
        self.layout1 = Frame(self.layout,bg='white')                   
        self.layout1.place(x=0,y=0,width=1024,height=378)

        self.layout2 = Frame(self.layout,bg='pink')                        
        self.layout2.place(x=0,y=378,width=1024,height=162)
          
        self.lay_button_relay = Frame(self.layout2,bg='white')
        self.lay_button_relay.place(x=0,y=0,width=513,height=162)
        
        self.lay_logo_switch = Frame(self.layout2,bg='white')
        self.lay_logo_switch.place(x=513,y=0,width=511,height=162)
        
        self.button_fan()
        self.button_testmode()
        self.logo()
      
        self.label_run_temp()
        self.display_kb = KEYBOARD()
        self.display_kb.create_layout(self.layout1)
        self.display_kb.btn_enter.config(command=lambda:self.test_pass())
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
                
                
    def event_page5(self): 
        # self.layout.place_forget()      # ẩn Frame PAGE4
        self.stopThreadAdruino();
        self.display5 = PAGE5()
        self.display5.adruino=self.adruino;
        self.display5.create_layout(self.layout)
        self.display5.createThreadAdruino();
        
    def notification(self):
        tkinter.messagebox.showinfo('Warning',"Enter password again please!")     
        
    def test_pass(self):
        self.mk = self.display_kb.equation.get()
        if self.mk == self.code:
            self.event_page5()
            # self.display5.layout.tkraise()
        else:
            self.notification()
            self.display_kb.clear()
            
              
    def button_fan(self):
        # img_fan_on = Image.open(get_path_img()+'sw_on.png').resize((139,65))
        # self.fan_on = ImageTk.PhotoImage(img_fan_on)
        # img_fan_off = Image.open(get_path_img()+'sw_auto.png').resize((139,65))
        # self.fan_off = ImageTk.PhotoImage(img_fan_off)

        self.btn_on_fan = Button(self.lay_logo_switch,text='ON',bg='#00FF00',font=('arial bold',22), bd=3,command=lambda:self.clickfan())
        self.btn_on_fan.place(x=14,y=28,width=139,height=70)
        self.is_fan_on = True
        
    def clickfan(self):
        ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
        if self.is_fan_on:
            self.btn_on_fan.config(text='OFF',bg='grey')
            self.is_fan_on = False 
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_ON;
            self.valuerelay_fan_phase.RELAY_SWITCHING_FAN_STATUS=0;
        else :
            self.btn_on_fan.config(text='ON',bg='#00FF00')
            self.is_fan_on = True
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
            self.valuerelay_fan_phase.RELAY_SWITCHING_FAN_STATUS=1;
        self.adruino.write_port(ADRUINO_PORT_CTRL_FAN,ADRUINO_REQ_STATUS_PORT);
    
    def setvalue_fan_phase(self):
        if self.valuerelay_fan_phase.RELAY_SWITCHING_FAN_STATUS:
            self.btn_on_fan.config(image=self.fan_on)
            self.is_fan_on = True 
        else :
            self.btn_on_fan.config(image=self.fan_off)
            self.is_fan_on = False    

    def button_testmode(self):
        # test_phase1 = Image.open(get_path_img()+'sw_1p.png').resize((139,65))
        # self.img_test_phase1 = ImageTk.PhotoImage(test_phase1)
        # test_phase3 = Image.open(get_path_img()+'sw_3p.png').resize((139,65))
        # self.img_test_phase3 = ImageTk.PhotoImage(test_phase3)

        self.btn_testmode_on = Button(self.lay_logo_switch,text='1P',bg='#00FF00',font=('arial bold',22), bd=3,command=lambda:self.clickphase())
        self.btn_testmode_on.place(x=170,y=28,width=139,height=70)
        self.is_test_phase1=True;

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

            
    def logo(self):
        logo = Image.open(get_path_img()+'logo.jpg').resize((117,117))
        self.piclo = ImageTk.PhotoImage(logo)
        self.label_logo = Label(self.lay_logo_switch, bg='red',image=self.piclo).place(x=349, y=4,width=117,height=117)
        
        self.lb_fan_control = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='FAN CONTROL').place(x=28,y=132,width=110,height=15)
        self.lb_test_mode = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='TEST MODE').place(x=184,y=132,width=110,height=15)
        self.lb_logo_name = Label(self.lay_logo_switch, bg='white',fg='black',font=('arial bold',10),text='TLC ENGINEERING SOLUTIONS').place(x=307,y=132,width=198,height=15)
        
    def timeset(self):
        time_string = strftime('%H:%M:%S %p   %x') # time format 
        self.time_string.set(time_string)
        self.lb_time.after(1000,self.timeset) # time delay of 1000 milliseconds 
            
    def label_run_temp(self):
        # self.run_lamp = Image.open(get_path_img()+'running_on.png').resize((122,44))
        # self.run = ImageTk.PhotoImage(self.run_lamp)
        # self.lb_running = Label(self.layout1,bg='white',image=self.run).place(x=906,y=0,width=101,height=40)
        self.time_string = StringVar()
        self.lb_time=Label(self.layout1,font=('arial', 15),bg='white',textvariable=self.time_string)
        self.lb_time.place(x=150,y=7,width=210,height=20)

        self.lb_running = Label(self.layout1,bg='white',text='Running',font=('arial bold',15)).place(x=894,y=7,width=80,height=20)
        self.lb_run_on = Label(self.layout1,bg='#00FF00').place(x=982,y=7,width=18,height=18)
        
            
        self.tempcc = StringVar()
        self.lb_temp = Label(self.layout1,bg='white',font=('arial',13),textvariable=self.tempcc).place(x=930,y=34,width=46,height=20)  
        self.lb_temp_c = Label(self.layout1,bg='white',font=('arial',13),text='ºC').place(x=980,y=34,width=23,height=20) 
    def createThreadAdruino(self):
        self.valueResArr = self.config_service.read_file2();
        if self.adruino.serial_con is not None:
            if self.adruino.serial_con.is_open ==True:
                threading_rep = Thread(target=self.loadingdata, args=());    
                self.flag_thread_req_rep = True;
                threading_rep.start();   
    def stopThreadAdruino(self):
        try: 
            self.flag_thread_req_rep=False;
            #self.threading_rep=None;
        except:
            pass
    def loadingdata(self):
        while self.flag_thread_req_rep:
            try:
                try:
                    item =self.adruino.getdatanewline(4)  
                    data = json.loads(item); 
                except:
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
                extPrint("Connect Server Abnormal Page 4")
                sleep(1)   
            
class KEYBOARD:  
    def __init__(self):
        pass
    def create_layout(self,layout1):
        self.layout10 = Frame(layout1,bg='black')
        self.layout10.place(x=376, y=54,width=272,height=324)

        self.layout11 = Frame(self.layout10,bg='black')
        self.layout11.place(x=0,y=54,width=272,height=270)

        self.equation = StringVar()
        self.entry_value=''
        Entry(self.layout10,bg='white',bd=0,justify='center',font=('Arial Bold',16),textvariable=self.equation,show='*').place(x=1,y=1,width=270,height=52)

        self.b1=Button(self.layout11,font=('Arial Bold',16),text='C',relief='flat',bg='white',command=lambda:self.clear()).place(x=1, y=0,width=66, height=53)
        self.b2=Button(self.layout11,font=('Arial Bold',16),text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=68, y=0,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='*',relief='flat',bg='white',command=lambda:self.show('*')).place(x=136, y=0,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='#',relief='flat',bg='white',command=lambda:self.show('#')).place(x=204, y=0,width=67, height=53)

        Button(self.layout11,font=('Arial Bold',16),text='7',relief='flat',bg='white',command=lambda:self.show('7')).place(x=1, y=54,width=66, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='8',relief='flat',bg='white',command=lambda:self.show('8')).place(x=68, y=54,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='9',relief='flat',bg='white',command=lambda:self.show('9')).place(x=136, y=54,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='_',relief='flat',bg='white',command=lambda:self.show('-')).place(x=204, y=54,width=67, height=53)

        Button(self.layout11,font=('Arial Bold',16),text='4',relief='flat',bg='white',command=lambda:self.show('4')).place(x=1, y=108,width=66, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='5',relief='flat',bg='white',command=lambda:self.show('5')).place(x=68, y=108,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='6',relief='flat',bg='white',command=lambda:self.show('6')).place(x=136, y=108,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=204, y=108,width=67, height=53)

        Button(self.layout11,font=('Arial Bold',16),text='1',relief='flat',bg='white',command=lambda:self.show('1')).place(x=1, y=162,width=66, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='2',relief='flat',bg='white',command=lambda:self.show('2')).place(x=68, y=162,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='3',relief='flat',bg='white',command=lambda:self.show('3')).place(x=136, y=162,width=67, height=53)
        self.btn_enter=Button(self.layout11,font=('Arial Bold',16),text='Enter',relief='flat',bg='white',command=lambda:self.show(''))
        self.btn_enter.place(x=204, y=162,width=67, height=107)
        Button(self.layout11,font=('Arial Bold',16),text='0',relief='flat',bg='white',command=lambda:self.show('0')).place(x=1, y=216,width=66, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='00',relief='flat',bg='white',command=lambda:self.show('00')).place(x=68, y=216,width=67, height=53)
        Button(self.layout11,font=('Arial Bold',16),text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=136, y=216,width=67, height=53)


    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
        
    # def set_text_entry(self,text):
    #     self.equation.set(text)
    
    

