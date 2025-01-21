from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
# import threading
# from time import sleep
# import client as clientCall
# import json
from extend import *

class PAGE1:
    def __init__(self):
        self.origin_data = None
        self.is_on = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
    def create_layout(self,lay1):
        
        # self.layout_page = Frame(l1, bg='white')
        # self.layout_page.place(x=0,y=64,width=1024,height=704)
        
        self.layout1 = Frame(lay1,bg='yellow')                     # 3 là 1
        self.layout1.place(x=0,y=60,width=512,height=540)

        self.layout2 = Frame(lay1,bg='pink')                        # 4 là 2
        self.layout2.place(x=512,y=60,width=512,height=540)
        
        self.lay_power_set = Frame(self.layout1,bg='red')
        self.lay_power_set.place(x=0,y=0,width=512,height=180)
        
        self.lay_timer_set = Frame(self.layout1,bg='purple')
        self.lay_timer_set.place(x=0,y=180,width=512,height=180)
        
        self.lay_button_load = Frame(self.layout1,bg='grey')
        self.lay_button_load.place(x=0,y=360,width=512,height=180)
        
        self.lay_power = Frame(self.layout2,bg='orange')
        self.lay_power.place(x=0,y=0,width=512,height=180)
        
        self.lay_parameter = Frame(self.layout2,bg='grey')
        self.lay_parameter.place(x=0,y=180,width=512,height=180)
        
        self.lay_logo_switch = Frame(self.layout2,bg='red')
        self.lay_logo_switch.place(x=0,y=360,width=512,height=180)
        
        

        # self.layout5 = Frame(self.layout1,bg='white')
        # self.layout5.place(x=0,y=540,width=512,height=160)
        
        self.label_powtime()
        self.tab_button()
        self.label_power()
        
        self.signal_object = []
        for i in range(16):
            x_spacing= i * 32
            self.display1 = SIGNAL()
            self.display1.create_layout(self.lay_button_load,x=x_spacing,text='RL' + str(i+1))
            self.signal_object.append(self.display1)
            if i==12:
                self.display1.text_relay_val.set('FAN')
            elif i==13:
                self.display1.text_relay_val.set('ALAR')
            elif i==14 or i==15:
                self.display1.text_relay_val.set('SPAR')
            elif i==11:
                self.display1.text_relay_val.set('1.2')
            elif i==10 or i==9:
                self.display1.text_relay_val.set('2.2')
            elif i==8 or i==7 or i==6:
                self.display1.text_relay_val.set('5.2')
            elif i==5 or i==4 or i==3:
                self.display1.text_relay_val.set('10.2')   
            else:
                self.display1.text_relay_val.set('20.2')
      
      
    def label_power(self):
        self.lb_running = Label(self.lay_power,bg='white',font=('arial bold',15),text='Running',fg='black').place(x=370,y=0,width=100,height=40)
       
        self.lamp = Image.open(get_path_img()+'lamp.png')
        self.piclamp = ImageTk.PhotoImage(self.lamp)
        self.lb_lamp_run = Label(self.lay_power,bg='white',image=self.piclamp).place(x=460,y=2,width=40,height=40)
        
        # self.tempcc = StringVar()
        self.lb_temp = Label(self.lay_power,bg='red',font=('arial bold',14),text='35.2.C',fg='black').place(x=420,y=36,width=80,height=22)            
        
       
        self.lb_power = Label(self.lay_power,bg='green',font=('arial bold',30),text='POWER',fg='red').place(x=24,y=70,width=220,height=75)
        # self.tkw = StringVar()
        self.lb_power_val = Label(self.lay_power,bg='green',font=('arial bold',49),text='58.1',fg='red').place(x=246,y=70,width=265,height=75)
        
    def label_powtime(self):
        self.lb_powset = Label(self.lay_power_set,bg='yellow',font=('arial bold',30),text='POWER\n SET',fg='#2E8B57').place(x=15,y=48,width=150,height=75)
        self.lb_powset_kw = Label(self.lay_power_set,bg='white',font=('arial bold',45),text='KW',fg='#8B2252').place(x=295,y=69,width=100,height=45)
        
        self.lb_powset_val = Label(self.lay_power_set,bg='pink',font=('arial bold',45),text='0',fg='#8B2252').place(x=175,y=69,width=105,height=45)

        self.lb_available = Label(self.lay_power_set,bg='purple',font=('arial bold',15),text='AVAILABLE POWER').place(x=15,y=145,width=197,height=20)
        self.lb_available_val = Label(self.lay_power_set,bg='purple',font=('arial bold',15),text='99.8').place(x=235,y=145,width=65,height=20)
        self.lb_available_val = Label(self.lay_power_set,bg='purple',font=('arial bold',15),text='KW').place(x=305,y=145,width=45,height=20)


        self.lb_timer = Label(self.lay_timer_set,bg='yellow',font=('arial bold',30),text='TIMER\n SET',fg='#2E8B57').place(x=15,y=48,width=120,height=76)
        self.lb_timer_mins = Label(self.lay_timer_set,bg='red',font=('arial bold',45),text='mins',fg='#8B2252').place(x=265,y=69,width=135,height=45)
        self.lb_timer_val = Label(self.lay_timer_set,bg='green',font=('arial bold',45),text='0',fg='#8B2252').place(x=150,y=69,width=100,height=45)

        
        

        

        
        # self.lb_power = Label(self.layout2,bg='white',font=('arial bold',48),text='POWER',fg='red').place(x=24,y=59,width=220,height=75)
        # self.tkw = StringVar()
        # self.lb_power_val = Label(self.layout2,bg='white',font=('arial bold',48),textvariable=self.tkw,fg='red').place(x=246,y=59,width=265,height=75)

    def tab_button(self):
        self.up = Image.open(get_path_img()+'up.png').resize((36,34))
        self.down = Image.open(get_path_img()+'down.png').resize((36,34))
        self.picup = ImageTk.PhotoImage(self.up)
        self.picdown = ImageTk.PhotoImage(self.down)
        
        self.btn_powset_up = Button(self.lay_power_set,bd=3, bg='#20B2AA',image=self.picup,command=lambda:self.increase_power_set()).place(x=412,y=18,width=84,height=55)
        self.btn_powset_down = Button(self.lay_power_set,bd=3,bg='#20B2AA',image=self.picdown,command=lambda:self.reduce_power_set()).place(x=412,y=108,width=84,height=55)

        self.btn_time_up = Button(self.lay_timer_set,bd=3,bg='#20B2AA',image=self.picup,command=lambda:self.increase_timer_set()).place(x=412,y=18,width=84,height=55)
        self.btn_time_down = Button(self.lay_timer_set,bd=3,bg='#20B2AA',image=self.picdown,command=lambda:self.reduce_timer_set()).place(x=412,y=108,width=84,height=55)

        
        self.btn_apply = Button(self.lay_button_load,bd=3,bg='#20B2AA',font=('arial bold',12),text='LOAD APPLY',fg='#8B2252')
        self.btn_apply.place(x=21,y=6,width=150,height=48)
        self.btn_stop = Button(self.lay_button_load,bd=3,bg='#20B2AA',font=('arial bold',12),text='LOAD STOP',fg='#8B2252')
        self.btn_stop.place(x=182,y=6,width=150,height=48)
        self.btn_drop = Button(self.lay_button_load,bd=3,bg='#20B2AA',font=('arial bold',12),text='LOAD DROP',fg='#8B2252')
        self.btn_drop.place(x=343,y=6,width=150,height=48)
        self.btn_logging = Button(self.lay_button_load,bd=3,bg='#20B2AA',font=('arial bold',12),text='LOAD LOGGING',fg='#8B2252')
        self.btn_logging.place(x=21,y=66,width=150,height=48)
        
    def increase_power_set(self):
        if self.power_value < 150:
            self.power_value += 1
            self.lb_powset_val = Label(self.lay_power_set,bg='pink',font=('arial bold',45),text=str(self.power_value),fg='#8B2252').place(x=175,y=69,width=105,height=45)
    def reduce_power_set(self):
        if self.power_value > 0:
            self.power_value -= 1
            self.lb_powset_val = Label(self.lay_power_set,bg='pink',font=('arial bold',45),text=str(self.power_value),fg='#8B2252').place(x=175,y=69,width=105,height=45)        
    def increase_timer_set(self):
        if self.time_value < 60:
            self.time_value +=1
            self.lb_timer_val = Label(self.lay_timer_set,bg='green',font=('arial bold',45),text=str(self.time_value),fg='#8B2252').place(x=150,y=69,width=100,height=45)        
    def reduce_timer_set(self):
        if self.time_value > 0:
            self.time_value -=1
            self.lb_timer_val = Label(self.lay_timer_set,bg='green',font=('arial bold',45),text=str(self.time_value),fg='#8B2252').place(x=150,y=69,width=100,height=45)    
        
class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,lay_button_load,x,text):
        self.layout =  Frame(lay_button_load,bg='white')
        self.layout.place(x=x+2,y=124, width=28,height=46)

        self.photol = Image.open(get_path_img()+'lamp.png').resize((30,28))
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout, bg='white',image=self.picl)
        self.lb_lamp.place(x=0,y=12.5,width=28,height=23)
        
        
        self.lb_relay = Label(self.layout, bg='red',font=('arial bold',8),fg='black',text=text).place(x=0,y=0,width=28,height=11)

        self.text_relay_val = StringVar()
        self.lb_relay_val = Label(self.layout, bg='red',font=('arial bold',8),fg='black',textvariable=self.text_relay_val).place(x=0,y=36,width=28,height=11)
