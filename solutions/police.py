#!/usr/bin/python2

import socket
import struct
from os import urandom
import random
import json
import hexconvert

def btos(b): return hexconvert.bytes_to_string(b)
def stob(b): return hexconvert.string_to_bytes(b)

def xor(buf, key):
    """ Repeated key xor """
    encrypted = []
    for i, cr in enumerate(buf):
        k = key[i % len(key)]
        encrypted += [ord(cr) ^ ord(k)]
    return btos(encrypted)

def secure_pad(buf):
    """ Ensure message is padded to block size. """
    key = urandom(5)
    buf = btos([0x13, 0x33, 0x7B, 0xEE, 0xF0]) + buf
    buf = buf + urandom(16 - len(buf) % 16)
    enc = xor(buf, key)
    return enc

def remove_pad(buf):
    """ Removes the secure padding from the msg. """
    if len(buf) > 0 and len(buf) % 16 == 0:
        encrypted_key = buf[:5]
        key = xor(encrypted_key, btos([0x13, 0x33, 0x7B, 0xEE, 0xF0]))
        dec = xor(buf, key)
        return dec[5:]

cookie=0

def getpacked(sock):
    global cookie
    raw = sock.recv(1024)
    data = remove_pad(raw)
    magic, gotcookie, sz = struct.unpack('!B2L',data[:9])
    if magic != 0xFF:
        return raw
    cookie = gotcookie
    return struct.unpack('!'+str(sz)+'s',data[9:9+sz])[0]

def getpolice(sock, entry):
    sock.sendall(secure_pad(struct.pack('!B2LHL',0xFF,cookie,0,1,entry)))
    return getpacked(sock)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('vuln2014.picoctf.com', 21212))
print 'connected'
sock.sendall("\x00\x00\x00\xAA")
print getpacked(sock)

badges = []
for i in range(0,1000):
    p = json.loads(getpolice(sock,i))
    if p['BADGE'] in badges:
        print p
        break
    else:
        badges += [p['BADGE']]
    
