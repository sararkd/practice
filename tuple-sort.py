# There is an array of 3-tuples, in the form of (a, 1, 5). 
# The first element in the tuple is the id, the second and third elements are both integers, 
# and the third is always larger than or equal to the second. 
# Assume that the array is sorted based on the second element of the tuple. 
# Write a function that breaks each of the 3-tuple into two 2-tuples like (a, 1) and (a, 5), and sort them according to the integer. 
# E.g. given (a, 1, 5), (b, 2, 4), (c, 7, 8), output (a, 1), (b, 2), (b, 4), (a, 5), (c, 7), (c, 8).
# - Nobody on September 11, 2014 in United States Report Duplicate | Flag 

import operator

inArr = [('a', 1, 5),
	     ('b', 2, 4),
	     ('c', 7, 8),
	     ('d', 7, 9),
	     ('e', 8, 9),
	     ('f', 9, 9),
	     ('a', 11, 15),
	     ('b', 12, 14),
	     ('c', 17, 18),
	     ('d', 17, 19),
	     ('e', 18, 19),
	     ('f', 19, 19),
	     ('a', 21, 25),
	     ('b', 22, 24),
	     ('c', 27, 28),
	     ('d', 27, 29),
	     ('e', 28, 29),
	     ('f', 29, 29),
	     ('a', 31, 35),
	     ('b', 32, 34),
	     ('c', 37, 38),
	     ('d', 37, 39),
	     ('e', 38, 39),
	     ('f', 39, 39),
	     ('a', 41, 45),
	     ('b', 42, 44),
	     ('c', 47, 48),
	     ('d', 47, 49),
	     ('e', 48, 49),
	     ('f', 49, 49),]

# in one line using python sort
def oneLiner(arr):
	newarr = []
	for a in arr:
		newarr.append(a[:2])
		newarr.append((a[0], a[-1]))

	newarr.sort(key = operator.itemgetter(1))
	print newarr

def binarySort(arr):
	newarr = []
	for a in arr:
		newarr.append(a[:2])

	print newarr
	for i, a in enumerate(arr):
		print i, a
		start = i + 1
		end = len(newarr) - 1
		placed = False
		while start <= end and not placed:
			mid = (start + end)/2
			print 'start end mid', start, end, mid
			if a[2] > newarr[mid][1]:
				if mid == len(newarr) or a[2] <= newarr[mid+1][1]:
					newarr.insert(mid +1, (a[0], a[2]))
					placed = True
				else:
					start = mid 
			else: #a <= newarr[mid]
				if a[2] >= newarr[mid-1][1]:
					newarr.insert(mid, (a[0], a[2]))
					placed = True
				else: 
					end = mid

		print newarr


binarySort(inArr)
# oneLiner(inArr)

