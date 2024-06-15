#include <Arduino.h>
#include "car_control.h"
#include "ultrasonic.h"
#include "ir_obstacle.h"

#define FOLLOW_DISTANCE 20
#define AVOID_DISTANCE 20

int8_t power_0, power_1,power_2, power_3;
int8_t rotate_power = 50;
int8_t power = 80;
bool leftIsClear = false;
bool rightIsClear = false;
bool middleIsClear = false;
int16_t remoteAngle = 0;
int16_t remoteHeading = 0;
bool remoteDriftEnable = false;
int8_t remotePower = 0;
char mode;
String receiverString;
bool isReceiverData=false;

void setup() {
  Serial.begin(115200);
  Serial3.begin(9600);
  carBegin();
  remoteHeading=90;
  remoteDriftEnable=true;
  remotePower=80;
}

void loop() 
{
  getData();
  switch (mode)
  {
    case '1':
      carMoveAround();
      power=80;
      break;
    case '2':
      carFollowObject();
      break;
    case '3':
      carObstacleAvoid();
      break;
    case '4':
      carStop();
      break;
    case 'w':
      carForward(power);
      break;
    case 's':
      carBackward(power);
      break;
    case 'a':
      carLeft(power);
      break;
    case 'd':
      carRight(power);
      break;
    case 'q':
      carLeftForward(power);
      break;
    case 'e':
      carRightForward(power);
      break;
    case 'z':
      carLeftBackward(power);
      break;
    case 'x':
      carRightBackward(power);
      break;
  }
}

void carMoveAround()
{
  float usDistance = ultrasonicRead();
  Serial.println("usDistance:");Serial.print(usDistance);
  if (usDistance<=25)
  {
    power_0=usDistance;
    power_1=-power_0;
    power_2=usDistance*2;
    power_3=-power_2;
  }
  else
  {
    power_0=power_1=power_2=power_3=0;
  }
  carSetMotors(power_0, power_1, power_2, power_3);
  // delay(20);
}

void carFollowObject()
{
  byte result = irObstacleRead();
  leftIsClear = result & 0b00000001;
  rightIsClear = result & 0b00000010;

  float usDistance = ultrasonicRead();
  Serial.print("usDistance:");Serial.print(usDistance);
  Serial.print(" leftIsClear:");Serial.print(leftIsClear);
  Serial.print(" rightIsClear:");Serial.println(rightIsClear);

  if (usDistance < 4) {
    carStop();
  } else if (usDistance < 10) {
    carForward(30);
  }
  else if (usDistance < FOLLOW_DISTANCE) {
    carForward(power);
  } else {
    if (!leftIsClear) {
      carTurnLeft(rotate_power);
    } else if (!rightIsClear) {
      carTurnRight(rotate_power);
    } else {
      carStop();
    }
  }
  // delay(20);
}

void carObstacleAvoid()
{
  byte result = irObstacleRead();
  leftIsClear = !(result & 0b00000001);
  rightIsClear = !(result & 0b00000010);

  float distance = ultrasonicRead();
  Serial.print("distance: ");Serial.print(distance);
  if (distance > AVOID_DISTANCE) {
    middleIsClear = true;
  } else {
    middleIsClear = false;
  }

  Serial.print("  obstacle: [ ");Serial.print(leftIsClear? "_" : "X");
  Serial.print(" ");Serial.print(middleIsClear? "_" : "X");
  Serial.print(" ");Serial.print(rightIsClear? "_" : "X");
  Serial.println("]");

  if (middleIsClear && leftIsClear && rightIsClear) {
    carForward(power);
  } else {
    if (leftIsClear) {
      carTurnLeft(rotate_power);
    } else if (rightIsClear) {
      carTurnRight(rotate_power);
    } else {
      carMove(0, 0, 20);
      // delay(20);
      carStop();
    }
  }
  // delay(20);
}

void getData()
{
  if(Serial3.available()>0)
  {
    char a=Serial3.read();
    if(a!='\n' && a!='\r')  mode=a;
    Serial.println(mode);
  }
}