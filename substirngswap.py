

def swapped(s, start, end):
	pre = s[:start]
	swap = s[start:end]
	post = s[end:]
	print pre, swap, post
	return pre + swap[::-1] + post


def subsetSwap(s):
	n = len(s)
	smallest = (s, 0, 0)
	for i in range(n-1):
		for j in range(i+2, n+1):
			sw = swapped(s, i, j)
			print 'sw:', sw
			if sw < smallest[0]:
				smallest = (sw, i, j-1)

	return smallest


print subsetSwap('babaabba')

