# thanks to www.imc.org/ietf-openpgp/mail-archive/msg06063.html 

from Crypto.Hash import SHA
import gmpy2, socket

def sha1(str):
    sha = SHA.new()
    sha.update(str)
    return sha.hexdigest()

def verify(cmd, sig):
    s = socket.socket()
    s.connect(('vuln2014.picoctf.com',4919))
    s.sendall(cmd + ' ' + hex(sig)[2:-1] + '\n')
    print 'sent ;)'
    print s.recv(1024)
    s.close()

def iscube(hexstr):
    return gmpy2.iroot_rem(mpz('0x'+hexstr),3)[1]==0

# sig = 2^1019 - (N * 2^34 / 3)  
# N = 2^168 - D
# D = hash

def getsig(n):
   return 2**1019 - (n * 2**34 / 3)

def getcmd(cmd):
    print cmd,hex(getsig(2**168-int(sha1(cmd),16)))[2:-1]

getcmd('ls')
getcmd('cat')
