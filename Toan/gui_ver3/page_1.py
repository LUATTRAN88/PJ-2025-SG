from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
import threading
from time import sleep
import client as clientCall
import json
from extend import *

class PAGE1:
    def __init__(self):
        self.origin_data = None
        self.is_on = False
        self.power_value = 0
        self.time_value = 0
    def create_layout(self,l1):
        self.layout3 = Frame(l1,bg='white')
        self.layout3.place(x=0,y=64,width=512,height=704)

        self.layout4 = Frame(l1,bg='white')
        self.layout4.place(x=512,y=64,width=512,height=704)

        self.layout5 = Frame(self.layout3,bg='white')
        self.layout5.place(x=0,y=540,width=512,height=160)
        
        self.label_powtime()
        self.tab_button()
        self.label_power()
        
        # self.display = SIGNAL()
        # self.display.create_layout(self.layout5)

        #   Mảng chứa các đối tượng SIGNAL
        self.signal_objects = []
         # Khoảng cách giữa các đối tượng SIGNAL
        # Chiều rộng mỗi khung là 28, cộng thêm khoảng cách 10 pixel giữa chúng
        #   spacing = 38  (là khoảng cách giữa các đối tượng)

        #Tạo và sắp xếp 16 đối tượng SIGNAL
        for i in range(16):
            
            signal = SIGNAL()
            signal.create_layout(self.layout5, x_offset=i * 32.2, text ='RL' + str(i+1) )
            if i==12:
                signal.set_relay_value("FAN");
            elif i==13:
                signal.set_relay_value("Alarm");
            elif i==14:
                signal.set_relay_value("Spar"); 
            elif i==15:
                signal.set_relay_value("Spar"); 
            else:
                signal.set_relay_value("20.0");   
            self.signal_objects.append(signal)

        # signal_13 = SIGNAL()
        # signal_13.create_layout(self.layout5, x_offset=13 * 32.2 , text= 'RL' + str(13+1))
        # signal_13.set_relay_value('Fan')
        # self.signal_objects.append(signal_13)

        # signal_14 = SIGNAL()
        # signal_14.create_layout(self.layout5, x_offset=14 * 32.2 , text= 'RL' + str(14+1))
        # signal_14.set_relay_value('Alarm')
        # self.signal_objects.append(signal_14)

        # signal_15 = SIGNAL()
        # signal_15.create_layout(self.layout5, x_offset=15 * 32.2 , text= 'RL' + str(15+1))
        # signal_15.set_relay_value('Spare')
        # self.signal_objects.append(signal_15)

        # signal_16 = SIGNAL()
        # signal_16.create_layout(self.layout5, x_offset=16 * 32.2 , text= 'RL' + str(16+1))
        # signal_16.set_relay_value('Spare')
        # self.signal_objects.append(signal_16)



            
        self.button_fan()
        secondary_thread = threading.Thread(target = self.loadingdata)
        secondary_thread.start()

    def label_powtime(self):
        fontp = tkFont.Font(family='Helvetica', size=48, weight=tkFont.BOLD )
        fontval = tkFont.Font(family='Helvetica', size=42, weight=tkFont.BOLD )
        self.lb_powset = Label(self.layout3,bg='white',font=fontp,text='POWER\n SET',fg='#2E8B57').place(x=0,y=30,width=255,height=130)
        self.lb_powset_kw = Label(self.layout3,bg='white',font=fontval,text='KW',fg='#8B2252').place(x=350,y=47,width=100,height=100)
        self.lb_powset_val = Label(self.layout3,bg='white',font=fontval,text='0',fg='#8B2252').place(x=255,y=47,width=95,height=100)

        self.lb_time = Label(self.layout3,bg='white',font=fontp,text='TIMER\n SET',fg='#2E8B57').place(x=0,y=210,width=225,height=130)
        self.lb_time_mins = Label(self.layout3,bg='white',font=fontval,text='mins',fg='#8B2252').place(x=320,y=230,width=130,height=100)
        self.lb_time_val = Label(self.layout3,bg='white',font=fontval,text='0',fg='#8B2252').place(x=225,y=230,width=95,height=100)

        fontrun = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_running = Label(self.layout4,bg='white',font=fontrun,text='Running',fg='black').place(x=412,y=0,width=100,height=40)

        self.photola = Image.open(get_path_img()+'lamprun.png')
        self.picla = ImageTk.PhotoImage(self.photola)
        self.lb_lamp_run = Label(self.layout4,bg='white',image=self.picla).place(x=378,y=2,width=40,height=40)

        fontpo = tkFont.Font(family='Helvetica', size=42, weight=tkFont.BOLD )
        self.lb_power = Label(self.layout4,bg='white',font=fontpo,text='POWER',fg='red').place(x=24,y=59,width=220,height=75)
        self.tkw = StringVar()
        self.lb_power_val = Label(self.layout4,bg='white',font=fontpo,textvariable=self.tkw,fg='red').place(x=246,y=59,width=265,height=75)

    def tab_button(self):
        self.photo1 = Image.open(get_path_img()+'up1.png').resize((50,46))
        self.pic1 = ImageTk.PhotoImage(self.photo1)
        self.btn_powset_up = Button(self.layout3,bd=0, bg='white',image=self.pic1,command=lambda:self.increase_powset()).place(x=462,y=43,width=50,height=46)

        self.photo2 = Image.open(get_path_img()+'down1.png').resize((50,46))
        self.pic2 = ImageTk.PhotoImage(self.photo2)
        self.btn_powset_down = Button(self.layout3,bd=0, bg='white',image=self.pic2,command=lambda:self.reduce_powset()).place(x=462,y=98,width=50,height=46)

        self.photo3 = Image.open(get_path_img()+'up1.png').resize((50,46))
        self.pic3 = ImageTk.PhotoImage(self.photo3)
        self.btn_time_up = Button(self.layout3,bd=0,bg='white',image=self.pic3,command=lambda:self.increase_time()).place(x=462,y=232,width=50,height=46)

        self.photo4 = Image.open(get_path_img()+'down1.png').resize((50,46))
        self.pic4 = ImageTk.PhotoImage(self.photo4)
        self.btn_time_down = Button(self.layout3,bd=0,bg='white',image=self.pic4,command=lambda:self.reduce_time()).place(x=462,y=287,width=50,height=46)

        fontb = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.btn_apply = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD APPLY',fg='#8B2252').place(x=0,y=375,width=170,height=65)
        self.btn_stop = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD STOP',fg='#8B2252').place(x=171,y=375,width=170,height=65)
        self.btn_drop = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD DROP',fg='#8B2252').place(x=342,y=375,width=170,height=65)
        self.btn_logging = Button(self.layout3,bd=3,bg='#20B2AA',font=fontb,text='LOAD LOGGING',fg='#8B2252').place(x=0,y=470,width=170,height=65)

    def increase_powset(self):
        if self.power_value < 150:
            self.power_value +=1
            self.lb_powset_val = Label(self.layout3,bg='white',font=('Arial Bold',42),text=str(self.power_value),fg='#8B2252').place(x=255,y=47,width=95,height=100)
            
    def reduce_powset(self):
        if self.power_value > 0:
            self.power_value -=1
            self.lb_powset_val = Label(self.layout3,bg='white',font=('Arial Bold',42),text=str(self.power_value),fg='#8B2252').place(x=255,y=47,width=95,height=100)

    def increase_time(self):
        if self.time_value < 60:
            self.time_value +=1
            self.lb_time_val = Label(self.layout3,bg='white',font=('Arial Bold',42),text=str(self.time_value),fg='#8B2252').place(x=225,y=230,width=95,height=100)
    def reduce_time(self):
        if self.time_value > 0:
            self.time_value -=1
            self.lb_time_val = Label(self.layout3,bg='white',font=('Arial Bold',42),text=str(self.time_value),fg='#8B2252').place(x=225,y=230,width=95,height=100)
    
    def label_power(self):
        fontt = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.tempcc = StringVar()
        self.lb_temp = Label(self.layout4,bg='white',font=fontt,textvariable=self.tempcc,fg='black').place(x=410,y=31,width=100,height=40)
        
        # hàng đàu tiên, hàng đơn vị
        fontri = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD )
        self.lb_pow = Label(self.layout4,bg='white',font=fontri,text='POWER\n KW',fg='black').place(x=65, y=150,width=70,height=50)
        self.lb_volt_ln = Label(self.layout4,bg='white',font=fontri,text='VOLT.\n L-N (V)',fg='black').place(x=136, y=150,width=70,height=50)
        self.lb_current = Label(self.layout4,bg='white',font=fontri,text='CURRENT\n (A)',fg='black').place(x=209, y=150,width=70,height=50)
        self.lb_pf = Label(self.layout4,bg='white',font=fontri,text='PF',fg='black').place(x=280, y=150,width=70,height=50)
        self.lb_none = Label(self.layout4,bg='white').place(x=355, y=150,width=70,height=50)
        self.lb_volt_ll = Label(self.layout4,bg='white',font=fontri,text='VOLT.\n L-L (V)',fg='black').place(x=428, y=150,width=70,height=50)

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
        self.lb_L1 = Label(self.layout4,bg='white',font=fonl1,text='L1',fg='red').place(x=22,y=201,width=43,height=39)
        self.lb_L1_none = Label(self.layout4,bg='white',font=fonl1,text='L1 - L2',fg='red').place(x=353,y=201,width=72,height=39)

        fonl1t = tkFont.Font(family='Helvetica', size=12 )
        self.kw1 = StringVar()
        self.lb_L1_power = Label(self.layout4,bg='white',font=fonl1t,textvariable=self.kw1,fg='red').place(x=66,y=201,width=69,height=39)
        self.vln1 = StringVar()
        self.lb_L1_volt_Ln = Label(self.layout4,bg='white',font=fonl1t,textvariable=self.vln1,fg='red').place(x=137,y=201,width=69,height=39)
        self.cur1 = StringVar()
        self.lb_L1_volt_cur = Label(self.layout4,bg='white',font=fonl1t,textvariable=self.cur1,fg='red').place(x=209,y=201,width=70,height=39)
        self.pf1 = StringVar()
        self.lb_L1_volt_pf = Label(self.layout4,bg='white',font=fonl1t,textvariable=self.pf1,fg='red').place(x=281,y=201,width=70,height=39)
        self.v12 = StringVar()
        self.lb_L1_volt_ll = Label(self.layout4,bg='white',font=fonl1t,textvariable=self.v12,fg='red').place(x=427,y=201,width=71,height=39)

        # hàng L2
        fonl2 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.lb_L2 = Label(self.layout4,bg='white',font=fonl2,text='L2',fg='orange').place(x=21,y=241,width=44,height=39)
        self.lb_L2_none = Label(self.layout4,bg='white',font=fonl2,text='L2 - L3',fg='orange').place(x=353,y=241,width=72,height=39)

        fonl2t = tkFont.Font(family='Helvetica', size=12)
        self.kw2 = StringVar()
        self.lb_L2_power = Label(self.layout4,bg='white',font=fonl2t,textvariable=self.kw2,fg='orange').place(x=66,y=241,width=69,height=39)
        self.vln2 = StringVar()
        self.lb_L2_volt_ln = Label(self.layout4,bg='white',font=fonl2t,textvariable=self.vln2,fg='orange').place(x=137,y=241,width=69,height=39)
        self.cur2 = StringVar()
        self.lb_L2_cur = Label(self.layout4,bg='white',font=fonl2t,textvariable=self.cur2,fg='orange').place(x=209,y=241,width=70,height=39)
        self.pf2 = StringVar()
        self.lb_L2_pf = Label(self.layout4,bg='white',font=fonl2t,textvariable=self.pf2,fg='orange').place(x=282,y=241,width=68,height=39)
        self.v23 = StringVar()
        self.lb_L2_volt_ll = Label(self.layout4,bg='white',font=fonl2t,textvariable=self.v23,fg='orange').place(x=427,y=241,width=72,height=39)

        # hàng L3  
        fonl3 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.lb_L3 = Label(self.layout4,bg='white',font=fonl3,text='L3',fg='blue').place(x=21,y=281,width=44,height=39)
        self.lb_L3_volt_none = Label(self.layout4,bg='white',font=fonl3,text='L3 - L1',fg='blue').place(x=353,y=281,width=72,height=39)

        fonl3t = tkFont.Font(family='Helvetica', size=12 )
        self.kw3 = StringVar()
        self.lb_L3_power = Label(self.layout4,bg='white',font=fonl3t,textvariable=self.kw3,fg='blue').place(x=66,y=281,width=69,height=39)
        self.vln3 = StringVar()
        self.lb_L3_volt_ln = Label(self.layout4,bg='white',font=fonl3t,textvariable=self.vln3,fg='blue').place(x=137,y=281,width=69,height=39)
        self.cur3 = StringVar()
        self.lb_L3_volt_cur = Label(self.layout4,bg='white',font=fonl3t,textvariable=self.cur3,fg='blue').place(x=209,y=281,width=70,height=39)
        self.pf3 = StringVar()
        self.lb_L3_volt_pf = Label(self.layout4,bg='white',font=fonl3t,textvariable=self.pf3 ,fg='blue').place(x=282,y=281,width=68,height=39)
        self.v31 = StringVar()
        self.lb_L3_volt_ll = Label(self.layout4,bg='white',font=fonl3t,textvariable=self.v31,fg='blue').place(x=427,y=281,width=72,height=39)

        # hàng FREQ
        fonl4 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD )
        self.lb_freq = Label(self.layout4,bg='white',font=fonl4,text='FREQ.',fg='black').place(x=21,y=321,width=44,height=39)
        self.lb_freq_cur = Label(self.layout4,bg='white',font=fonl4,text='TEMP.',fg='black').place(x=209,y=321,width=70,height=39)

        fonl4t = tkFont.Font(family='Helvetica', size=12 )
        self.freqq = StringVar()
        self.lb_freq_pow_vol = Label(self.layout4,bg='white',font=fonl4t,textvariable=self.freqq,fg='black').place(x=66,y=321,width=141,height=39)
        self.tempc = StringVar()
        self.lb_freq_cur = Label(self.layout4,bg='white',font=fonl4t,textvariable=self.tempc,fg='black').place(x=282,y=321,width=216,height=39)

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
            
    def loadingdata(self):
        while True:
            try:
                response = clientCall.requestGET('20002');
                if response.status == 200:
                    #parse data
                    data = json.loads(response.read().decode())
                    # print(data)
                    # print(type())
                    self.origin_data = data['data']
                    self.kw1.set(str(self.origin_data['kw1']))
                    #print(self.kw1)
                    self.kw2.set(str(self.origin_data['kw2']))
                    self.kw3.set(str(self.origin_data['kw3']))
                    self.vln1.set(str(self.origin_data['vln1']))
                    self.vln2.set(str(self.origin_data['vln2']))
                    self.vln3.set(str(self.origin_data['vln3']))
                    self.cur1.set(str(self.origin_data['cur1']))
                    self.cur2.set(str(self.origin_data['cur2']))
                    self.cur3.set(str(self.origin_data['cur3']))
                    self.pf1.set(str(self.origin_data['pf1']))
                    self.pf2.set(str(self.origin_data['pf2']))
                    self.pf3.set(str(self.origin_data['pf3']))
                    self.v12.set(str(self.origin_data['v12']))
                    self.v23.set(str(self.origin_data['v23']))
                    self.v31.set(str(self.origin_data['v31']))
                    self.freqq.set(str(self.origin_data['freq'])+' Hz')
                    self.tempc.set(str(self.origin_data['tempc'])+' ºC')
                    self.tempcc.set(str(self.origin_data['tempc'])+' ºC')
                    self.tkw.set(str(self.origin_data['tkw'])+' KW')
                    self.rl_array = self.origin_data['rl']
                    index=0;
                    for i in self.rl_array:
                        self.signal_objects[index].setonoff(i["on"])
                        index+=1;
                    pass
                else:
                   print("Status: {} and reason: {}".format(response.status, response.reason)) 
                
                sleep(1)
            except:
                print("Connect Server Abnormal")
                sleep(1)
           




