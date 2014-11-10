# number of routes between topleft and bottom right squares that pass only 1 squares on a board of 0 and 1's
# can only move down and right, right?

# n*n matrix, b: dictionary of places (tuples) of 1 squares
def numRoutes(n, b):
	nRoutes = [[0]*n for x in range(n)]
	
	nRoutes[0][0] = 1
	for j in range(1, n):
		if (0, j) in b: 
			nRoutes[0][j] = nRoutes[0][j-1]
	for i in range(1, n):
		if (i, 0) in b: 
			nRoutes[i][0] = nRoutes[i-1][0]

	for i in range(1, n):
		for j in range(1, n):
			if (i, j) in b:
				nRoutes[i][j] =  nRoutes[i-1][j] + nRoutes[i][j-1]

	return nRoutes[n-1][n-1]

#complete 3*3
# board = {(0, 0):1, (0, 1):1, (0, 2):1, (1, 0):1, (1, 1):1, (1, 2):1, (2, 0):1, (2, 1):1, (2, 2):1}
board = {(0, 0):1, (0, 1):1, (0, 2):1, (1, 0):1, (1, 1):1, (1, 2):1, (2, 0):1, (2, 1):1, (2, 2):1}

print numRoutes(3, board)