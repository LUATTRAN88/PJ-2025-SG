#!/usr/bin/python3

from pathlib import Path
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time 
import pandas as pd
import os
from tkinter import messagebox as mb
from time import sleep
STATE_M_CONNECTION =100
STATE_M_CONNECTED =101
STATE_M_CONNECT_FAILED=102

ADRUINO_REQ_FULL_DATA = 1000
ADRUINO_REQ_STOP_ALL_LOAD = 1003
ADRUINO_REQ_CTRL_SINGLE_RELAY = 1010
ADRUINO_REQ_CTRL_LOAD_APPLY = 1001
ADRUINO_REQ_CTRL_LOAD_DROP = 1007
ADRUINO_REQ_CTRL_LOAD_STOP = 1009

ADRUINO_PORT_CTRL_RL1 = 0
ADRUINO_PORT_CTRL_RL2 = 1
ADRUINO_PORT_CTRL_RL3= 2
ADRUINO_PORT_CTRL_RL4 = 3
ADRUINO_PORT_CTRL_RL5 = 4
ADRUINO_PORT_CTRL_RL6 = 5
ADRUINO_PORT_CTRL_RL7 = 6
ADRUINO_PORT_CTRL_RL8 = 7
ADRUINO_PORT_CTRL_RL9 = 8
ADRUINO_PORT_CTRL_RL10 = 8
ADRUINO_PORT_CTRL_RL11 = 10
ADRUINO_PORT_CTRL_RL12 = 11
ADRUINO_PORT_CTRL_FAN = 12
ADRUINO_PORT_CTRL_ALARM = 13
ADRUINO_PORT_CTRL_PHASE = 14


ADRUINO_STATUS_PORT_ON =1;
ADRUINO_STATUS_PORT_OFF =0;

FLAG_EXT_PRINT =TRUE

class VALUERELAY_FAN_PHASE:
    def __init__(self):
        RELAY_SWITCHING_FAN_STATUS=1;
        RELAY_SWITCHING_PHASE_STATUS=1

class POP_LOG:
    def __init__(self):
        self.adruino=None
    def create_layout(self):
        self.window = Tk()
        self.window.title('popup')
        self.window.geometry("572x220")
        self.text_log = Text(self.window, height = 10, width = 70)
        self.text_log.pack()
        btn_save = Button(self.window,bg='#191970',bd=3,fg='orange', font=('arial bold',16), text = "Save").place(x=0, y=165,width=286,height=55)
        btn_exit = Button(self.window,bg='#191970',bd=3,fg='orange', font=('arial bold',16), text = "Exit",command=self.window.destroy).place(x=286, y=165,width=286,height=55)
    def insertText(self,txt):
        self.text_log.insert(END, txt,"\n");
    def ClearText(self,txt):
        self.text_log.delete('1.0', END);




def get_path_img():
    path=Path(__file__).parent.resolve()
    final_path=str(path.as_posix())+'/img/'
    return final_path



class SIGNAL:
    def __init__(self):
        pass
    def create_layout(self,lay_button_relay,x,y,text):
        self.layout =  Frame(lay_button_relay,bg='white')
        self.layout.place(x=x+1,y=y, width=28,height=52)

        # self.lamp_on = Image.open(get_path_img()+'lamp_on.png').resize((17,17))
        # self.pic_lamp_on = ImageTk.PhotoImage(self.lamp_on)
        
        # self.lamp_off = Image.open(get_path_img()+'lamp_off1.png').resize((17,17))
        # self.pic_lamp_off = ImageTk.PhotoImage(self.lamp_off)
        
        
        self.lb_lamp = Label(self.layout, bg='#00FF00')
        self.lb_lamp.place(x=4,y=15,width=18,height=19)
        
        
        self.lb_relay = Label(self.layout, bg='white',font=('arial bold',8),fg='black',text=text).place(x=0,y=0,width=28,height=11)

        self.text_relay = StringVar()
        self.lb_relay_val = Label(self.layout,bg='white',pady=0,font=('arial bold',8),fg='black',textvariable=self.text_relay).place(x=0,y=32,width=28,height=17)  
        pass
    def set_relay_value(self,text):
        self.text_relay.set(text)
        
    def setonoff(self,val):
        if val == 1:
            self.lb_lamp.configure(bg='#00FF00')
        else:
            self.lb_lamp.configure(bg='grey')

