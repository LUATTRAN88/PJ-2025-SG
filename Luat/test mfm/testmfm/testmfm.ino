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
byte arrReqMFM383[21][6] ={
              {0x01, 0x04, 0x00,0x00,0x00,0x18},// V1N
              {0x01, 0x04, 0x00,0x18,0x00,0x18},// V2N
              {0x01, 0x04, 0x00,0x30,0x00,0x0C},// V3N
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
  pzemSerial.setTimeout(10000);
  //SPI.begin();
  //SPI.Stop();
  thermoCouple.begin();
  thermoCouple.setSPIspeed(4000000);
  // PIN MODE
  pinMode(13, OUTPUT);
 
                     // cho phép ngắt toàn cục
}






void loop() {
    reqmfm383(sendmfm383(2),8);
    Serial.println("--");
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
  for(int col=0 ; col <8 ; col++ )
  {

     Serial.println(datacmd[col],HEX);
  }
  return datacmd;

}
byte repdata[125]={}; // 30 * 4 + 5 byte
float reqmfm383(byte *reqdata, int length)
{
    pzemSerial.write(reqdata,length);
    int cnt_data=0;
    int data_length=29;


    while(cnt_data<data_length)
    { 
      repdata[cnt_data++]=(byte)pzemSerial.read();

    }
  for(int col=0 ; col <data_length ; col++ )
  {

     Serial.print(repdata[col],HEX);
     Serial.print(" ");
  }
    Serial.println("");
    pzemSerial.flush();
    crc.clearCrc();
     unsigned short checksum =getCombine2Bytes(repdata[data_length-1],repdata[data_length-2]);
    //Modbus
    unsigned short crcvalue  = crc.Modbus(repdata,0,data_length-2);// 125 -2 

 
    float value=convertFloat(repdata[19],repdata[20],repdata[21],repdata[22]);
    delayMicroseconds(1000);
    if(crcvalue==checksum)
    {
      Serial.println(value);
      return value;
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
float convertFloat( byte b1, byte b2,byte b3,byte b4) {
  uint16_t H_value= getCombine2Bytes(b1,b2);
  uint16_t L_value= getCombine2Bytes(b3,b4);
  unsigned short data[2] = {L_value, H_value};
  float value;
  memcpy(&value, data, 4);
  return value;
}
