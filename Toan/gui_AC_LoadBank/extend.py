from pathlib import Path
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from time import strftime
import pandas as pd

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

        self.photol = Image.open(get_path_img()+'lamp_on.png').resize((17,17))
        self.picl = ImageTk.PhotoImage(self.photol)
        self.lb_lamp = Label(self.layout, bg='white',image=self.picl)
        self.lb_lamp.place(x=0,y=12,width=28,height=23)
        
        
        self.lb_relay = Label(self.layout, bg='white',font=('arial bold',8),fg='black',text=text).place(x=0,y=0,width=28,height=11)

        self.text_relay = StringVar()
        self.lb_relay_val = Label(self.layout,bg='white',pady=0,font=('arial bold',8),fg='black',textvariable=self.text_relay).place(x=0,y=32,width=28,height=17)  
        pass

array_load_bank = [{'id':1, 'kw': 1, 'port':0x01},
       {'id': 2, 'kw': 2, 'port':0x02},
       {'id': 3, 'kw': 3, 'port': 0x03},
       {'id': 4, 'kw': 5, 'port': 0x04},
       {'id': 5, 'kw': 5, 'port': 0x05},
       {'id': 6, 'kw': 5, 'port': 0x06},
       {'id': 7, 'kw': 10, 'port': 0x07},
       {'id': 8, 'kw': 10, 'port': 0x08},
       {'id': 9, 'kw': 10, 'port': 0x09},
       {'id': 10, 'kw': 20, 'port': 0x0A},
       {'id': 11, 'kw': 20, 'port': 0x0B},
       {'id': 12, 'kw': 20, 'port': 0x0C},]

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