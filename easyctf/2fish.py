from twofish import Twofish
import sys

T = Twofish(sys.argv[1])
crypt = raw_input('encrypted data: ')

print 'decrypted:'
i = 0
while (i < len(crypt)):
	sys.stdout.write(T.decrypt(crypt[i:i+16]))
	i+=16
