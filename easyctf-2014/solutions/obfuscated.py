from itertools import starmap, cycle
import string

i = 5
def mystery(a, b):
    def enc(c,k):
        return chr(((ord(k) + ord(c)) % 26) + ord('A'))
    def dec(c,k):
        return chr(ord(c)-ord('A')+26*i-ord(k))
  
    return ''.join(starmap(dec, zip(a,cycle(b))))

text = "SWQHRGZZUSSWWBJWMRQTMRYVWVXJMADMKICSVBZCZXMENGJLVWEUDUQYVSEMKRWUBFJF"
apple = "FOODISYUMMY"

p1 = mystery(text, apple)
i = 6
p2 = mystery(text, apple)
print ''.join([p1[x] if p1[x] in string.ascii_uppercase else p2[x] for x in range(len(p1))])