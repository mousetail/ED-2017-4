import socket
import traceback
import sys
try:
	ip = raw_input()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.connect((ip, 1024))
	
	length=""
	lengthGot=False
	#serversocket.send('hello')
	print ("opening file...")
	f = open("f.jpg", "w")
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
except:
	traceback.print_exception(*sys.exc_info())
	raw_input()
finally:
	
	f.close()