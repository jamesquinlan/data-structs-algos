# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Chapter 5 - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
# Insertion Sort O(n^2)

x = [2, 5, 1, 7, 6, 9, 8, 3]

for k in range(1,len(x)):
  j = k
  cur = x[k]
  while j > 0 and x[j-1] > cur:
    x[j] = x[j-1]
    j = j - 1
  x[j] = cur

print(x)

# R-5.7
''' 
Let A be an array of size n >= 2 containing integers from 1 to n-1, inclusive, 
with exactly 1 repeat (by Pigenhole). Write an algorithm to find the repeated 
value.
'''
def f(x):
  found = [False]*len(x)
  for val in x:
    if found[val]:
      return val
    else:
      found[val] = True
      print(found)

x = [2, 5, 1, 4, 6, 5, 7, 3]
print(f(x))

# [2, 5, 1, 4, 6, 5, 7, 3]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0  1  1  0  1  1  1  0]
#

# R-5.11

x = [[1,2,3],[4,5,6],[7,8,9]]
print(x)

s = 0
for i in range(len(x)):                     
  for j in range(len(x[i])):
    s = s + x[i][j]

print(s)



# R-5.12 
'''
Show built-in `sum` function combined with comprehension to compute the sum of 
all numbers in an n x n data set, represented as a list of lists.
'''
x = [[1,2,3],[4,5,6],[7,8,9]]

sum(sum(subset) for subset in x)

for subset in x:
  print(sum(subset))

