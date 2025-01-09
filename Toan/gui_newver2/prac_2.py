from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

class PAGE2:
    def __init__(self):
        pass
    def create_layout(self,l2):
        self.layout = Frame(l2, bg='#458B74')
        self.layout.place(x=2,y=64,width=636,height=415)

        self.relays = []

        # Vòng lặp tạo 12 đối tượng RELAYS_CONTROL
        for i in range(12):
            relay = RELAYS_CONTROL()
            self.relays.append(relay)

            # Tính toán vị trí x, y cho từng đối tượng
            c = (i % 6) * 106 + 2  # Cách nhau 105 pixel, tối đa 4 cột
            h = (i // 6) * 207 + 2  # Cách nhau 210 pixel theo hàng

            # Tạo layout cho từng đối tượng
            relay.create_layout(self.layout, c, h, text='Relay ' + str(i+1) )
            # relay.set_name_relay('Relay ' + str(i))

class RELAYS_CONTROL:
    def __init__(self):
        self.is_on = True
    def create_layout(self,layout, c, h, text):
        self.relay1 = Frame(layout, bg='#F0FFFF')
        self.relay1.place(x=c,y=h,width=103,height=204)

        self.label1=Label(self.relay1,bg='blue',text=text, fg='white', font=('Arial',13,'bold'))
        self.label1.place(x=0,y=0,width=103,height=21)     
            
        self.label3=Label(self.relay1,bg='#0000CD',text='Auto', fg='white', font=('Arial',12,'bold'))
        self.label3.place(x=13,y=47,width=77,height=19)
            
        photoc = Image.open('clock.png')
        self.picc = ImageTk.PhotoImage(photoc)
        self.clock=Label(self.relay1,bg='#E0EEEE',image=self.picc)
        self.clock.place(x=13,y=65,width=77,height=34)
            
        self.label4=Label(self.relay1,bg='#C1CDCD',text='Setting', fg='blue', font=('Arial',9))
        self.label4.place(x=13,y=99,width=77,height=19)

        self.button_toggle()
        
    def button_toggle(self):
        a1 = Image.open('on123.png').resize((85,81))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('off123.png').resize((85,81))
        self.off = ImageTk.PhotoImage(a2)

        self.button_on = Button(self.relay1,image=self.on, bd=0,command= self.button_toggle)
        self.button_on.place(x=9,y=121,width=85,height=81)

        if self.is_on:
            self.button_on.config(image=self.off)
            photo0 = Image.open('module0.png')
            m0= photo0.resize((77,26))
            self.pic0 = ImageTk.PhotoImage(m0)
            self.label2=Label(self.relay1,bg='#E0EEEE',text='Module 1', fg='#007FFF', font=('Arial',9),image=self.pic0)
            self.label2.place(x=13,y=21,width=77,height=26)
            self.is_on = False 
        else:
            self.button_on.config(image=self.on)
            photo1 = Image.open('module1.png')
            m1 = photo1.resize((77,26))
            self.pic1 = ImageTk.PhotoImage(m1)
            self.label2=Label(self.relay1,bg='#E0EEEE',text='Module 1', fg='#007FFF', font=('Arial',9),image=self.pic1)
            self.label2.place(x=13,y=21,width=77,height=26)
            self.is_on = True

    # def set_name_relay(self,name):
    #     self.label1.config(text=name)
        