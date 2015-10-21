from collections import deque
class Node:
	def __init__(self, info):
		self.info = info
		self.left = None
		self.right = None
		self.level = None
	def __str__(self):
		return str(self.info)
def BFT(node):
	even = deque()
	odd = deque()
	stack = []
	stack2 = []
	odd.append(node)
	while True:
		if len(odd) > 0:
			while len(odd) > 0:
				current = odd.pop()
				print(str(current))
				if current.right != None:
					even.append(current.left)
				if current.left != None:	
					even.append(current.right)

		if (len(even) > 0):
			while len(even) > 0:
				cur = even.pop()
				stack.append(cur)
				if cur.right != None:
					odd.append(cur.right)
				if cur.left != None:	
					odd.append(cur.left)

			if len(stack) > 0:
				while len(stack) > 0:
					stack2.append(stack.pop())
				while len(stack2) > 0:
					print(stack2.pop())
	
		if len(stack) == 0 and len(odd) == 0 and len(even) == 0:
			break
test_root = Node(9)
test_root.left = Node(2)
test_root.right = Node(4)
test_root.left.left = Node(1)
test_root.left.right = Node(3)
test_root.right.left = Node(5)
test_root.right.right = Node(7)
test_root.left.left.left = Node(6)
test_root.left.left.right = Node (17)
test_root.left.right.left = Node(8)
test_root.left.right.right = Node(9)
test_root.right.left.left = Node(11)
test_root.right.left.right = Node(13)
test_root.right.right.left = Node(12)
test_root.right.right.right = Node (50)

BFT(test_root)
