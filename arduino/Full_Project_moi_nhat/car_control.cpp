#include "car_control.h"

#include <Arduino.h>
#include <SoftPWM.h>

#define MOTOR_POWER_MIN 28  // 28/255

/* 
  Set the pid parameters
*/
#define KP (float)0.8 
#define KI (float)0.0
#define KD (float)20.0
#define ENCODER_PIN_1 21
#define ENCODER_PIN_2 20
#define ENCODER_PIN_3 19
#define ENCODER_PIN_4 18
// motor1
#define Kp1 1
#define Kd1 0.0002
#define Ki1 0.04
// motor2
#define Kp2 1
#define Kd2 0.0002
#define Ki2 0.04
// motor3
#define Kp3 1
#define Kd3 0.0002
#define Ki3 0.04
// motor4
#define Kp4 1
#define Kd4 0.0002
#define Ki4 0.04

#define T 0.1

int32_t _lastError = 0, errorIntegral = 0, vel=101;
int16_t originHeading;
float pulse1, pulse2, pulse3, pulse4;

float velocity_1, velocity_2, velocity_3, velocity_4;
float set_velocity_1, set_velocity_2, set_velocity_3, set_velocity_4;

float pulse_ref_1, pulse_ref_2, pulse_ref_3, pulse_ref_4;

double E_1, E1_1, E2_1, out_1, E_2, E1_2, E2_2, out_2, E_3, E1_3, E2_3, out_3, E_4, E1_4, E2_4, out_4;
double alpha_1, beta_1, gamma_1, alpha_2, beta_2, gamma_2, alpha_3, beta_3, gamma_3, alpha_4, beta_4, gamma_4;
double output_1, last_output_1, output_2, last_output_2, output_3, last_output_3, output_4, last_output_4;

unsigned long timeNow, timeLast;

/** 
* @brief Initialize the motor, and (block) the initialization compass
*/

void carBegin() {
  SoftPWMBegin();
  for (uint8_t i = 0; i < 8; i++) {
    SoftPWMSet(MOTOR_PINS[i], 0);
    SoftPWMSetFadeTime(MOTOR_PINS[i], 100, 100);
  }

  compassBegin();
  for (uint8_t i = 0; i < AVERAGE_FILTER_SIZE; i++) {
    carResetHeading();
  }

  for(int i=18;i<22;i++)  pinMode(i,INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(ENCODER_PIN_1), pulseEncoder1, RISING);
  attachInterrupt(digitalPinToInterrupt(ENCODER_PIN_2), pulseEncoder2, RISING);
  attachInterrupt(digitalPinToInterrupt(ENCODER_PIN_3), pulseEncoder3, RISING);
  attachInterrupt(digitalPinToInterrupt(ENCODER_PIN_4), pulseEncoder4, RISING);
}

/** 
 * @name simple move functions with CAR_DEFAULT_POWER
 */
void carForward(int8_t power)       { carMove(   0, power, 0); }
void carBackward(int8_t power)      { carMove( 180, power, 0); }
void carLeft(int8_t power)          { carMove( -90, power, 0); }
void carRight(int8_t power)         { carMove(  90, power, 0); }
void carTurnLeft(int8_t power)      { carMove(   0, 0, power); }
void carTurnRight(int8_t power)     { carMove(   0, 0, -power); }
void carLeftForward(int8_t power)   { carMove( -45, power, 0); }
void carRightForward(int8_t power)  { carMove(  45, power, 0); }
void carLeftBackward(int8_t power)  { carMove(-135, power, 0); }
void carRightBackward(int8_t power) { carMove( 135, power, 0); }
void carStop()          { carMove(   0, 0, 0); }

/** 
 * @brief Set speed for 4 motors
 *
 * @param power0  0 ~ 100
 * @param power1  0 ~ 100
 * @param power2  0 ~ 100
 * @param power3 0 ~ 100
 */

