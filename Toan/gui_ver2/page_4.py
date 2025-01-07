from tkinter import *
from tkinter import ttk

class PAGE3:
    def __init__(self):
        pass
    def Progressbar(self,l4):
        layout4 = Frame(l4, bg='#DCDCDC')
        layout4.place(x=0,y=61,width=640,height=420)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar", background='red')

        my_scale1 = Scale(layout4, from_=0, to=100, orient='vertical',length=200)
        # my_scale1.set(75) # default value of slider kept at 75 
        my_scale1.grid(row=0,column=0,columnspan=3) 
        my_scale1.place(x=0, y=150)

mainloop()




# import tkinter as tk
# from tkinter import ttk
# my_w = tk.Tk()
# my_w.geometry("400x300") 

# s = ttk.Style()
# s.theme_use('alt')
# s.configure("red.Horizontal.TProgressbar", background='red')
# s.configure("yellow.Horizontal.TProgressbar", background='yellow')
# s.configure("green.Horizontal.TProgressbar", background='green')

# l1=tk.Label(my_w,text='Changing style of Progress bar',font=16,bg='yellow')
# l1.grid(row=0,column=0,columnspan=3,pady=15)

# prg1=ttk.Progressbar(my_w,length=320,mode='determinate',maximum=100,value=75,
# style='yellow.Horizontal.TProgressbar')
# prg1.grid(row=1,column=0,columnspan=3,padx=20,pady=45) 

# def my_upd(value): # update the progress bar using scale input
#     prg1['value'] =my_scale1.get() 

# b1=tk.Button(my_w,text='Red',bg='red',font=20,
# 	command=lambda:prg1.config(style='red.Horizontal.TProgressbar'))
# b1.grid(row=2,column=0)
# b2=tk.Button(my_w,text='Yellow',bg='yellow',font=20,
# 	command=lambda:prg1.config(style='yellow.Horizontal.TProgressbar'))
# b2.grid(row=2,column=1)
# b3=tk.Button(my_w,text='Green',bg='lightgreen',font=20,
# 	command=lambda:prg1.config(style='green.Horizontal.TProgressbar'))
# b3.grid(row=2,column=2)

# my_scale1 = tk.Scale(my_w, from_=0, to=100, orient='vertical'
#     ,command=my_upd,length=200)
# my_scale1.set(75) # default value of slider kept at 75 
# my_scale1.grid(row=3,column=0,columnspan=3) 
# my_scale1.place(x=0, y=20)
# my_w.mainloop()