#Adam Burford
#COP4533
#Section 3594

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
		if self.iter_node == self.tail:
			raise StopIteration
		
		self.iter_node = self.iter_node.next
		
		return self.iter_node.data
	
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


	def __str__(self):
		s = "["

		if self.head != None:
			s += str(self.head.data)

			current_node = self.head.next
			while current_node != None:
				s += ", " + str(current_node.data)
				current_node = current_node.next

		s += "]"

		return repr(s)
		


def main():
	myList = LinkedList()

	for x in range(10):
		myList.add(x + 1)

	print(myList)

	myList = sorted(myList)
	print(myList)

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

if __name__ == "__main__":
	main()







