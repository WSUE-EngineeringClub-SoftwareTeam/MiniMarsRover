//What needs to be done each cycle? 
//Check for input data on the bluetooth
//If we have some, add all of it to our command buffer 
//While something is in the command buffer, parse a single command off the top and parse it
//Simplify commands, possible run each one until a next one? for now use delay
//W = Forward
//A = Left wheel stop
//D = right wheel stop
//S = Reverse
//X = Stop all

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
  
  recentCommand;
  
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
  }
  
}

void respondToData(){
  char newCommand;
  if(BLUETOOTH.available() > 0){
      newCommand = BLUETOOTH.read();
      driveCar(newCommand);
  }
  
 
}
