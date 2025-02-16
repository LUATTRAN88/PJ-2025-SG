from tkinter import *
# from tkinter import font as tkFont
from PIL import ImageTk, Image
# import threading
from time import sleep
import client as clientCall
import json
from extend import *
from time import strftime
from threading import Thread

# import http.client


class PAGE1:
    def __init__(self):
        self.adruino=None
        self.origin_data = None
        # self.is_on = False
        # self.is_test = False
        self.is_switch = False
        self.power_value = 0
        self.time_value = 0
        self.hold_powerup=FALSE;
        self.hold_timeup=FALSE;
        self.valuerelay_fan_phase=None;
        self.threading_rep = None;
    def create_layout(self,lay1):
        self.root= lay1;
        self.layout1 = Frame(lay1,bg='white')                   
        self.layout1.place(x=0,y=60,width=512,height=540)

        self.layout2 = Frame(lay1,bg='white')                        
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
        self.button_testmode()
        self.logo()
        self.line()
        self.timeset()
        
        self.signal_list = []
        for i in range(16):
            x_spacing= i * 32
            signal = SIGNAL() 
            signal.create_layout(self.lay_button_load,x=x_spacing,y=124,text='RL' + str(i+1))
            self.signal_list.append(signal)
            if i==12:
                signal.text_relay.set('Fan')
            elif i==13:
                signal.text_relay.set('Alar')
            elif i==14 or i==15:
                signal.text_relay.set('Spar')
            elif i==11:
                signal.text_relay.set('1.2')
            elif i==10 or i==9:
                signal.text_relay.set('2.2')
            elif i==8 or i==7 or i==6:
                signal.text_relay.set('5.2')
            elif i==5 or i==4 or i==3:
                signal.text_relay.set('10.2')   
            else:
                signal.text_relay.set('20.2')
                
        signal = None
      

    def timeset(self):
        l1=Label(self.lay_power,font=('arial', 15),bg='white')
        l1.place(x=150,y=7,width=210,height=20)
        time_string = strftime('%H:%M:%S %p   %x') # time format 
        l1.config(text=time_string)
        l1.after(1000,self.timeset) # time delay of 1000 milliseconds 
         
    def label_power(self):
        # self.run_on = Image.open(get_path_img()+'running_on.png').resize((122,44))
        # self.picrun = ImageTk.PhotoImage(self.run_on)
        # self.lb_running = Label(self.lay_power,bg='white',image=self.picrun).place(x=394,y=0,width=101,height=40)
        self.lb_running = Label(self.lay_power,bg='white',text='Running',font=('arial bold',15)).place(x=382,y=7,width=80,height=20)
        self.lb_run_on = Label(self.lay_power,bg='#00FF00').place(x=470,y=7,width=18,height=18)
        
        
        self.tempcc = StringVar()
        self.lb_temp = Label(self.lay_power,bg='white',font=('arial',13),textvariable=self.tempcc).place(x=423,y=33,width=46,height=22)  
        self.lb_temp_c = Label(self.lay_power,bg='white',font=('arial',13),text='ºC').place(x=468,y=33,width=23,height=22) 
         
        self.lb_power = Label(self.lay_power,bg='white',font=('arial bold',30),text='POWER',fg='red').place(x=25,y=75,width=150,height=30)
        self.tkw = StringVar()
        self.lb_power_val = Label(self.lay_power,bg='white',font=('arial bold',49),textvariable=self.tkw,fg='red').place(x=190,y=65,width=165,height=48)
        self.lb_power_kw = Label(self.lay_power,bg='white',font=('arial bold',49),text='KW',fg='red').place(x=370,y=65,width=110,height=48)
        
    def line(self):
        self.lb_line_dt1 = Label(self.lay_power,bg='black').place(x=0,y=0,width=1,height=180)
        self.lb_line_dt2 = Label(self.lay_logo_switch,bg='black').place(x=0,y=0,width=1,height=180)
        self.lb_line_dt3 = Label(self.lay_timer_set,bg='black').place(x=0,y=0,width=512,height=1)
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
        self.cur1 = StringVar()
        self.lb_L1_A = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.cur1,fg='red').place(x=256,y=37,width=83,height=34)
        self.v12 = StringVar()
        self.lb_L1_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.v12,fg='red').place(x=426,y=37,width=84,height=34)
        
         # hàng L2
        self.lb_L2 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L2',fg='orange').place(x=1,y=73,width=83,height=34)
        self.lb_L2_none5 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L2 - L3',fg='orange').place(x=341,y=73,width=83,height=34)

        self.kw2 = StringVar()
        self.lb_L2_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.kw2,fg='orange').place(x=86,y=73,width=83,height=34)
        self.vln2 = StringVar()
        self.lb_L2_ln_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.vln2,fg='orange').place(x=171,y=73,width=83,height=34)
        self.cur2 = StringVar()
        self.lb_L2_A = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.cur2,fg='orange').place(x=256,y=73,width=83,height=34)
        self.v23 = StringVar()
        self.lb_L2_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.v23,fg='orange').place(x=426,y=73,width=84,height=34)

        # hàng L3  
        self.lb_L3 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L3',fg='blue').place(x=1,y=109,width=83,height=34)
        self.lb_L3_none5 = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='L3 - L1',fg='blue').place(x=341,y=109,width=83,height=34)

        self.kw3 = StringVar()
        self.lb_L3_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.kw3,fg='blue').place(x=86,y=109,width=83,height=34)
        self.vln3 = StringVar()
        self.lb_L3_ln_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.vln3,fg='blue').place(x=171,y=109,width=83,height=34)
        self.cur3 = StringVar()
        self.lb_L3_A = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.cur3,fg='blue').place(x=256,y=109,width=83,height=34)
        self.v31 = StringVar()
        self.lb_L3_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.v31,fg='blue').place(x=426,y=109,width=84,height=34)
        
        # hàng FRE.
        self.lb_freq = Label(self.lay_parameter,bg='white',font=('arial bold',15),text='FRE.',fg='black').place(x=1,y=145,width=83,height=33)
        self.freqq = StringVar()
        self.lb_fre_kw = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.freqq,fg='black').place(x=86,y=145,width=83,height=33)
        self.lb_fre_ln_v = Label(self.lay_parameter,bg='white',font=('arial BOLD',15),text='A.LN',fg='black').place(x=171,y=145,width=83,height=33)
        
        
        self.txt_aln_sum = StringVar()
        self.lb_aln_sum= Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.txt_aln_sum,fg='black')
        self.lb_aln_sum.place(x=256,y=145,width=83,height=33)
        
        
        
        self.txt_apf_sum = StringVar()
        self.lb_fre_none5 = Label(self.lay_parameter,bg='white',font=('arial BOLD',15),text='A.PF',fg='black').place(x=341,y=145,width=83,height=33)
        self.lb_fre_ll_v = Label(self.lay_parameter,bg='white',font=('arial',15),textvariable=self.txt_apf_sum,fg='black').place(x=426,y=145,width=84,height=34)
         
    def button_fan(self):
        # img_fan_on = Image.open(get_path_img()+'sw_on.png').resize((139,65))
        # self.fan_on = ImageTk.PhotoImage(img_fan_on)
        # img_fan_off = Image.open(get_path_img()+'sw_auto.png').resize((139,65))
        # self.fan_off = ImageTk.PhotoImage(img_fan_off)

        self.btn_on_fan = Button(self.lay_logo_switch,text='ON',bg='#00FF00',font=('arial bold',22) ,bd=3,command=lambda:self.clickfan())
        self.btn_on_fan.place(x=15,y=46,width=139,height=70)
        self.is_fan_on = True
       
    def clickfan(self):
        ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
        if self.is_fan_on:
            self.btn_on_fan.config(text='OFF',bg='White')
            self.is_fan_on = False 
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;
            self.valuerelay_fan_phase.RELAY_SWITCHING_FAN_STATUS=0;
        else :
            self.btn_on_fan.config(text='ON',bg='#00FF00')
            self.is_fan_on = True
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_ON;
            self.valuerelay_fan_phase.RELAY_SWITCHING_FAN_STATUS=1;
        self.adruino.write_port(ADRUINO_PORT_CTRL_FAN,ADRUINO_REQ_STATUS_PORT);
        
   
    def setvalue_fan_phase(self):
        
        if self.valuerelay_fan_phase.RELAY_SWITCHING_FAN_STATUS:
            self.btn_on_fan.config(image=self.fan_on)
            self.is_fan_on = True
        else :
            self.btn_on_fan.config(image=self.fan_off)
            self.is_fan_on = False
        
        
        
        # if self.valuerelay_fan_phase.RELAY_SWITCHING_PHASE_STATUS:
        #     self.btn_testmode_on.config(image=self.img_test_phase1)
        #     self.is_test_phase1=True;
        # else :
        #     self.btn_testmode_on.config(image=self.img_test_phase3)
        #     self.is_test_phase1=False;
        
           
           
            
    def button_testmode(self):
        # test_phase1 = Image.open(get_path_img()+'sw_1p.png').resize((139,65))
        # self.img_test_phase1 = ImageTk.PhotoImage(test_phase1)
        # test_phase3 = Image.open(get_path_img()+'sw_3p.png').resize((139,65))
        # self.img_test_phase3 = ImageTk.PhotoImage(test_phase3)

        self.btn_testmode_on = Button(self.lay_logo_switch,text='1P',bg='#00FF00',font=('arial bold',22), bd=3,command=lambda:self.clickphase())
        self.btn_testmode_on.place(x=171,y=46,width=139,height=70)
        self.is_test_phase1=TRUE;
        
    def clickphase(self):  
        ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF   
        if self.is_test_phase1:
            self.btn_testmode_on.config(text='3P',bg='white')
            self.is_test_phase1= False 
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_ON;
        else :
            self.btn_testmode_on.config(text='1P',bg='#00FF00')
            self.is_test_phase1 = True
            ADRUINO_REQ_STATUS_PORT=ADRUINO_STATUS_PORT_OFF;

        self.adruino.write_port(ADRUINO_PORT_CTRL_PHASE,ADRUINO_REQ_STATUS_PORT);
    


            
    def logo(self):
        logo = Image.open(get_path_img()+'logo.jpg').resize((117,117))
        self.piclo = ImageTk.PhotoImage(logo)
        self.label_logo = Label(self.lay_logo_switch, bg='red',image=self.piclo).place(x=350, y=22,width=117,height=117)
        
        self.lb_fan_control = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='FAN CONTROL').place(x=29,y=150,width=110,height=15)
        self.lb_test_mode = Label(self.lay_logo_switch, bg='white',fg='orange',font=('arial bold',10),text='TEST MODE').place(x=185,y=150,width=110,height=15)
        self.lb_logo_name = Label(self.lay_logo_switch, bg='white',fg='black',font=('arial bold',10),text='TLC ENGINEERING SOLUTIONS').place(x=308,y=150,width=198,height=15)
        
    def label_powtime(self):
        self.lb_powset = Label(self.lay_power_set,bg='white',font=('arial bold',30),text='POWER\n SET',fg='orange').place(x=15,y=48,width=150,height=75)
        self.lb_powset_kw = Label(self.lay_power_set,bg='white',font=('arial bold',45),text='KW',fg='orange').place(x=295,y=69,width=100,height=45)
        
        self.lb_powset_val = Label(self.lay_power_set,bg='white',font=('arial bold',45),text='0',fg='orange').place(x=175,y=69,width=105,height=45)

        self.lb_available = Label(self.lay_power_set,bg='white',font=('arial bold',15),text='AVAILABLE POWER').place(x=15,y=145,width=197,height=20)
        self.lb_available_val = Label(self.lay_power_set,bg='white',font=('arial bold',15),text='99.8').place(x=235,y=145,width=65,height=20)
        self.lb_available_val = Label(self.lay_power_set,bg='white',font=('arial bold',15),text='KW').place(x=305,y=145,width=45,height=20)


        self.lb_timer = Label(self.lay_timer_set,bg='white',font=('arial bold',30),text='TIMER\n SET',fg='orange').place(x=15,y=48,width=120,height=76)
        self.lb_timer_mins = Label(self.lay_timer_set,bg='white',font=('arial bold',45),text='mins',fg='orange').place(x=265,y=69,width=135,height=45)
        self.lb_timer_val = Label(self.lay_timer_set,bg='white',font=('arial bold',45),text='0',fg='orange').place(x=150,y=69,width=100,height=45)

      
      
      
      
    
      
      
    def tab_button(self):
        # self.up = Image.open(get_path_img()+'up.png').resize((36,34))
        # self.down = Image.open(get_path_img()+'down.png').resize((36,34))
        # self.picup = ImageTk.PhotoImage(self.up)
        # self.picdown = ImageTk.PhotoImage(self.down)
        
        self.btn_powset_up = Button(self.lay_power_set,bd=3,fg='orange',bg='#191970',text='Up',font=('arial bold',16),command=lambda:self.increase_power_set())
        self.btn_powset_up.place(x=412,y=18,width=84,height=55)
        
        self.btn_powset_up.bind("<ButtonPress-1>", self.on_press_powerup)
        self.btn_powset_up.bind("<ButtonRelease-1>", self.on_release_powerup)
    
        
        self.btn_powset_down = Button(self.lay_power_set,bd=3,fg='orange',bg='#191970',text='Down',font=('arial bold',16),command=lambda:self.reduce_power_set()).place(x=412,y=108,width=84,height=55)

        self.btn_time_up = Button(self.lay_timer_set,bd=3,fg='orange',bg='#191970',text='Up',font=('arial bold',16),command=lambda:self.increase_timer_set())
        self.btn_time_up.place(x=412,y=18,width=84,height=55)
        
        self.btn_time_up.bind("<ButtonPress-1>", self.on_press_timesetup)
        self.btn_time_up.bind("<ButtonRelease-1>", self.on_release_timesetup)
        
        
        self.btn_time_down = Button(self.lay_timer_set,bd=3,fg='orange',bg='#191970',text='Down',font=('arial bold',16),command=lambda:self.reduce_timer_set()).place(x=412,y=108,width=84,height=55)

        
        self.btn_apply = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD APPLY',fg='white')
        self.btn_apply.place(x=21,y=6,width=150,height=48)
        self.btn_stop = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD STOP',fg='white')
        self.btn_stop.place(x=182,y=6,width=150,height=48)
        self.btn_drop = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD DROP',fg='white')
        self.btn_drop.place(x=343,y=6,width=150,height=48)
        self.btn_logging = Button(self.lay_button_load,bd=3,bg='#191970',font=('arial bold',12),text='LOAD LOGGING',fg='white')
        self.btn_logging.place(x=21,y=66,width=150,height=48)
    def on_press_powerup(self, event):
        self.hold_powerup = True
        extPrint("test")
        self.hold_event_updown()

    def on_release_powerup(self, event):
        self.hold_powerup = False   
            
    def increase_power_set(self):
        if self.power_value < 100:
            self.power_value += 1
            self.lb_powset_val = Label(self.lay_power_set,bg='white',font=('arial bold',45),text=str(self.power_value),fg='orange').place(x=175,y=69,width=105,height=45)
            result=number_of_objects(self.power_value)
            extPrint(result)
    def reduce_power_set(self):
        if self.power_value > 0:
            self.power_value -= 1
            self.lb_powset_val = Label(self.lay_power_set,bg='white',font=('arial bold',45),text=str(self.power_value),fg='orange').place(x=175,y=69,width=105,height=45)        
            result=number_of_objects(self.power_value)
            extPrint(result)
            
    def on_press_timesetup(self, event):
        self.hold_timeup = True
        extPrint("test time")
        self.hold_event_updown()

    def on_release_timesetup(self, event):
        self.hold_timeup = False   
    def hold_event_updown(self):
        if self.hold_timeup == TRUE:
            self.increase_timer_set()
            self.root.after(100, self.hold_event_updown)  # Repeat action every 100ms      
        elif self.hold_powerup == TRUE:
            self.increase_power_set()
            self.root.after(100, self.hold_event_updown)  # Repeat action every 100ms 
            
            
    def increase_timer_set(self):
        if self.time_value <= 300:
            self.time_value +=1
            self.lb_timer_val = Label(self.lay_timer_set,bg='white',font=('arial bold',45),text=str(self.time_value),fg='orange').place(x=150,y=69,width=100,height=45)        
            
    def reduce_timer_set(self):
        if self.time_value > 0:
            self.time_value -=1
            self.lb_timer_val = Label(self.lay_timer_set,bg='white',font=('arial bold',45),text=str(self.time_value),fg='orange').place(x=150,y=69,width=100,height=45)    
            
    def createThreadAdruino(self):
        print ("Create Thread1")
        #self.threading_req = Thread(target=self.requestdata, args=()); 
        if self.threading_rep == None:
            self.threading_rep = Thread(target=self.loadingdata, args=());    
            self.flag_thread_req_rep = True;
            self.threading_rep.start();  
    

    def stopThreadAdruino(self):
        print ("Stop Thread1")     
        try: 
            self.flag_thread_req_rep=False;
            self.threading_rep=None;
        except:
            pass
    def loadingdata(self):
        while self.flag_thread_req_rep:
            
                response = clientCall.requestGET("20002").readline();
 
                data = json.loads(response);
                
                self.origin_data = data['info']
                self.kw1.set(str(self.origin_data['kw1']))
                    #extPrint(self.kw1)
                self.kw2.set(str(self.origin_data['kw2']))
                self.kw3.set(str(self.origin_data['kw3']))
                self.vln1.set(str(self.origin_data['vln1']))
                self.vln2.set(str(self.origin_data['vln2']))
                self.vln3.set(str(self.origin_data['vln3']))
                self.cur1.set(str(self.origin_data['cur1']))
                self.cur2.set(str(self.origin_data['cur2']))
                self.cur3.set(str(self.origin_data['cur3']))
                self.v12.set(str(self.origin_data['v12']))
                self.v23.set(str(self.origin_data['v23']))
                self.v31.set(str(self.origin_data['v31']))
                self.freqq.set(str(self.origin_data['freq']))
                self.tempcc.set(str(self.origin_data['tempc']))
                self.tkw.set(str(self.origin_data['tkw']))

                self.txt_apf_sum.set(str(self.origin_data['avpf']))
                self.txt_aln_sum.set(str(self.origin_data['vln']))
                self.rl_array = data['rls']
                index=0;
                for i in self.rl_array: 
                    if i==1:
                        self.signal_list[index].setonoff(1);
                    else:
                        self.signal_list[index].setonoff(0);
                    index+=1;

                sleep(0.1)
