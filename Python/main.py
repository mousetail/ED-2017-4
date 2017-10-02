#!python

import socket
import sys
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
		conn, addr = s.accept()
		print 'Connected with ' + addr[0] + ':' + str(addr[1])
finally:
	s.close()