from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

class PAGE2:
    def __init__(self):
        pass
    def create_layout(self,l2):
        self.layout1 = Frame(l2, bg='#008B8B')
        self.layout1.place(x=2,y=61,width=636,height=417)

        # self.layout2 = Frame(l2, bg='yellow')
        # self.layout2.place(x=478,y=61,width=160,height=417)
    
        # self.rc1 = RELAY_CONTROL()
        # self.rc1.create_layout(self.layout1)
        # self.rc1.set_position(2,2)
        
        # self.rc2 = RELAY_CONTROL()
        # self.rc2.create_layout(self.layout1)
        # self.rc2.set_position(106,2)
     
     
        # Tạo mảng chứa các đối tượng RELAY_CONTROL
        self.relays = []
#   self.relays[0].set_position(x, y)
        # Số lượng đối tượng
        num_relays = 12
        cols = 6  # Số cột
        spacing_x, spacing_y = 106, 206  # Khoảng cách ngang và dọc giữa các đối tượng

        for i in range(num_relays):
            relay = RELAY_CONTROL()  # Tạo đối tượng RELAY_CONTROL
            relay.create_layout(self.layout1)
            relay.set_name_relays("Relay- "+str(i))

            # Tính toán vị trí (x, y) dựa trên chỉ số i
            
            
            x = (i % cols) * spacing_x
            y = (i // cols) * spacing_y
            relay.set_position(x, y)

            # Thêm vào mảng
            self.relays.append(relay)

 
class RELAY_CONTROL:
    def __init__(self):
        self.is_on = True
    def create_layout(self,layout1):
        self.k1 = Frame(layout1,bg='#F0FFFF')
        self.k1.place(x=2,y=2,width=103,height=204)
            
        self.k2=Label(self.k1,bg='blue', fg='white', font=('Arial',13,'bold'))
        self.k2.place(x=0,y=0,width=103,height=21)
            
        photo3 = Image.open('module.jpg')
        m3 = photo3.resize((77,26))
        self.pic3 = ImageTk.PhotoImage(m3)
        self.k3=Label(self.k1,bg='#E0EEEE',text='Module 1', fg='#007FFF', font=('Arial',9),image=self.pic3)
        self.k3.place(x=13,y=21,width=77,height=26)
            
        self.k4=Label(self.k1,bg='#0000CD',text='Auto', fg='white', font=('Arial',12,'bold'))
        self.k4.place(x=13,y=47,width=77,height=19)
            
        photo = Image.open('clock.jpg')
        self.pic = ImageTk.PhotoImage(photo)
        self.clock=Label(self.k1,bg='#E0EEEE',image=self.pic)
        self.clock.place(x=13,y=65,width=77,height=34)
            
        self.k5=Label(self.k1,bg='#C1CDCD',text='Setting', fg='blue', font=('Arial',9))
        self.k5.place(x=13,y=99,width=77,height=19)
            
        # photo5 = Image.open('manual.png')
        # self.pic5 = ImageTk.PhotoImage(photo5)
        # self.k5=Label(self.k1,bg='#F0FFFF',image=self.pic5,border=0)
        # self.k5.place(x=13,y=127,width=78,height=36)

    # gọi hàm button_toggle, ko truyền đối số vào, vì ko cần
    # phải tạo 1 biến ban đầu để xét if else:  self.is_on = True  , chú ý biến này phải đặt ở:  def __init__(self)  
        self.button_toggle()
              
    def button_toggle(self):
        a1 = Image.open('on.jpg').resize((85,81))
        self.on = ImageTk.PhotoImage(a1)
        a2 = Image.open('off.jpg').resize((85,81))
        self.off = ImageTk.PhotoImage(a2)

        self.button_on = Button(self.k1,image=self.on, bd=0,command= self.button_toggle)
        self.button_on.place(x=9,y=121,width=85,height=81)

        # self.button_on = Button(self.k1,image=self.on, bd=0,command= self.button_toggle)
        # self.button_on.place(x=19,y=159,width=65,height=42)
            
        if self.is_on:
            self.button_on.config(image=self.off)
            self.k3.config(image=self.off)
            self.is_on = False 
        else:
            self.button_on.config(image=self.on)
            self.is_on = True

            
                
            
    def set_name_relays(self,name):
        self.k2.config(text=name)       
    def set_position(self,x,y):
          self.k1.place(x=x,y=y,width=103,height=204)


# class RELAY_CONTROL_OFF:
      
         


















   
        # # Tạo mảng chứa các đối tượng RELAY_CONTROL
        # self.relays = []

        # # Số lượng đối tượng
        # num_relays = 12
        # cols = 6  # Số cột
        # spacing_x, spacing_y = 106, 206  # Khoảng cách ngang và dọc giữa các đối tượng

        # for i in range(num_relays):
        #     relay = RELAY_CONTROL()  # Tạo đối tượng RELAY_CONTROL
        #     relay.create_layout(self.layout1)

        #     # Tính toán vị trí (x, y) dựa trên chỉ số i
        #     x = (i % cols) * spacing_x
        #     y = (i // cols) * spacing_y
        #     relay.set_position(x, y)

        #     # Thêm vào mảng
        #     self.relays.append(relay)























# class PAGE2:
#     def __init__(self):
#         pass
#     def create_layout(self,l2):
#         self.layout1 = Frame(l2, bg='red')
#         self.layout1.place(x=2,y=61,width=476,height=417)

#         self.layout2 = Frame(l2, bg='yellow')
#         self.layout2.place(x=478,y=61,width=160,height=417)
#     def hide(self):
#         self.layout1.pack();
#         self.layout2.pack();
#     def show(self):
#         self.layout1.pack_forget();
#         self.layout2.pack_forget();
    