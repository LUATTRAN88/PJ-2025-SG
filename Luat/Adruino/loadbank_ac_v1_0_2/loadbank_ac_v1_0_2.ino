#include <SoftwareSerial.h> 
#include "PCF8575.h"
#include <Crc16.h>
#include <ArduinoJson.h>
#include "MAX6675.h"

#define ID_DEVICE  250101

#define BUZZ_ALARM_ON_ARUINO_PORT 13
#define ALARM_RELAY_PORT 14
//STATUS RESPONSE
#define STS_SEND_NRM 200
#define STS_SEND_ERR 201
#define STS_SEND_BUSY 202
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
byte arrReqMFM383[3][6] ={
              {0x01, 0x04, 0x00,0x00,0x00,0x18},// Address :0x00  LENGTH 24 data
              {0x01, 0x04, 0x00,0x18,0x00,0x18},// Address :0x18  LENGTH 24 data
              {0x01, 0x04, 0x00,0x30,0x00,0x0C},// Address :0x30  LENGTH 12 data 
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
volatile float KVA1=0.0;
volatile float KVA2=0.0;
volatile float KVA3=0.0;
volatile float KVAr1=0.0;
volatile float KVAr2=0.0;
volatile float KVAr3=0.0;
volatile float TKVA=0.0;
volatile float TKVAr=0.0;
volatile float FRQ=0.0;
volatile float APF=0.0;
volatile float PF1=0.0;
volatile float PF2=0.0;
volatile float PF3=0.0;
volatile float TKW=0.0;
volatile float KWH=0.0;
volatile float temperature;
volatile long timer1_counter_val=-1;
volatile long timer1_counter_set=-1;
volatile byte flag_timer_cnt_target = -1;

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
  //SPI.begin();
  //SPI.Stop();
  thermoCouple.begin();
  thermoCouple.setSPIspeed(4000000);
  // PIN MODE
  pinMode(13, OUTPUT);
 
  //Scheduler.startLoop(sendmfm383relaytorasp);
   
  cli();                                  // tắt ngắt toàn cục   
  TCCR1A = 0;
  TCCR1B = 0;
  TIMSK1 = 0;
  TCCR1B |= (1 << CS12) | (1 << CS10);    // prescale = 1024
  TCNT1 = 49911; // 1s interrupt
  TIMSK1 = (1 << TOIE1);                  // Overflow interrupt enable 
  sei();                        // cho phép ngắt toàn cục
}

