# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LinkedStack - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class LinkedStack:

  # ------------- Node Subclass --------------- #
  class Node:
    __slots__ = 'element','next'

    def __init__(self, element, next):
      # Self = Node 
      self.element = element
      self.next = next

  # ------------ Stack Methods --------------- #
  def __init__(self):
    # Self = Linked List (Stack)
    self.head = None
    self.size = 0

  def push(self,val):
    self.head = self.Node(val,self.head)
    self.size += 1

  def top(self):
    return self.head.element
  
  def pop(self):
    element_to_return = self.head.element
    self.head = self.head.next
    self.size -= 1
    return element_to_return



# Driver code
# ------------------
x = LinkedStack()
x.push(5)
x.top()

