import socket
s = socket.socket()
s.connect(('python.easyctf.com',10660))
math = s.recv(1024)
s.sendall(str(eval(math[6:])))
print s.recv(1024)
