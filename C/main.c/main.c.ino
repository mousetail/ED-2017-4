/*
  Arduino Yún USB-to-Serial

  Allows you to use the YunShield/Yún processor as a
  serial terminal for the Linux side on the Yún.

  Upload this to a YunShield/Yún via serial (not WiFi) then open
  the serial monitor at 115200 to see the boot process of Linux.
  You can also use the serial monitor as a basic command line
  interface for Linux using this sketch.

  From the serial monitor the following commands can be issued:

  '~' followed by '0' -> Set the UART speed to 57600 baud
  '~' followed by '1' -> Set the UART speed to 115200 baud
  '~' followed by '2' -> Set the UART speed to 250000 baud
  '~' followed by '3' -> Set the UART speed to 500000 baud
  '~' followed by '~' -> Sends the bridge's shutdown command to
                        obtain the console.

  The circuit:
   YunShield/Yún

  created March 2013
  by Massimo Banzi
  modified by Cristian Maglie

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/YunSerialTerminal

*/

#include "Bridge.h"

long linuxBaud = 250000;

void setup() {
  SERIAL_PORT_USBVIRTUAL.begin(115200);  // open serial connection via USB-Serial
  SERIAL_PORT_HARDWARE.begin(linuxBaud); // open serial connection to Linux

  while (SERIAL_PORT_HARDWARE.read() >= 0);

  SERIAL_PORT_HARDWARE.println("");
  writeToUsb();
  SERIAL_PORT_HARDWARE.println("mount dev/sdb1 /usbstick 2>>error1.txt");
  writeToUsb();
  SERIAL_PORT_HARDWARE.println("cd /usbstick 2>>error2.txt");
  writeToUsb();
  SERIAL_PORT_HARDWARE.println("/bin/ash update.sh 2>> error3.txt");
  writeToUsb();
  SERIAL_PORT_HARDWARE.println("python /usbstick/Python/main.py 2>> error4.txt");

  writeToUsb();
}

void writeToUsb() {
  int c;
  while ((c = SERIAL_PORT_HARDWARE.read()) != -1){
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
  c = SERIAL_PORT_HARDWARE.read();          // read from UART
  if (c != -1) {                            // got anything?
    SERIAL_PORT_USBVIRTUAL.write(c);        //    write to USB-CDC
  }
}
