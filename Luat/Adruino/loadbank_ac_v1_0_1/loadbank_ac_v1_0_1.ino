#include <SoftwareSerial.h> 
#include "PCF8575.h"
#include <Crc16.h>
#include <ArduinoJson.h>
#include "MAX6675.h"

#define ID_DEVICE  250101

#define ALARM_RELAY_PORT 14
//STATUS RESPONSE
#define STS_SEND_NRM 200
#define STS_SEND_ERR 201
//ERROR CODE
#define ERR_1  1

#define ON_RELAY_LOAD  LOW
#define OFF_RELAY_LOAD  HIGH
#define NUM_RELAY       16

// MAX6675 Thermocouple
const int dataPin   = 5;
const int clockPin  = 3;
const int selectPin = 4;
MAX6675 thermoCouple(selectPin, dataPin, clockPin);
void TaskBlink( void *pvParameters );
Crc16 crc; 
// SERIAL INPUT CONTROL
String dataInputCtrl = "";      // a String to hold incoming data
bool dataComplete = false;  // whether the string is complete
String output="";
SoftwareSerial pzemSerial(9,8); //rx, tx new board
byte datacmd[8];
byte list_port_inf[16];
byte arrReqMFM383[21][6] ={
              {0x01, 0x04, 0x00,0x00,0x00,0x02},// V1N
              {0x01, 0x04, 0x00,0x02,0x00,0x02},// V2N
              {0x01, 0x04, 0x00,0x04,0x00,0x02},// V3N
              {0x01, 0x04, 0x00,0x06,0x00,0x02},// Average Voltage LN
              {0x01, 0x04, 0x00,0x08,0x00,0x02},// V12
              {0x01, 0x04, 0x00,0x0A,0x00,0x02},// V23
              {0x01, 0x04, 0x00,0x0C,0x00,0x02},// V31
              {0x01, 0x04, 0x00,0x0E,0x00,0x02},// VLL
              {0x01, 0x04, 0x00,0x10,0x00,0x02},// I1
              {0x01, 0x04, 0x00,0x12,0x00,0x02},// I2
              {0x01, 0x04, 0x00,0x14,0x00,0x02},// I3
              {0x01, 0x04, 0x00,0x16,0x00,0x02},// Average Current
              {0x01, 0x04, 0x00,0x18,0x00,0x02},// KW1
              {0x01, 0x04, 0x00,0x1A,0x00,0x02},// KW2
              {0x01, 0x04, 0x00,0x1C,0x00,0x02},// KW3
              {0x01, 0x04, 0x00,0x2A,0x00,0x02},// Total KW
              {0x01, 0x04, 0x00,0x38,0x00,0x02}, // Frequency
              {0x01, 0x04, 0x00,0x30,0x00,0x02},// PF1
              {0x01, 0x04, 0x00,0x32,0x00,0x02}, // PF2
              {0x01, 0x04, 0x00,0x34,0x00,0x02}, // PF3
              {0x01, 0x04, 0x00,0x36,0x00,0x02} // AVPF
     
            }; // Fequency

PCF8575 pcf8575(0x20);
long flag_send_yn = 0;
long timer1_counter_val=0;
struct CheckInParams {
  public:
    float alm_lmt_temp;
    float alm_lmt_vol_l_n;
    float alm_lmt_pwr;
    float emg_lmt_temp;
    float emg_lmt_vol_ln;
    float emg_lmt_cur;
    bool flag_emg_stop=0;
};

struct OutParams {
  public:
    float V1N;
    float V2N;
    float V3N;
    float VLN;
    float V12;
    float V23;
    float V31;
    float VLL;
    float I1;
    float I2;
    float I3;
    float AVI;
    float KW1;
    float KW2;
    float KW3;
    float FRQ;
    float AVPF;
    float PF1;
    float PF2;
    float PF3;
    float TKW;
    float temperature;
    float timer1_counter_val;
};

CheckInParams checkInParams;
OutParams  outParams;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  pzemSerial.begin(9600);
  pzemSerial.flush();
  //pzemSerial.setTimeout(10);
  init_pcf8575();
  SPI.begin();
  thermoCouple.begin();
  thermoCouple.setSPIspeed(4000000);
  //Scheduler.startLoop(sendmfm383relaytorasp);
   
  cli();                                  // tắt ngắt toàn cục   
  TCCR1A = 0;
  TCCR1B = 0;
  TIMSK1 = 0;
  TCCR1B |= (1 << CS12) | (1 << CS10);    // prescale = 1024
  TCNT1 = 49911;
  TIMSK1 = (1 << TOIE1);                  // Overflow interrupt enable 
  sei();                              // cho phép ngắt toàn cục
}

