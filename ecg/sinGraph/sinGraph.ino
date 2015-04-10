
#include <math.h>
int led=13;
double t=0;
void setup() {
pinMode(led,OUTPUT); 
Serial.begin(9600);
}

void loop() {
 double x= sin(t);
 t=t+0.1;
 Serial.println(x);
 delay(10);
} 
