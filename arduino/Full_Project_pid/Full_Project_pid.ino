#include <Arduino.h>
#include "car_control.h"
#include "ultrasonic.h"
#include "ir_obstacle.h"

#define FOLLOW_DISTANCE 20
#define AVOID_DISTANCE 20

int8_t power_0, power_1,power_2, power_3, rotate_power = 50, power = 80, remotePower = 0, isReceiverData=false;
bool leftIsClear = false, rightIsClear = false, middleIsClear = false, remoteDriftEnable = false;
int16_t remoteAngle = 0, remoteHeading = 0;
char mode;
String receiverString;

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
    // defult:
    //   carStop();
  }

  
}

void carMoveAround()
{
  float usDistance = ultrasonicRead();

  Serial3.print(leftIsClear); Serial3.print(rightIsClear); Serial3.println(usDistance);

  if (usDistance<=25)
  {
    power_0=usDistance*0.8+20;
    power_1=-power_0;
    power_2=usDistance*1.5+40;
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
  
  Serial3.print(leftIsClear); Serial3.print(rightIsClear); Serial3.println(usDistance);

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

  Serial3.print(leftIsClear); Serial3.print(rightIsClear); Serial3.println(distance);
  
  if (distance > AVOID_DISTANCE) {
    middleIsClear = true;
  } else {
    middleIsClear = false;
  }

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
    if(a!='\n' && a!='\r' && a!=' ')  mode=a;
    Serial.println(mode);
  }
}