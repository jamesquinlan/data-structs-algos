# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Chapter 6 - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# R-6.5
'''
Implement a function that reverses a list of elements by pushing them onto a 
stack in one order, and writing them back to the list in reversed order.

Note: Stack and Queue Classes contained at the bottom of this file.
'''

x = [1, 2, 3, 4, 5]
S = Stack()
for i in x:
  S.push(i)
for i in range(S.numel()):
  x[i] = S.pop()

# Results
x

# R-6.3
'''
Implement a functino with signature `transfer(S,T)` which takes stack S :-onto-> T.
The top of S maps to the bottom of T and vice-versa.
'''

def transfer(S,T):
  while not S.is_empty():
    T.push(S.pop())

# R-6.3

# Driver Code
S = Stack()
T = Stack()
S.push(6)
S.push(3)
S.push(5)
S.push(13)
transfer(S,T)
# S.disp()
T.disp()

# C-6.23
'''
Suppose you have three nonempty stacks R, S, and T.  Describe a sequence of steps
that results in S storing all elements originally in T below all of S's original
elements.  The final config should have R untouched (hint after pushing onto for
temporary storage) and S = [T, S].  In effect, move elements of T to the bottom
of the stack preserving order in both T and S.  For example, R = [1,2,3], S = [4,5], 
and T = [6,7,8,9].  In the end, S = [6,7,8,9,4,5].
'''



class Empty(Exception):
  pass

class Stack:
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

  def disp(self):
    for i in self._data:
      print(i)

# Test Stack
X = Stack()

X.push(4)
X.push(5)

X.top()

X.pop()

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