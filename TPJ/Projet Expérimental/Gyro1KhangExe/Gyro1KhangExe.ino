int XgyroPin = 3;               
int YgyroPin = 4;  
float gyroVoltage = 3.3;         
float gyroZeroVoltage = 337.59;   
float gyroSensitivity = .009;  
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
 
  float gyroRate = (analogRead(XgyroPin));

  gyroRate -= gyroZeroVoltage;


  if (gyroRate >= rotationThreshold || gyroRate <= -rotationThreshold) 
  {
 
    currentAngle += gyroRate;
  }

  if (currentAngle < 0)
    currentAngle += 360;
  else if (currentAngle > 359)
    currentAngle -= 360;
    
  delay(10);
  
  if (gyroRate > 90)
 {
   digitalWrite(ledPin, HIGH);
 }
  else
 {
  digitalWrite(ledPin, LOW);
 } 
 gyroRate -= gyroRate;
}
