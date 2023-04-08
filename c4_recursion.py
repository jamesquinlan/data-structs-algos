# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Recursion Examples - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def hello(n):
  if n <= 0:
    return 
  else:
    print("Hello")
    hello(n-1)

hello(10)

# Adding
n = 10
s = 0
for i in range(n+1):
  s += i
print(s)

# Recursive add

def addit(n):
  if n == 0:
    return 0
  else:
    return n + addit(n-1)

n = 10
addit(10)

# Binary searach

def bsearch(data,target, low, high):
  if low > high:
    return None
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return mid
    elif target < data[mid]:
      return bsearch(data, target, low, mid - 1)
    else:
      return bsearch(data, target, mid + 1, high)


# Driver
data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
idx = bsearch(data, 22, 0, len(data)-1)
print(idx, data[idx])

# Iterative Binary Search

def itbinsearch(data, target):
  # Set up
  start = 0
  end = len(data)-1
  mid = (start + end) // 2

  # Search
  while (start <= end) and (data[mid] != target):
    if (target < data[mid]):
      end = mid - 1
    else:
      start = mid + 1
    mid = (start + end) // 2
  
  # Return Results
  if data[mid]==target:
    return mid
  else:
    return -1


# Driver code
data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
idx = itbinsearch(data, 29)
print(idx)

def pow2(n):
  if n == 0:
    return 1
  else:
    return 2*pow2(n-1)


# Driver
print(pow2(5))

# kth even number

def even(k):
  if k < 1:
    return 0
  elif k == 1:
    return 2
  else:
    return even(k-1) + 2

# Driver
even(5)

def merge(x,y):
  z = [0]*(len(x)+len(y))
  i = 0
  left = 0
  right = 0
  print(left, i, right)
  while left < len(x) and right < len(y):
    
    if x[left] <= y[right]:
      z[i] = x[left]
      left += 1
    else:
      z[i] = y[right]
      right += 1
    i += 1
    
    # If no elements left in one sub-list
    if left == len(x):
      z[i] = y[right]
    elif right == len(y):
      z[i] = x[left]
    print(left, i, right)
  return z



x = [1, 2, 8, 11, 19]
y = [2, 3, 5, 7, 9]
print(merge(x,y))