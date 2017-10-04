#!python

print "Engeneering design group 4"
print "Version 0.0.7"
print "Python version 2.7"
print "__________________________"

def GetChar(Block=True): #only works on linux
  if Block or select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
    return sys.stdin.read(1)
  return ''

import socket
import sys
import traceback
import select
HOST = ''
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
read_list=[s]
name=""
try:
	print ("Socket opened")

	#bind socket to post
	try:
		msg = s.bind((HOST, PORT))
	except:
		print 'Error:', str(msg[0])
		print msg[1]
	print ("Socket bound")

	s.listen(1) #maximum one connection
	while True:
		c = GetChar(False);
		if (c == "#"):
			print ("clean shutdown on #")
			break;
		readable, writable, errored = select.select(read_list, [], [], 0.1) #timeout of 0.1 seconds
		for r in readable:
			if r is s:
				client_socket, address = s.accept()
				read_list.append(client_socket)
				print "Connection from", address
				client_socket.send(str(len(content)))
				client_socket.send(";")
				client_socket.send(content)
			else:
				try:
					data = r.recv(1024)
					name+=data
					if (";" in name):
						pos=name.index(";")
						filename = name[:pos]
						name=name[pos+1:]
						
						if "/" not in filename and ".." not in filename:
							try:
								print "sending",repr(filename)
								f=open("~/"+filename, "rb")
								r.send(str(len(f))+";"+f.read())
								f.close()
							except IOError:
								r.send("0;")
								traceback.print_exception(*sys.exc_info())
				except socket.error:
					print "disconnected"
					read_list.remove(r)
finally:
	for r in read_list:
		r.close()