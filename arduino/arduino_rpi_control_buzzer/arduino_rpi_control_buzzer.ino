/*
  Runs a particular tune when 
  it reads an integer from the 
  serial input
  http://www.arduino.cc/en/Tutorial/Tone
*/

#include "pitches.h"
int speakerPin = 3;
int message = 0;


//Link secret found
int melody1[] = {
   NOTE_G5, NOTE_FS5, NOTE_DS5, NOTE_A4, NOTE_GS4, 
   NOTE_E5, NOTE_GS5, NOTE_C6 
  };
int noteDurations1[] = {
  //8,8,8,8,8,8,8,3
  10,10,10,10,10,10,10,3
};

//Quick tones
int melody2[] = {
  NOTE_C5, NOTE_D3, NOTE_E5, NOTE_C4 
};
int noteDurations2[] = {
  10,10,10,10 
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
    int pauseBetweenNotes = noteDuration * 1.20;
    //int pauseBetweenNotes = noteDuration*1.1;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(speakerPin);
  }
}

void setup() {
  delay(5000);
  
  
  Serial.begin(9600);

  while (!Serial) {
    delay(1000);
    ; // wait for serial port to connect. Needed for native USB
  }
  ring(melody1,noteDurations1);
}

void loop() {
  //Serial.println('temp');
  //delay(100);
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
  
}
