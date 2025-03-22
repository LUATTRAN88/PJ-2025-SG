#!/usr/bin/python3

import serial
from threading import Thread
from time import sleep
import json
import queue 
import yaml
from extend import *
class Arduino:
    def __init__(self):
        self.serial_con = None;
        self.store_data = "";
        self.baudrate = 9600;
        self.threading_read = None;
        self.threading_control = None;
        self.flag_thread_read = False;
        self.flag_thread_control = True;
        #self.PORT_NAME = '/dev/ttyUSB0';
        self.queue = queue.Queue(maxsize=10); 
        self.flag_get_data =False;
        self.PORT_NAME = 'COM5';
    def getdata(self):
        if self.flag_get_data:
            return self.store_data
        else:
            return {}
    def connect_port(self):
            try:
                self.serial_con = serial.Serial(self.PORT_NAME, baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)
                self.serial_con.timeout=1;
               
                #self.serial_con.open();
                if self.serial_con==0:
                    print("Failed to connect");
                    return False;
                else:
                    print("Connect successfully!");
                    #self.threading_read = Thread(target=self.getdatanewline3, args=());          
                    #self.flag_thread_read = True;
                    #self.threading_read.start();
            except:
                 print("Failed to connect");
              
            return True;
    
    def disconnect_port(self):
        self.flag_thread_read = False;
        self.serial_con.close();
    
    
    def write_port(self, port,status):
        if self.serial_con != None:
            if self.serial_con.is_open:
                
                obj= {"req":ADRUINO_REQ_CTRL_SINGLE_RELAY , "port": port, "status":status};
                data = json.dumps(obj)
                data +='\r\n\n'
                print(data)
                self.serial_con.write(bytes(data, 'utf-8'));
    
    def write_obj(self, obj):
        if self.serial_con != None:
            if self.serial_con.is_open:
              
                data = json.dumps(obj)
                data +='\r\n\n'
                print(data)
                self.serial_con.write(bytes(data, 'utf-8'));
                del data 
    def getdatanewline(self, page):

                if self.serial_con != None:
                    if self.serial_con.is_open:
                        if self.flag_get_data ==False :
                                self.flag_get_data=True
                                self.write_obj({"req":ADRUINO_REQ_FULL_DATA,"page":page})
                                sleep(0.05)
                                data=self.serial_con.read_until(b"#").decode("utf-8")
                                datastrm= data.replace('#',"\n")
                                dataj= ''.join(datastrm)
                                self.serial_con.flush();
                                self.flag_get_data=False
                                print(dataj)
                                return datastrm; 
   