array_load_bank = [{'id':0, 'kw': 1, 'port':0},
       {'id': 1, 'kw': 2, 'port':1},
       {'id': 2, 'kw': 2, 'port': 2},
       {'id': 3, 'kw': 5, 'port': 3},
       {'id': 4, 'kw': 5, 'port': 4},
       {'id': 5, 'kw': 5, 'port': 5},
       {'id': 6, 'kw': 10, 'port': 6},
       {'id': 7, 'kw': 10, 'port': 7},
       {'id': 8, 'kw': 10, 'port': 8},
       {'id': 9, 'kw': 20, 'port': 9},
       {'id': 10, 'kw': 20, 'port': 10},
       {'id': 11, 'kw': 20, 'port': 11},]

# print(array_load_bank[11]['port'])
# print(type(array_load_bank[0]['port']))

def number_of_objects(input_kw):
    cnt = {20:3, 10:3, 5:3, 3:1, 2:1, 1:1}
    ans = 0
    num = 0
    val = 0
    # id = -1
    id = len(array_load_bank)-1
    stores = []
    sum_kw = 0
    for k,v in cnt.items():
        sum_kw += k * v
    if sum_kw < input_kw:
        return -1
    else:
        total_port = 0
        while input_kw > 0:
            for i in range(id, -1, -1):
                curr_val = array_load_bank[i]['kw']
                # print('cv ', curr_val)
                if input_kw >= curr_val:
                    num = input_kw // curr_val
                    num = min(num, cnt[curr_val])
                    val = curr_val
                    id=i
                    break
            input_kw -= num * val
            ans += num
            for i in range(id, id-num, -1):
                stores.append(array_load_bank[i])
            id -= num
        for i in stores:
            total_port += i['port']
    return stores, total_port

data_auto_test = {
'vln1': [], 
'vln2': [],
'vln3': [],
'cur1': [],
'cur2': [],
'cur3': [],
'kw1': [],
'kw2': [],
'kw3': [], 
'pf1': [], 
'pf2': [], 
'pf3': [], 
'rl1_val': [],
'rl2_val': [],
'rl3_val': [],
'rl4_val': [],
'rl5_val': [],
'rl6_val': [],
'rl7_val': [],
'rl8_val': [],
'rl9_val': [],
'rl10_val': [],
'rl11_val': [],
'rl12_val': [],
'rl13_val': [],
'rl14_val': [],
'rl15_val': [],
'rl16_val': [],
'rl1_on': [],
'rl2_on': [],
'rl3_on': [],
'rl4_on': [],
'rl5_on': [],
'rl6_on': [],
'rl7_on': [],
'rl8_on': [],
'rl9_on': [],
'rl10_on': [],
'rl11_on': [],
'rl12_on': [],
'rl13_on': [],
'rl14_on': [],
'rl15_on': [],
'rl16_on': [],
'rl_power1_val':[],
'rl_power2_val':[],
'rl_power3_val':[],
'rl_power4_val':[],
'rl_power5_val':[],
'rl_power6_val':[],
'rl_power7_val':[],
'rl_power8_val':[],
'rl_power9_val':[],
'rl_power10_val':[],
'rl_power11_val':[],
'rl_power12_val':[],
'rl_power1_on':[],
'rl_power2_on':[],
'rl_power3_on':[],
'rl_power4_on':[],
'rl_power5_on':[],
'rl_power6_on':[],
'rl_power7_on':[],
'rl_power8_on':[],
'rl_power9_on':[],
'rl_power10_on':[],
'rl_power11_on':[],
'rl_power12_on':[],
'freq': [],
'tkw': [],
'v12': [],
'v23': [],
'v31': [],
'tempc': [],
}

def store_file(filepath, data):
    file = open(filepath, 'w')
    file.write(str(data))    
    file.write('\n')
    file.close()
    print('Data is written into the file.')

