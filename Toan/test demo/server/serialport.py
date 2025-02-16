from serial import *
from threading import Thread
from time import sleep
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
        #self.PORT_NAME = '/dev/ttyUSB0';
        self.PORT_NAME = 'COM5';
    def connect_port(self):
            self.serial_con = Serial(self.PORT_NAME)
            self.serial_con.baudrate = self.baudrate;
            self.serial_con.timeout=1;
            if self.serial_con == None:
                print("Failed to connect");
                return False;
            else:
                print("Connect successfully!");
                self.threading_read = Thread(target=self.read_data, args=());          
                self.flag_thread_read = True;
                self.threading_read.start();
              
            return True;
    
    def disconnect_port(self):
        self.flag_thread_read = False;
        self.serial_con.close();
    
    def write_port(self, port,status):
        if self.serial_con != None:
            if self.serial_con.is_open:
                
                obj= {"req":2000 , "port": port, "status":status};
                data = json.dumps(obj)
                data +='\r\n'
                print(data)
                self.serial_con.write(bytes(data, 'utf-8'));
    
    def write_obj(self, obj):
        if self.serial_con != None:
            if self.serial_con.is_open:
                data = json.dumps(obj)
                data +='\r\n'
                self.serial_con.write(bytes(data, 'utf-8'));
        
    def read_data(self):
        while self.flag_thread_read:
            if self.serial_con != None:
                if self.serial_con.is_open:
                    self.write_obj({"req":1001});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )

                    self.write_obj({"req":1002});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )
                    self.write_obj({"req":1003});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )
                    self.write_obj({"req":1004});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )
                    self.write_obj({"req":1005});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )
                    
                    self.write_obj({"req":1006});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )
                    self.write_obj({"req":1007});
                    self.store_data = self.serial_con.readline();
                    print(self.store_data )

                    sleep(2);
    def readline(self):
        if self.serial_con != None:
            if self.serial_con.is_open:
                self.write_obj({"req":1001});
                self.store_data = self.serial_con.readline();
        return self.store_data;
