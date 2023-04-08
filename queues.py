# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Queues - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Empty(Exception):
  pass

class Queue:
  '''Queue, FIFO'''
  '''Use Circular List as storage'''
  
  CAPACITY = 6

  def __init__(self):
    self._data = [None]*Queue.CAPACITY
    self._size = 0
    self._front = 0

  def numel(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def first(self):
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def nq(self, x):
    n = (self._front + self._size) % Queue.CAPACITY
    self._data[n] = x
    self._size += 1

  def dq(self):
    if self.is_empty():
      raise Empty('Queue is empty')
    who = self._data[self._front]
    self._data[self._front] = None
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return who

  def _resize(self):
    ''' Double capacity '''
    prior = self._data
    self._data = [None]*(2*len(prior))
    f = self._front
    for k in range(self._size):
      self._data[k] = prior[f]
      f = (f + 1) % len(prior)
    self._front = 0

Q=Queue()  # Don't forget the () after Queue



# DRIVER
# ---------------
Q.nq(7)
Q.nq(5)
Q.nq(1)
for i in Q._data:
  print(i)

Q.first()


Q.dq()
for i in Q._data:
  print(i)




# R-6.5
'''
Implement a function that reverses a list of elements by pushing them onto a 
stack in one order, and writing them back to the list in reversed order.
'''