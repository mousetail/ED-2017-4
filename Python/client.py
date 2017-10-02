import socket
try:
	ip = raw_input()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.connect((ip, 1024))
	clientsocket.send('hello')
finally:
	raw_input()