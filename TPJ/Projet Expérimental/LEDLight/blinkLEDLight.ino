/*
Teste 1 Khang Arduino Uno
*/
// 13 a deja une led dedans 
int ledPin = 13;

void setup ()
{
   pinMode(ledPin, OUTPUT);  
}

void loop ()
{
  //digitalWrite qui change proprieter physique (voltage dans cet cas) low is 0V et High is 3.3V ou 5V
   digitalWrite(ledPin, HIGH);
   //delay qui est en millisecond (1000 millisecond = 1 second)
   delay(1000);
   digitalWrite(ledPin, LOW);
   delay(1000);
}
