# from tkinter import *
# from tkinter import font as tkFont
# from PIL import ImageTk, Image
# from page_1 import *
# from page_2 import *
# from page_3 import *
# from page_4 import *


# class MAINGUI:
#     def __init__(self):
#         self.flag=1
#         pass
#     def create_layout(self):
#         self.layout = Tk()
#         self.layout.title('AC Load Bank')
#         self.layout.geometry('1024x768')
#         self.layout.config(bg='#C1CDCD')

#         # layout1 chứa tab_button / layout2 chứa label_light
#         self.layout2 = Frame(self.layout,bg='#303030',width=1024,height=64)
#         self.layout2.place(x=0,y=0)

#         self.layout1 = Frame(self.layout,bg='yellow',width=1024,height=56)
#         self.layout1. place(x=0,y=4)

#         self.tab_button()

#         self.button1.bind('<Button-1>', self.event_page1)
#         self.button2.bind('<Button-1>', self.event_page2)
#         self.button3.bind('<Button-1>', self.event_page3)
#         self.button4.bind('<Button-1>', self.event_page4)
#         self.display1 = PAGE1()
#         # self.display1.create_layout(self.layout)  
#         # self.display1.show()
#         self.display2 = PAGE2()
#         # self.display2.create_layout(self.layout)  
#         # self.display2.hide()
#         # self.display3 = PAGE3()
#         # self.display3.create_layout(self.layout)  
#         # self.display4 = PAGE4()
#         # self.display4.create_layout(self.layout)  

#     def event_page1(self,event):
        
#         print('page1')
#         self.display2.hide();
#         self.display1.create_layout(self.layout) 
        
#     def event_page2(self,event):
#         print('page2')
#         self.display1.hide()
#         self.display2.create_layout(self.layout)
#     def event_page3(self,event):
#         display3 = PAGE3()
#         display3.create_layout(self.layout)
#     def event_page4(self,event):
#         display4 = PAGE4()
#         display4.create_layout(self.layout)    

#     def tab_button(self):
#         helv36 = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD )
#         self.button1 = Button(self.layout1,bg='#303030',font=helv36,bd=2,text='AUTO TEST',fg='#00CDCD',command=lambda:self.label_light1())
#         self.button1.place(x=0,y=0,width=256, height=56)

#         self.button2 = Button(self.layout1,bg='#303030', font=helv36, text='MANUAL TEST',fg='#00CDCD',command=lambda:self.label_light2())
#         self.button2.place(x=256,y=0,width=256, height=56)
        
#         self.button3 = Button(self.layout1,bg='#303030',font=helv36,text='SETTING',fg='#00CDCD',command=lambda:self.label_light3())
#         self.button3.place(x=512,y=0,width=256, height=56)
        
#         self.button4 = Button(self.layout1,bg='#303030',text='SERVICE', font=helv36,fg='#00CDCD',command=lambda:self.label_light4())
#         self.button4.place(x=768,y=0,width=256, height=56)

#     def label_light1(self):
#         color1 = '#7FFF00'
#         color2 = '#00CDCD'
#         color3 = '#303030'
#         self.label1 = Label(self.layout2,bg=color1).place(x=0,y=0,width=256,height=64)
#         self.label2 = Label(self.layout2,bg=color3).place(x=256,y=0,width=256,height=64)
#         self.label3 = Label(self.layout2, bg=color3).place(x=512,y=0,width=256,height=64)
#         self.label4 = Label(self.layout2, bg=color3).place(x=768,y=0,width=256,height=64)
#         self.button1.config(fg=color1)
#         self.button2.config(fg=color2)
#         self.button3.config(fg=color2)
#         self.button4.config(fg=color2)
#     def label_light2(self):
#         color1 = '#7FFF00'
#         color2 = '#00CDCD'
#         color3 = '#303030'
#         self.label2 = Label(self.layout2,bg=color1).place(x=256,y=0,width=256,height=64)
#         self.label1 = Label(self.layout2,bg=color3).place(x=0,y=0,width=256,height=64)
#         self.label3 = Label(self.layout2, bg=color3).place(x=512,y=0,width=256,height=64)
#         self.label4 = Label(self.layout2, bg=color3).place(x=768,y=0,width=256,height=64)
#         self.button2.config(fg=color1)
#         self.button1.config(fg=color2)
#         self.button3.config(fg=color2)
#         self.button4.config(fg=color2)
#     def label_light3(self):
#         color1 = '#7FFF00'
#         color2 = '#00CDCD'
#         color3 = '#303030'
#         self.label3 = Label(self.layout2, bg=color1).place(x=512,y=0,width=256,height=64)
#         self.label1 = Label(self.layout2,bg=color3).place(x=0,y=0,width=256,height=64)
#         self.label2 = Label(self.layout2,bg=color3).place(x=256,y=0,width=256,height=64)
#         self.label4 = Label(self.layout2, bg=color3).place(x=768,y=0,width=256,height=64)
#         self.button3.config(fg=color1)
#         self.button1.config(fg=color2)
#         self.button2.config(fg=color2)
#         self.button4.config(fg=color2)
#     def label_light4(self):
#         color1 = '#7FFF00'
#         color2 = '#00CDCD'
#         color3 = '#303030'
#         self.label4 = Label(self.layout2, bg=color1).place(x=768,y=0,width=256,height=64)
#         self.label1 = Label(self.layout2,bg=color3).place(x=0,y=0,width=256,height=64)
#         self.label2 = Label(self.layout2,bg=color3).place(x=256,y=0,width=256,height=64)
#         self.label3 = Label(self.layout2, bg=color3).place(x=512,y=0,width=256,height=64)
#         self.button4.config(fg=color1)
#         self.button1.config(fg=color2)
#         self.button2.config(fg=color2)
#         self.button3.config(fg=color2)


