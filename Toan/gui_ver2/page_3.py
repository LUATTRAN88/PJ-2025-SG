from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
class PAGE3:
    def __init__(self):
        pass
    def create_layout(self,l4):
        self.layout = Frame(l4, bg='#DCDCDC',width=640,height=420)
        self.layout.place(x=0,y=61)
        
		# self.layout1 = Frame(l4,  bg='red',width=200,height=417)
		# self.layout1.place(x=438,y=61)
  
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar")
        hel1 = tkFont.Font(family='Helvetica', size=17, weight=tkFont.BOLD )
        self.name1 = Label(self.layout, bg='#DCDCDC', width=5,height=2, text='Vol',font=hel1,fg='#006400').place(x=5,y=46)
        self.name2 = Label(self.layout, bg='#DCDCDC', width=5,height=2, text='Ampe',font=hel1,fg='#006400').place(x=165,y=46)
        self.name3 = Label(self.layout, bg='#DCDCDC', width=7,height=2, text='Setpoint',font=hel1,fg='#006400').place(x=313,y=46)
      

        scale1 = Scale(self.layout, from_=0, to=100, orient='vertical',length=200,bg='#DCDCDC')
        scale1.place(x=21, y=100)
        
        scale2 = Scale(self.layout, from_=0, to=100, orient='vertical',length=200,bg='#DCDCDC')
        scale2.place(x=181, y=100)
        
        scale3 = Scale(self.layout, from_=0, to=100, orient='vertical',length=200,bg='#DCDCDC')
        scale3.place(x=341, y=100)
        
        self.create_label()
        
    def create_label(self):
        helv1 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
        self.label1 = Label(self.layout, bg='#303030',font=helv1,fg='white').place(x=438,y=0,width=200,height=37)
        self.label2 = Label(self.layout, bg='#303030',font=helv1,fg='white').place(x=438,y=38,width=200,height=37)
		# self.label3 = Label(self.layout, bg='#303030',font=helv1,fg='white').place(x=438,y=76,width=200,height=37)
 
  

	
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
		
		# helv366 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
		# label8 = Label(layout3, bg='#303030',text='Limits [Warn/Stop]',font=helv366,fg='white')
		# label8.place(x=0, y=266,width=200,height=37)
		# 	########################   
		
		# helv_font = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD )
		# label3 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label3.place(x=0, y=76,width=200,height=37)
				
		# label4 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label4.place(x=0, y=114,width=200,height=37)
				
		# label5 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label5.place(x=0, y=152,width=200,height=37)

		# label6 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label6.place(x=0, y=190,width=200,height=37)
				
		# label7 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label7.place(x=0, y=228,width=200,height=37)
				
		# label9 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label9.place(x=0, y=304,width=200,height=37)
				
		# label10 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label10.place(x=0, y=342,width=200,height=37)
				
		# label11 = Label(layout3, bg='#A6A6A6',font=helv_font)
		# label11.place(x=0, y=380,width=200,height=37)























