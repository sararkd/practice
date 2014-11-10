
from collections import deque

def BFS(graph, start):
    seen = {start:True}
    bfsQue = deque(start)
    level = 0
    while bfsQue:
        # print level
        # print 'Que', bfsQue
        # print 'seen', seen
        level += 1
        node = bfsQue.popleft()
        print node #, ':',
        for adj in graph[node]:
            # print adj,
            if not adj in seen:
                bfsQue.append(adj)
                seen[adj] = True
        # print 


def BFSPath(graph, start, end):
    found = False
    pred = {start: None}
    bfsQue = deque(start)
    level = 0
    while bfsQue:
        # print level
        # print 'Que', bfsQue
        # print 'seen', seen
        level += 1
        node = bfsQue.popleft()
        # print node #, ':',
        for adj in graph[node]:
            # print adj,
            if not adj in pred:
                bfsQue.append(adj)
                pred[adj] = node
                if end == adj: 
                    found = True
                    break
        if found: break

    if not found:
        print 'No path :('
    else:
        path = [] 
        next = end
        while next:
          path.append(next)
          next = pred[next]
        for i in range(len(path)-1, -1, -1):
            print path[i]


def DFS(graph, start, seen):
    print start
    seen[start] = True
    for adj in graph[start]:
        if not adj in seen:
            DFS(graph, adj, seen)



graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

graph0 = {'A': ['B'],
          'B': ['C', 'I'],
          'C': ['D', 'H'],
          'D': ['E', 'G'],
          'E': ['F'],
          'F': [],
          'G': [],
          'H': [],
          'I': [],}

BFSPath(graph, 'A', 'F')
# BFS(graph0, 'A')
# seen = {}
# DFS(graph0, 'A', seen)