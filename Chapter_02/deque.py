class Deque:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def add_front(self, item):
		self.items.append(item)
	def add_rear(self, item):
		self.items.insert(0, item)
	def remove_front(self):
		return self.items.pop()
	def remove_rear(self):
		return self.items.pop(0)
	def size(self):
		return len(self.items)
d = Deque()
d.add_front("athul")
d.add_front("ravi")
d.add_front("shibin")
d.add_rear("chalu")
d.add_rear("ansab")
print d.remove_rear()
print d.size()
