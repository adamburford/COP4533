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
	
	def isEmpty(self):
		'''Returns True if Linked List is empty, False if it contains data'''
		return self.head == None

	def add(self,item):
		'''Add new item at first position in the list'''
		new_node = Node(item)
		new_node.next = self.head
		self.head = new_node
		if self.tail == None:
			self.tail = new_node

	def size(self):
		'''Returns number of nodes'''
		return sum(1 for _ in self)

	def __len__(self):
		return self.size()

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

	def append(self, item):
		'''Adds item to the end of the list'''
		new_node = Node(item)

		tail.setNext(new_node)
		tail = new_node

	def insert(self, item, index):
		'''Inserts item at specified index in list'''
		new_node = Node(item)

		if index == 0:
			new_node.next = self.head
			self.head = new_node
			return

		previous_node = self.node_at(index - 1)
		current_node = previous_node.next

		new_node.next = current_node
		if current_node == self.tail:
			self.tail == new_node
		previous_node.next = new_node

	def element_at(self, index):
		'''Returns item at specified index'''
		return self.node_at(index).data


	def node_at(self, index):
		current_node = self.head
		for i in range(index):
			current_node = current_node.next
		return current_node

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

	def removeAt(self, index):
		'''Removes node at specified index'''

	def __len__(self):
		return self.size()

	def __getitem__(self, key):
		return self.element_at(key)

	def __setitem__(self, key):
		self.insert(key)

	def __delitem__(self, key):
		self.pop(key)

	def __contains__(self, item):
		return self.search(item)

	def __str__(self):
		return "[" + ", ".join((str(x) for x in self)) + "]"
		
def fill_list(list, count = 1000000):
	for x in range(count):
		list.append(random.randrange(1,101))

def main():

	time = timeit.timeit(setup = "python_list = []", stmt = "fill_list(python_list)", number = 3, globals=globals())
	print(time)

	mysetup = '''test'''

	python_deque = deque()
	fill_list(python_deque, 100)
	print(python_deque)

	my_list = LinkedList()

	for x in range(10):
		my_list.add(x + 1)

	print("TEST LIST: " + str(my_list))
	for x in my_list:
		print(x)

	myList = sorted(my_list)

	print("Sorted: " + str(myList))
	for x in myList:
		print(x)

	test1 = LinkedList()
	test1.add(0)
	test1.insert(1,1)

	print(test1)

	test2 = LinkedList()

	test2.add(100)
	test2.insert(200,0)
	print(test2)
	test2.insert(300,1)
	print(test2)
	test2.pop()
	print(test2)
	test2.add(400)
	test2.add(500)
	test2.insert(600,0)
	print(test2)
	test2.insert(650,0)
	print(test2)
	test2.insert(675,0)
	test2.insert(710,1)
	test2.insert(700,1)
	print(test2)
	print(sorted(test2))
	print(test2)
	test2.pop()
	print(test2)
	test2.pop(0)
	print(test2)
	test2.pop(1)
	print(test2)

if __name__ == "__main__":
	main()






