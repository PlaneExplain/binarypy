import random
import time

#sorted single linked list creator
class Node:
  def __init__(self):
    self.data = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def addNode(self, data):
    curr = self.head
    if curr is None:
      n = Node()
      n.data = data
      self.head = n
      return

    if curr.data > data:
      n = Node()
      n.data = data
      n.next = curr
      self.head = n
      return

    while curr.next is not None:
      if curr.next.data > data:
        break
      curr = curr.next
    n = Node()
    n.data = data
    n.next = curr.next
    curr.next = n
    return

  def __str__(self):
    data = []
    curr = self.head
    while curr is not None:
      data.append(curr.data)
      curr = curr.next
    return "[%s]" %(', '.join(str(i) for i in data))

  def __repr__(self):
    return self.__str__()


#BST
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

#AVL
class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1

class AVLTree(object):

    def insert(self, root, key):
	
        if not root:
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

        root.h = 1 + max(self.getHeight(root.l),
						self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.value:
            return self.rRotate(root)

        if b < -1 and key > root.r.value:
            return self.lRotate(root)

        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)

    def printHeight(self, root):

        if not root:
            return
        
        print(root.h)


#drivers
#Sorted Single Link List driver
def SSLL(arr):
    ll = LinkedList()
    for num in arr:
        ll.addNode(num)
    print(ll)

#BST driver
def BSTdriver(arr):
    bst = BSTNode()
    for num in arr:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

    print("deleting " + str(arr))
    for num in arr:
        bst.delete(num)
    print("#")

#AVL driver
def AVLdriver(arr):
    Tree = AVLTree()
    root = None

    for num in arr:
        root = Tree.insert(root,num)

    Tree.printHeight(root)
    print ()

#array with no duplicates generator
amount = 1000
arr = random.sample(range(3*amount), amount)
AVLdriver(arr)