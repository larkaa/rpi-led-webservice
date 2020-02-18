/***********************************************
* name:Infrared-Receiver
* function:press the Power key of a remote control,
* and both the LED attached and that connected to pin 13 on the SunFounder Uno board will light up.
* Then press any other key, and the LEDs will go out.
**********************************************/
#include  <IRremote.h>

const int irReceiverPin = 10; //the SIG of receiver module attach to pin7 
const int ledPin = 13;//pin 13 built-in led

IRrecv irrecv(irReceiverPin); //Creates a variable of type IRrecv
decode_results results;

void setup()
{
  pinMode(ledPin,OUTPUT);//set ledpin as OUTPUT
  Serial.begin(9600);//initialize serial 
  irrecv.enableIRIn(); //enable ir receiver module 
  //digitalWrite(ledPin,LOW);
}

void loop() 
{
  if (irrecv.decode(&results)) //if the ir receiver module receiver data
  { 
    Serial.print("irCode: "); //print"irCode: " 
    Serial.print(results.value, HEX); //print the value in hexdecimal 
    Serial.print(", bits: "); //print" , bits: " 
    Serial.println(results.bits); //print the bits
    irrecv.resume(); // Receive the next value 
  } 
  delay(600); //delay 600ms
  if(results.value == 0xE318261B)//if receiver module receive OxE318261B
  {
    digitalWrite(ledPin,HIGH);//turn on the led
  }
  else
  {
    digitalWrite(ledPin,LOW);//turn off the led
  }
}
