from tkinter import *
from PIL import *
from page_1 import *
from page_2 import *
from PIL import ImageTk, Image
from tkinter import font as tkFont
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

  
class MAINLAYOUT:
    def __init__(self):
        pass
    def create_layout(self):
        self.layout = Tk();
        self.layout.title('BLU Application');
        self.layout.geometry('640x480');
        self.layout.config(bg='#DCDCDC');
        layout1 = Frame( self.layout, bg='yellow',width=636,height=56)
        layout1.place(x=2,y=0)
        
        layout2 = Frame( self.layout, bg='#DCDCDC',width=636,height=4)
        layout2.place(x=2,y=56)
        self.tab_button(layout1,layout2);
        self.label_light1(layout2);
    
        self.display1=PAGE1();
        self.display1.create_layout( self.layout);
        # self.display1.show();
        # self.display2=PAGE2();
        # self.display2.create_layout( self.layout);
        # self.display2.hide();



    # tạo thêm sự kiện cho button
        self.button1.bind('<Button-1>',self.callTabevent1 );
        self.button2.bind('<Button-1>',self.callTabevent2 );
    
    def callTabevent1(self,event):
        self.display1=PAGE1();
        self.display1.create_layout(self.layout);
        pass
    def callTabevent2(self,event):
        self.display2=PAGE2();
        self.display2.create_layout(self.layout);
        pass
    
    # layout1 chứa tab_button / layout2 chứa label_light cho button
    def tab_button(self,layout1,layout2):
        helv36 = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD )
        self.button1 = Button(layout1,bg='#303030',font=helv36, text='Settings', fg='#00FFFF',command=lambda: self.label_light1(layout2))
        self.button1.place(x=0,y=0,width=106, height=56)
        
        self.button2 = Button(layout1,bg='#303030', font=helv36, text='Parameter',fg='#00FFFF',command=lambda: self.label_light2(layout2))
        self.button2.place(x=106,y=0,width=106, height=56)
        
        self.button3 = Button(layout1,bg='#303030',font=helv36,text='Run',fg='#00FFFF',command=lambda: self.label_light3(layout2))
        self.button3.place(x=212,y=0,width=106, height=56)
        
        self.button4 = Button(layout1,bg='#303030',text='Pause', font=helv36,fg='#00FFFF',command=lambda: self.label_light4(layout2))
        self.button4.place(x=318,y=0,width=106, height=56)
        
        self.button5 = Button(layout1,bg='#303030', text='Stop', font=helv36,fg='#00FFFF',command=lambda: self.label_light5(layout2))
        self.button5.place(x=424,y=0,width=106, height=56)
        
        photo = Image.open('home.png')
        self.pic = ImageTk.PhotoImage(photo)
        self.button6 = Button(layout1,bg='#303030', image=self.pic,command=lambda: self.label_light6(layout2))
        self.button6.place(x=530,y=0,width=106, height=56)

    def label_light1(self,layout2):
        color1 = '#00FFFF'
        color2 = '#303030'      
        self.label1 = Label(layout2, bg=color1).place(x=0,y=0,width=106,height=4)
        self.label2 = Label(layout2, bg=color2).place(x=106,y=0,width=106,height=4)
        self.label3 = Label(layout2, bg=color2).place(x=212,y=0,width=106,height=4)
        self.label4 = Label(layout2, bg=color2).place(x=318,y=0,width=106,height=4)
        self.label5 = Label(layout2, bg=color2).place(x=424,y=0,width=106,height=4)
        self.label6 = Label(layout2, bg=color2).place(x=530,y=0,width=106,height=4)
    def label_light2(self,layout2):
        color1 = '#00FFFF'
        color2 = '#303030'       
        self.label2 = Label(layout2, bg=color1).place(x=106,y=0,width=106,height=4)      
        self.label1 = Label(layout2, bg=color2).place(x=0,y=0,width=106,height=4)
        self.label3 = Label(layout2, bg=color2).place(x=212,y=0,width=106,height=4)
        self.label4 = Label(layout2, bg=color2).place(x=318,y=0,width=106,height=4)
        self.label5 = Label(layout2, bg=color2).place(x=424,y=0,width=106,height=4)
        self.label6 = Label(layout2, bg=color2).place(x=530,y=0,width=106,height=4)  
    def label_light3(self,layout2):
        color1 = '#00FFFF'
        color2 = '#303030'       
        self.label3 = Label(layout2, bg=color1).place(x=212,y=0,width=106,height=4)     
        self.label1 = Label(layout2, bg=color2).place(x=0,y=0,width=106,height=4)
        self.label2 = Label(layout2, bg=color2).place(x=106,y=0,width=106,height=4)
        self.label4 = Label(layout2, bg=color2).place(x=318,y=0,width=106,height=4)
        self.label5 = Label(layout2, bg=color2).place(x=424,y=0,width=106,height=4)
        self.label6 = Label(layout2, bg=color2).place(x=530,y=0,width=106,height=4) 
    def label_light4(self,layout2):
        color1 = '#00FFFF'
        color2 = '#303030'      
        self.label4 = Label(layout2, bg=color1).place(x=318,y=0,width=106,height=4)      
        self.label1 = Label(layout2, bg=color2).place(x=0,y=0,width=106,height=4)
        self.label2 = Label(layout2, bg=color2).place(x=106,y=0,width=106,height=4)   
        self.label3 = Label(layout2, bg=color2).place(x=212,y=0,width=106,height=4)
        self.label5 = Label(layout2, bg=color2).place(x=424,y=0,width=106,height=4)
        self.label6 = Label(layout2, bg=color2).place(x=530,y=0,width=106,height=4)
    def label_light5(self,layout2):
        color1 = '#00FFFF'
        color2 = '#303030'     
        self.label5 = Label(layout2, bg=color1).place(x=424,y=0,width=106,height=4)      
        self.label1 = Label(layout2, bg=color2).place(x=0,y=0,width=106,height=4)
        self.label2 = Label(layout2, bg=color2).place(x=106,y=0,width=106,height=4)  
        self.label3 = Label(layout2, bg=color2).place(x=212,y=0,width=106,height=4)
        self.label4 = Label(layout2, bg=color2).place(x=318,y=0,width=106,height=4)
        self.label6 = Label(layout2, bg=color2).place(x=530,y=0,width=106,height=4)
    def label_light6(self,layout2):
        color1 = '#00FFFF'
        color2 = '#303030'      
        self.label6 = Label(layout2, bg=color1).place(x=530,y=0,width=106,height=4)      
        self.label1 = Label(layout2, bg=color2).place(x=0,y=0,width=106,height=4)
        self.label2 = Label(layout2, bg=color2).place(x=106,y=0,width=106,height=4) 
        self.label3 = Label(layout2, bg=color2).place(x=212,y=0,width=106,height=4)
        self.label4 = Label(layout2, bg=color2).place(x=318,y=0,width=106,height=4)
        self.label5 = Label(layout2, bg=color2).place(x=424,y=0,width=106,height=4)

mainlayout= MAINLAYOUT();
mainlayout.create_layout();

# def callevent(event):
#     print("hello")
# display1=PAGE1();
# display1.create_layout(layout);
# display1.button1.bind("<Button-1>",callevent);

# display2=PAGE2();
# display2.layout_page2(layout);


mainloop()

