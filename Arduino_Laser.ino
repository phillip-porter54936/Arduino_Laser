// Code tuned for robot 3
// modified: 10/03/2017, Houman Dallali
// modified: 11/9/17   Phillip Porter
// COMP 469

#include <Servo.h>

#define START_BYTE '$'
#define SEPARATOR  '/'
#define END_BYTE   '!'
#define ANGLE_BYTES 3
#define DISTANCE_BYTES 3
#define LENGTH 8


void setup()
{
  Serial.begin(9600);
}

void loop()
{
  byte buffer[LENGTH];
  char byte_read = '\0';
  boolean found_start = false;
  boolean found_end   = false;
  
  long angle    = 0;
  long distance = 0;
  
  // Find the start
  while(!found_start)
  {
      if (Serial.available() > 0)
      {
         byte_read = Serial.read();
         found_start = (byte_read == START_BYTE); 
      }
  }
  
  // Fill buffer
  while (!found_end)
  {
    int index = 1;
    if (Serial.available() > 0)
    {
      byte_read = Serial.read();
      buffer[index++] = byte_read;
      found_end = (byte_read == END_BYTE);
    } 
  }  
  
  // Get values
  memcpy((byte*)&angle, buffer + 1, ANGLE_BYTES);
  memcpy((byte*)&distance, buffer + 2 + ANGLE_BYTES, DISTANCE_BYTES);
  
  Serial.print("Angle: ");
  Serial.print(angle);
  Serial.print(", Distance: ");
  Serial.println(distance);
  
  for (int i = 0; i < LENGTH; i++)
  {
      
  }
  
  buffer[LENGTH-1] = '\0';
  
  Serial.println((char*)buffer);
  
  /* TODO: what to do with this
  
  // Parse reading
  if (buffer.length() == LENGTH)
  {
    angle    = buffer.substring(0,ANGLE_BYTES).toInt();
    distance = buffer.substring(ANGLE_BYTES+1,LENGTH-1).toInt();
    
    Serial.print("Angle: ");
    Serial.print(angle);
    Serial.print(", Distance: ");
    Serial.println(distance);
  }
  else
  {
    Serial.print("\nERROR: length invalid: ");
    Serial.print(buffer); 
  }
  */
}