class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,layout5,text, x_offset=0):
        self.layout =  Frame(layout5,bg='white')
        self.layout.place(x=x_offset,y=13, width=28,height=114)

        self.photol = Image.open(get_path_img()+'lamp.png')
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout, bg='white',image=self.picl)
        self.lb_lamp.place(x=1.5,y=38.4,width=24,height=38)
        
        fontr = tkFont.Font(family='Helvetica', size=8)
        self.lb_relay = Label(self.layout, bg='white',font=fontr,fg='black',text=text).place(x=0,y=7,width=28,height=33)

        fontreva = tkFont.Font(family='Helvetica', size=9)
        self.relay_text_value = StringVar()
        self.lb_relay_val = Label(self.layout, bg='white',font=fontreva,text='20.2',fg='black',textvariable=self.relay_text_value).place(x=0,y=71.4,width=28,height=33)

    def set_relay_value(self,text):
        self.relay_text_value.set(text)
        
    def setonoff(self,val):
        print(val)
        if val == 1:
            img2 = ImageTk.PhotoImage(Image.open(get_path_img()+'lamp.png'))
            self.lb_lamp.configure(image=img2)
            self.lb_lamp.image=img2
        else:
            img3 = ImageTk.PhotoImage(Image.open(get_path_img()+'lamp_off.png'))
            self.lb_lamp.configure(image=img3)
            self.lb_lamp.image=img3
            
           
            
        

        

   




       