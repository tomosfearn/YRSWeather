void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(13, OUTPUT); 
}

void Open(){
 //Needs coding 
}

void Close(){
 //Needs coding 
}




void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {
    if (Serial.read() == 'Open') {
      Open();
      delay(1000);
    }
    else if (Serial.read() == "Close"){
      Close();
      delay(1000); 
    }
  }
}








