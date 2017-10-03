import socket
try:
	ip = raw_input()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.connect((ip, 1024))
	#serversocket.send('hello')
	
	f = open("f.jpg")
	while True:
		f.write(serversocket.read())
finally:
	f.close()
	raw_input()