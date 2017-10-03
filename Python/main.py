#!python

print "Engeneering design group 4"
print "Version 0.0.5"
print "Python version 2.7"
print "__________________________"

def GetChar(Block=True): #only works on linux
  if Block or select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
    return sys.stdin.read(1)
  return ''

import socket
import sys
import select
HOST = ''
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	print ("Socket opened")

	#bind socket to post
	try:
		s.bind((HOST, PORT))
	except:
		print 'Error:', str(msg[0])
		print msg[1]

	print ("Socket bound")

	s.listen(1) #maximum one connection

	while 1:
		char = GetChar(False):
		print repr(char);
		if (char == "#"):
			break
		conn, addr = s.accept()
		print 'Connected with ' + addr[0] + ':' + str(addr[1])
finally:
	s.close()