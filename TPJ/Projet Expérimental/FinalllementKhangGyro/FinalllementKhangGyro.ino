#include "cool.h"
//http://developer.mbed.org/cookbook/ITG-3200-Gyroscope

int gyroPin = 3;  
int gyroPin2 = 4;
int gyroPin3 = 5;
int ledPin = 13;
int buttonPin = 2;
int buttonPine = 0;
int readX1 = 0;
int readY1 = 0;
int readZ1 = 0;

void setup ()
{
  Serial.begin (9600);
   pinMode (gyroPin, INPUT);
   pinMode (buttonPin, INPUT);
   pinMode (gyroPin2, INPUT);
   pinMode (ledPin, OUTPUT);
   digitalWrite (ledPin, LOW);
   digitalWrite (buttonPin, LOW);


}

void loop ()
{
        readX1 = readX();
      readY1 = readY();
      readZ1 = readZ();
 Serial.print("x");
 Serial.print(readX1);
 Serial.print("\t");
 Serial.print("y");
 Serial.print(readY1);
 Serial.print("\t");
 Serial.print("z");
 Serial.print(readZ1);
 Serial.print("\t");
 delay(2000);
}
