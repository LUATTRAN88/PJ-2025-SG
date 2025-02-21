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

volatile float V1N=0.0;
volatile float V2N=0.0;
volatile float V3N=0.0;
volatile float VLN=0.0;
volatile float V12=0.0;
volatile float V23=0.0;
volatile float V31=0.0;
volatile float VLL=0.0;
volatile float I1=0.0;
volatile float I2=0.0;
volatile float I3=0.0;
volatile float AVI=0.0;
volatile float KW1=0.0;
volatile float KW2=0.0;
volatile float KW3=0.0;
volatile float FRQ=0.0;
volatile float AVPF=0.0;
volatile float PF1=0.0;
volatile float PF2=0.0;
volatile float PF3=0.0;
volatile float TKW=0.0;
volatile float temperature;
volatile float timer1_counter_val;
//manage Time delay;
unsigned long time_mask_coldata = 1000;


CheckInParams checkInParams;
void setup() {

  Serial.begin(9600);
  Serial.setTimeout(1000);
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

  time_mask_coldata=millis();

}




void loop() {
  if(dataComplete==false)   
  { 
    serialEvent();
    dataComplete = false;
  }

   if(millis() -time_mask_coldata >500){
      sendmfm383relaytorasp();
     // getdata_V(200);
      time_mask_coldata=millis();
    }
                                                                                                                                                                                                                                                                                                                     

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
    }
  }
}// Read PORT Relay
void sendmfm383relaytorasp()
{
 
V1N=reqmfm383(sendmfm383(0),8);
//delayMicroseconds(10);
V2N=reqmfm383(sendmfm383(1),8);
//delayMicroseconds(100);
V3N=reqmfm383(sendmfm383(2),8);
//delayMicroseconds(10);
VLN=reqmfm383(sendmfm383(3),8);
//delayMicroseconds(10);
V12=reqmfm383(sendmfm383(4),8);
//delayMicroseconds(10);
V23=reqmfm383(sendmfm383(5),8);
//delayMicroseconds(10);
V31=reqmfm383(sendmfm383(6),8);
delayMicroseconds(10);
VLL=reqmfm383(sendmfm383(7),8);
//delayMicroseconds(10);
I1=reqmfm383(sendmfm383(8),8);
//delayMicroseconds(10);
I2=reqmfm383(sendmfm383(9),8);
//delayMicroseconds(10);
I3=reqmfm383(sendmfm383(10),8);
//delayMicroseconds(10);
AVI=reqmfm383(sendmfm383(11),8);
//delayMicroseconds(10);
KW1=reqmfm383(sendmfm383(12),8);
//delayMicroseconds(10);
KW2=reqmfm383(sendmfm383(13),8);
//delayMicroseconds(10);
KW3=reqmfm383(sendmfm383(14),8);
//delayMicroseconds(10);
TKW=reqmfm383(sendmfm383(15),8);
//delayMicroseconds(10);
FRQ=reqmfm383(sendmfm383(16),8);
//delayMicroseconds(10);
PF1=reqmfm383(sendmfm383(17),8);
//delayMicroseconds(10);
PF2=reqmfm383(sendmfm383(18),8);
//delayMicroseconds(10);
PF3=reqmfm383(sendmfm383(19),8);
//delayMicroseconds(10);
AVPF=reqmfm383(sendmfm383(20),8);

int thermo_status = thermoCouple.read();
temperature = thermoCouple.getTemperature();
}

