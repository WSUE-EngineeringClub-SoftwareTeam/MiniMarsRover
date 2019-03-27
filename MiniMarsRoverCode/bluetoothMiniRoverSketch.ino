
//What needs to be done each cycle? 
//Check for input data on the bluetooth
//If we have some, call the drivecar method
//Write the to motors the most recent command until we get another

///CONTROLS///
//W = Forward
//A = Backwards Left
//D = Backwards Right
//S = Reverse
//X = Stop all
//Q = Forward Left
//E = Forward Right

#define BLUETOOTH Serial1
#define MOTOR Serial2 
#define TERMINAL Serial

void setup() {
    TERMINAL.begin(9600); // set the baud rate of the serial terminal to 9600
    BLUETOOTH.begin(9600); // set the baud rate of the RNBT-59DF Bluetooth module to 9600
    MOTOR.begin(9600); // set the baud rate of the Sabertooth 2x25 motor controller to 9600
}

void loop() {
    respondToData();
}

void driveCar(char recentCommand){
  
  switch(recentCommand){
    case 'x': 
        MOTOR.write(0);
        break;
    case 's':
        MOTOR.write(80);
        MOTOR.write(200);
        break;
    case 'w':
       MOTOR.write(48);
       MOTOR.write(176);
       break;
    case 'a':
        MOTOR.write(64);
        MOTOR.write(208);
        break;
    case 'd':
        MOTOR.write(80);
        MOTOR.write(192);
        break;
    //DOESNT WORK 
    //NEED TO FIND NEW INPUTS FOR "DRIVE BACK AND LEFT"
	//try using 160 instead of 180 for case q - derek
    case 'q': 
        MOTOR.write(54);
        MOTOR.write(180); 
        break;
    case 'e':
        MOTOR.write(64);
        MOTOR.write(176);
        break;
  }
  
}

void respondToData(){
  char newCommand;
  if(BLUETOOTH.available() > 0){
      newCommand = BLUETOOTH.read();
      driveCar(newCommand);
  } 
}
