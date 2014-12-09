# build z3py, run this with hexconvert.py in same dir
# output is 'solving_equations_is_lot_lot_fun', looks like 'solving_equations_is_lots_of_fun'
# no need to compute more

from z3 import *
from hexconvert import *

s = Solver()
a = BitVec('a', 32)
b = BitVec('b', 32)
c = BitVec('c', 32)
d = BitVec('d', 32)
e = BitVec('e', 32)
f = BitVec('f', 32)
g = BitVec('g', 32)
h = BitVec('h', 32)

s.add(b+c == 0xc0dcdfce)
s.add(a+b == 0xd5d3dddc)
s.add(a*3+b*5 == 0x404A7666)
s.add(d^a == 0x18030607)
s.add(a&d == 0x666C6970)
s.add(e*b == 0xb180902b)
s.add(c*e == 0x3e436b5f)
s.add(e+f*2 == 0x5c483831)
s.add(f&0x70000000 == 0x70000000)
#s.add(f/g == 0x0e000cec)
s.add(f==g) # idk
s.add(e*3+h*2 == 0x3726eb17)
s.add(h*8-h+c*4 == 0x8b0b922d)
#s.add(h*3+0x28 == 0xb9cf9c91)

def mtox(m):
	return hex_to_string(hex(m.as_long()).strip('0x'))[::-1]

if str(s.check()) == "sat":
	print 'solution: '
	m = s.model()
	print mtox(m[a]) + mtox(m[b]) + mtox(m[c]) + mtox(m[d]) + mtox(m[e]) + mtox(m[f]) + mtox(m[g])+mtox(m[h])
else:
	print 'no solution'
