
int temperaturePin = 0; //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree centigrade 
                        //(500 mV offset) to make negative temperatures an option
void setup()
{
  Serial.begin(9600);  //Start the serial connection with the copmuter
                       //to view the result open the serial monitor 
                       //last button beneath the file bar (looks like a box with an antenae)
}
 
void loop()                     // run over and over again
{
 float temperature = getVoltage(temperaturePin);  //getting the voltage reading from the tem
                    //perature sensor
 temperature = temperature*100;          //converting from 10 mv per degree wit 500
                    // mV offset
                                                  //to degrees ((volatge - 500mV) times 100)
 Serial.println(temperature);                     //printing the result
 delay(100);                                     //waiting a second
}

float getVoltage(int pin){
 return (analogRead(pin) * .004882814); //converting from a 0 to 1023 digital range
                                        // to 0 to 5 volts (each 1 reading equals ~ 5 milliv
                    //olts
}

