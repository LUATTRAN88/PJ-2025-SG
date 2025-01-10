from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from prac_1 import *
from prac_2 import *
from prac_3 import *
from prac_4 import *
class MAINGUI:
    def __init__(self):
        pass
    def create_layout(self):
        self.layout = Tk()
        self.layout.title('demo project')
        self.layout.config(bg='#C1CDCD')
        self.layout.geometry('640x480')

        # layout1 chứa tab_button / layout2 chứa label_light
        self.layout2 = Frame(self.layout,bg='#303030',width=636,height=62)
        self.layout2.place(x=2,y=0)

        self.layout1 = Frame(self.layout,bg='yellow',width=636,height=56)
        self.layout1. place(x=1,y=3)

        self.tab_button()
        self.display1 = PAGE1()
        self.display1.create_layout(self.layout)
        
    # gọi thêm nhiều hơn 1 sự kiện cho button 
        self.button1.bind('<Button-1>', self.event_page1)
        self.button2.bind('<Button-1>', self.event_page2)
        self.button3.bind('<Button-1>', self.event_page3)
        self.button4.bind('<Button-1>', self.event_page4)
    # tạo sự kiện mới cho button
    def event_page1(self,event):
        self.display1 = PAGE1()
        self.display1.create_layout(self.layout)
    def event_page2(self,event):
        self.display2 = PAGE2()
        self.display2.create_layout(self.layout)
    def event_page3(self,event):
        self.display3 = PAGE3()
        self.display3.create_layout(self.layout)
    def event_page4(self,event):
        self.display4 = PAGE4()
        self.display4.create_layout(self.layout)
        
    def tab_button(self):
        helv36 = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD )
        self.button1 = Button(self.layout1,bg='#303030',font=helv36,bd=2,text='Display',fg='#7FFF00',command=lambda:self.label_light1())
        self.button1.place(x=0,y=0,width=159, height=56)

        self.button2 = Button(self.layout1,bg='#303030', font=helv36, text='Control',fg='#7FFF00',command=lambda:self.label_light2())
        self.button2.place(x=159,y=0,width=159, height=56)
        
        self.button3 = Button(self.layout1,bg='#303030',font=helv36,text='Demo',fg='#7FFF00',command=lambda:self.label_light3())
        self.button3.place(x=318,y=0,width=159, height=56)
        
        self.button4 = Button(self.layout1,bg='#303030',text='Setting', font=helv36,fg='#7FFF00',command=lambda:self.label_light4())
        self.button4.place(x=477,y=0,width=159, height=56)

    def label_light1(self):
        color1 = '#7FFF00'
        color2 = '#303030'
        self.label1 = Label(self.layout2,bg=color1).place(x=0,y=0,width=159,height=62)
        self.label2 = Label(self.layout2,bg=color2).place(x=159,y=0,width=159,height=62)
        self.label3 = Label(self.layout2, bg=color2).place(x=318,y=0,width=159,height=62)
        self.label4 = Label(self.layout2, bg=color2).place(x=477,y=0,width=159,height=62)
    def label_light2(self):
        color1 = '#7FFF00'
        color2 = '#303030'
        self.label2 = Label(self.layout2,bg=color1).place(x=159,y=0,width=159,height=62)
        self.label1 = Label(self.layout2,bg=color2).place(x=0,y=0,width=159,height=62)
        self.label3 = Label(self.layout2, bg=color2).place(x=318,y=0,width=159,height=62)
        self.label4 = Label(self.layout2, bg=color2).place(x=477,y=0,width=159,height=62)
    def label_light3(self):
        color1 = '#7FFF00'
        color2 = '#303030'
        self.label3 = Label(self.layout2, bg=color1).place(x=318,y=0,width=159,height=62)
        self.label1 = Label(self.layout2,bg=color2).place(x=0,y=0,width=159,height=62)
        self.label2 = Label(self.layout2,bg=color2).place(x=159,y=0,width=159,height=62)
        self.label4 = Label(self.layout2, bg=color2).place(x=477,y=0,width=159,height=62)
    def label_light4(self):
        color1 = '#7FFF00'
        color2 = '#303030'
        self.label4 = Label(self.layout2, bg=color1).place(x=477,y=0,width=159,height=62)
        self.label1 = Label(self.layout2,bg=color2).place(x=0,y=0,width=159,height=62)
        self.label2 = Label(self.layout2,bg=color2).place(x=159,y=0,width=159,height=62)
        self.label3 = Label(self.layout2, bg=color2).place(x=318,y=0,width=159,height=62)
   
display = MAINGUI()
display.create_layout()


mainloop()
