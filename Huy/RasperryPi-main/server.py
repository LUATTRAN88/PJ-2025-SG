import serial
from threading import Thread
import time

PORT_NAME = 'COM9';


class Arduino:
    def __init__(self):
        self.serial_con = None;
        self.store_data = "";
        self.baudrate = 9600;
        self.threading_read = None;
        self.threading_control = None;
        self.flag_thread_read = False;
        self.flag_thread_control = True;
        
    def connect_port(self):
        self.serial_con = serial.Serial(PORT_NAME);
        self.serial_con.baudrate = self.baudrate;
        if self.serial_con == None:
            print("Failed to connect");
            # return False;
        else:
            print("Connect successfully!");
            self.threading_read = Thread(target=self.read_port, args=());
            self.threading_control = Thread(target=self.control, args=());
            
            self.flag_thread_read = True;
            self.threading_read.start();
            self.threading_control.start();
            self.threading_read.join();
            self.threading_control.join();
        # return True;
    
    def disconnect_port(self):
        self.flag_thread_read = False;
        self.serial_con.close();
        
    def write_port(self, data):
        self.serial_con.write(bytes(data, 'utf-8'));
        
    def read_port(self):
        while self.flag_thread_read:
            self.store_data = self.serial_con.readline();
            time.sleep(1000/1000);
            print(self.store_data);

    def control(self):
        while self.flag_thread_control:
            print('Enter character:')
            input_prompt = input();
            print(input_prompt)
            if input_prompt == 'a':
                self.disconnect_port();
                # self.flag_thread_control = False;
                break;
        
if __name__ == '__main__':
    
    arduino = Arduino(); 
    
    arduino_con_yn = arduino.connect_port();
    

    
    
    
    
    
        
        
    
    
    
        

