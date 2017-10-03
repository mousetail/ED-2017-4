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
read_list=[s]
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
	while True:
		readable, writable, errored = select.select(read_list, [], [])
		c = GetChar(False);
		if (c == "#"):
			break;
		for r in readable:
			if r is s:
				client_socket, address = s.accept()
				read_list.append(client_socket)
				print "Connection from", address
			else:
				data = r.recv(1024)
				if data:
					r.send(data)
finally:
	for r in read_list:
		r.close()