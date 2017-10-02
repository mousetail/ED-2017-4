#!/bin/sh
rm -rf .
curl -l -k https://codeload.github.com/mousetail/ED-2017-4/zip/master > archive.zip
unzip archive.zip -d .
mv myprojectname-master .
rm -f archive.zip