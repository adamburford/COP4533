#Adam Burford
#COP4533
#Section 3594

class BinarySearchTree:
    """Binary Search Tree class from:
    Problem Solving with Algorithms and Data Structures using Python
    By Brad Miller and David Ranum, Luther College
    --Minor refactoring by Adam Burford
    --Also removed key from nodes, now operates only on values"""

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, value):
        if self.root:
            self._put(value, self.root)
        else:
            self.root = TreeNode(value)
        self.size = self.size + 1

    def _put(self, value, current_node):
        if value < current_node.value:
            if current_node.hasLeftChild():
                   self._put(value, current_node.left_child)
            else:
                   current_node.left_child = TreeNode(value, parent = current_node)
        else:
            if current_node.hasRightChild():
                   self._put(value, current_node.right_child)
            else:
                   current_node.right_child = TreeNode(value,parent=current_node)



    def get(self, value):
       if self.root:
           match = self._get(value, self.root)
           if match:
                  return match.value
           else:
                  return None
       else:
           return None

    def _get(self, value, current_node):

       if not current_node:
           return None
       elif current_node.value == value:
           return current_node
       elif value < current_node.value:
           return self._get(value, current_node.left_child)
       else:
           return self._get(value, current_node.right_child)

    def __getitem__(self, value):
       return self.get(value)

    def __setitem__(self, k, v):
       self.put(k, v)

    def __contains__(self, key):
       return self._get(key, self.root) != None

    def delete(self, value):
      if self.size > 1:
         nodeToRemove = self._get(value, self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.value == value:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def remove(self, currentNode):
         if currentNode.isLeaf():
           if currentNode == currentNode.parent.left_child:
               currentNode.parent.left_child = None
           else:
               currentNode.parent.right_child = None
         elif currentNode.hasBothChildren():
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.value = succ.value

         else:
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.left_child.parent = currentNode.parent
                 currentNode.parent.left_child = currentNode.left_child
             elif currentNode.isRightChild():
                 currentNode.left_child.parent = currentNode.parent
                 currentNode.parent.right_child = currentNode.left_child
             else:
                 currentNode.replaceNodeData(currentNode.left_child.value,
                                    currentNode.left_child.left_child,
                                    currentNode.left_child.right_child)
           else:
             if currentNode.isLeftChild():
                 currentNode.right_child.parent = currentNode.parent
                 currentNode.parent.left_child = currentNode.right_child
             elif currentNode.isRightChild():
                 currentNode.right_child.parent = currentNode.parent
                 currentNode.parent.right_child = currentNode.right_child
             else:
                 currentNode.replaceNodeData(currentNode.right_child.value,
                                    currentNode.right_child.left_child,
                                    currentNode.right_child.right_child)

class TreeNode:
    """Binary Search Tree Node class from:
    Problem Solving with Algorithms and Data Structures using Python
    By Brad Miller and David Ranum, Luther College
    --Minor refactoring by Adam Burford"""

    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left_child

    def hasRightChild(self):
        return self.right_child

    def isLeftChild(self):
        return self.parent and self.parent.left_child == self

    def isRightChild(self):
        return self.parent and self.parent.right_child == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right_child or self.left_child)

    def hasAnyChildren(self):
        return self.right_child or self.left_child

    def hasBothChildren(self):
        return self.right_child and self.left_child

    def spliceOut(self):

        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.right_child.findMin()
        else:
            if self.parent:
                   if self.isLeftChild():
                       succ = self.parent
                   else:
                       self.parent.right_child = None
                       succ = self.parent.findSuccessor()
                       self.parent.right_child = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left_child
        return current

    def replaceNodeData(self, value, lc, rc):
        self.key = key
        self.value = value
        self.left_child = lc
        self.right_child = rc
        if self.hasLeftChild():
            self.left_child.parent = self
        if self.hasRightChild():
            self.right_child.parent = self