void carSetMotors(int8_t power0, int8_t power1, int8_t power2, int8_t power3) {

  bool dir[4];
  int8_t newPower[4];
  // power0=power1=power2=power3=9;
  set_velocity_1=abs(power0);
  set_velocity_2=abs(power1);
  set_velocity_3=abs(power2);
  set_velocity_4=abs(power3);

  timeNow=millis();

  if(timeNow-timeLast>1000*T)
  {
    PID();

    timeLast=millis();
  }

  if(power0>vel) power0=output_1;
  if(power1>vel) power1=output_2;
  if(power2>vel) power2=output_3;
  if(power3>vel) power3=output_4;

  int8_t power[4] = {power0, power1, power2, power3};

  for (uint8_t i = 0; i < 4; i++) {
    dir[i] = power[i] > 0;

    if (MOTOR_DIRECTIONS[i]) dir[i] = !dir[i];

    if (power[i] == 0) {
      newPower[i] = 0;
    } else {
      newPower[i] = map(abs(power[i]), 0, 100, MOTOR_POWER_MIN, 255);
    }
    SoftPWMSet(MOTOR_PINS[i*2], dir[i] * newPower[i]);
    SoftPWMSet(MOTOR_PINS[i*2+1], !dir[i] * newPower[i]);
  }
}

/** 
  * Control the car to move
  *  
  * @code {.cpp}
  * carMove(-90, 80, 0);
  * @endcode
  * 
  * @param angle the direction you want the car to move 
  * @param power moving speed  
  * @param rot the car fixed rotation angle during the movement
  * @param drift Whether it is a drift mode, default flase 
  *              true, drift mode, the car body will return to square
  *              flase, drift mode, the car body will not return to square
  */
void carMove(int16_t angle, int8_t power, int8_t rot, bool drift) {
  int8_t power_0, power_1, power_2, power_3;
  float speed;
  // Make forward 0
  angle += 90;
  // Offset angle as 0 to the front
  float rad = angle * PI / 180;

  if (rot == 0) speed = 1;
  else speed = 0.5;

  power /= sqrt(2);
  // Calculate 4 wheel
  if (drift) {
    power_0 = (power * sin(rad) - power * cos(rad)) * speed + rot * speed * 0.1;
    power_1 = (power * sin(rad) + power * cos(rad)) * speed - rot * speed * 0.1;
    power_2 = (power * sin(rad) - power * cos(rad)) * speed + rot * speed * 2.25;
    power_3 = (power * sin(rad) + power * cos(rad)) * speed - rot * speed * 2.25;
  } else {
    power_0 = (power * sin(rad) - power * cos(rad)) * speed - rot * speed;
    power_1 = (power * sin(rad) + power * cos(rad)) * speed + rot * speed;
    power_2 = (power * sin(rad) - power * cos(rad)) * speed + rot * speed;
    power_3 = (power * sin(rad) + power * cos(rad)) * speed - rot * speed;
  }


  carSetMotors(power_0, power_1, power_2, power_3);
}


/** 
  * Use the field center method to control the movement of the car
  *
  * @param angle the direction you want the car to move 
  * @param power moving speed  
  * @param heading the car head pointing
  * @param drift Whether it is a drift mode, default flase 
  *              true, drift mode, the car body will return to square
  *              flase, drift mode, the car body will not return to square
  */
void carMoveFieldCentric(int16_t angle, int8_t power, int16_t heading, bool drift) {
  int16_t currentHeading = 0;
  int32_t error = 0;
  int32_t offset = 0;
  int8_t rot = 0;

  currentHeading = compassReadAngle();

  error = currentHeading - originHeading - heading;

  // convert -360 to 360 to -180 to 180
  while (error > 180) {
    error -= 360;
  }
  while (error < -180) {
    error += 360;
  }

  if (error > 1 || error < -1) {
    offset += KP * error + KI * errorIntegral + KD * (error - _lastError);
    rot += max(-100, min(100, offset));
    errorIntegral += error;
    _lastError = error;
  }

  angle = angle - currentHeading + originHeading;
  carMove(angle, power, rot, drift);

}