ISR (TIMER1_OVF_vect) 
{
    TCNT1 = 49911;
}
void init_pcf8575()
{
  // Set pinMode to OUTPUT
	pcf8575.pinMode(P0, OUTPUT);
  pcf8575.pinMode(P1, OUTPUT);
  pcf8575.pinMode(P2, OUTPUT);
  pcf8575.pinMode(P3, OUTPUT);
  pcf8575.pinMode(P4, OUTPUT);
  pcf8575.pinMode(P5, OUTPUT);
  pcf8575.pinMode(P6, OUTPUT);
  pcf8575.pinMode(P7, OUTPUT);
          
  pcf8575.pinMode(P8, OUTPUT);
  pcf8575.pinMode(P9, OUTPUT);
  pcf8575.pinMode(P10, OUTPUT);
  pcf8575.pinMode(P11, OUTPUT);
  pcf8575.pinMode(P12, OUTPUT);
  pcf8575.pinMode(P13, OUTPUT);
  pcf8575.pinMode(P14, OUTPUT);
  pcf8575.pinMode(P15, OUTPUT);
  pcf8575.begin();


}

void loop() {

//serialInputData();
//sendmfm383relaytorasp(1001,STS_SEND_NRM);       
serialEvent();
sendmfm383relaytorasp();                                                                                                                                                                                                                                                                                                                                   

}


// Read Serial Command
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    dataInputCtrl += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      dataComplete = true;
      deliverCtrl(dataInputCtrl);
      dataInputCtrl="";
      Serial.flush();
    }
  }
}// Read PORT Relay
void sendmfm383relaytorasp()
{
 
outParams.V1N=reqmfm383(sendmfm383(0),8);
delayMicroseconds(1000);
outParams.V2N=reqmfm383(sendmfm383(1),8);
delayMicroseconds(1000);
outParams.V3N=reqmfm383(sendmfm383(2),8);
delayMicroseconds(1000);
outParams.VLN=reqmfm383(sendmfm383(3),8);
delayMicroseconds(1000);
outParams.V12=reqmfm383(sendmfm383(4),8);
delayMicroseconds(1000);
outParams.V23=reqmfm383(sendmfm383(5),8);
delayMicroseconds(1000);
outParams.V31=reqmfm383(sendmfm383(6),8);
delayMicroseconds(1000);
outParams.VLL=reqmfm383(sendmfm383(7),8);
delayMicroseconds(1000);
outParams.I1=reqmfm383(sendmfm383(8),8);
delayMicroseconds(1000);
outParams.I2=reqmfm383(sendmfm383(9),8);
delayMicroseconds(1000);
outParams.I3=reqmfm383(sendmfm383(10),8);
delayMicroseconds(1000);
outParams.AVI=reqmfm383(sendmfm383(11),8);
delayMicroseconds(1000);
outParams.KW1=reqmfm383(sendmfm383(12),8);
delayMicroseconds(1000);
outParams.KW2=reqmfm383(sendmfm383(13),8);
delayMicroseconds(1000);
outParams.KW3=reqmfm383(sendmfm383(14),8);
delayMicroseconds(1000);
outParams.TKW=reqmfm383(sendmfm383(15),8);
delayMicroseconds(1000);
outParams.FRQ=reqmfm383(sendmfm383(16),8);
delayMicroseconds(1000);
outParams.PF1=reqmfm383(sendmfm383(17),8);
delayMicroseconds(1000);
outParams.PF2=reqmfm383(sendmfm383(18),8);
delayMicroseconds(1000);
outParams.PF3=reqmfm383(sendmfm383(19),8);
delayMicroseconds(1000);
outParams.AVPF=reqmfm383(sendmfm383(20),8);

int thermo_status = thermoCouple.read();
outParams.temperature = thermoCouple.getTemperature();





}



