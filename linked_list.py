# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Linked Lists - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Empty(Exception):
  pass

class SLL:
  '''Single Linked List Data Structure'''
  '''Insert and delete occurs at head'''

  # Node Subclass
  class Node:
    __slots__ = 'value','next'

    def __init__(self, value, next):
      self.value = value
      self.next = next

 
  # ------------- List Methods --------------- #
  def __init__(self):
    self.head = None
    self.size = 0

  def insert(self, x):
    self.head = self.Node(x,self.head)
    self.size += 1
  
  def remove(self):
    '''Removes element from head'''
    self.head = self.head.next
    self.size -= 1

  def first(self):
    return self.head.value

  def isempty(self):
    return self.size == 0



# TESTS
L = SLL()
L.insert(1)
L.insert(2)
L.isempty()

L.insert(3)
L.insert(4)
L.insert(5)
L.size

L.head.value
L.head.next.value
L.Node.next

# Loop through nodes
node = L.head
while node is not None:
  print(node.value)
  node = node.next

L.remove()

L.head.next

L.head

# Node Subclass
class Node:
    __slots__ = 'value','next'

    def __init__(self, value, next):
      self.value = value
      self.next = next

x = Node(3,None)

x.value

y = Node(1,x)

y.value

y.next.value

class Testing:
  def __init__(self):
    self.head = None
    self.size = 0
x = Testing()
x.size





# Double linked list
class DoubleLL:

  class Node:
    __slots__ = 'value','prev','next'

    def __init__(self, value, prev, next):
      self.value = value
      self.prev = prev
      self.next = next

  def __init__(self):
    self.head = self.Node(None, None, None)
    self.tail = self.Node(None, None, None)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.size = 0

  def isempty(self):
    return self.size == 0

  def insert(self, value, before, after):
    new = self.Node(value, before, after)
    before.next = new
    after.prev = new
    self.size += 1
    return new

  def delete(self, node):
    # shuffle points
    if self.node.value != None:
      self.node.prev.next = self.node.next
      self.node.next.prev = self.node.prev
      self.size -= 1

# Create DLL
x = DoubleLL()

# Insert new element (node)
y = x.insert(5,x.head, x.tail)

# Check on its value
y.value
y.next

# Insert two more elements
a = x.insert(1,x.head, y)
b = x.insert(2,a,y)
a.value
a.next.value
b.prev.value
b.prev.prev.value


# ADDITIONAL RESOURCES 
# Underscores in Python
# https://www.datacamp.com/community/tutorials/role-underscore-python

# Python tips
# https://book.pythontips.com/en/latest/__slots__magic.html

# 
# https://realpython.com/linked-lists-python/


