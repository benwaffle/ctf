from string import printable

def enc(c):
    c = ord(c)
    x = (c & 0xe0) >> 2
    y = (c & 0x18) << 3
    z = (c & 0x7)
    return chr(x | y | z)

flag = open('flag.enc').read()
dec = ''

while len(flag) > 0:
    for c in printable:
        if enc(c) == flag[0]:
            dec += c
            flag = flag[1:]
            break

print dec
