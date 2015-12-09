def f(x):
    return g(x) - w(x)

def g(x):
    print 'g(', x, ')'
    if x == 0 or x == 1:
        return x
    return (g(x-1) + g(x-2))**2

wcache = {}
def w(x):
    print 'w(', x, ')'
    if x == 0 or x == 1:
        return x
    if x in wcache: return wcache[x]
    wcache[x] = w(x-1)**2 + w(x-2)**2
    return wcache[x]

#print(sum(map(int, str(f(30)))))
print w(30)