ISR (TIMER1_OVF_vect) 
{
    TCNT1 = 49911;

    if(timer1_counter_val>0){
      
      timer1_counter_val--;
      flag_timer_cnt_target=1;
    }
    if(timer1_counter_val== 0)
    {
        flag_timer_cnt_target=0;
        timer1_counter_val=-1;
        
    }


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
  if(millis() -time_mask_coldata >100){
      sendmfm383relaytorasp();

     // getdata_V(200);
     time_mask_coldata=millis();
 } 
  /*if(dataComplete==false)   
  { 
    serialEvent();
    dataComplete = false;
  }
  delay(1000);
   */                                                                                                                                                                                                                                                                                              
  // timer control
    if( flag_timer_cnt_target== 0)
    {
      stopAllLoad();
      flag_timer_cnt_target=-1;
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

reqmfm383(sendmfm383(0),8,1);
reqmfm383(sendmfm383(0),8,2);
reqmfm383(sendmfm383(2),8,3);


int thermo_status = thermoCouple.read();
temperature = thermoCouple.getTemperature();
}

void collectiondata(int req, int page)
{
    
     readPortPCF8575();
      String output;
      output.reserve(100);
      output +="{";
      output +="\"req\":"+String(req) +",";
      output +="\"status\":"+String(200) +",";
      output +="\"page\":"+String(page) +",";
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
      output +="\"avpf\" : "+String(APF) +",";
      sendStringSerial(output);
      output="";
      output.reserve(100);
      output +="\"tim1cnt\" : "+String(timer1_counter_val) +",";
      output +="\"tim1set\" : "+String(timer1_counter_set) +",";
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
      sendStringSerial(output+"#");

}

byte* sendmfm383(int row)
{
  memset(datacmd, 0, sizeof(datacmd));
  for(int col=0 ; col <6 ; col++ )
  {
    datacmd[col]=arrReqMFM383[row][col];
  }
  crc.clearCrc();
  unsigned short crcvalue  = crc.Modbus(datacmd,0,6);
  byte L_Byte= (byte)crcvalue;
  byte H_Byte= (byte)(crcvalue>>8);
  datacmd[6]=L_Byte;
  datacmd[7]=H_Byte;
 /* for(int col=0 ; col <8 ; col++ )
  {

     Serial.println(datacmd[col],HEX);
  }*/
  return datacmd;

}

int data_length=0;
float reqmfm383(byte *reqdata, int length, int intv)
{
  byte repdata[70]={}; // 30 * 4 + 5 byte
   memset(repdata, 0, 70);

    pzemSerial.write(reqdata,length);
    int cnt_data=0;
    data_length=0;
    if( intv == 1 || intv == 2 ) 
    {
      data_length=53;
    }
    else
    {
      data_length=29;
    }
 


    while(cnt_data<data_length)
    { 
      if(pzemSerial.available() > 0)
      {
        repdata[cnt_data++]=(byte)pzemSerial.read();
      }


    }

    pzemSerial.flush();
    crc.clearCrc();
     unsigned short checksum =getCombine2Bytes(repdata[data_length-1],repdata[data_length-2]);
    //Modbus
    unsigned short crcvalue  = crc.Modbus(repdata,0,data_length-2);// 125 -2 


    delayMicroseconds(1000);
    if(crcvalue==checksum)
    {
        if( intv == 1) 
        {

            V1N=convertFloat(repdata[3],repdata[4],repdata[5],repdata[6]);
            V2N=convertFloat(repdata[7],repdata[8],repdata[9],repdata[10]);
            V3N=convertFloat(repdata[11],repdata[12],repdata[13],repdata[14]);
            VLN=convertFloat(repdata[15],repdata[16],repdata[17],repdata[18]);
            V12=convertFloat(repdata[19],repdata[20],repdata[21],repdata[22]);
            V23=convertFloat(repdata[23],repdata[24],repdata[25],repdata[26]);
            V31=convertFloat(repdata[27],repdata[28],repdata[29],repdata[30]);
            VLL=convertFloat(repdata[31],repdata[32],repdata[33],repdata[34]);
            I1=convertFloat(repdata[35],repdata[36],repdata[37],repdata[38]);
            I2=convertFloat(repdata[39],repdata[40],repdata[41],repdata[42]);
            I3=convertFloat(repdata[43],repdata[44],repdata[45],repdata[46]);
            AVI=convertFloat(repdata[48],repdata[49],repdata[50],repdata[51]);
        }
        else if ( intv == 2)
        {
          
            KW1=convertFloat(repdata[3],repdata[4],repdata[5],repdata[6]);
            KW2=convertFloat(repdata[7],repdata[8],repdata[9],repdata[10]);
            KW3=convertFloat(repdata[11],repdata[12],repdata[13],repdata[14]);
            KVA1=convertFloat(repdata[15],repdata[16],repdata[17],repdata[18]);
            KVA2=convertFloat(repdata[19],repdata[20],repdata[21],repdata[22]);
            KVA3=convertFloat(repdata[23],repdata[24],repdata[25],repdata[26]);
            KVAr1=convertFloat(repdata[27],repdata[28],repdata[29],repdata[30]);
            KVAr2=convertFloat(repdata[31],repdata[32],repdata[33],repdata[34]);
            KVAr3=convertFloat(repdata[35],repdata[36],repdata[37],repdata[38]);
            TKW=convertFloat(repdata[39],repdata[40],repdata[41],repdata[42]);
            TKVA=convertFloat(repdata[43],repdata[44],repdata[45],repdata[46]);
            TKVAr=convertFloat(repdata[48],repdata[49],repdata[50],repdata[51]);

        }
        else
        {
            PF1=convertFloat(repdata[3],repdata[4],repdata[5],repdata[6]);
            PF2=convertFloat(repdata[7],repdata[8],repdata[9],repdata[10]);
            PF3=convertFloat(repdata[11],repdata[12],repdata[13],repdata[14]);
            APF=convertFloat(repdata[15],repdata[16],repdata[17],repdata[18]);
            FRQ=convertFloat(repdata[19],repdata[20],repdata[21],repdata[22]);
            KWH=convertFloat(repdata[23],repdata[24],repdata[25],repdata[26]);
        }
      return 0;
    }
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
/*float convertFloat(unsigned short reg_low, unsigned short reg_high) {

  unsigned short data[2] = {reg_low, reg_high};
  float value;
  memcpy(&value, data, 4);
  return value;
}*/
float convertFloat( byte b1, byte b2,byte b3,byte b4) {
  uint16_t H_value= getCombine2Bytes(b1,b2);
  uint16_t L_value= getCombine2Bytes(b3,b4);
  unsigned short data[2] = {L_value, H_value};
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
    {
        /*checkInParams.alm_lmt_temp= (int) myObject["alm_lmt_temp"];
        checkInParams.alm_lmt_vol_l_n= (int) myObject["alm_lmt_vol_l_n"];
        checkInParams.alm_lmt_pwr= (int) myObject["alm_lmt_vol_pwr"];
        checkInParams.emg_lmt_temp= (int) myObject["emg_lmt_temp"];
        checkInParams.emg_lmt_cur= (int) myObject["emg_lmt_cur"];
        checkInParams.emg_lmt_vol_ln= (int) myObject["emg_lmt_vol_ln"];*/
        int page= (int) myObject["page"];
        collectiondata(resq,page);
      break;
    }
    case 1001: // vll
    {
        alarmRunning(4,150);
        timer1_counter_val = myObject["tm_s"];
       
        timer1_counter_set = timer1_counter_val;
        TIMSK1 = (1 << TOIE1); 
        JsonArray actions = myObject["port"];

        byte portlist[16];
        int index=0;
        for (JsonVariant value : actions) {
           portlist[index++]=value.as<byte>();
        }
        ctrlRelayLoad(index,portlist,ON_RELAY_LOAD);
        alarmRunning(3,150);
      break;
    }
    case 1007: // Enable counter Timer 1
    {
      alarmRunning(4,50);
      TIMSK1 = (0 << TOIE1);   // Stop timer
      timer1_counter_val=-1;
      flag_timer_cnt_target=-1;
      dropAllLoad();
     
      break;
    }
    case 1008: // Enable counter Timer 1
    {
       TIMSK1 = (1 << TOIE1); 
      break;
    }
    case 1009: //Stop All Load
    {
      alarmRunning(4,50);
      TIMSK1 = (0 << TOIE1);   // Stop timer
      timer1_counter_val=-1;
      flag_timer_cnt_target=-1;
      stopAllLoad();
      //sendmfm383relaytorasp(resq,STS_SEND_NRM);
      break;
    }
    case 1010: //control single Relay
    {
       
        alarmRunning(4,150);
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
        break;
    }

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
void dropAllLoad()
{
  for(int port_index = 0 ; port_index<16; port_index++)
  {
      pcf8575.digitalWrite(port_index, OFF_RELAY_LOAD);
      delay(1000);
      
  }
  alarmRunning(3,50);
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

void ctrlRelayLoad(int len, byte *_portls,int onoff) 
{
  for(int pix = 0 ; pix<NUM_RELAY; pix++)
  {
    int no_exit_lyn=true;
    for(int ix = 0 ; ix<len; ix++)
    {
        if(_portls[ix] ==pix)
        {
          no_exit_lyn=false;
          break; 
        }
    }
    if(no_exit_lyn==true)
    {
      onoffCtrlRelay(pix, OFF_RELAY_LOAD);
    }
  }

  for(int ix = 0 ; ix<len; ix++)
  {
    uint8_t p_val=pcf8575.digitalRead(_portls[ix],true);
    if(p_val==OFF_RELAY_LOAD)
    {
      onoffCtrlRelay(_portls[ix], ON_RELAY_LOAD);
      delay(1000);
    }
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
void alarmRunning(int mode, int delay_time)
{
   if(mode == 1) // tick 1
   {
      PINB = bit (5); // toggle D13
      delay (delay_time); 
      PINB = bit (5); // toggle D13 
   }
   else if(mode == 2) // tick tick
   {
      PINB = bit (5); // toggle D13
      delay (delay_time); 
      PINB = bit (5); // toggle D13 
      delay (delay_time);
      PINB = bit (5); // toggle D13
      delay (delay_time);
      PINB = bit (5); // toggle D13
   }
   else if(mode == 3) // tick tick tick
   {
      PINB = bit (5); // toggle D13
      delay (delay_time); 
      PINB = bit (5); // toggle D13 
      delay (delay_time);
      PINB = bit (5); // toggle D13
      delay (delay_time);
      PINB = bit (5); // toggle D13
      delay (delay_time);
      PINB = bit (5); // toggle D13
      delay (delay_time);
      PINB = bit (5); // toggle D13
   }
  else if(mode == 4) // tick --- .....
   {
      PINB = bit (5); // toggle D13
      delay (delay_time); 
      delay (delay_time);
      delay (delay_time);
      PINB = bit (5); // toggle D13

   }
}
