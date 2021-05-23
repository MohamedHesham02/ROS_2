#define Channel_A 2
#define Channel_B 3
int counter=0;

void setup() {
  // put your setup code here, to run once
pinMode(ISR_A,INPUT);
pinMode(ISR_B,INPUT);
attachInterrupt(digitalPinToInterrupt(2), ISR_A, CHANGE);
attachInterrupt(digitalPinToInterrupt(3), ISR_B, CHANGE);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
}

void ISR_A(){

 counter++;
 if (digitalRead(Channel_B)==0 & digitalRead(Channel_A)==1)
 
 {
 counter++;
 Serial.println(counter);
 }
 else
 {
 counter--;
 Serial.println(counter);
 }

}

void ISR_B(){

 counter++;
 if (digitalRead(Channel_A)==0 & digitalRead(Channel_B)==1)
 {
 counter++;
 Serial.println(counter);
 }
 else
 {
 counter--;
 Serial.println(counter);
 }
}
