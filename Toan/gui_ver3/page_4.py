from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

class PAGE4:
    def __init__(self):
        self.is_on = False
    def create_layout(self,l4):
        self.layout = Frame(l4,bg='#C1CDCD')
        self.layout.place(x=0,y=64,width=1024,height=704)

        self.label_power()
        self.button_fan()
        self.signal_objects = []
        for i in range(16):
            signal = SIGNAL()
            signal.create_layout(self.layout, x_offset=i * 32.2, text ='RL' + str(i+1) )
                    
            if i==12:
                signal.set_relay_value('Fan')
            elif i==13:
                signal.set_relay_value('Alrm')
            elif i==14:
                signal.set_relay_value('Spar')
            elif i==15:
                signal.set_relay_value('Spar')
            else:
                signal.set_relay_value('20.0')

            self.signal_objects.append(signal)
        self.display_cal = CALCULATOR()
        self.display_cal.create_layout(self.layout)


    def label_power(self):
        fontrun = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_running = Label(self.layout,bg='#C1CDCD',font=fontrun,text='Running',fg='black').place(x=924,y=0,width=100,height=40)

        self.photola = Image.open('lamp4.png')
        self.picla = ImageTk.PhotoImage(self.photola)
        self.lb_lamp_run = Label(self.layout,bg='#C1CDCD',image=self.picla).place(x=890,y=2,width=40,height=40)

        fontt = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD )
        self.lb_temp = Label(self.layout,bg='#C1CDCD',font=fontt,text='35.2 ºC',fg='black').place(x=922,y=31,width=100,height=40)
        
        # label logo
        fonlogo = tkFont.Font(family='Helvetica', size=50, weight=tkFont.BOLD )
        self.label_logo = Label(self.layout, bg='#C1CDCD',text='LOGO',font=fonlogo,fg='black').place(x=732, y=458,width=270,height=170)
   
    def button_fan(self):
        a1 = Image.open('fan_on.png').resize((170,170))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('fan_off.png').resize((170,170))
        self.off = ImageTk.PhotoImage(a2)

        self.btn_on = Button(self.layout,image=self.on,bg='#C1CDCD', bd=0,command=lambda:self.button_fan())
        self.btn_on.place(x=540,y=460,width=170,height=170)

        if self.is_on:
            self.btn_on.config(image=self.off)
            self.is_on = False 
        else:
            self.btn_on.config(image=self.on)
            self.is_on = True


class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,layout,text, x_offset=0):
        self.layout9 =  Frame(layout,bg='#C1CDCD')
        self.layout9.place(x=x_offset,y=553, width=28,height=114)

        self.photol = Image.open('lamp4.png')
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout9, bg='#C1CDCD',image=self.picl).place(x=1.5,y=38.4,width=24,height=38)
        
        fontr = tkFont.Font(family='Helvetica', size=8)
        self.lb_relay = Label(self.layout9, bg='#C1CDCD',font=fontr,fg='black',text=text).place(x=0,y=7,width=28,height=33)

        fontreva = tkFont.Font(family='Helvetica', size=9)
        self.relay_text_value = StringVar()
        self.lb_relay_val = Label(self.layout9, bg='#C1CDCD',font=fontreva,text='20.2',fg='black',textvariable=self.relay_text_value).place(x=0,y=71.4,width=28,height=33)

    def set_relay_value(self,text):
        self.relay_text_value.set(text)
        pass


class CALCULATOR:  
    def __init__(self):
        pass
    def create_layout(self,layout):
        self.layout10 = Frame(layout,bg='brown')
        self.layout10.place(x=348, y=20,width=331,height=414)

        self.layout11 = Frame(self.layout10,bg='#53868B')
        self.layout11.place(x=0,y=70,width=331,height=344)

        self.equation = StringVar()
        self.entry_value=''
        Entry(self.layout10,bg='#fff',justify='center',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0,width=331,height=70)

        self.b1=Button(self.layout11,font=('Arial Bold',20),text='Tab',relief='flat',bg='#7AC5CD',command=lambda:self.show('Tab')).place(x=0, y=0,width=82, height=68)
        self.b2=Button(self.layout11,font=('Arial Bold',25),text='/',relief='flat',bg='#7AC5CD',command=lambda:self.show('/')).place(x=82.5, y=0,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='*',relief='flat',bg='#7AC5CD',command=lambda:self.show('*')).place(x=166, y=0,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',20),text='BS',relief='flat',bg='#7AC5CD',command=lambda:self.show('BS')).place(x=248.5, y=0,width=82, height=68)

        Button(self.layout11,font=('Arial Bold',25),text='7',relief='flat',bg='#7AC5CD',command=lambda:self.show('7')).place(x=0, y=69,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='8',relief='flat',bg='#7AC5CD',command=lambda:self.show('8')).place(x=82.5, y=69,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='9',relief='flat',bg='#7AC5CD',command=lambda:self.show('9')).place(x=166, y=69,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='_',relief='flat',bg='#7AC5CD',command=lambda:self.show('-')).place(x=249, y=69,width=82, height=68)

        Button(self.layout11,font=('Arial Bold',25),text='4',relief='flat',bg='#7AC5CD',command=lambda:self.show('4')).place(x=0, y=138,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='5',relief='flat',bg='#7AC5CD',command=lambda:self.show('5')).place(x=83, y=138,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='6',relief='flat',bg='#7AC5CD',command=lambda:self.show('6')).place(x=166, y=138,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='+',relief='flat',bg='#7AC5CD',command=lambda:self.show('+')).place(x=249, y=138,width=82, height=68)

        Button(self.layout11,font=('Arial Bold',25),text='1',relief='flat',bg='#7AC5CD',command=lambda:self.show('1')).place(x=0, y=207,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='2',relief='flat',bg='#7AC5CD',command=lambda:self.show('2')).place(x=82.5, y=207,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='3',relief='flat',bg='#7AC5CD',command=lambda:self.show('3')).place(x=166, y=207,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',22),text='Enter',relief='flat',bg='#7AC5CD',command=lambda:self.show('')).place(x=249, y=207,width=82, height=136.5)

        Button(self.layout11,font=('Arial Bold',25),text='0',relief='flat',bg='#7AC5CD',command=lambda:self.show('0')).place(x=0, y=276,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='00',relief='flat',bg='#7AC5CD',command=lambda:self.show('00')).place(x=82.5, y=276,width=82, height=68)
        Button(self.layout11,font=('Arial Bold',25),text='.',relief='flat',bg='#7AC5CD',command=lambda:self.show('.')).place(x=166, y=276,width=82, height=68)




    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

















# self.lb_monitor = Label(self.layout,bg='white').place(x=350,y=30,width=320,height=60)