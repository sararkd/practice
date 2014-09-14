
def firstNonAsc(arr):
	for i, a in enumerate(arr):
		if i == len(arr)-1: 
			return None
		if arr[i+1] < a:
			return arr[i+1]


print firstNonAsc([1, 3, 4, 5, 67, 13, 8])
