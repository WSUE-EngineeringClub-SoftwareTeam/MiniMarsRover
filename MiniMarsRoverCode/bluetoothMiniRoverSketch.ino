
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

//MOTOR WRITE DOCUMENTATION//
//192     -> STOPS THE RIGHT SIDE
//160-192 -> Range for driving right motor forward
//192-224 -> Range for driving right motor backward
//64      -> STOPS THE LEFT SIDE
//32-64   -> Range for driving left motor forward
//64-96   -> Range for driving left motor backward
void driveCar(char recentCommand){
  
  switch(recentCommand){
    case 'x': 
        MOTOR.write(0);
        break;
    case 's':
        MOTOR.write(80);
        MOTOR.write(206);
        break;
    case 'w':
       MOTOR.write(42);
       MOTOR.write(170);
       break;
	case 'W':
       MOTOR.write(54);
       MOTOR.write(182);
       break;
    case 'a':
        MOTOR.write(64);
        MOTOR.write(208);
        break;
    case 'd':
        MOTOR.write(80);
        MOTOR.write(192);
        break;
    case 'e': 
        MOTOR.write(50);
        MOTOR.write(192); 
        break;
    case 'q':
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