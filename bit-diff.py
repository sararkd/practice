
# Write a function to determine the number of bits required to convert integer A to integer B
# Input: 31, 14 
# Output: 2


def bitDiff(a, b):
	print '{0:010b}'.format(a)
	print '{0:010b}'.format(b)
	diff = a ^ b
	count = 0
	while not diff == 0:
		if diff & 1: count += 1
		diff = diff >> 1
	return count

print bitDiff(123, 60)
print bitDiff(124, 75)