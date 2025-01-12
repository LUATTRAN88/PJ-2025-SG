from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image


class MAINGUI:
    def __init__(self):
        pass
    def create_layout(self):
        self.layout = Tk()
        self.layout.title('AC Load Bank')
        self.layout.geometry('640x480')
        self.layout.config(bg='white')

        # layout1 chứa các label_light / layout2 chứa các button_main
        self.layout1 = Frame(self.layout,bg='blue',width=640,height=56).place(x=0,y=0)
        self.layout2 = Frame(self.layout,bg='yellow',width=640,height=56).place(x=0,y=0)

      
        # self.label_light1()
        # self.label_light2()
        # self.label_light()
       
        self.tab_button()
        # self.label_light()

        # self.color_button1()
        # self.color_button2()

    # def label_light(self):
    #     self.label1 = Label(self.layout2, bg='brown').place(x=0,y=0,width=160,height=56)
    #     self.label2 = Label(self.layout2, bg='#458B74').place(x=160,y=0,width=160,height=56)
    #     self.label3 = Label(self.layout2, bg='#0000FF').place(x=320,y=0,width=160,height=56)
    #     self.label4 = Label(self.layout2, bg='#7FFF00').place(x=480,y=0,width=160,height=56)


    def tab_button(self):
        fontb = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.button1 = Button(self.layout2,bg='white',font=fontb,text='AUTO TEST',fg='black',command=lambda:self.color_button1()).place(x=28,y=8,width=100,height=40)
        self.button2 = Button(self.layout2,bg='white',font=fontb,text='MANUAL TEST',fg='black',command=lambda:self.color_button2()).place(x=183,y=8,width=112,height=40)
        self.button3 = Button(self.layout2,bg='white',font=fontb,text='SETTING',fg='black').place(x=359,y=8,width=80,height=40)
        self.button4 = Button(self.layout2,bg='white',font=fontb,text='SERVICE',fg='black').place(x=522,y=8,width=75,height=40)

    def color_button1(self):
        fontb = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        # self.labeln1 = Label(self.layout2,bg='red').place(x=0,y=0,width=160,height=56)
        # self.labeln2 = Label(self.layout2,bg='white').place(x=160,y=0,width=160,height=56)
        # self.labeln3 = Label(self.layout2,bg='white').place(x=320,y=0,width=160,height=56)

        self.label1 = Label(self.layout2, bg='black').place(x=0,y=0,width=160,height=56)
        self.button1 = Button(self.layout2,bg='white',font=fontb,text='AUTO TEST',fg='black')
        self.button1.place(x=28,y=8,width=100,height=40)

        self.label2 = Label(self.layout2, bg='white').place(x=160,y=0,width=160,height=56)
        self.button2 = Button(self.layout2,bg='white',font=fontb,text='MANUAL TEST',fg='black')
        self.button2.place(x=183,y=8,width=112,height=40)
        # self.label3 = Label(self.layout2, bg='white').place(x=320,y=0,width=160,height=56)
        # self.button3 = Button(self.layout2,bg='white',font=fontb,text='SETTING',fg='black').place(x=359,y=8,width=80,height=40)

        # self.label4 = Label(self.layout2, bg='white').place(x=480,y=0,width=160,height=56)
        # self.button4 = Button(self.layout2,bg='white',font=fontb,text='SERVICE',fg='black').place(x=522,y=8,width=75,height=40)



    def color_button2(self):
        fontb = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.label2 = Label(self.layout2, bg='black').place(x=160,y=0,width=160,height=56)
        self.button2 = Button(self.layout2,bg='white',font=fontb,text='MANUAL TEST',fg='black')
        self.button2.place(x=183,y=8,width=112,height=40)

        self.label1 = Label(self.layout2, bg='white').place(x=0,y=0,width=160,height=56)
        self.button1 = Button(self.layout2,bg='white',font=fontb,text='AUTO TEST',fg='black')
        self.button1.place(x=28,y=8,width=100,height=40)






    #     fontb = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
    #     self.label2 = Label(self.layout2, bg='black').place(x=160,y=0,width=160,height=56)
    #     self.button2 = Button(self.layout2,bg='white',font=fontb,text='MANUAL TEST',fg='black').place(x=183,y=8,width=112,height=40)

    #     self.label1 = Label(self.layout2, bg='white').place(x=0,y=0,width=160,height=56)
    #     self.button1 = Button(self.layout2,bg='white',font=fontb,text='AUTO TEST',fg='black').place(x=28,y=8,width=100,height=40)
        
        
display = MAINGUI()
display.create_layout()

mainloop()


   
        

     
    
    
   




    #     self.button_main()
    #     # self.change_color_b1()
    #     # self.change_color_b2()

    # def button_main(self):
    #     fontb = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD )
    #     self.button1 = Button(self.layout, bg='pink',font=fontb,text='AUTO TEST',fg='black',command=self.change_color_b1).place(x=0,y=0,width=160, height=60)
    #     self.button2 = Button(self.layout, bg='pink',font=fontb,text='MANUAL TEST',fg='black',command=self.change_color_b2).place(x=160,y=0,width=160, height=60)
    #     # self.button3 = Button(self.layout, bg='white',font=fontb,text='SETTING',fg='black').place(x=320,y=0,width=160, height=60)
    #     # self.button4 = Button(self.layout, bg='white',font=fontb,text='SERVICE',fg='black').place(x=480,y=0,width=160, height=60)

    # def change_color_b1(self):
    #     fontb = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD )
    #     self.button1 = Button(self.layout, bg='pink',font=fontb,text='AUTO TEST',fg='black').place(x=0,y=0,width=160, height=60)
    #     self.button2 = Button(self.layout, bg='white',font=fontb,text='MANUAL TEST',fg='black').place(x=160,y=0,width=160, height=60)
    #     # self.button3 = Button(self.layout, bg='white',font=fontb,text='SETTING',fg='black').place(x=320,y=0,width=160, height=60)
    #     # self.button4 = Button(self.layout, bg='white',font=fontb,text='SERVICE',fg='black').place(x=480,y=0,width=160, height=60)

    # def change_color_b2(self):
    #     fontb = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD )
    #     self.button2 = Button(self.layout, bg='pink',font=fontb,text='MANUAL TEST',fg='black').place(x=160,y=0,width=160, height=60)
    #     self.button1 = Button(self.layout, bg='white',font=fontb,text='AUTO TEST',fg='black').place(x=0,y=0,width=160, height=60)
    #     # self.button3 = Button(self.layout, bg='white',font=fontb,text='SETTING',fg='black').place(x=320,y=0,width=160, height=60)
    #     # self.button4 = Button(self.layout, bg='white',font=fontb,text='SERVICE',fg='black').place(x=480,y=0,width=160, height=60)

