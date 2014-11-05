import gmpy2, string
from gmpy2 import mpz,divm
from hexconvert import *

N = mpz("0xfd2adfc8f9e88d3f31941e82bef75f6f9afcbba4ba2fc19e71aab2bf5eb3dbbfb1ff3e84b6a4900f472cc9450205d2062fa6e532530938ffb9e144e4f9307d8a2ebd01ae578fd10699475491218709cfa0aa1bfbd7f2ebc5151ce9c7e7256f14915a52d235625342c7d052de0521341e00db5748bcad592b82423c556f1c1051")

def div(x,y):
    return divm(x,y,N)

i1 = mpz(52)
i2 = mpz(37)
a = div(i1,i2)
b = (-(i1*i2) + (i1**2))%N

c1 = mpz("0x1348effb7ff42372122f372020b9b22c8e053e048c72258ba7a2606c82129d1688ae6e0df7d4fb97b1009e7a3215aca9089a4dfd6e81351d81b3f4e1b358504f024892302cd72f51000f1664b2de9578fbb284427b04ef0a38135751864541515eada61b4c72e57382cf901922094b3fe0b5ebbdbac16dc572c392f6c9fbd01e")%N
c2 = mpz("0x81579ec88d73deaf602426946939f0339fed44be1b318305e1ab8d4d77a8e1dd7c67ea9cbac059ef06dd7bb91648314924d65165ec66065f4af96f7b4ce53f8edac10775e0d82660aa98ca62125699f7809dac8cf1fc8d44a09cc44f0d04ee318fb0015e5d7dcd7a23f6a5d3b1dbbdf8aab207245edf079d71c6ef5b3fc04416")%N

num = b*(c1 + (2*(a**3)*c2) - (b**3))
den = a*(c1 - ((a**3)*c2) + (2*(b**3)))

m1 = div(num,den)
m = div(m1 - i2**2,i2)
print hex((m*i2 + i2**2)**3 %N)
x = hex(int(m%N))[2:].rstrip('L')
print hex_to_string(x)

