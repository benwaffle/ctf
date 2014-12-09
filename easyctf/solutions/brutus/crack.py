import hashlib

def md5(s):
	m = hashlib.md5()
	m.update(s)
	return m.hexdigest()

for num in open('numbers.txt'):
	for adj in open('adjectives.txt'):
		for col in open('colors.txt'):
			for ani in open('animals.txt'):
				num = num.rstrip('\r\n')
				adj = adj.rstrip('\r\n')
				col = col.rstrip('\r\n')
				ani = ani.rstrip('\r\n')
				
				if md5(num+adj+col+ani) == 'f54f10fd6e38929084d505d0c2e9c997':
					print (num+adj+col+ani)
					exit(0)
				
