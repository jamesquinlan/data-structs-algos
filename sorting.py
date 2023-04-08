# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Sorting - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# ------------------------------
# Selection Sort
# Simple, but inefficient
# O(n^2)

# 1st iteration selects smallest element & swaps with first element.
# 2nd iteration finds next smallest element & swaps with 2nd element.
# 0: [34, 56, 14, 20, 77, 51, 93, 30, 15, 52] 
# 1: [14, 56, 34, 20, 77, 51, 93, 30, 15, 52] 
# 2: [14, 15, 34, 20, 77, 51, 93, 30, 56, 52] 
# 3: [14, 15, 20, 34, 77, 51, 93, 30, 56, 52] 
# 4: [14, 15, 20, 30, 77, 51, 93, 34, 56, 52]
# ...
# -------------------------------

x = [34, 56, 14, 20, 77, 51, 93, 30, 15, 52]

for i in range(0,len(x)-1):
  idx = i
  for j in range(i+1,len(x)):
    if x[j] < x[idx]:
      idx = j
  x[idx],x[i] = x[i],x[idx]

print(x)

# Insertion Sort - Due for Homework
# Simple, but inefficient
# O(n^2)