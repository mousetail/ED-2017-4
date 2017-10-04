#include "Bridge.h"

long linuxBaud = 250000;

void setup() {
  SERIAL_PORT_USBVIRTUAL.begin(115200);  // open serial connection via USB-Serial
  SERIAL_PORT_HARDWARE.begin(linuxBaud); // open serial connection to Linux

  delay(1000);
  writeToUsb(true); //1
  SERIAL_PORT_HARDWARE.println("##?"); //shut down any existing python instance
  delay(100);
  writeToUsb(true); //2
  SERIAL_PORT_HARDWARE.println("ls --color=never");
  delay(200);
  writeToUsb(true); //5
  SERIAL_PORT_HARDWARE.println("cd /usbstick 2>>error2.txt");
  delay(250);
  writeToUsb(true);//6
  SERIAL_PORT_HARDWARE.println("/bin/ash update.sh 2>> error3.txt");
  delay(250);
  writeToUsb(true);//7
  SERIAL_PORT_HARDWARE.println("ifconfig");
  delay(250);
  writeToUsb(true);//8
  SERIAL_PORT_HARDWARE.println("python /usbstick/Python/main.py 2>> error4.txt");

  writeToUsb(true);//9
}

int getChar(){
  int c = SERIAL_PORT_HARDWARE.read();
  while (c >= 128 || (13 < c && c < 32)){
    c = SERIAL_PORT_HARDWARE.read(); 
  }
  return c;
}

void writeToUsb(bool firstChar) {
  static int linenumber = 0;
  linenumber+=1;
  
  int c;
  if (firstChar){
    SERIAL_PORT_USBVIRTUAL.print("[");
    SERIAL_PORT_USBVIRTUAL.print(linenumber);
    SERIAL_PORT_USBVIRTUAL.print("]");
    c = getChar();
    if (c!=-1){
      SERIAL_PORT_USBVIRTUAL.print("[");
      SERIAL_PORT_USBVIRTUAL.write(c);
      SERIAL_PORT_USBVIRTUAL.print("]");
    }
  }
  while ((c = getChar()) != -1){
    SERIAL_PORT_USBVIRTUAL.write(c);
  }
}


void loop() {
  // copy from USB-CDC to UART
  int c = SERIAL_PORT_USBVIRTUAL.read();    // read from USB-CDC
  if (c != -1) {                            // got anything?
    SERIAL_PORT_HARDWARE.write(c);      //    otherwise write char to UART
  }

  // copy from UART to USB-CDC
  c = getChar();          // read from UART
  if (c != -1) {                            // got anything?
    SERIAL_PORT_USBVIRTUAL.write(c);        //    write to USB-CDC
  }
}
