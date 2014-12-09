from Crypto.Cipher import Blowfish
import sys, libnum

def pkcs7(s, b):
	need = len(s) / b + 1
	byte = need*b - len(s)
	return s + chr(byte)*byte

key = sys.argv[1]
crypt = raw_input('encrypted data: ')
print 'decrypted:',Blowfish.new(pkcs7(key, 8)).decrypt(crypt)
