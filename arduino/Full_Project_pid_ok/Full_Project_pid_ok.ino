#include <Arduino.h>
#include "car_control.h"
#include "ultrasonic.h"
#include "ir_obstacle.h"

#define FOLLOW_DISTANCE 20
#define AVOID_DISTANCE 20
#define MAX_POWER 80

int8_t power_0, power_1,power_2, power_3, rotate_power = 35, power = 80, remotePower = 0, isReceiverData=false, divp=5;
bool leftIsClear = false, rightIsClear = false, middleIsClear = false, remoteDriftEnable = false;
int16_t remoteAngle = 0, remoteHeading = 0;
char mode;
int usDistance;
String receiverString;

void setup() {
  Serial.begin(115200);
  Serial3.begin(9600);
  carBegin();
  irObstacleBegin();
  remoteHeading=90;
  remoteDriftEnable=true;
  remotePower=80;
}

void loop() 
{
  getData();
  readSensor();
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
    case 'n':
      carFollowWall();
      break;
    case '4':
      carStop();
      break;
    case 'w':
      carForward(power);
      break;
    case 'x':
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
    case 'c':
      carRightBackward(power);
      break;
    case '5':
      power=MAX_POWER-divp;
      break;
    case '6':
      power=MAX_POWER-divp*2;
      break;
    case '7':
      power=MAX_POWER-divp*2;
      break;
    case '8':
      power=MAX_POWER-divp*4;
      break;
     case '9':
      power=MAX_POWER-divp*5;
      break;
    case 't':
      power=MAX_POWER-divp*6;
      break;                             
    case 'y':
      power=MAX_POWER-divp*7;
      break;
    case 'u':
      power=MAX_POWER-divp*8;
      break;
     case 'i':
      power=MAX_POWER-divp*9;
      break;
     case 'v':
      carMove(0,0,power);
      break;
     case 'b':
      carMove(0,0,-power); 
      break;    
  }

  
}

void carMoveAround()
{
  usDistance=ultrasonicRead();
  if (usDistance<=25)
  {
    power_0=usDistance*0.8+10;
    power_1=-power_0;
    power_2=usDistance*1.5+40;
    power_3=-power_2;
  }
  else
  {
    power_0=power_1=power_2=power_3=0;
  }
  carSetMotors(power_0, power_1, power_2, power_3);
}

void carFollowObject()
{
  usDistance=ultrasonicRead();
  if (usDistance < 4) carStop();
  else if (usDistance < FOLLOW_DISTANCE)  carForward(power);
  else 
  {
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
  usDistance=ultrasonicRead();
  if (usDistance > AVOID_DISTANCE) {
    middleIsClear = true;
  } else {
    middleIsClear = false;
  }

  if (middleIsClear && !leftIsClear && !rightIsClear) {
    carForward(power);
  } 
  else 
  {
    if (leftIsClear) {
      carTurnLeft(rotate_power);
    } else if (rightIsClear) {
      carTurnRight(rotate_power);
    } else {
      carMove(0, 0, 20);
      // delay(20);
      // carStop();
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

void readSensor()
{
  byte result = irObstacleRead();
  leftIsClear = result & 0b00000001;
  rightIsClear = result & 0b00000010;
  int usDistance = ultrasonicRead();
  if(usDistance>100) usDistance=99;
  Serial3.print(leftIsClear); Serial3.print(rightIsClear); Serial3.println(usDistance);
}

void carFollowWall()
{
  bool frontIR, backwardIR;
  frontIR=digitalRead(50);
  backwardIR=digitalRead(51);
  usDistance=ultrasonicRead();
  if(usDistance<AVOID_DISTANCE)
  {
    carMove(0,0,-power+10);
    delay(1000);
  }
  else if(!frontIR && !backwardIR) carLeftForward(power-10);
  else if(frontIR && !backwardIR) carMove(0,0,-power+10);
  else if(!frontIR && backwardIR) carMove(0,0,power-10);
  else if(frontIR && backwardIR) carRightForward(power-10); 
}
