import socket
import traceback
import sys

def downloadFile(socket, name):
	length=""
	lengthGot=False
	print ("opening file...")
	socket.send(name+";")
	f = open(name, "w")
	try:
		bytes = 0
		while True:
			t=socket.recv(1)
			if lengthGot:
				bytes+=len(t)
				if (bytes%1000==0):
					print bytes, "bytes read"
			
				f.write(t)
				if bytes >= length:
					break
			else:
				if t==';':
					length = int(length)
					print "length:", length
					lengthGot = True
					bytes = 0
					if (length == 0):
						break
				else:
					length += t
					print(length)
	finally:
		f.close()

try:
	ip = raw_input()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.connect((ip, 1024))
	#serversocket.send('hello')
	
	downloadFile(serversocket, "test.png")
	downloadFile(serversocket, "test.jpg")
	downloadFile(serversocket, "test.raw")
	
except:
	traceback.print_exception(*sys.exc_info())
	raw_input()
	
