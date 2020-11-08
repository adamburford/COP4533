#Adam Burford
#COP4533
#Section 3594

from collections import deque
import timeit
import random

class Node:

    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class LinkedList():
	'''Horrible implementation of doubly ended queue'''

	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		self.iter_node = self.head
		return self

	def __next__(self):
		if self.iter_node == None:
			raise StopIteration
		
		data = self.iter_node.data

		self.iter_node = self.iter_node.next
		
		return data

	def element_at(self, index):
		'''Returns item at specified index'''
		return self.node_at(index).data


	def node_at(self, index):
		'''Helper function returns node at index'''
		current_node = self.head
		for i in range(index):
			current_node = current_node.next
		return current_node

	def isEmpty(self):
		'''Returns True if Linked List is empty, False if it contains data'''
		return self.head == None

	def add(self, item):
		'''Prepend item to list'''
		new_node = Node(item)
		new_node.next = self.head
		self.head = new_node
		if self.tail == None:
			self.tail = new_node

	def append(self, item):
		'''Append item to list'''
		new_node = Node(item)

		if self.tail != None:

			self.tail.next = new_node
			self.tail = new_node
		else:

			self.head = new_node
			self.tail = new_node

	def __len__(self):
		current = self.head
		count = 0

		while current != None:
			count = count + 1
			current = current.next

		return count

	def search(self, item):
		'''Returns true if item is found in list, false otherwise'''
		current = self.head
		found = False

		while current != None and not found:
			if current.data == item:
				found = True
			else:
				current = current.next

		return found

	def remove(self, item):
		'''Removes first instance of item found in list'''
		current = self.head
		previous = None
		found = False
		while not found:
			if current.data == item:
				found = True
			else:
				previous = current
				current = current.next

		if previous == None:
			self.head = current.next
		else:
			previous.setNext(current.next)
			if current.next == None:
				tail = previous

	def insert(self, item, index):
		'''Inserts item at specified index in list'''
		new_node = Node(item)

		if index == 0:
			new_node.next = self.head
			self.head = new_node
			return

		current_node = self.head
		previous_node = None
		for i in range(index):
			previous_node = current_node
			current_node = current_node.next

		new_node.next = current_node
		if current_node == self.tail:
			self.tail == new_node
		previous_node.next = new_node

	def index(self, index):
		'''Returns item at specified index'''
		if position == 0:
			return head.data

		current_node = head
		for i in range(index):
			current_node = current_node.next

		return current_node.data

	def clear():
		'''Removes all items, good luck garbage collector'''
		self.head = None
		self.tail = None

	def pop(self, index = None):
		'''Removes and returns item at specified index in the list
		Removes last item if index not specified'''

		if index == 0:
			return_node = self.head
			if self.head == self.tail:
				self.tail = None
			self.head = self.head.next
			return return_node

		current_node = self.head
		previous_node = None

		if index == None:

			while current_node.next != None:
				previous_node = current_node
				current_node = current_node.next

			previous_node.next = None
			tail = previous_node

		else:
			for x in range(index):
				previous_node = current_node
				current_node = current_node.next

			if current_node.next != None:
				previous_node.next = current_node.next
			else:
				previous_node.next = None
				tail = previous_node

		return current_node

	def __str__(self):
		return "[" + ", ".join((str(x) for x in self)) + "]"
		
def fill_list(list, count = 1000000):
	for x in range(count):
		list.append(42)

def fill_list_appendleft(list, count = 10000000):
	for x in range(count):
		list.appendleft(42)

def fill_list_prepend(list, count = 10000000):
	for x in range(count):
		list.add(42)

def main():

	print("Test Results\n")
	print("Populating lists with 1,000,000 numbers, 5 runs each")
	print("-------------------------------------")

	times = timeit.repeat(setup = "python_list = []", stmt = "fill_list(python_list)", number = 1, repeat = 5, globals=globals())
	print("Python List: " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "", stmt = "python_list = [42] * 500000", number = 1, repeat = 5, globals=globals())
	print("Python List (ver 2): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "", stmt = "python_list = [42 for _ in range(500000)]", number = 1, repeat = 5, globals=globals())
	print("Python List (ver 3): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "python_deque = deque()", stmt = "fill_list(python_deque)", number = 1, repeat = 5, globals=globals())
	print("Python Deque (append): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "python_deque = deque()", stmt = "fill_list_appendleft(python_deque)", number = 1, repeat = 5, globals=globals())
	print("Python Deque (prepend): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "my_list = LinkedList()", stmt = "fill_list(my_list)", number = 1, repeat = 5, globals=globals())
	print("My List (append): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "my_list = LinkedList()", stmt = "fill_list_prepend(my_list)", number = 1, repeat = 5, globals=globals())
	print("My List (prepend): " + str(["{0:0.5f}".format(time) for time in times]))

	print("\nSorting lists")
	print("-------------------------------------")

	times = timeit.repeat(setup = "python_list = []\nfor x in range(1000000):\n	python_list.append(random.randrange(1,1001))", stmt = "python_list.sort()", number = 1, repeat = 5, globals=globals())
	print("Python list.sort(): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "python_list = []\nfor x in range(1000000):\n	python_list.append(random.randrange(1,1001))", stmt = "sorted_list = sorted(python_list)", number = 1, repeat = 5, globals=globals())
	print("Python list sorted(): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "python_deque = deque()\nfor x in range(1000000):\n	python_deque.append(random.randrange(1,1001))", stmt = "sorted_list = sorted(python_deque)", number = 1, repeat = 5, globals=globals())
	print("Python deque sorted(): " + str(["{0:0.5f}".format(time) for time in times]))

	times = timeit.repeat(setup = "my_list = LinkedList()\nfor x in range(1000000):\n	my_list.append(random.randrange(1,1001))", stmt = "sorted_list = sorted(my_list)", number = 1, repeat = 5, globals=globals())
	print("My list sorted(): " + str(["{0:0.5f}".format(time) for time in times]))
	
if __name__ == "__main__":
	main()







