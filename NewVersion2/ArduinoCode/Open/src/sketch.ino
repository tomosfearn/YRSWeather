//Arduino Code
const int dPin = 9;
const int sPin = 10;

int sVal = 0;
int fVal = 140;

void setup()
{
  pinMode(dPin, OUTPUT);
  pinMode(sPin, OUTPUT);
  pinMode(11,OUTPUT);
  digitalWrite(11,LOW); 
  analogWrite(dPin, sVal);
}

void loop()
{
  actuatorForwards();
}

void actuatorForwards()
{
  digitalWrite(sPin, HIGH);
  analogWrite(dPin, fVal);
  delay(10000);
  analogWrite(dPin, sVal);
  delay(1000);  
}
