import random
import time
import socket
import thread

host = ""
port = 10661
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
flag="xxxxxxxx"
def clientthread(conn):
    conn.sendall("%s\n" % "try to guess my secret!");
    random.seed()
    random_secret=random.random()
    print "Just type in: ", random_secret
    data = conn.recv(1024)
    # print data,float(data),type(data),random_secret,type(random_secret)
    try:
        float(data);
    except Exception:
        conn.close();
        return;
    if abs(float(data)-random_secret) < 0.00000001:
        conn.sendall(flag)
    else:
        conn.sendall("Nope!")
    conn.close();

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    # print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is
    #the tuple of arguments to the function.
    thread.start_new_thread(clientthread ,(conn,))
