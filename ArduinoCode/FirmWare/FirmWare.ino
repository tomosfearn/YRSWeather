const int dPin = 9;
const int sPin = 10;

int sVal = 0;
int fVal = 140;


void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(13, OUTPUT); 
  pinMode(dPin, OUTPUT);
  pinMode(sPin, OUTPUT);
  analogWrite(dPin, sVal);
}

void Open(){
  digitalWrite(sPin, HIGH);
  analogWrite(dPin, fVal);
  delay(10000);
  analogWrite(dPin, sVal);
  delay(1000);  
}

void Close(){
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
    if (Serial.read() == 'Open') {
      Open();
      delay(1000);
    }
    //else if (Serial.read() == "Close"){
     // Close();
      //delay(1000); 
    //}
  }
}








