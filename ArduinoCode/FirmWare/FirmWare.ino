const int dPin = 9;
const int sPin = 10;

int sVal = 0;
int fVal = 140;

void setup()
{
  pinMode(dPin, OUTPUT);
  pinMode(sPin, OUTPUT);
  analogWrite(dPin, sVal);
}

void actuatorForwards()
{
  digitalWrite(sPin, HIGH);
  analogWrite(dPin, fVal);
  delay(10000);
  analogWrite(dPin, sVal);
  delay(1000);
}

void actuatorReverse()
{
  digitalWrite(sPin, LOW);
  analogWrite(dPin, fVal);
  delay(10000);
  analogWrite(dPin, sVal);
  delay(10000);
}

void loop()
{
  // if there's any serial available, read it:
 while (Serial.available() > 0) {
 if (Serial.read() == 'O') {
 	actuatorForwards()
 }
 else if (Serial.read() == "C") {
	actuatorReverse()
 }
 }
}

