from Crypto.Cipher import Blowfish
import sys, libnum

def pkcs7(s, b):
	if len(s) % b == 0:
		return s
	need = len(s) / b + 1
	byte = need*b - len(s)
	return s + chr(byte)*byte

key = 'tetraodontidae'

print Blowfish.new(pkcs7(key, 8)).decrypt(libnum.n2s(0x1e95153b6c941098227a4b08d9d74cb9d7b9387f83c74097))
