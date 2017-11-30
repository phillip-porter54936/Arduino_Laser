// Code tuned for robot 3
// modified: 10/03/2017, Houman Dallali
// modified: 11/9/17   Phillip Porter
// COMP 469

#include <Servo.h>
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  static int count = 0;
  if (Serial.available())
  {
    Serial.print((char)(Serial.read()));
    if (count++ > 60)
    {
      Serial.println("");
      count = 0;
    }
  }
}
