
// Mini Mars Rover wireless motor control code
// By Derek Thompson
// March 2019

const byte numChars = 32;
char receivedChars[numChars];
char parsedCmd[5];
int cmdSize = 4;

int testCtr = 10;

boolean newData = false;

// for analog control
//// Motor pins
//const int mtrLeft = 11;
//const int mtrRight = 12;

void setup() {
// for analog control
//    pinMode(mtrLeft, OUTPUT);
//    pinMode(mtrRight, OUTPUT);  
//    analogWrite(mtrLeft, 127);
//    analogWrite(mtrRight, 127);
    Serial.begin(9600); // set the baud rate of the serial terminal to 9600
    Serial1.begin(9600); // set the baud rate of the RNBT-59DF Bluetooth module to 9600
    Serial2.begin(9600); // set the baud rate of the Sabertooth 2x25 motor controller to 9600
    Serial.println("<Arduino is ready>");
}

void loop() {
//  while (Serial.available() && testCtr != 0) {
    recvWithStartEndMarkers();
//    Serial.print("before parse: ");
//    Serial.println(receivedChars);
    parseCommand();
//      Serial.print("After parse: ");
//    Serial.println(receivedChars);
    showNewData();
    driveMotors(parsedCmd);//receivedChars);
//    testCtr--;
//  }
}
 
void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial1.available() > 0 && newData == false) {
        rc = Serial1.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("This just in ... ");
        Serial.println(receivedChars);
        Serial.println(parsedCmd);
        newData = false;
    }
}

// parses the next command off of the input array and stores it in.
// Useful if you want to send a giant string of commands
void parseCommand() {
  int index =0;
  int dropIncompleteCmd = 0;
  char tempArray[numChars-cmdSize];
//  Serial.print("index: ");
//  Serial.println(index);
  for (index; index<cmdSize; index++) {
    parsedCmd[index] = receivedChars[index];
  }
  //parsedCmd[index] = '\0';  // C automatically initializes arrays to 0
//  Serial.print("index: ");
//  Serial.println(index);
//  Serial.print("parsed cmd: ");
//  Serial.println(parsedCmd);
  // the following code truncates the input array to exclude the parsed instruction
  for (int i=0; receivedChars[index] != '\0'; i++) {
    tempArray[i] = receivedChars[index];
    index++;
    dropIncompleteCmd++;
  }
//  Serial.print("index: ");
//  Serial.println(index);
  if (dropIncompleteCmd <= 3){
    for (int i=0; receivedChars[i] != '\0'; i++) {
      receivedChars[i] = '\0';
    }
  }
  else {
    tempArray[index-cmdSize] = receivedChars[index]; // terminate the temp array with null
    for (int i=0; i <= (index-cmdSize); i++ ) {
      receivedChars[i] = tempArray[i];
    }
  }
}


// This function takes the command input from the user and drives the motors accordingly
void driveMotors(char cmdArray[]) {
    int cmd = atoi(cmdArray);
    switch (cmd) {
      case 0100: // Drives left motors forward
        Serial2.write(80); 
        Serial2.write(192);
        delay(1000);
        Serial2.write(0);
        break;
      case 1000: // Drives right motors forward
        Serial2.write(64);
        Serial2.write(208);
        delay(1000);
        Serial2.write(0);
        break;
      case 1100: // Drives all four motors forward
        Serial2.write(80);
        Serial2.write(208);
        delay(1000);
        Serial2.write(0);
        break;
      case 0001: // Drives left motors backward
        // send a value of 1-127 to command motor 1
        Serial2.write(54); // commands motor 1 to half speed
        // send a value of 128-255 to command motor 2
        Serial2.write(180); // command motor 2 to half speed  
        //Serial.println("made it");
        delay(1000);
        Serial2.write(0); // stops both motors  
        break;
      case 0010: // Drives right motors backward
        Serial2.write(64);
        Serial2.write(176);
        delay(1000);
        Serial2.write(0);
        break;
      case 0011: // Drives all four motors backward
        Serial2.write(48);
        Serial2.write(176);
        delay(1000);
        Serial2.write(0);
        break;
      default: // Stops all motors
        Serial2.write(0); // stops both motors
        break;
    } 
}