byte* sendmfm383(int row)
{
  memset(datacmd, 0, sizeof(datacmd));
  for(int col=0 ; col <6 ; col++ )
  {
    datacmd[col]=arrReqMFM383[row][col];
  }
  unsigned short crcvalue  = crc.Modbus(datacmd,0,6);
  byte L_Byte= (byte)crcvalue;
  byte H_Byte= (byte)(crcvalue>>8);
  datacmd[6]=L_Byte;
  datacmd[7]=H_Byte;
  return datacmd;

}
float reqmfm383(byte *reqdata, int length)
{
    pzemSerial.write(reqdata,length);
    int cnt_data=0;
    int data_length=9;
    byte repdata[9]={};
    while(cnt_data<100)
    { 
      if(pzemSerial.available()>8)
      { 
        //  repdata[i]=pzemSerial.read();
        pzemSerial.readBytes(repdata,data_length);
        break;
      }
      cnt_data++;
      delayMicroseconds(1000);
    }
    pzemSerial.flush();
    crc.clearCrc();
    /*for(int j =0 ;j <data_length;j++)
    {
      Serial.println(repdata[j],HEX);
    }*/
    unsigned short checksum =getCombine2Bytes(repdata[data_length-1],repdata[data_length-2]);
    //Modbus
    unsigned short crcvalue  = crc.Modbus(repdata,0,7);

    uint16_t H_value= getCombine2Bytes(repdata[3],repdata[4]);
    uint16_t L_value= getCombine2Bytes(repdata[5],repdata[6]);
    float value=convertFloat(L_value,H_value);
    /*Serial.println(H_value,HEX);
    Serial.println(L_value,HEX);
    Serial.println(value);
    //Serial.println(value,HEX);*/
    if(crcvalue==checksum)
      return value;
    else
      return -1;
}
 unsigned short getCombine2Bytes(byte hight_bytes,byte low_bytes)
{
  //byte arr[] = { 0x80, 0x7F };  result: 0x807F
  unsigned long result = (( unsigned short)hight_bytes << 8) | ( unsigned short)low_bytes;
  return result;
}
uint16_t getCombine4Bytes(uint16_t h1,uint16_t h2,uint16_t h3,uint16_t h4)
{
  //byte arr[] = { 0x80, 0x7F, 0xC0, 0x3F };  result: 0x807FC03F
  uint16_t result = ((uint16_t)h1 << 24) | ((uint16_t)h2 << 16 ) | ((uint16_t)h3 << 8) | (uint16_t)h4;
  return result;
}
float convertFloat(unsigned short reg_low, unsigned short reg_high) {

  unsigned short data[2] = {reg_low, reg_high};
  float value;
  memcpy(&value, data, 4);
  return value;
}


void readPortPCF8575()
{
   memset(list_port_inf, 0, sizeof(list_port_inf));
  for(int port_index = 0 ; port_index<16; port_index++)
  {
    uint8_t portval=pcf8575.digitalRead(port_index,true);
    list_port_inf[port_index]=portval?0:1;
   
  }
}
void controlRelayOnOFF(uint8_t port, uint8_t val)
{
  digitalWrite(port, val);
}

