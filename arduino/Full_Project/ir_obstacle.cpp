//#include "WCharacter.h"
#include "Arduino.h"
#include "ir_obstacle.h"
// #define LEFT_IR 48
// #define RIGHT_IR 49
void irObstacleBegin() {
  pinMode(LEFT_IR,INPUT);
  pinMode(RIGHT_IR,INPUT);
}

byte irObstacleRead() {
  byte isLeftIR =  !byte(digitalRead(LEFT_IR));
  byte isRightIR = !byte(digitalRead(RIGHT_IR));
  return isRightIR<<1|isLeftIR;
}
