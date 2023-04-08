# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Chapter 1 - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


### Legend
R = Reinforcement

C = Creativity

P = Project
"""

# R-1.1 

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function, ismultiple(m,n) that takes two integer values and returns 
# True if m is a multiple of n, and False otherwise
# ----------------------------------------------------------------------------

def ismultiple(m,n):
  if m > n:
    if m % n == 0:
      return True
    else:
      return False
  else:
    return False

ismultiple(50,7)

# Note: check if m and n are integers

# R-1.2

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write iseven(k) that takes an integer value and returns True if k is even,
# False otherwise.   
# ----------------------------------------------------------------------------

def iseven(k):
  if type(k)==int:
    if k % 2 == 0:
      return True
    else:
      return False
  else:
    print('Input must be integer')


iseven(44)

# R-1.2 (Added restrictions)

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write is_even(k) that takes an integer value and returns True if k is even,
# False otherwise without using multiplication, modulo, or division.
# ----------------------------------------------------------------------------

def is_even(k):
  if type(k)==int:
    while k >= 2:
      k -= 2   # k = k - 2
  else:
    print('Input must be integer')
  
  if k == 0:
    return True
  else:
    return False

is_even(21.32)

# R-1.3

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function, minmax(data), that takes a sequence of one or more numbers
# and returns the smallest and largest numbers in the form of a tuple of length
# two.  Do not use the built-in functions min or max in the implementation.
# ----------------------------------------------------------------------------

# Function definition
def minmax(data):
  m = data[0]  # Min
  M = data[0]  # Max
  for item in data:
    if item < m:
      m = item
    if item > M:
      M = item
  return (m,M)

# Main program
data = [8, 2, 4, 9, 1, -5]
minmax(data)

# R-1.4

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes a positive integer n and returns the sum of 
# squares of all positive integers less than n.
# ----------------------------------------------------------------------------
# NOTE if n = 1, directions are incomplete.

def ss(n):
  s = 0
  if type(n)==int and  n > 0:
    for i in range(n):
      s += i*i
  return s


ss(5)
# 5 --> 1 + 4 + 9 + 16 = 30

# R-1.5

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a compreshension using built-in sum that results in the sum of 
# squares of all positive integers less than n.  
# ----------------------------------------------------------------------------

n = 5
sum([(k*k) for k in range(1,n)])

# R-1.6

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes a positive integer n and returns the sum of 
# squares of all _odd_ positive integers less than n.  
# ----------------------------------------------------------------------------

def sso(n):
  s = 0
  if type(n)==int and  n > 0:
    for i in range(1,n,2):
      s += i*i
  return s


sso(7)

# R-1.7

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Give a single command that returns the sum of  squares of all _odd_ positive
# integers less than n.  Use list compreshension and built-in SUM command.   
# ----------------------------------------------------------------------------

n=6
sum([i*i for i in range(1,n,2)])

# R-1.8 

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Python allows negative integers to be used as indices into a sequence.
# If string S has length n, and expression S[k] is used for index -n =< k <= 0.
# What is the equivalent index j >= 0 such that S[j] == S[k]   
# ----------------------------------------------------------------------------

# Test
S = [1, 2, 3, 4, 5, 6]
n = len(S)

k = 2
j = n - k
S[-k]
S[-k] == S[n - k]

# Answer:
j = n - k

# R-1.9

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# What parameters should be sent to the range constructor to produce a range
# with values 50, 60, 70, 80.
# ----------------------------------------------------------------------------

[i for i in range(50,81,10)]
# Note: 81 could also be 82 or 90.  That is, anything less than 91.

# R-1.10

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# What parameters should be sent to the range constructor to produce a range
# with values 8, 6, 4, 2, 0, -2, -4, -6, -8.
# ----------------------------------------------------------------------------

[i for i in range(8,-9,-2)]

# R-1.11

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Use list comprehension to produce the list [1,2,4,8,16,32,64,128,256]
# ----------------------------------------------------------------------------

[2**k for k in range(9)]

# R-1.12

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Python's random module includes a function choice(data) that returns a
# random element from a non-empty sequence.  The random module includes a more 
# basic function randrange, with parameterization similar to the built-in
# function, that return a random choice from the given range.  Using only the
# randrange function, implement your own version of the choice function.
# ----------------------------------------------------------------------------

from random import randrange

def randchoice(data):
  return data[randrange(len(data))]

data = [1,4,3,6,2,9,8,7]
print(randchoice(data))

"""----"""

# C-1.13

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that reverses a list of n integers.
# ----------------------------------------------------------------------------

data = [1,4,3,6,2,9,8,7]

def reverso(data):
  atad=[0*i for i in range(len(data))] # atad=[] produced index error
  for i in range(len(data)):
    atad[i] = data[len(data)-1-i]
  return atad

reverso(data)

# Note: Assuming list is integers and do not verify.

# C-1.14

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes a sequences of integer values and determines if
# there is a distinct pair of numbers in the sequence whose product is odd.
# ----------------------------------------------------------------------------

def oddpair(data):
  for i in range(len(data)-1):
    for j in range(i+1,len(data)):
      if data[i]*data[j] % 2 == 1:
        return True

data = [2,4,3,6,7,10,8,12]
if oddpair(data):
  print('True')
else:
  print('False')


# Alternative approach - determine if there are two odd numbers
def oddpair2(data):
  count = 0
  for i in range(len(data)):
    if data[i] % 2 == 1:
      count += 1
      if count == 2:
        return True

if oddpair2(data):
  print('True')
else:
  print('False')

# C-1.15

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes a sequences of integer values and determines if
# the numbers are distinct.
# ----------------------------------------------------------------------------

def isdistinct(data):
  n = len(data)
  for i in range(n-1):
    for j in range(i+1,n):
      if data[i]==data[j]:
        return False
  return True
  

data = [1,4,3,5,2,9,8,2]
isdistinct(data)

# C-1.16

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------

# C-1.17

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------

# C-1.18 XXXXXXXXXX

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Use list comprehension to produce the list [0,2,6,12,20,30,42,56,72,90].
# That is, start at 0, +2, +4, +6, +8, +10, +12, +14, +16, +18
# ----------------------------------------------------------------------------

[k*(k+1) for k in range(10)]

# C-1.19

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Use list comprehension to produce ['a', 'b', 'c', ..., 'z']
# ----------------------------------------------------------------------------

# Hint: 'a' = chr(97)
letters = [chr(k) for k in range(97,97+26)]
print(letters,end = ' ')

# alternative
x = ''
for i in range(97,97+26):
  x = x + chr(i)

print(x)

# C-1.20

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# The random module include the function shuffle(data) that accepts a list
# and randomly reorders the elements so each possible order occurs with equal
# probability.  The random module includes a more basic function randint(a,b)
# that returns a uniformly random integer from a to b (inclusive).  Using only
# the randint function, implement a version of the shuffle function
# ----------------------------------------------------------------------------

import random as rnd

data = [1, 2, 3, 4, 5, 6, 7, 8]

# r.shuffle(data)         # In-place shuffle
# print(data)

n = len(data)

shuffled=[]
for i in range(n):
  m = len(data)
  r = rnd.randint(0,m-1)
  shuffled.append(data[r])
  data.pop(r)

print(shuffled)

# C-1.21 xxxxxxxxxxxxxxxx

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Repeatedly read lines from standard input until an EOFError is raised.
# Output those lines in reverse order.  User and indicated end of input using
# ctrl-D
# ----------------------------------------------------------------------------

lines = []
while not EOFError:
  x = input('Enter a line: ')
  lines.append(x)

# C-1.22

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes two integer vectors of length n and returns the
# Hadamard (element-wise) product.  NOTE: Error in book, NOT the dot product.  
# ----------------------------------------------------------------------------

def hadamard(x,y):
  z = x
  for i in range(len(x)):
    z[i] = x[i]*y[i]
  return z

x = [3,2,8]
y = [4, 5, 2]
print(hadamard(x,y))

# C-1.23

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Give an example of code that attempts to write an element to a list based 
# on an index that is out of bounds.  Catch the error (exception) and print 
# "Don't try buffer overflow attachs in Python"
# ----------------------------------------------------------------------------

# C-1.24

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that counts the number of vowels in a character string.
# ----------------------------------------------------------------------------

def vowelcount(data):
  count = 0
  for i in range(len(data)):
    if data[i] in ['a','e','i','o','u']:
      count += 1
  return count

data = 'This is a string'
print(vowelcount(data))

# C-1.25

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes a string representing a sentence and returns 
# a copy of the string with all punctuation removed.  For example, given 
# "Let's try, Mike." will return "Lets try Mike".
# ----------------------------------------------------------------------------

punks = {"'",".",","}

sentence = "Let's try, Mike."
result = ''
for c in sentence:
  if c not in punks:
    result = result + c

print(result)

# C-1.26

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write a function that takes three integers, a, b, and c from console and
# determines if they can be used in a correct arithmetic formula, like 
# a+b=c, a=b-c, a*b=c
# ----------------------------------------------------------------------------

a = 1
b = 2
c = 3

if a+b==c:
  print('True')

if a==b-c:
  print('True')

if a*b==c:
  print('True')

def factors(n):
  k = 1
  while k*k < n:
    if n % k == 0:
      yield k
      yield n //k
    k += 1
  if k*k == n:
    yield k

# C-1.27

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Implement a generator that reports factors (see Page 41) in increasing order.
# However, keeps the general performace advantages.
# ----------------------------------------------------------------------------

def factors(n): # generator that computes factors
  k = 1 
  while k*k < n: # while k < sqrt(n)
    if n % k == 0: 
      yield k
      yield n // k 
    k += 1 
  if k*k == n: # special case if n is perfect square
    yield k

# Test Original
print(list(factors(100)))

def factors(n):
  k = 1
  upperfactors = []
  while k*k < n:
    if n % k == 0:
      yield k
      x = n//k
      upperfactors.append(x)
    k += 1
  for i in range(len(upperfactors)-1,0,-1):
    yield upperfactors[i]
  if k*k == n:
    yield k*k
print(list(factors(100)))

# C-1.28

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# The p-norm of a vector v=(v1,v2,...,vn) in n-dimensinoal space is defined as
# \[
#     ||v||_p = (v1^p + ... + vn^p)^{1/p}
# \]
# Write a function called, norm(v,p) that returns the p-norm.  Make default=2.
# ----------------------------------------------------------------------------

def norm(v,p=2):
  x = sum([pow(i,p) for i in v])
  return pow(x,1/p)

v = (1,2,3)
norm(v,5)

# P-1.29

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------

words = ['c','a','t','d','o', 'g']
n = len(words)
for i1 in range(n):
  for i2 in range(i1+1,n):
    for i3 in range(i2+1,n):
      for i4 in range(i3+1,n):
        for i5 in range(i4+1,n):
          for i6 in range(i5+1,n):
            print(i1,i2,i3,i4,i5,i6)
            print(words[i1]+words[i2]+words[i3]+words[i4]+words[i5]+words[i6])


#import random


# list.remove(element)
#A = {1,2,3,4,5,6}
#i = random.randint(1,len(A))
#print(i)
#B = {i}
#A = A - B
#print(A)

# P-1.30

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write code that takes a positive integer greater than 2 as input and write
# out the number of times one must repeatedly divide this number by 2 before 
# getting a value less than 2.  For example, 15 -> 7.5 -> 3.75 -> 1.875 -> 0.9
# ----------------------------------------------------------------------------

def repeatdivby2(n):
  count = 0
  while n >= 2:
    n = n/2
    count += 1
  return count

print(repeatdivby2(100))

1.875/2

# P-1.31

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write code that can make change by taking two numbers, the amount of purchase
# and the amount given.  Return the number of each bill and coin.  Also, 
# return the minimal amount of bills and coins (i.e., a nickel instead of 5
# pennies).
# ----------------------------------------------------------------------------

# P-1.32

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------

# P-1.33

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------

# P-1.34

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# Write code that produces the sentence "I will never spam my friends again.", 
# 100 times with eigth different random-looking typos.  Number the sentences.
# ----------------------------------------------------------------------------

import random

sentences = [
              "I will never spam my friends again.",
              "I well never spam my friends agian."
            ]

x = random.randint(0,1)
print(x,sentences[x])

# P-1.35 (Birthday Paradox)

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# The birthday paradox says P(two people in a room have same birthday) = 50%
# for n = 23.  Write a program to test this by a series of experiements on
# randomly generated birthdays, for n = 5, 10, 15, 20, ..., 100.
# ----------------------------------------------------------------------------

import random

n = 23
match = 0
for s in range(101):  # do 100 times
  people = []
  for i in range(n):
    month = 100*random.randint(1,12)
    day = random.randint(1,30)
    birthday = month + day
    # print(birthday)
    if birthday in people:
        match += 1
        break
    people.append(birthday)
print(match)


'''  
for n in range(50,51):
  birthday=[]
  for i in range(n):
    birthday.append(random.randint(1,365))
    print(birthday[i])
'''

x = [1,2,3]
5 in x

# P-1.36

# DSC-270
# Fall 2021
# Quinlan, J
# ----------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------

# note: Use raw_input (Use input in Python 3.x). Pressing Ctrl+D will cause EOFError exception.
while True:
    try:
        input('Enter something: ') 
    except EOFError:
        break

print('done')

