# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tree Class - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Tree():
  
  def __init__(self):
    self.nodes = [1,2,3]

  def getIndex(self,x):
    return self.index(x)

  def addNode(self,value):
    pass

  def parent(self,x):
    idx = self.getIndex(x)
    if idx != 0:
      return math.floor((idx-1)/2)




# TESTS
x = [1,2,3]
x.index(2)
T = Tree()
T

import math
def getIndex(T,x):
  return T.index(x)

def addNode(T,value):
  pass

def parent(T,x):
  idx = getIndex(T,x)
  if idx != 0:
    return math.floor((idx-1)/2) 

def children(T,x):
  idx = getIndex(T,x)
  left = 2*idx+1
  right = 2*idx+2
  return (left,right)

def bfs(T,x):
  # Find x in tree T.
  pass



# Additional TESTS
T = [1,2,3]
getIndex(T,2)
parent(T,3)
left, right = children(T,1)
T[left]

