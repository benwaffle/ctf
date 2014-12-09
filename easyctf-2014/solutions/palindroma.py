findin = args[0]

def pal(s):
  if len(s) == 0:
    return False
  s = ''.join([x for x in s if x not in '!?., ']).lower()
  return s[::-1]==s

longest = ''
for start in range(0,len(findin)):
	for end in range(0,len(findin)):
		cdt = findin[start:end]
		if pal(cdt) and len(cdt) > len(longest):
			longest = cdt
print longest[2:]