# write function that returns x, y, or z, each with probability exactly 1/3 using function that returns a and b with probability of exactly 1/2

import random

def half():
	random.seed()
	return random.choice(['a', 'b'])

def third():
	i = half()
	j = half()
	ij = i + j

	if ij == 'aa':
		return 'x'
	elif ij == 'ab':
		return 'y'	
	elif ij == 'ba':
		return 'z'
	else: 
		print '!!'
		return third()

def fifth():
	s = half() + half() + half() + half() + half()

	if s <= 'aaba':
		return 'a'
	elif s <= 'abab':
		return 'b'	
	elif s <= 'baaa':
		return 'c'
	elif s <= 'babb':
		return 'd'
	elif s <= 'bbba':
		return 'e'
	else: 
		print '*'
		return fifth()

# aaaa
# aaab
# aaba
# *
# aabb
# abaa
# abab
# *
# abba
# abbb
# baaa
# *
# baab
# baba
# babb
# *
# bbaa
# bbab
# bbba
# *
# bbbb


for x in range(10):
	print fifth()