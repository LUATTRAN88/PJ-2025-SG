from serial import *
from threading import Thread
import time
import json


class Arduino:
    def __init__(self):
        self.serial_con = None;
        self.store_data = "";
        self.baudrate = 9600;
        self.threading_read = None;
        self.threading_control = None;
        self.flag_thread_read = False;
        self.flag_thread_control = True;
        self.PORT_NAME = 'COM3';
        
    def connect_port(self):
        try:
            self.serial_con = Serial(self.PORT_NAME)
            self.serial_con.baudrate = self.baudrate;
            self.serial_con.timeout=500;
            if self.serial_con == None:
                print("Failed to connect");
                return False;
            else:
                print("Connect successfully!");
                self.threading_read = Thread(target=self.read_port, args=());          
                self.flag_thread_read = True;
                self.threading_read.start();
              
            return True;
        except:
            return False;
    
    def disconnect_port(self):
        self.flag_thread_read = False;
        self.serial_con.close();
        
    def write_port(self, obj):
        data = json.dumps(obj)
        data +='\n'
        print(data)
        self.serial_con.write(bytes(data, 'utf-8'));
        
    def read_port(self):
        while self.flag_thread_read:
            self.store_data = self.serial_con.readline();
            time.sleep(1000/1000);
            print(self.store_data);
    def readline(self):
        self.store_data = self.serial_con.readline();
        return self.store_data;
