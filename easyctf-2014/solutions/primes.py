import math

def isprime(x):
  x = abs(int(x))
  if x < 2: return False
  if x == 2: return True
  if not x&1: return False
  for n in range(3, int(x**0.5)+1, 2):
    if x%n == 0:
      return False
  return True

cache = {1:2,2:3}

def prime(th):
  if th <= 1: return 2
  if th in cache: return cache[th]

  cur = th-1
  while cur not in cache and cur > 1:
    cur -= 1

  chk = cache[cur]

  while cur != th:
    chk += 2
    if isprime(chk):
       cur += 1
  cache[th] = chk
  return chk

def q(x):
  return sum(prime(prime(i)) for i in range(1,x+1))

print q(5), q(35), q(85)
