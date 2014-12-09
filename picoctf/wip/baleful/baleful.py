import struct, sys

f = open('prog.pico', 'r').read()
lines = f.split('\n')
prog = []
for ln in lines:
    if ln[-1:] == 'h':
        prog += [int(ln[:-1], 16)]
    else:
        prog += [int(ln)]

nop = 0x0
add = 0x2
sub = 0x3
mul = 0x4
div = 0x5
xor = 0x6
neg = 0x7
i_not = 0x8
i_and = 0x9
i_or = 0xA
test = 0xB
shl = 0xC
shr = 0xD
jmp = 0xE
jnz = 0x10
jlz = 0x11
jle = 0x12
jgz = 0x13
jge = 0x14
jz = 0x15
and_no_write = 0x16
minus_no_write = 0x17
mov = 0x18
inc = 0x19
dec = 0x1A
set_from_code_offset = 0x1B
change_code_from_offset = 0x1C
ret = 0x1D
set_from_something_p = 0x1F
call = 0x20

bothptr = 0
op1ptr = 1
op2ptr = 2
noptr = 4

def i4(i):
	return struct.unpack('<I', ''.join([chr(x) for x in prog[i:i+4]]))[0]

mem = []
for i in range(0,31):
	mem += 0

def mems(i):
	return 'mem[' + str(i) + ']'

# binary instructions (eg. a+b)
def flagstr(i, flag):
	if flag == op1ptr:
		return (5, mems(prog[i]), str(i4(i+1)))
	elif flag == op2ptr:
		return (5, str(i4(i)), mems(prog[i+4]))
	elif flag == bothptr:
		return (2, mems(prog[i]), mems(prog[i+1]))
	else:
		return (8, str(i4(i)), str(i4(i+4)))


# main decoder
something_p = 0xF000

i = 0
while i < len(prog):
	ins = prog[i]

	sys.stdout.write('0x%08x: '%i)

	if ins == ret:
		break

	elif ins == nop:
		print 'nop'
		i += 1
		continue

	elif ins == add:
		skip, op1, op2 = flagstr(i+3, prog[i+1])
		print 'mem[%d] = %s + %s'%(prog[i+2],op1,op2)
		i += skip + 3

	elif ins == xor:
		skip, op1, op2 = flagstr(i+3, prog[i+1])
		print 'mem[%d] = %s ^ %s'%(prog[i+2],op1,op2)
		i += skip + 3

	elif ins == jmp:
		print 'jmp 0x%x'%i4(i+1)
		i += 5

	elif ins == jge:
		print 'if (result >= 0) jmp 0x%x'%i4(i+1)
		i += 5

	elif ins == minus_no_write:
		skip, op1, op2 = flagstr(i+2, prog[i+1])
		print 'result = %s - %s'%(op1, op2)
		i += skip + 2

	elif ins == mov:
		if prog[i+1] == 1:
			print 'mem[%d] = 0x%x'%(prog[i+2],i4(i+3))
			i += 7
		else:
			print 'mem[%d] = mem[%d]'%(prog[i+2],prog[i+3])
			i += 4

	elif ins == set_from_code_offset:
		print 'result = mem[%d] = prog[mem[%d]]'%(prog[i+1], prog[i+2])
		i += 3

	elif ins == change_code_from_offset:
		print 'result = prog[mem[%d]] = mem[%d]'%(prog[i+1], prog[i+2])
		i += 3

	else:
		print 'unknown instruction 0x%x'%ins
		i += 1