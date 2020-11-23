#Adam Burford
#COP4533
#Section 3594

from binary_tree import BinarySearchTree

class BinaryTreeStringList():
    """Binary Tree String List"""


    def __init__(self):
        
        self.__tree = BinarySearchTree()

    def __iter__(self):
        return iter(self.__tree)

    def __getitem__(self, key):
        return self.__tree[key]

    def __setitem__(self, key, value):
        self.__tree[key] = value

    def __str__(self):
        return str(self.__tree)

    def __len__(self):
        return len(self.__tree)

    def add(self, value):
        self.__tree.put(value)
        
    def find(self, value):
        return value in self.__tree