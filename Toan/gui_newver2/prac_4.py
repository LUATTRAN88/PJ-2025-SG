from tkinter import *
from PIL import ImageTk, Image
from tkinter import font as tkFont

class PAGE4:
    def __init__(self):
        self.is_on = True
    def create_layout(self,l4):
        self.layout = Frame(l4,bg='#76EEC6',).place(x=2,y=64,width=636,height=412)
        self.button_luat()

    def button_luat(self):
        a1 = Image.open('lula.png').resize((200,200))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('lu.png').resize((200,200))
        self.off = ImageTk.PhotoImage(a2)

        self.button_on = Button(self.layout,image=self.on,bg='#76EEC6', bd=0,command= self.button_luat)
        self.button_on.place(x=214,y=75,width=200,height=200)

        if self.is_on:
            self.button_on.config(image=self.off)
            hel1 = tkFont.Font(family='Helvetica', size=26, weight=tkFont.BOLD )
            self.label2=Label(self.layout,bg='#76EEC6',text='Law Fast hi everybody',fg='#008B00',font=hel1).place(x=125,y=280,width=380,height=110)
            self.is_on = False 
        else:
            self.button_on.config(image=self.on,)
            hel2 = tkFont.Font(family='Helvetica', size=26, weight=tkFont.BOLD )
            self.label2=Label(self.layout,bg='#76EEC6',text='Team Project 2025',fg='#008B00',font=hel2).place(x=125,y=275,width=380,height=70)
            self.label3=Label(self.layout,bg='#76EEC6',text='Happy New Year',fg='#008B00',font=hel2).place(x=125,y=332,width=380,height=45)
            
            photof = Image.open('flower.png').resize((40,40))
            self.picf = ImageTk.PhotoImage(photof)
            
            self.label4=Label(self.layout,bg='#76EEC6',image=self.picf).place(x=251,y=389,width=40,height=40)
            self.label5=Label(self.layout,bg='#76EEC6',image=self.picf).place(x=296,y=389,width=40,height=40)
            self.label6=Label(self.layout,bg='#76EEC6',image=self.picf).place(x=341,y=389,width=40,height=40)
            self.is_on = True

    

