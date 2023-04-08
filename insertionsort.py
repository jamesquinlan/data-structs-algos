# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Insertion Sort - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
# Insertion Sort
Given a list of numbers $a_1, a_2, \dots, a_n$, __insertion sort__ returns $a_1', a_2', \dots, a_n'$ such that $a_1' \le a_2' \le \dots \le a_n'$.

Insertion sort is efficient for small $n$, however, overall time-complexity is $O(n^2)$.  

---
'''

# Insertion Sort
# ---------------
# Input: unordered sequence (list) of numbers
# Output: Ordered list
# ---------------

list = [5, 6, 9, 2, 1, 8, 4, 3]

for i in range(1,len(list)):
  j = i - 1
  key = list[i]
  while j > -1 and list[j] > key:
    list[j+1] = list[j]
    list[j] = key
    j = j - 1
  print(list)

  # NOTES: j > -1 is more efficient than j >= 0 as this requires 1 more comparison, 
  # that is (j>0) or (j=0).

