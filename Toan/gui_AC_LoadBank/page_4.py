import tkinter as tk
from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
# import threading
# from time import sleep
# import client as clientCall
# import json
from extend import *

class PAGE4:
    def __init__(self):
        self.origin_data = None
        self.is_on = False
        self.is_test = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
    def create_layout(self,lay4):
        self.layout1 = Frame(lay4,bg='white')                   
        self.layout1.place(x=0,y=60,width=1024,height=378)

        self.layout2 = Frame(lay4,bg='pink')                        
        self.layout2.place(x=0,y=438,width=1024,height=162)
          
        self.lay_button_relay = Frame(self.layout2,bg='white')
        self.lay_button_relay.place(x=0,y=0,width=513,height=162)
        
        self.lay_logo_switch = Frame(self.layout2,bg='white')
        self.lay_logo_switch.place(x=513,y=0,width=511,height=162)
        
        self.button_fan()
        self.button_test()
        self.logo()
        self.timeset()
        self.label_run_temp()
        display_kb = KEYBOARD()
        display_kb.create_layout(self.layout1)
        
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
        
    def timeset(self):
            l1=Label(self.layout1,font=('arial', 15),bg='white')
            l1.place(x=692,y=7,width=210,height=20)
            time_string = strftime('%H:%M:%S %p %x') # time format 
            l1.config(text=time_string)
            l1.after(1000,self.timeset) # time delay of 1000 milliseconds 
            
    def label_run_temp(self):
        self.run_lamp = Image.open(get_path_img()+'running_on.png').resize((122,44))
        self.run = ImageTk.PhotoImage(self.run_lamp)
        self.lb_running = Label(self.layout1,bg='white',image=self.run).place(x=906,y=0,width=101,height=40)
            
        self.tempcc = StringVar()
        self.lb_temp = Label(self.layout1,bg='white',font=('arial',13),textvariable=self.tempcc).place(x=930,y=34,width=46,height=20)  
        self.lb_temp_c = Label(self.layout1,bg='white',font=('arial',13),text='ºC').place(x=980,y=34,width=23,height=20) 
        
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
        Entry(self.layout10,bg='white',bd=0,justify='center',font=('Arial Bold',16),textvariable=self.equation).place(x=1,y=1,width=270,height=52)

        self.b1=Button(self.layout11,font=('Arial Bold',16),text='Tab',relief='flat',bg='white',command=lambda:self.show('Tab')).place(x=1, y=0,width=66, height=53)
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

