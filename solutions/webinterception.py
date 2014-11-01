#!/usr/bin/env python
import os, random, time, socket, string, sys

def escp(s):
    for x in s:
        if x not in string.letters and x not in string.digits and x not in string.punctuation and x != ' ' and x != '\n' and x != '\r' and ord(x) != 27:
            sys.stdout.write('\\x'+x.encode('hex'))
        elif x == '\n':
            sys.stdout.write('\\n')
        elif x == '\r':
            sys.stdout.write('\\r')
        elif ord(x) == 27:
            sys.stdout.write('\\e')
        else:
            sys.stdout.write(x)
    sys.stdout.write('\n')

#from Crypto.Cipher.AES import AESCipher

key = 'XXXXXXXXXXXXXXXX' # obviously, this is not the real key.
secret_data = 'This is not the real secret data'

def pkcs7_pad(s):
  l = len(s)
  needed = 16 - (l % 16)
  return s + (chr(needed) * needed)

def pkcs7_unpad(s):
  # this is not actually used, but we wanted to put it in so you could see how to implement it.
  assert len(s) % 16 == 0
  assert len(s) >= 16
  last_char = s[-1]
  count = ord(last_char)
  assert 0 < count <= 16
  assert s[-count:] == last_char * count
  return s[:-count]

def oracle(s):
  # so, this is simulated. In reality we'd have to run javascript on a target web browser
  # and capture the traffic. That's pretty hard to do in a way that scales, though, so we
  # simulate it instead.
  # This uses ECB mode.
  #  return AESCipher(key).encrypt(pkcs7_pad('GET /' + s.decode('hex') + secret_data))
#    escp(s)
    s = 'AAAAAAAAAAA' + s
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('vuln2014.picoctf.com', 65414))
    sock.recv(1024) # prompt
    sock.sendall(s.encode('hex')+'\n')
    return sock.recv(1024).strip('\n').decode('hex')[16:]

bs = len(oracle("")) / 16
prev = 'A' * 16
secret = ''
for block in range(0,bs):
    known = ''
    print "block",block
    for char in range(0,16):
        base = prev[-(16-(char+1)):]
        if char == 15: base = ''
        real = oracle(base)[16*block:16*(block+1)]
        found = False
#        for guess in range(0,256):
        for guess in string.printable:
            cipher = oracle(base + secret + guess)[16*block:16*(block+1)]
            if cipher == real:
                known += guess
                secret += guess
                escp(secret)
                found = True
                break
        assert found
    prev = known
print secret
