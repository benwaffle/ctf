from string import digits
import hashlib

def md5(txt):
    h = hashlib.md5()
    h.update(txt)
    return h.hexdigest()

salt = '369f9c43642f89a9295e7ee80a340d1f'
target = '37e3292fce3e67d28d02ec97a829557d'

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                code = a+b+c+d
                if md5(salt+code) == target:
                    print code
                    print md5(salt+code+code)
                    quit()
