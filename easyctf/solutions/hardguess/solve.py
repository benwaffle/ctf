import socket, time, random

while True:
	s = socket.socket()
	s.connect(('python.easyctf.com',10663))
	random.seed(long((time.time()+.0003)*256))
	s.recv(80)
	s.sendall(repr(random.random()))
	print s.recv(80)