/** 
  * Reset origin head pointing
  */
void carResetHeading() 
{
  originHeading = compassReadAngle();
}

void pulseEncoder1()
{
  pulse1++;
}

void pulseEncoder2()
{
  pulse2++;
}

void pulseEncoder3()
{
  pulse3++;
}

void pulseEncoder4()
{
  pulse4++;
}

void PID()
{
  velocity_1=(pulse1/300.0)*1/T*60.0; //vong/phut
  velocity_2=(pulse2/300.0)*1/T*60.0;
  velocity_3=(pulse3/300.0)*1/T*60.0;
  velocity_4=(pulse4/300.0)*1/T*60.0;

  pulse_ref_1=pulse1;
  pulse_ref_2=pulse2;
  pulse_ref_3=pulse3;
  pulse_ref_4=pulse4;

  // Serial.print(pulse1); Serial.print("-"); Serial.print(pulse2); Serial.print("-"); 
  // Serial.print(pulse3); Serial.print("-"); Serial.println(pulse4); 

  // Serial.print(velocity_1); Serial.print("-"); Serial.print(velocity_2); Serial.print("-"); 
  // Serial.print(velocity_3); Serial.print("-"); Serial.println(velocity_4);  

  Serial.print(output_1); Serial.print("-"); Serial.print(output_2); Serial.print("-"); 
  Serial.print(output_3); Serial.print("-"); Serial.println(output_4); 

  pulse1=pulse2=pulse3=pulse4=0;

  E_1=set_velocity_1-velocity_1;
  E_2=set_velocity_2-velocity_2;
  E_3=set_velocity_3-velocity_3;
  E_4=set_velocity_4-velocity_4;

  alpha_1=2*T*Kp1 + Ki1*T*T + 2*Kd1;
  alpha_2=2*T*Kp2 + Ki2*T*T + 2*Kd2;
  alpha_3=2*T*Kp3 + Ki3*T*T + 2*Kd3;
  alpha_4=2*T*Kp4 + Ki4*T*T + 2*Kd4;

  beta_1 = T*T*Ki1 - 4*Kd1 - 2*T*Kp1;
  beta_2 = T*T*Ki2 - 4*Kd2 - 2*T*Kp2;
  beta_3 = T*T*Ki3 - 4*Kd3 - 2*T*Kp3;
  beta_4 = T*T*Ki4 - 4*Kd4 - 2*T*Kp4;

  gamma_1=2*Kd1;
  gamma_2=2*Kd2;
  gamma_3=2*Kd3;
  gamma_4=2*Kd4;

  output_1 = (alpha_1*E_1 + beta_1*E1_1 + gamma_1*E2_1 + 2*T*last_output_1)/(2*T);
  output_2 = (alpha_2*E_2 + beta_2*E1_2 + gamma_2*E2_2 + 2*T*last_output_2)/(2*T);
  output_3 = (alpha_3*E_3 + beta_3*E1_3 + gamma_3*E2_3 + 2*T*last_output_3)/(2*T);
  output_4 = (alpha_4*E_4 + beta_4*E1_4 + gamma_4*E2_4 + 2*T*last_output_4)/(2*T);

  if(output_1<0) output_1=0;
  else if(output_1>80) output_1=80;
  if(output_2<0) output_2=0;
  else if(output_2>80) output_2=80;
  if(output_3<0) output_3=0;
  else if(output_3>80) output_3=80;
  if(output_4<0) output_4=0;
  else if(output_4>80) output_4=80;

  last_output_1=output_1;
  last_output_2=output_2;
  last_output_3=output_3;
  last_output_4=output_4;

  E1_1=E_1;
  E1_2=E_2;
  E1_3=E_3;
  E1_4=E_4;

  E2_1=E1_1;
  E2_2=E1_2;
  E2_3=E1_3;
  E2_4=E1_4;

}