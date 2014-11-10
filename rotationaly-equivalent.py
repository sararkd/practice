

# ab -> ef
# Write a function that takes as input a list of strings, and outputs any set of strings of size > 1 that are rotationally equivalent, 
# under any rotation.
# ['ab', 'ef', 'az', 'x', 'z', 'no', 'op', 'hello', 'za']
# 'ab', 'za', 'ef', 'no', 'op'
# 'x', 'z'

def rotEq(s1, s2):
	if not len(s1) == len(s2): 
		return False
	
	delta = (ord(s1[0]) - ord(s2[0])) % 26 
	for i, ch in enumerate(s1):
		if  not (ord(ch) - ord (s2[i])) % 26 == delta:
			return False
	return True 

def FindRotEq(strList):
	matched = [False for x in strList]
	for i in range(0, len(strList)-1):
		if matched[i]: continue
		x = strList[i]
		matchFound = False
		for j in range(i+1, len(strList)):
			if matched[j]: continue
			y = strList[j]
			if rotEq(x, y):
				matched[i] = matched[j] = True
				if not matchFound:
					print x, y,
					matchFound = True
				else: 
					print y,
		if matchFound: print 


l = ['ab', 'ef', 'az', 'x', 'z', 'no', 'op', 'hello', 'za']
FindRotEq(l)

