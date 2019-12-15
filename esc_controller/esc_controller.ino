#include <Servo.h>
Servo ESC;     // create servo object to control the ESC
int potValue;  // value from the analog pin
int deger=0;
void setup() {
  // Attach the ESC on pin 9
  ESC.attach(9,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  Serial.begin(9600);
}
void loop() {
    // reads the value of the potentiometer (value between 0 and 1023)
  //Serial.println("Esc ye gönderilecek bilgiyi giriniz");
  if(Serial.available()){

      deger=Serial.parseInt();
      potValue = map(deger, 0, 255, 25, 180);   // scale it to use it with the servo library (value between 0 and 180)
      Serial.println(deger);
      ESC.write(potValue);    // Send the signal to the ESC
    
    }
  
}
