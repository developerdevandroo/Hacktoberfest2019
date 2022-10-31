# Python3 program for the above approach
from collections import deque
from math import sqrt, ceil, floor

# Structure of a
# Binary Tree Node
class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

# Function to replace all nodes
# at even and odd levels with their
# nearest even or odd perfect squares
def LevelOrderTraversal(root):

	# Base Case
	if (root == None):
		return

	# Create an empty queue
	# for level order traversal
	q = deque()

	# Enqueue root
	q.append(root)

	# Initialize height
	lvl = 1

	# Iterate until queue is not empty
	while (len(q) > 0):

		# Store the size
		# of the queue
		n = len(q)

		# Traverse in range [1, n]
		for i in range(n):

			# Store the current node
			node = q.popleft()

			# Store its square root
			num = sqrt(node.data)
			x1 = floor(num)
			x2 = ceil(num)

			# Check if it is a perfect square
			if (x1 == x2):

				# If level is odd and value is even,
				# find the closest odd perfect square
				if ((lvl & 1) and not (x1 & 1)):
					num1, num2 = x1 - 1, x1 + 1
					node.data = (num1 * num1) if (abs(node.data - num1 * num1) < abs(node.data - num2 * num2)) else (num2 * num2)

				# If level is even and value is odd,
				# find the closest even perfect square
				if (not (lvl & 1) and (x1 & 1)):
					num1,num2 = x1 - 1, x1 + 1
					node.data = (num1 * num1) if (abs(node.data - num1 * num1) < abs(node.data - num2 * num2)) else (num2 * num2)

			# Otherwise, find the find
			# the nearest perfect square
			else:
				if (lvl & 1):
					node.data = (x1 * x1) if (x1 & 1) else (x2 * x2)
				else:
					node.data = (x2 * x2) if (x1 & 1) else (x1 * x1)

			# Prfront of queue
			# and remove it from queue
			print(node.data, end = " ")

			# Enqueue left child
			if (node.left != None):
				q.append(node.left)

			# Enqueue right child
			if (node.right != None):
				q.append(node.right)

		# Increment the level by 1
		lvl += 1
		print()

# Driver Code
if __name__ == '__main__':

	# Binary Tree
	root = Node(5)
	root.left = Node(3)
	root.right = Node(2)
	root.right.left = Node(16)
	root.right.right = Node(19)

	LevelOrderTraversal(root)

	# This code is contributed by mohit kumar 29.
