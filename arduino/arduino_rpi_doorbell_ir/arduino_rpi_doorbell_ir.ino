/*

  This example code is in the public domain.
  http://www.arduino.cc/en/Tutorial/Tone
*/

#include "pitches.h"
#include  <IRremote.h>

// setup of doorbell
//
int speakerPin = 3;
int message = 0;
// Setup of ir/mhz input
const int irReceiverPin = 9; //the SIG of receiver module attach to pin7 
const int ledPin = 13;//pin 13 built-in led
IRrecv irrecv(irReceiverPin); //Creates a variable of type IRrecv
decode_results results;


//Link secret found
int melody1[] = {
   NOTE_G4, NOTE_FS4, NOTE_DS4, NOTE_A3, NOTE_GS3, 
   NOTE_E4, NOTE_GS4, NOTE_C5 
  };
int noteDurations1[] = {
  //8,16,16,8,16,8,16,8
  8,8,8,8,8,8,8,3
};

//Quick tones
int melody2[] = {
  NOTE_C5, NOTE_D3, NOTE_E5, NOTE_C4 
};
int noteDurations2[] = {
  8,8,8,8 
};

//Doorbell melody
int melody3[] = {
  NOTE_E4, NOTE_C4, NOTE_D4, NOTE_G3, 0, NOTE_G3, NOTE_D4,  NOTE_E4, NOTE_C4 
};
int noteDurations3[] = {
  4, 4, 4, 1, 8, 4, 4, 4, 1
};

void ring(int melody[], int noteDurations[]){
 // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 9; thisNote++) {
    // to calculate the note duration, take one second divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(speakerPin, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    //int pauseBetweenNotes = noteDuration * 1.10;
    int pauseBetweenNotes = noteDuration;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(speakerPin);
  }
}







void setup() {
  Serial.begin(9600);
  
  //Setup IR/mhz input
  irrecv.enableIRIn(); //enable ir receiver module 
}

void loop() {
  
  if (Serial.available())  {
    message = Serial.read() - '0';
    Serial.println(message);
    
    if (message == 1) {
      ring(melody1,noteDurations1);
    }
    else if (message == 2) {
      ring(melody2,noteDurations2);
    }
    else if (message == 3){
      ring(melody3,noteDurations3);
    } 
  }
  
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
