const int fPin = 3;
const int rPin = 4;

void setup()
{
  pinMode(fPin, OUTPUT);
  pinMode(rPin, OUTPUT);
  digitalWrite(fPin, LOW);
  digitalWrite(rPin, LOW);
}

//assuming 0 is complete stop
//it may be 127
//ou will have to check
void loop()
{
  // forwards
  analogWrite(rPin, 0);
  analogWrite(fPin, 255);
  delay(1000);
  //backwards
  analogWrite(fPin, 0);
  analogWrite(rPin, 255);
  delay(1000);
}
