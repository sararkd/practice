
import copy 

# knight (horse :D)
def threatens(a, b, cache = {}):
	if (a, b) in cache:
                 return cache[(a,b)]
	deltaX = abs(a[0] - b[0])
	deltaY = abs(a[1] - b[1])
	if (deltaX == 1 and deltaY == 2) or (deltaX == 2 and deltaY == 1):
		cache[(a,b)] = True
	else:
		cache[(a,b)] = False
	return cache[(a,b)]


def maxPiecesBT(n, pieceType):
	#in this one board is represented by a dictionary of pieces
	brd = {}
	maxx = 0
	count = 1
	boardStack = [copy.copy(brd)]
	while boardStack:
		brd = boardStack.pop()
		for i in range(n):
			for j in range(n):
				# print i, j, brd
				if not (i, j) in brd:						
					threatened = False
					for p in brd:
						if threatens(p, (i, j)):
							threatened = True
					if not threatened:
						brd[(i, j)] = True
						count +=1
						if len(brd) > maxx: maxx = len(brd)
						print count, brd, len(brd)
						boardStack.append(copy.copy(brd))
						# print boardStack, "&&&&&&&&&&&"
						del brd[(i, j)]
	return maxx

maxPiecesBT(3, 'knight')
