void setup(){
 pinMode(13, OUTPUT); 
}

void loop(){
int incomingByte = Serial.read();
if(incomingByte=='1'){
//Open window code
digitalWrite(13, HIGH);

}
}

