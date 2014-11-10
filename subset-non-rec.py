
import sys

#returns indices of next k-element subset of n-element set given previous elements in p
#next subset is in lexiographical order and p is ordered and of size k
def nextSubset(n, k, p):
	i = k - 1
	succ = list(p)
	while i >= 0:
		if p[i] < n-k+i:
			succ[i] += 1
			for j  in range(i+1, k):
				succ[j] = succ[j-1] + 1
			return succ
		else: 
			i -= 1
	return None

#print subset given list of indices
def printSubset(s, p):
	subset = []
	for i in p:
		subset.append(s[i])
	print subset


def printSubsets(s):
	count = 0
	n = len(s) 
	for i in range(n+1):
		subset = range(i)
		while not subset == None:
			count += 1
			print count,		
			printSubset(s, subset) 
			subset = nextSubset(n, i, subset)


s = [1, 2, 3, 4, 5]
printSubsets(s)
# print nextSubset(5, 2, [3,4])

# 1 2
# 1 3
# 1 4
# 1 5
# 1 2 3 
# 1 2 4
# 1 2 5
# 1 3 4 
# 1 3 5
# 1 4 5 
# 2 3 4 
# 2 3 5
# 2 4 5
# 3 4 5 
# 0      1     ... i     ...  k-2  k-1
# n-k  n-k+1   ... n-k+i ...  n-2  n-1  
# 5! / (2! * 3!) = 4 * 5 / 2 = 10 