debug = False

def allAdj(x, n):
    adj = []
    #left 
    if x[0] > 0: 
        adj.append((x[0]-1, x[1]))
    #right
    if x[0] < n-1:
        adj.append((x[0]+1, x[1]))
    #top
    if x[1] > 0: 
        adj.append((x[0], x[1]-1))
    #bottom
    if x[1] < n-1: 
        adj.append((x[0], x[1]+1))
    return adj


def computeSP(maze, S, D):
    n = len(maze)
    path = [[(-1, -1) for x in range(n)] for x in range(n)]
    dist = [[n*n for x in range(n)] for x in range(n)]

    dist[S[0]][S[1]] = 0
    path[S[0]][S[1]] = S

    changeFlag = True
    while changeFlag:
        if debug: print dist
        changeFlag = False
        for x in range(n):
            for y in range(n):
                adj = allAdj((x,y), n)
                for a in adj:
                    if dist[a[0]][a[1]] + 1 < dist[x][y] and maze[a[0]][a[1]] == 0 and maze[x][y] == 0:
                        dist[x][y] = dist[a[0]][a[1]] + 1
                        path[x][y] = a
                        changeFlag = True

    if debug: print 'path: ', path
    
    print 'distance = ', dist[D[0]][D[1]]
    P = D
    route = [D]
    while not P == S:
        P = path[P[0]][P[1]]
        route.insert(0, P)
    print route


maze = [[0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0], 
        [0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0],]
S = (0,0)
D = (2,2)
computeSP(maze, S, D)