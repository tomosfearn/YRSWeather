#include <Arduino.h>

void setup();
void loop();
void actuatorReverse();
#line 1 "src/sketch.ino"
const int dPin = 9;
const int sPin = 10;

int sVal = 0;
int fVal = 140;

void setup()
{
  pinMode(dPin, OUTPUT);
  pinMode(sPin, OUTPUT);
  pinMode(11,OUTPUT);
  digitalWrite(11,HIGH);
  analogWrite(dPin, sVal);
}

void loop()
{
   actuatorReverse();
}

void actuatorReverse()
{
  digitalWrite(sPin, LOW);
  analogWrite(dPin, fVal);
  delay(10000);
  analogWrite(dPin, sVal);
  delay(10000); 
}
