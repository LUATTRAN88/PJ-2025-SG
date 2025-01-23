from pathlib import Path
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from time import strftime

def get_path_img():
    path=Path(__file__).parent.resolve()
    final_path=str(path.as_posix())+'/img/'
    return final_path






class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,lay_button_relay,x,y,text):
        self.layout =  Frame(lay_button_relay,bg='white')
        self.layout.place(x=x+1,y=y, width=28,height=46)

        self.photol = Image.open(get_path_img()+'lamp_on.png').resize((17,17))
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout, bg='white',image=self.picl)
        self.lb_lamp.place(x=0,y=12,width=28,height=23)
        
        
        self.lb_relay = Label(self.layout, bg='white',font=('arial bold',8),fg='black',text=text).place(x=0,y=0,width=28,height=11)

        self.text_relay = StringVar()
        self.lb_relay_val = Label(self.layout, bg='white',font=('arial bold',8),fg='black',textvariable=self.text_relay).place(x=0,y=36,width=28,height=11)
        pass



def timeset(ly):
    l1=Label(ly,font=('arial', 15),bg='white')
    l1.place(x=180,y=7,width=210,height=20)
    time_string = strftime('%H:%M:%S %p %x') # time format 
    l1.config(text=time_string)
    l1.after(1000,timeset) # time delay of 1000 milliseconds 