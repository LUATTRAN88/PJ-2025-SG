from serial import *
from threading import Thread
from time import sleep
import json
import queue 

class Arduino:
    def __init__(self):
        self.serial_con = None;
        self.store_data = "";
        self.baudrate = 9600;
        self.threading_read = None;
        self.threading_control = None;
        self.flag_thread_read = False;
        self.flag_thread_control = True;
        self.PORT_NAME = '/dev/ttyUSB0';
        self.queue = queue.Queue(maxsize=10); 
        self.flag_get_data =False;
        #self.PORT_NAME = 'COM5';
    def getdata(self):
        if self.flag_get_data:
            return self.store_data
        else:
            return {}
    def connect_port(self):
            self.serial_con = Serial(self.PORT_NAME)
            self.serial_con.baudrate = self.baudrate;
            self.serial_con.timeout=2;
            if self.serial_con==0:
                print("Failed to connect");
                return False;
            else:
                print("Connect successfully!");
                self.threading_read = Thread(target=self.readline, args=(self.queue,));          
                self.flag_thread_read = True;
                #self.threading_read.start();
              
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
                del data 
    def getdatanewline(self):
            if self.serial_con != None:
                if self.serial_con.is_open:
                       if self.flag_get_data ==False :
                            self.flag_get_data=True
                            self.write_obj({"req":1000})
                            sleep(0.05)
                            data=self.serial_con.readline()
                            self.flag_get_data=False
                            return data; 
            return {}


    def read_data(self):
        while self.flag_thread_read:
            if self.serial_con != None:
                if self.serial_con.is_open:
                    data ="";
                    data = self.serial_con.readline();
                    print( "111 ")
                    if len(data)>0 :
                        print( "--- 666 ---")
                        self.store_data =data
                    else:
                        print( "--- 777 ---")
                    self.serial_con.reset_input_buffer()
                    sleep(2);
    def readline(self,q):
        line = []
        print( "--- 888 ---")
        while True:
            for c in self.serial_con.read():
                line.append(chr(c))
                if chr(c) == '\n':
                    data=''.join(line)
                    try:
                        #q.put(data, block=True)
                        print(f"Produced: {data}")
                        print( "--- 333 --- %s", data)
                        if not self.flag_get_data:
                            self.store_data = data;
                            self.flag_get_data=True;
                            print( "--- 22 --- %s", data)
                    except:
                        #q.get(block=False)
                        #q.task_done()
                        print("Queue full, waiting...")
                    print( "--- 444 --- %s", data)
                    line = []
                    break
        

       