# display = MAINGUI()
# display.create_layout()

# mainloop()


from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from page_1 import *
from page_2 import *
from page_3 import *
from page_4 import *

class MAINGUI:
    def __init__(self):
        self.current_page = None  # Keep track of the currently active page

    def create_layout(self):
        self.layout = Tk()
        self.layout.title('demo project')
        self.layout.config(bg='#C1CDCD')
        self.layout.geometry('1024x768')
        # self.layout.resizable(False,False)

        # layout1 contains tab_button / layout2 contains label_light
       
#         # layout1 chứa tab_button / layout2 chứa label_light
        self.layout2 = Frame(self.layout,bg='#303030',width=1024,height=64)
        self.layout2.place(x=0,y=0)

        self.layout1 = Frame(self.layout,bg='yellow',width=1024,height=56)
        self.layout1. place(x=0,y=4)


        self.tab_button()
        self.event_page1(None)  # Default to PAGE1 on startup

        # Bind buttons to respective events
        self.button1.bind('<Button-1>', self.event_page1)
        self.button2.bind('<Button-1>', self.event_page2)
        self.button3.bind('<Button-1>', self.event_page3)
        self.button4.bind('<Button-1>', self.event_page4)

    # Destroy current page and load PAGE1
    def event_page1(self, event):
        self._destroy_current_page()
        self.display1 = PAGE1()
        self.display1.create_layout(self.layout)
        self.current_page = self.display1

    # Destroy current page and load PAGE2
    def event_page2(self, event):
        self._destroy_current_page()
        self.display2 = PAGE2()
        self.display2.create_layout(self.layout)
        self.current_page = self.display2

    # Destroy current page and load PAGE3
    def event_page3(self, event):
        self._destroy_current_page()
        self.display3 = PAGE3()
        self.display3.create_layout(self.layout)
        self.current_page = self.display3

    # Destroy current page and load PAGE4
    def event_page4(self, event):
        self._destroy_current_page()
        self.display4 = PAGE4()
        self.display4.create_layout(self.layout)
        self.current_page = self.display4

    # Destroy the currently active page if it exists
    def _destroy_current_page(self):
        if self.current_page is not None:
            for widget in self.layout.winfo_children():
                if widget != self.layout1 and widget != self.layout2:
                    widget.destroy()

    def tab_button(self):
        helv36 = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD)
        self.button1 = Button(self.layout1, bg='#303030', font=helv36, bd=2, text='AUTO TEST', fg='#7FFF00', command=self.label_light1)
        self.button1.place(x=0, y=0, width=256, height=56)

        self.button2 = Button(self.layout1, bg='#303030', font=helv36, text='MANUAL TEST', fg='#7FFF00', command=self.label_light2)
        self.button2.place(x=256, y=0, width=256, height=56)

        self.button3 = Button(self.layout1, bg='#303030', font=helv36, text='SETTING', fg='#7FFF00', command=self.label_light3)
        self.button3.place(x=512, y=0, width=256, height=56)

        self.button4 = Button(self.layout1, bg='#303030', font=helv36, text='SERVICE', fg='#7FFF00', command=self.label_light4)
        self.button4.place(x=768, y=0, width=256, height=56)

    def label_light1(self):
        self._update_label_colors(0)

    def label_light2(self):
        self._update_label_colors(1)

    def label_light3(self):
        self._update_label_colors(2)

    def label_light4(self):
        self._update_label_colors(3)

    def _update_label_colors(self, active_index):
        color1 = '#7FFF00'
        color2 = '#303030'
        colors = [color1 if i == active_index else color2 for i in range(4)]
        self.label1 = Label(self.layout2, bg=colors[0]).place(x=0, y=0, width=256, height=64)
        self.label2 = Label(self.layout2, bg=colors[1]).place(x=256, y=0, width=256, height=64)
        self.label3 = Label(self.layout2, bg=colors[2]).place(x=512, y=0, width=256, height=64)
        self.label4 = Label(self.layout2, bg=colors[3]).place(x=768, y=0, width=256, height=64)

# Start the application
display = MAINGUI()
display.create_layout()

mainloop()
        

     
    
    
   



