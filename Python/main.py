#!python

print "Engeneering design group 4"
print "Version 0.0.9"
print "Python version 2.7"
print "__________________________" #427531

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
	except socket.error as ex:
		print 'Error:', str(ex)
		print ex
		sys.exit(1)
	print ("Socket bound")

	s.listen(1) #maximum one connection
	while True:
		c = GetChar(False);
		if (c == "#"):
			print ("clean shutdown on #")
			break;
		elif (c == "^"):
			print ("current name: ", name)
		readable, writable, errored = select.select(read_list, [], [], 0.1) #timeout of 0.1 seconds
		for r in readable:
			if r is s:
				client_socket, address = s.accept()
				read_list.append(client_socket)
				print "Connection from", address
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
								print "sending",repr(filename),
								f=open("/root/"+filename, "rb")
								content=f.read()
								assert len(content)!=0
								f.close()
								print "(length",len(content),")"
								r.send(str(len(content))+";"+content)
							except IOError:
								r.send("0;")
								traceback.print_exception(*sys.exc_info())
						else:
							print ("filename",filename)
				except socket.error:
					print "disconnected"
					read_list.remove(r)
finally:
	for r in read_list:
		r.close()