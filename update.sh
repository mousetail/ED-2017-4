#!/bin/ash
curl -f http://arduino.cc/asciilogo.txt || exit 1
rm -rf ./*
curl -l -k https://codeload.github.com/mousetail/ED-2017-4/zip/master > archive.zip
unzip archive.zip -d .
mv ED-2017-4-master/* .
rm ED-2017-4-master -r 
rm -f archive.zip