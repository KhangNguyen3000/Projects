/*
teste2 Khang Arduino led light avec button
*/

int buttonPin = (pin qui se trouve le bouton);
int ledPin = (pin qui se trouve la led light);

void setup ()
{
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop ()
{
  // == veut dire is equal too
  if (digitalRead(buttonPin) == HIGH)
  {
    digitalWrite(ledPin, HIGH);
  }
  // if (digitalRead(buttonPin) == LOW) fonctionnerait aussi mais il a seulement 2 possibiliters
  else
  {
    digitalWrite(ledPin, LOW);
  }
}
