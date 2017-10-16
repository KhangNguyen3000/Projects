int XgyroPin = 3;               
int YgyroPin = 4;  
float gyroVoltage = 5;         
float gyroZeroVoltage = 2.2;   
float gyroSensitivity = .022;  
float rotationThreshold = 1;
int ledPin = 13;

float currentAngle = 0;         

void setup() 
{
  Serial.begin (9600);
  pinMode(ledPin, OUTPUT);
  pinMode (XgyroPin, INPUT);
  digitalWrite(ledPin, LOW);
}

void loop() 
{
  float gyroRate = (analogRead(XgyroPin) * gyroVoltage) / 1023;

  gyroRate -= gyroZeroVoltage;

  gyroRate /= gyroSensitivity;

  if (gyroRate >= rotationThreshold || gyroRate <= -rotationThreshold) 
  {
    gyroRate /= 100;
    currentAngle += gyroRate;
  }

  if (currentAngle < 0)
    currentAngle += 360;
  else if (currentAngle > 359)
    currentAngle -= 360;
  Serial.println(currentAngle);

  delay(10);
  
  if (currentAngle > 30)
 {
   digitalWrite(ledPin, HIGH);
 }
  else
 {
  digitalWrite(ledPin, LOW);
 } 
}
