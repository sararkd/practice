

# even length n
def printEvenPalindromes(n):
	count = 0
	for secondHalf in range (2**(n/2)):
		firstHalf = 0 
		count += 1
		for i in range(n/2):
			firstHalf = firstHalf | (secondHalf & 2**i) << (n - (2*i + 1))
		fst = '{0:0'+str(n)+'b}'
		print '{0:03d}'.format(count), fst.format(firstHalf | secondHalf)
		
printEvenPalindromes(22)


# (x&1)<<7 | (x&2)<<5 | (x&4)<<3 | (x&8)<1
# OR[i: 0..n/2] [(x&2^i)<< n-(2i+1)]


# 0000 0000 
# 1000 0001
# 0100 0010
# 1100 0011
# 0010 0100
# 1010 0101
# 0110 0110
# 1110 0111
# 0001 1000
# 1001 1001
# . . . . .
# 1111 1111



