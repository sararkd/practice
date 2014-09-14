
h = [[4, 3, 2, 1],
     [],
     []]

def moveDisk(fromTower, toTower):
	if not len(h[toTower]) == 0 and h[fromTower][-1] > h[toTower][-1]:
		print 'Error: cannot move from tower', fromTower, 'to tower', toTower
		return

	disk = h[fromTower].pop()
	h[toTower].append(disk)
	print fromTower, '-->', toTower, '******', h[0], "\t", h[1], "\t", h[2]

def hanoi(fromTower, toTower, nDisks):
	thirdTower = 3 - fromTower - toTower
	if nDisks == 0:
		return
	hanoi(fromTower, thirdTower, nDisks-1)
	moveDisk(fromTower, toTower)
	hanoi(thirdTower, toTower, nDisks-1)

hanoi(0, 1, 4)