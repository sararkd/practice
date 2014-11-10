# delete all repetitions of b and ac from string in O(n)

def deleteSubString(ss, sub):
	return ss.replace(sub, '')

s = 'afddsfadfgadfgadfgadfgdfg'
print deleteSubString(s, 'g')



