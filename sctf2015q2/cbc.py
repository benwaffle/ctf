#!/usr/bin/python2
import sys
import string

enc = open('flag.enc').read()

answer = ''
for i in range(len(enc)):
    answer += chr(ord(enc[i]) ^ ord(enc[i-1]))

print answer

