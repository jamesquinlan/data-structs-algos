# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Chapter 4 - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""

# R-4.6 

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Describe a recursive function for Harmonic number H_n = sum_{k=1}^n 1/k
# ----------------------------------------------------------------------------

def H(n):
  if n == 1:
    return 1
  else:
    return 1/n + H(n-1)

H(3)

# Iterative implementation
n = 3
h = 0
for k in range(1,n+1):
  h += 1/k

print(h)

# R-4.9 

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Recursive MAX function
# ----------------------------------------------------------------------------

def Max(data):
  m1 = data[0]
  if len(data) > 1:
    m2 = Max(data[1:len(data)])
  else:
    m2 = data[0]
    
  if m1 > m2:
    return m1
  else:
    return m2

data = [5,3,8,4,11,2,1]
print(Max(data))

# C-4.12 
# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Recursive product (m,n)
# ----------------------------------------------------------------------------

def prod(m,n):
  # m = multiplier
  # n = number
  # m*n = n + n + n + ... + n (m-times)

  if m == 1:
    return n
  else:
    return n + prod(m-1,n)

# Test function 
prod(5,9)

# C-4.14 
# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Towers of Hanoi (Classic recursion problem)
# ----------------------------------------------------------------------------

import random
from time import time 
n = 50
data = random.sample(range(1, 10*n), n)

start_time = time()
data.sort()
stop_time = time()
elapsed = stop_time - start_time
print(elapsed,'seconds')

# 4.15
'''
Write a recursive function that will output all the subsets of a set of n
elements (without repeating the subsets)
'''

def subsets(A):
  if len(A)==0:
    return set()
  else:
    B = subsets(A[1:])
    return B | {x for x in B}

x = [1,2,3]
print(subsets(x))

def subsets(A):
    if A == []:
        return [[]]

    x = subsets(A[1:])

    return x + [[A[0]] + y for y in x]

A = [1,2,3]
print(subsets(A))

def subsets(A):
    if len(A)==0:
        return set()

    x = subsets(A[1:])

    return x | {{A[0]} | y for y in x}

A = [1,2,3]
print(subsets(A))

# 4.19
'''
Write recursive function that takes a list and put all even numbers before 
all odds
'''

def evens_then_odds(x,low,high):
  if low < high:
    if x[high] & 1 == 0:                # bitwise parity
      x[low],x[high] = x[high], x[low]  # switch
      evens_then_odds(x,low+1,high)     # move bottom up one, recurse
    else:
      evens_then_odds(x,low,high-1)     # move end down one, recurse

# Reverse a list recursively.

def reverse(X,first,last):
  if first < last:
    X[first],X[last] = X[last], X[first]
    reverse(X,first+1,last-1)
  return X

X = [4,3,6,2,8,9,5]
print(reverse(X,0,len(X)-1))

def power(x,n):
  if n == 0:
    return 1
  else:
    y = power(x,n>>1)
    z = y*y
    if n&1 == 1:
      z = z*x
    return z

power(2,6)
'''
Algo uses fact that when n is even, x^n = (x^n/2)^2 and when n is odd, 
x^n = x*(x^(n-1)/2)^2
'''

