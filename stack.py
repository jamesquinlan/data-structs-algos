# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Stack Implementation - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Empty(Exception):
  pass

class ArrayStack:
  '''Stack, FILO or LIFO'''
  '''Use List as storage'''

  def __init__(self):
    self._data = []

  def numel(self):
    return len(self._data)

  def is_empty(self):
    return len(self._data) == 0
  
  def push(self, x):
    self._data.append(x)

  def top(self):
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]

  def pop(self):
    if self.is_empty():
      raise Empty('Static is empty')
    return self._data.pop()



# DRIVER
# -----------
S = ArrayStack()
S.push(4)
S.push(7)
S.is_empty()
S.numel()
S.is_empty()
S.pop()
S._data
S.push(3)