void collectiondata()
{
    
     readPortPCF8575();
      String output;
      output.reserve(100);
      output +="{\"req\":200,";
      output +="\"status\":200,";
      output +="\"info\":{";
      sendStringSerial(output);
      String output2;
      output2="";
      output.reserve(100);
      output2 +="\"vln1\" : "+String(V1N) +",";
      output2 +="\"vln2\" : "+String(V2N) +",";
      sendStringSerial(output2);
      output="";
      output.reserve(100);
      output +="\"vln3\" : "+String(V3N) +",";
      output +="\"vln\" : "+String(VLN) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"v12\" : "+String(V12) +",";
      output +="\"v23\" : "+String(V23) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"v31\" : "+String(V31) +",";
      output +="\"vll\" : "+String(VLL) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"cur1\" : "+String(I1) +",";
      output +="\"cur2\" : "+String(I2) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
  
      output +="\"cur3\" : "+String(I3) +",";
      output +="\"avi\" : "+String(AVI) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      
      output +="\"kw1\" : "+String(KW1) +",";
      output +="\"kw2\" : "+String(KW2) +",";
      output +="\"kw3\" : "+String(KW3) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"tkw\" : "+String(TKW) +",";
      output +="\"freq\" : "+String(FRQ) +",";
      output +="\"pf1\" : "+String(PF1) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"pf2\" : "+String(PF2) +",";
      output +="\"pf3\" : "+String(PF3) +",";
      output +="\"avpf\" : "+String(AVPF) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"tim1_cnt\" : "+String(timer1_counter_val) +",";
      output +="\"tempc\" : "+String(temperature) +"";
      output +="},";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"rls\":[";
      output +=String(list_port_inf[0]) +"," ;
      output +=String(list_port_inf[1]) +"," ;
      output +=String(list_port_inf[2]) +"," ;
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +=String(list_port_inf[3]) +"," ;
      output +=String(list_port_inf[4]) +"," ;
      output +=String(list_port_inf[5]) +"," ;
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +=String(list_port_inf[6]) +"," ;
      output +=String(list_port_inf[7]) +"," ;
      output +=String(list_port_inf[8]) +"," ;
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +=String(list_port_inf[9]) +"," ;
      output +=String(list_port_inf[10]) +"," ;
      output +=String(list_port_inf[11]) +"," ;
      output +=String(list_port_inf[12]) +"," ;
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +=String(list_port_inf[13]) +"," ;
      output +=String(list_port_inf[14]) +"," ;
      output +=String(list_port_inf[15]) +"" ;
      output +="]}";
      sendStringSerial(output+"\r\n\n\n");

}
void getdata_V(int rep)
{
      String output;
      output="";
      output +="status:200\n";
      output +="rep:"+String(rep)+"\n";
      output +="vln:"+String(V1N,2)+"-" +String(V2N,2) +"-"+String(V3N,2)+ "-"+String(VLN,2)+"\n";
      output +="vpp:"+String(V12,2)+"-" +String(V23,2) +"-"+String(V31,2)+ "-"+String(VLL,2)+"\n";
      output +="cur:"+String(I1,2)+"-" +String(I2,2) +"-"+String(I3,2)+ "-"+String(AVI,2)+"\n";
      output +="pf:"+String(PF1,2)+"-" +String(PF2,2) +"-"+String(PF3,2)+ "-"+String(AVPF,2)+"\n";
      output +="kw:"+String(KW1,2)+"-" +String(KW2,2) +"-"+String(KW3,2)+ "-"+String(TKW,2)+"\n";
      output +="v2:"+String(temperature,2) +"\n";
      output +="fq:"+String(FRQ,2) +"\n";
      output +="rls:[";
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
      output +="]";
      output +="####";
      sendStringSerial(output);
      
}


void getdata_Relays(int rep)
{
      
     readPortPCF8575();
     String output;
      output="";
      output +="{\"rep\":"+String(rep)+",";
      output +="\"status\":200,";
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
      sendStringSerial(output);

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
    delayMicroseconds(1000);
    while(cnt_data<100)
    { 
      if(pzemSerial.available()>8)
      { 
        //  repdata[i]=pzemSerial.read();
        pzemSerial.readBytes(repdata,data_length);
        break;
      }
      cnt_data++;
      delayMicroseconds(10000);
    }
    pzemSerial.flush();
    crc.clearCrc();
     unsigned short checksum =getCombine2Bytes(repdata[data_length-1],repdata[data_length-2]);
    //Modbus
    unsigned short crcvalue  = crc.Modbus(repdata,0,7);

    uint16_t H_value= getCombine2Bytes(repdata[3],repdata[4]);
    uint16_t L_value= getCombine2Bytes(repdata[5],repdata[6]);
    float value=convertFloat(L_value,H_value);
    delayMicroseconds(1000);
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
        /*checkInParams.alm_lmt_temp= (int) myObject["alm_lmt_temp"];
        checkInParams.alm_lmt_vol_l_n= (int) myObject["alm_lmt_vol_l_n"];
        checkInParams.alm_lmt_pwr= (int) myObject["alm_lmt_vol_pwr"];
        checkInParams.emg_lmt_temp= (int) myObject["emg_lmt_temp"];
        checkInParams.emg_lmt_cur= (int) myObject["emg_lmt_cur"];
        checkInParams.emg_lmt_vol_ln= (int) myObject["emg_lmt_vol_ln"];*/
        collectiondata();
      break;
    case 1001: // vll
      //getdata_V(resq,V12,V23,V31,FRQ);
      break;
    case 1002: // v1n
     // getdata_V(resq,V1N,V2N,V3N,VLN);
      break;
    case 1003: // cur
      //getdata_V(resq,I1,I2,I3,AVI);
      break;
    case 1004: // pf
      //getdata_V(resq,PF1,PF2,PF3,AVPF);
      break;
    case 1005: // kw
     // getdata_V(resq,KW1,KW2,KW3,TKW);
      break;
    case 1006: // INFO
     // getdata_V(resq,FRQ,temperature,timer1_counter_val,0.0);
      break;
    case 1007: // Read Data sensor and control
     // getdata_Relays(resq);
      break;
    case 1008: // Enable counter Timer 1
       TIMSK1 = (1 << TOIE1); 
      break;
    case 1009: //Stop All Load
      TIMSK1 = (0 << TOIE1);   // Stop timer
      stopAllLoad();
      //sendmfm383relaytorasp(resq,STS_SEND_NRM);
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
         
      }
      //getdata_Relays(2000);
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