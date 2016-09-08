#!/usr/bin/python3
import base64, random, string, sys

"""
flag = open('flag.txt').read()

for i in range(80):
    if random.random() < 0.5:
        flag = base64.b64encode(flag.encode('utf8')).decode('utf8')
    else:
        alphabet = string.ascii_letters + string.digits
        shift = random.randint(1,len(alphabet))
        alphabet_shift = alphabet[shift:] + alphabet[:shift]
        flag = flag.translate(str.maketrans(alphabet, alphabet_shift))

open('encrypted.txt','w').write(flag)
"""

alphabet = string.ascii_letters + string.digits

def printable(s):
    for c in s:
        if not c in string.printable:
            return False
    return True

import traceback
def is_b64(s):
    try:
        dec = base64.b64decode(s).decode('utf8')
        if printable(dec):
            print('is b64')
            return True #dec.decode('utf8')
        else:
            print('non printable')
            return False
    except TypeError as e:
        traceback.print_exception(e, None, None)
        print(e)
        print('except')
        return False
    except UnicodeDecodeError as e:
        traceback.print_exception(e, None, None)
        print(e)
        print('except')
        return False

def attempt(s):
    if '{' in s:
        print(s)
        sys.exit()

    if is_b64(s):
        attempt(base64.b64decode(s).decode('utf8'))
    else:
        print('base64 bad')

        for shift in range(1, len(alphabet)+1):
            alphabet_shift = alphabet[shift:] + alphabet[:shift]
            s = s.translate(str.maketrans(alphabet_shift, alphabet))
            attempt(s)

enc = open('encrypted.txt').read()
attempt(enc)
