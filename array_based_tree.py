# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Assignment - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class BinTree:
  """Class to add to and search an array-based binary tree. 
  Array should have None where there could be nodes if not complete/full.
  Read depth first then left to right."""

  def __init__(self, array):
    self.array = array

  # (i) get parent and children
  def get_parent(self, node_index):
    if node_index % 2 == 0:
      return self.array[int((node_index)/2)-1]
    else:
      return self.array[int((node_index-1)/2)]

  def left(self, node_index):
    if 2*node_index+1 <= len(self.array):
      left = 2*node_index+1
    else:
      left = None
    return left

  def right(self, node_index):
    if 2*node_index+2 <= len(self.array):
      right = 2*node_index+2
    else:
      right = None
    return right

  def get_children(self, node_index):
    return self.array[self.left(node_index)], self.array[self.right(node_index)]

  # (iii) get depth of the tree
  # out of order because I use depth in my insertion functions

  def depth(self):
    depth = 0
    n = len(self.array)
    while n > 0:
      n -= 2**depth
      depth += 1
    return depth

  # (ii) add a new leaf node

  def insert_left(self, parent_index, new_value):
    if 2*parent_index+1 <= len(self.array):
      self.array[2*parent_index+1] = new_value
    else:
      self.array += [None]*(2**self.depth())
      self.array[2*parent_index+1] = new_value


  def insert_right(self, parent_index, new_value):
    if 2*parent_index+2 <= len(self.array):
      self.array[2*parent_index+2] = new_value
    else:
      self.array += [None]*(2**self.depth())
      self.array[2*parent_index+2] = new_value

  # (iv) breadth-first search, preorder search, and binary search

  def breadth_search(self, value):
    # array is arranged breadth first already
    for i in range(len(self.array)):
      if self.array[i] == value:
        return i

  def preorder_search(self, root, value):
    if self.array[root] == value:
      return root
    elif self.left(root) != None:
      root = self.left(root)
      self.preorder_search(root,value)
    elif self.left(root) == None and self.right(root) == None:
      self.preorder_search(self.get_parent(root), value)
    else:
      root = self.right(root)
      self.preorder_search(root,value)
    
  def bin_search(self,root,value):
    # only works on a binary search tree
    if self.array[root] is None or self.array[root] == value:
      return root
    elif self.array[root] > value:
      root = self.right(root)
      self.bin_search(root,value)
    elif self.array[root] < value:
      root = self.left(root)
      self.bin_search(root,value)

# tree 1 initialization (complete binary tree)
array = [45, 17, 60, 5, 23, 50, 70, 2, 12, 19, 72, None, None, None, None]
tree1 = BinTree(array)

# what is the parent of node 60 (index = 2)?
print('parent of node 60:', tree1.get_parent(2))

# what are the children of node 60?
print('children of node 60:', tree1.get_children(2))

tree1.breadth_search(60)

# what is the depth of this tree?
print('depth:', tree1.depth())

print('number of nodes:', len(tree1.array))

#  


# tree 1 initialization (complete binary tree)
array = [45, 17, 60, 5, 23, 50, 70, 2, 12, 19, 72, None, None, None, None]
tree1 = BinTree(array)

# what is the parent of node 60 (index = 2)?
print('parent of node 60:', tree1.get_parent(2))

# what are the children of node 60?
print('children of node 60:', tree1.get_children(2))

# what is the depth of this tree?
print('depth:', tree1.depth())

# find node 72 using breadth first search
print('node 72 index:', tree1.breadth_search(72))

# tree2 initialization (incomplete binary tree)
array2 = [45,17,60,5,23,None,70,2,None,19,72,None,None,50,None]
tree2 = BinTree(array2)

# what is the parent of node 60 (index = 2)?
print('parent of node 60:', tree2.get_parent(2))

# what are the children of node 60?
print('children of node 60:', tree2.get_children(2))

# what is the depth of this tree?
print('depth:', tree2.depth())

# find node 5 using preorder search
print('node 5 index:', tree2.preorder_search(0,5))

# tree3 initialization (binary search tree)
array3 = [14,7,27,5,10,20,28,4,6,9,11,None,None,None,None]
tree3 = BinTree(array3)

# what is the parent of node 27 (index = 2)?
print('parent of node 60:', tree3.get_parent(2))

# what are the children of node 27?
print('children of node 60:', tree3.get_children(2))

# what is the depth of this tree?
print('depth:', tree3.depth())

# find node 28 using breadth first search
print('node 28 index:', tree3.breadth_search(28))

# find node 5 using binary search
print('node 20 index:', tree3.bin_search(0,5))