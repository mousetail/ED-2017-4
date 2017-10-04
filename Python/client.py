import socket
import traceback
import sys

def downloadFile(socket, name):
	length=""
	lengthGot=False
	print ("opening file...")
	socket.send(name+";")
	f = open(name, "w")
	bytes = 0
	while True:
		t=serversocket.recv(1)
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
			else:
				length += t

try:
	ip = raw_input()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.connect((ip, 1024))
	#serversocket.send('hello')
	
	downloadFile("test.png")
	downloadFile("test.jpg")
	downloadFile("test.raw")
	
except:
	traceback.print_exception(*sys.exc_info())
	raw_input()
finally:
	
	f.close()
	
