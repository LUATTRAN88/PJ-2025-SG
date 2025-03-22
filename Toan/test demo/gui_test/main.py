#!/usr/bin/python3

from tkinter import *
from page_1 import *
from page_2 import *
from page_3 import *
from page_4 import *
from page_5 import *
from extend import *

class MAINGUI:
    def __init__(self):
        pass
        # self.current_page = None
        self.current_page=1;
    def create_layout(self):
        self.layout = Tk()
        self.layout.title('test demo')
        self.layout.geometry('1024x600')
        self.layout.config(bg='white')
        self.layout.overrideredirect(1)

        self.layout_btn = Frame(self.layout, bg='yellow')
        self.layout_btn.place(x=0,y=0,width=1024,height=60)

        self.button_main()
        # self.current_page = None
        # self.event_page1(None)
        self.valuerelay_fan_phase=VALUERELAY_FAN_PHASE();


        self.btn_auto_test.bind('<Button-1>', self.event_page1)
        self.btn_manual_test.bind('<Button-1>', self.event_page2)
        self.btn_setting.bind('<Button-1>', self.event_page3)
        self.btn_service.bind('<Button-1>', self.event_page4)
        self.btn_light_auto()
        
        self.aruidno = ard.Arduino();
        self.aruidno.connect_port();
        self.display4 = PAGE4()
        self.display4.adruino=self.aruidno
        self.display4.create_layout(self.layout)
        #self.display4.createThreadAdruino();

        self.display3 = PAGE3()
        self.display3.adruino=self.aruidno
        self.display3.create_layout(self.layout)
        #self.display3.createThreadAdruino();
        self.display3.valuerelay_fan_phase=self.valuerelay_fan_phase;

        self.display2 = PAGE2()
        self.display2.adruino=self.aruidno
        self.display2.create_layout(self.layout)
        #self.display2.createThreadAdruino();
        self.display2.valuerelay_fan_phase=self.valuerelay_fan_phase;

        self.display1 = PAGE1()
        self.display1.adruino=self.aruidno
        self.display1.create_layout(self.layout)
        self.display1.createThreadAdruino();
        self.display1.valuerelay_fan_phase=self.valuerelay_fan_phase;
        

        self.state_ctrl = STATE_M_CONNECTION;
        self.state_margin();
          
    def state_margin(self):
        if self.state_ctrl == STATE_M_CONNECTION:
            
            result=True;
            if result==True:
                self.state_ctrl=STATE_M_CONNECTED;
                self.state_margin()
            else:
                tkinter.messagebox.showinfo('Warning',"Hardware Connection Failed!") 
        elif self.state_ctrl == STATE_M_CONNECTED:
            pass;          

    def stopAllThreadAdruino(self):
        self.display1.stopThreadAdruino()
        self.display2.stopThreadAdruino()
        self.display3.stopThreadAdruino()
        self.display4.stopThreadAdruino()
        if self.display4.display5 is not None:
            self.display4.display5.stopThreadAdruino()
        pass
    def event_page1(self,event):
        try:
            if self.current_page ==1:
                return;
            self.current_page=1;
            self.stopAllThreadAdruino()
            self.display1.createThreadAdruino();
            self.display1.layout1.tkraise()
            self.display1.layout2.tkraise() 
            self.display1.setvalue_fan_phase();
            
            
          
        except:
            pass

    def event_page2(self,event):
        try:
            if self.current_page ==2:
                return;
            self.stopAllThreadAdruino()
            self.current_page =2
            self.display2.createThreadAdruino();
            self.display2.layout1.tkraise()
            self.display2.layout2.tkraise() 
            self.display2.setvalue_fan_phase();
        
          
        except:
            pass
    def event_page3(self,event):
        try:
            if self.current_page ==3:
                return;
            self.stopAllThreadAdruino()
            self.current_page =3
            self.display3.createThreadAdruino();
            self.display3.layout1.tkraise()
            self.display3.layout2.tkraise() 
            self.display3.setvalue_fan_phase();
           
         
        except:
            pass
    def event_page4(self,event):
        try:
            if self.current_page ==4:
                return;
            self.current_page =4
            self.stopAllThreadAdruino()
            self.display4.createThreadAdruino();
            if self.display4.display5 is not None :
                self.display4.display5.stopThreadAdruino();
                self.display4.display5.layout1.destroy();
                self.display4.display5.layout2.destroy();
                self.display4.display5=None;
            self.display4.layout.tkraise()
            self.display4.setvalue_fan_phase();
           
           
        except:
            pass       
        
     
    def button_main(self):
        self.btn_auto_test = Button(self.layout_btn,bd=3,fg='#7D7D7D', bg='white',font=('Arial Bold',20),text='AUTO TEST',command=self.btn_light_auto)
        self.btn_auto_test.place(x=0,y=0,width=256,height=60)

        self.btn_manual_test = Button(self.layout_btn,bd=3,fg='#7D7D7D', bg='white',font=('Arial Bold',20),text='MANUAL TEST',command=self.btn_light_manual)
        self.btn_manual_test.place(x=256,y=0,width=256,height=60)

        self.btn_setting = Button(self.layout_btn,bd=3,fg='#7D7D7D', bg='white',font=('Arial Bold',20),text='SETTING',command=self.btn_light_setting)
        self.btn_setting.place(x=512,y=0,width=256,height=60)

        self.btn_service = Button(self.layout_btn,bd=3,fg='#7D7D7D',bg='white',font=('Arial Bold',20),text='SERVICE',command=self.btn_light_service)
        self.btn_service.place(x=768,y=0,width=256,height=60)

    def btn_light_auto(self):
        self.btn_auto_test.config(fg='black',bg='#ED9121')
        self.btn_manual_test.config(fg='#7D7D7D',bg='white')
        self.btn_setting.config(fg='#7D7D7D',bg='white')
        self.btn_service.config(fg='#7D7D7D',bg='white')
    def btn_light_manual(self):
        self.btn_auto_test.config(fg='#7D7D7D',bg='white')
        self.btn_manual_test.config(fg='black',bg='#ED9121')
        self.btn_setting.config(fg='#7D7D7D',bg='white')
        self.btn_service.config(fg='#7D7D7D',bg='white')
    def btn_light_setting(self):
        self.btn_auto_test.config(fg='#7D7D7D',bg='white')
        self.btn_manual_test.config(fg='#7D7D7D',bg='white')
        self.btn_setting.config(fg='black',bg='#ED9121')
        self.btn_service.config(fg='#7D7D7D',bg='white')
    def btn_light_service(self):
        self.btn_auto_test.config(fg='#7D7D7D',bg='white')
        self.btn_manual_test.config(fg='#7D7D7D',bg='white')
        self.btn_setting.config(fg='#7D7D7D',bg='white')
        self.btn_service.config(fg='black',bg='#ED9121')


display = MAINGUI()
display.create_layout()

mainloop()
















































