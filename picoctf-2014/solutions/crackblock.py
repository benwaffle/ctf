import sys, string, pickle

SBoxes = [[15, 1, 7, 0, 9, 6, 2, 14, 11, 8, 5, 3, 12, 13, 4, 10], [3, 7, 8, 9, 11, 0, 15, 13, 4, 1, 10, 2, 14, 6, 12, 5], [4, 12, 9, 8, 5, 13, 11, 7, 6, 3, 10, 14, 15, 1, 2, 0], [2, 4, 10, 5, 7, 13, 1, 15, 0, 11, 3, 12, 14, 9, 8, 6], [3, 8, 0, 2, 13, 14, 5, 11, 9, 1, 7, 12, 4, 6, 10, 15], [14, 12, 7, 0, 11, 4, 13, 15, 10, 3, 8, 9, 2, 6, 1, 5]]

SInvBoxes = [[3, 1, 6, 11, 14, 10, 5, 2, 9, 4, 15, 8, 12, 13, 7, 0], [5, 9, 11, 0, 8, 15, 13, 1, 2, 3, 10, 4, 14, 7, 12, 6], [15, 13, 14, 9, 0, 4, 8, 7, 3, 2, 10, 6, 1, 5, 11, 12], [8, 6, 0, 10, 1, 3, 15, 4, 14, 13, 2, 9, 11, 5, 12, 7], [2, 9, 3, 0, 12, 6, 13, 10, 1, 8, 14, 7, 11, 4, 5, 15], [3, 14, 12, 9, 5, 15, 13, 2, 10, 11, 8, 4, 1, 6, 0, 7]]

def S(block, SBoxes):
    output = 0
    for i in xrange(0, len(SBoxes)):
        output |= SBoxes[i][(block >> 4*i) & 0b1111] << 4*i
    return output

PBox = [13, 3, 15, 23, 6, 5, 22, 21, 19, 1, 18, 17, 20, 10, 7, 8, 12, 2, 16, 9, 14, 0, 11, 4]
PInvBox = [21, 9, 17, 1, 23, 5, 4, 14, 15, 19, 13, 22, 16, 0, 20, 2, 18, 11, 10, 8, 12, 7, 6, 3]
def permute(block, pbox):
    output = 0
    for i in xrange(24):
        bit = (block >> pbox[i]) & 1
        output |= (bit << i)
    return output

def encrypt_data(data, key):
    enc = ""
    for i in xrange(0, len(data), 3):
        block = int(data[i:i+3].encode('hex'), 16)
        for j in xrange(0, 3):
            block ^= key
            block = S(block, SBoxes)
            block = permute(block, PBox)
        block ^= key
        enc += ("%06x" % block).decode('hex')
    return enc

def decrypt_data(data, key):
    dec = ""
    for i in xrange(0, len(data), 3):
        block = int(data[i:i+3].encode('hex'), 16)
        block ^= key
        for j in xrange(0, 3):
            block = permute(block, PInvBox)
            block = S(block, SInvBoxes)
            block ^= key
        dec += ("%06x" % block).decode('hex')

    return dec

def encrypt(data, key1, key2):
    encrypted = encrypt_data(data, key1)
    encrypted = encrypt_data(encrypted, key2)
    return encrypted

def decrypt(data, key1, key2):
    decrypted = decrypt_data(data, key2)
    decrypted = decrypt_data(decrypted, key1)
    return decrypted

encrypted = open("encrypted", "r")
data = ""
while True:
    read = encrypted.read(1024)
    if len(read) == 0:
        break
    data += read
encrypted.close()

crypts = {}
for key1 in xrange(0,0xffffff+1):
    if key1%1000000 == 0:
        print "gen",key1
    crypts[encrypt_data("messag", key1)] = key1

for key2 in xrange(0,0xffffff+1):
    if key2%1000000 == 0: print "search",key2
    cdt = decrypt_data(data[:6],key2)
    if cdt in crypts:
        dx = crypts[cdt]
        print "key1",dx,"key2",key2
        print "decrypted:",decrypt(data,dx,key2)
