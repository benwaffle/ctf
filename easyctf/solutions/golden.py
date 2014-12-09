th = 0
a = 0
b = 1

while th != 16:
	c = b
	b += a
	a = c
	if a % 1618 == 0 and str(a).find('1618') != -1:
		th += 1

print(len(str(a))) 