int listrelay[16];
void deliverCtrl(String rawDT)
{

  JsonDocument myObject;
  deserializeJson(myObject, rawDT);
  int resq= (int) myObject["req"];
  switch(resq)
  {
    case 1000: // init param
        checkInParams.alm_lmt_temp= (int) myObject["alm_lmt_temp"];
        checkInParams.alm_lmt_vol_l_n= (int) myObject["alm_lmt_vol_l_n"];
        checkInParams.alm_lmt_pwr= (int) myObject["alm_lmt_vol_pwr"];
        checkInParams.emg_lmt_temp= (int) myObject["emg_lmt_temp"];
        checkInParams.emg_lmt_cur= (int) myObject["emg_lmt_cur"];
        checkInParams.emg_lmt_vol_ln= (int) myObject["emg_lmt_vol_ln"];
        returnServerStatus(resq,"",STS_SEND_NRM);    
      break;
    case 1001: // Read Data sensor and control
      readPortPCF8575();
      output="";
      output +="{";
      output +="\"req\" : 1001,";
      output +="\"status\" : 200,";
      output +="\"info\" : {";
      sendStringSerial(output);
      output="";
      output +="\"vln1\" : "+String(outParams.V1N) +",";
      sendStringSerial(output);
      output="";
      output +="\"v12\" : "+String(outParams.V12) +",";
      output +="\"v23\" : "+String(outParams.V23) +",";
      output +="\"v31\" : "+String(outParams.V31) +",";
      output +="\"vll\" : "+String(outParams.VLL) +",";
      sendStringSerial(output);
      output="";
      output +="\"cur1\" : "+String(outParams.I1) +",";
      output +="\"cur2\" : "+String(outParams.I2) +",";
      output +="\"cur3\" : "+String(outParams.I3) +",";
      output +="\"avi\" : "+String(outParams.AVI) +",";
      sendStringSerial(output);
      output="";
      output +="\"kw1\" : "+String(outParams.KW1) +",";
      output +="\"kw2\" : "+String(outParams.KW2) +",";
      output +="\"kw3\" : "+String(outParams.KW3) +",";
      sendStringSerial(output);
      output="";
      output +="\"tkw\" : "+String(outParams.TKW) +",";
      output +="\"freq\" : "+String(outParams.FRQ) +",";
      output +="\"pf1\" : "+String(outParams.PF1) +",";
      output +="\"pf2\" : "+String(outParams.PF2) +",";
      output +="\"pf3\" : "+String(outParams.PF3) +",";
      output +="\"avpf\" : "+String(outParams.AVPF) +",";
      sendStringSerial(output);
      output="";
      output +="\"tim1_cnt\" : "+String(outParams.timer1_counter_val) +",";
      output +="\"tempc\" : "+String(outParams.temperature) +"";
      output +="},";
      sendStringSerial(output);
      output="";
      output +="\"rls\":[";
      output +=String(list_port_inf[0]) +"," ;
      output +=String(list_port_inf[1]) +"," ;
      output +=String(list_port_inf[2]) +"," ;
      output +=String(list_port_inf[3]) +"," ;
      output +=String(list_port_inf[4]) +"," ;
      output +=String(list_port_inf[5]) +"," ;
      output +=String(list_port_inf[6]) +"," ;
      output +=String(list_port_inf[7]) +"," ;
      output +=String(list_port_inf[8]) +"," ;
      output +=String(list_port_inf[9]) +"," ;
      output +=String(list_port_inf[10]) +"," ;
      output +=String(list_port_inf[11]) +"," ;
      output +=String(list_port_inf[12]) +"," ;
      output +=String(list_port_inf[13]) +"," ;
      output +=String(list_port_inf[14]) +"," ;
      output +=String(list_port_inf[15]) +"" ;
      output +="]}";
      sendStringSerial(output+"\r\n");
      break;
    case 1002: // Enable counter Timer 1
       TIMSK1 = (1 << TOIE1); 
      break;
    case 1003: //Stop All Load
      TIMSK1 = (0 << TOIE1);   // Stop timer
      stopAllLoad();
      //sendmfm383relaytorasp(resq,STS_SEND_NRM);
      break;
    case 1004:
      output="";
      output +="\"vln1\" : "+String(outParams.V1N) +",";
      sendStringSerial(output);
      output="";
      output +="\"v12\" : "+String(outParams.V12) +",";
      output +="\"v23\" : "+String(outParams.V23) +",";
      output +="\"v31\" : "+String(outParams.V31) +",";
      output +="\"vll\" : "+String(outParams.VLL) +",";
      sendStringSerial(output);
      break;
    case 2000: //control single Relay
      int port= (int) myObject["port"];
      int status= (int) myObject["status"];
      if(port>=0 && port<=16)
      {
        if(status==1)
        {
          onoffCtrlRelay(port,ON_RELAY_LOAD);
        }
        else if(status==0)
        {
          onoffCtrlRelay(port,OFF_RELAY_LOAD);
        }
         //sendmfm383relaytorasp(resq,STS_SEND_NRM); 
      }
      
      break;
  }
  
}
void sendStringSerial(String buffer)
{
  if(buffer.length()==0) 
  {
    return;
  }
  //buffer=buffer+"\r\n";
  for(long i = 0 ; i<buffer.length();i++)
  {
    Serial.write(buffer[i]);
  }
  Serial.flush();
}

void stopAllLoad()
{
  for(int port_index = 0 ; port_index<16; port_index++)
  {
      pcf8575.digitalWrite(port_index, OFF_RELAY_LOAD);
   
  }
}
void onoffCtrlRelay(int port,int onoff)
{
  if(port<0 || port>15)
    return;
  pcf8575.digitalWrite(port, onoff);
}

void ctrlRelayLoad(int len, int *data)
{
  for(int i = 0 ; i<len; i++)
  {
     onoffCtrlRelay(data[i], ON_RELAY_LOAD);
  }
}
void returnServerStatus(int resp, String error, int status)
{
  output="";
  output +="{\"error:\""+error+",";
  output +="\"dev:\""+String(ID_DEVICE)+",";
  output +="\"status:\""+String(status)+",";
  output +="\"resp:\""+String(resp)+"";
  output +="}}/r/n";
  Serial.println(output);
}

void checkLimitParams(float temp_c, float lmt_pw, float vol_ln, float lmt_cur)
{
  if(checkInParams.flag_emg_stop==false)
  {
    //ALARM
    if(temp_c>= checkInParams.alm_lmt_temp || lmt_pw>= checkInParams.alm_lmt_pwr || lmt_cur >= checkInParams.alm_lmt_vol_l_n )
    {
        onoffCtrlRelay(ALARM_RELAY_PORT, ON_RELAY_LOAD);
    }
    else
    {
        onoffCtrlRelay(ALARM_RELAY_PORT, OFF_RELAY_LOAD);
    }
    // RISK
    if(temp_c>= checkInParams.emg_lmt_temp || vol_ln>=checkInParams.emg_lmt_vol_ln || lmt_cur>=checkInParams.emg_lmt_cur)
    {
      // only reset system
      stopAllLoad();
      checkInParams.flag_emg_stop =true;
    }
  }

}