/*
teste3 Khang Arduino led light avec button toggle
*/

int buttonPin = 3;
int ledPin = 13;
boolean ledState = false;


void setup ()
{
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop ()
{
  // lesState est si le led est on (false = off, true = on)
  if (digitalRead(buttonPin) == HIGH && ledState == false)
  {
    digitalWrite(ledPin, HIGH);
    ledState = true;
  }
  // si led est on turn off et set ledState a false
  if (digitalRead(buttonPin) == HIGH && ledState == true)
  {
    digitalWrite(ledPin, LOW);
    ledState = false;
  }
}
