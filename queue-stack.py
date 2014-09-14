
class myQueue():
	
	stacks = {0:[], 1:[]}
	def __init__(self, que):
		self.stacks = {0:que, 1:[]}
	
	def push(self, item):
		self.stacks[0].append(item)

	def pop(self):
		if self.stacks[0] == []: 
			return None
		
		while not len(self.stacks[0]) > 1:
			x = self.stacks[0].pop()
			self.stacks[1].append(x)
		popped = self.stacks[0].pop()
		while not self.stacks[1] == []:
			x =self.stacks[1].pop()
			self.stacks[0].append(x)

		return popped

	def printQue(self):
		print self.stacks[0]


q = myQueue([4,5,6])
q.printQue()
print q.pop()
q.printQue()
q.push(8)
q.printQue()
