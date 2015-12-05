import socket, re

r = re.compile('You need to send a string that encrypts to \'(\w+)\'', re.MULTILINE)

def calc(src, dst, target):
    a = ''.join(src[dst.index(x)] for x in target)
    print 'calc(%s,%s,%s) = %s' % (src,dst,target,a)
    return a

def read(s):
    buf = ''
    while True:
        c = s.recv(1)
        if c == '\n' or c == '':
            break
        else:
            buf += c
    return buf

def send(s, msg):
    s.sendall(msg + '\n')

def main():
    s = socket.socket()
    s.connect(('randBox-iw8w3ae3.9447.plumbing', 9447))
    read(s)
    while True:
        prob = read(s)
        read(s)
        print '[',prob,']'
        m = r.match(prob)
        target = m.group(1)
        print 'target = ', target
        src = 'abcdef0123456789'
        send(s, src)
        dst = read(s)
        read(s)
        print dst
        send(s, calc(src, dst, target))
        print read(s)
        print read(s)

if __name__ == '__main__':
    main()