# store_file('data.txt', res)
def read_file(filepath):
    file = open(filepath, 'r')
    print(file.read())
    
def store_file_csv(filepath, data):
    # print(data)
    data_auto_test['vln1'].append(data['vln1'])
    data_auto_test['vln2'].append(data['vln2'])
    data_auto_test['vln3'].append(data['vln3'])
    data_auto_test['cur1'].append(data['cur1'])
    data_auto_test['cur2'].append(data['cur2'])
    data_auto_test['cur3'].append(data['cur3'])
    data_auto_test['kw1'].append(data['kw1'])
    data_auto_test['kw2'].append(data['kw2'])
    data_auto_test['kw3'].append(data['kw3'])
    data_auto_test['pf1'].append(data['pf1'])
    data_auto_test['pf2'].append(data['pf2'])
    data_auto_test['pf3'].append(data['pf3'])
    for i in range(16):
        data_auto_test['rl'+str(i+1)+'_val'].append(data['rl'][i]['val'])
        data_auto_test['rl'+str(i+1)+'_on'].append(data['rl'][i]['on'])
    for i in range(12):
        data_auto_test['rl_power'+str(i+1)+'_val'].append(data['rl_power'][i]['val'])
        data_auto_test['rl_power'+str(i+1)+'_on'].append(data['rl_power'][i]['on'])
    data_auto_test['freq'].append(data['freq'])
    data_auto_test['tkw'].append(data['tkw'])
    data_auto_test['v12'].append(data['v12'])
    data_auto_test['v23'].append(data['v23'])
    data_auto_test['v31'].append(data['v31'])
    data_auto_test['tempc'].append(data['tempc'])
    
    df = pd.DataFrame(data_auto_test)
    # print('DF ')
    print(df)
    df.to_csv(filepath, index=False)

# store_file_csv('data.csv', res)s

# def control_relay(req,id,status):
#     req={'req':req,'id':id,'status':status};
#     print(req)
#     return req

def control_relay(req,id,status):
    req = {'req':req,'id':id,'status':status}
    print(req)
    return req
def extPrint(data):
    if FLAG_EXT_PRINT:
        print("%s-%s",time.time(),data)
        
def exitapp(adruino,page):
    res=mb.askquestion('Exit Application', 'Do you really want to exit')
    if res == 'yes' :
        if adruino.serial_con is not None:
            if adruino.serial_con.is_open ==True:
                adruino.write_obj({"req":ADRUINO_REQ_CTRL_LOAD_DROP,"page":page})
                sleep(3);
                data=adruino.serial_con.read_until(b"#").decode("utf-8")
                
                #os.system("shutdown now -h")
                os.system('systemctl poweroff') 
                os._exit(os.EX_OK);
                return
        os.system('systemctl poweroff') 
        os._exit(os.EX_OK)
    else :
        mb.showinfo('Return', 'Returning to main application')
def rebootapp(adruino,page):
    res=mb.askquestion('Reboot Application', 'Do you really want to reboot')
    if res == 'yes' :
        if adruino.serial_con is not None:
            if adruino.serial_con.is_open ==True:
                adruino.write_obj({"req":ADRUINO_REQ_CTRL_LOAD_DROP,"page":page})
                sleep(3);
                data=adruino.serial_con.read_until(b"#").decode("utf-8")
                
                #os.system("shutdown now -h")
                os.system('echo "123456" | sudo reboot') 
                os._exit(os.EX_OK);
                return
        os.system('echo "123456" | sudo reboot') 
        os._exit(os.EX_OK)
    else :
        mb.showinfo('Return', 'Returning to main application')
def closeapp(adruino,page):
    res=mb.askquestion('EXIT Application', 'Do you really want to exit')
    if res == 'yes' :
        if adruino.serial_con is not None:
            if adruino.serial_con.is_open ==True:
                adruino.write_obj({"req":ADRUINO_REQ_CTRL_LOAD_DROP,"page":page})
                sleep(3);
                data=adruino.serial_con.read_until(b"#").decode("utf-8")
                os._exit(os.EX_OK);
                return
        os._exit(os.EX_OK)
    else :
        mb.showinfo('Return', 'Returning to main application')