void setup(){
 pinMode(13, OUTPUT);s 
}

void loop(){
int incomingByte = Serial.read();
if(incomingByte=='1'){
//Open window code
digitalWrite(13, HIGH);

}
}

