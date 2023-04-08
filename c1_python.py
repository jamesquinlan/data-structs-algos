# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Intro. Python - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Chapter 1 - Python Primer

### Learning Objectives
* Overview of Python (version #, IDE, developed by)
* Basic Data Structures
* Expressions, Operators, Precedence
* Flow Control
* Functions
* I/O
* Exceptions
* Iterators and Generators
* Conveniences (i.e., compreshensions)
* Scopes and Namespaces
* Modules and Import Statement

----

## 1.1 Python Overview

* developed by van Rossum in the early 1990s
* latest version freely available at www.python.org, along with documentation & tutorials
* Python is formally an interpreted language (as opposed to C++)
* source code stored in a file named with the `.py`
* Interactive Python Notebooks, `.ipynb` (e.g., Jupyter, Colab) 
* Integrated Developing Environments (IDE) e.g., VS Code, PyCharm, etc.
* 2nd most used language
* Python ~ 1990, Python 2 ~ 2000, Python 3 ~ 2010
* Use Python 3 (unless you been coding in Python 20 years ago)
* Python uses "duck typing" or "dynamic typing"
* Python depends on whitespace to identify control structures
* Python is an Objected-oriented programming language
  - _Classes_ are the basis of all objects

### Comments
* Single-line comments begin with the hashtag (#)
* Multi-line (or block) comments begin, and end, with three single quotation marks, '''
* NOTE: Code should speak for itself and not need tons of explanations.
* Good Practice is to clean comments (and code)
"""

# This is a comment in python.  It will be ignored by the interpreter.

"""### 1.2.1 - Identifiers, Objects, and the Assignment Statement

* The equals sign, `=`, is an **assignment statement**
  - in R ```<-```
* An **identifier** (or variable, name) sits on the left-hand side of assignment.  
  - Python IS case-sensitive
  - alpha-numeric and underscores, but cannont begin with a digit
    - ```nine_lives``` but not ```9lives```
  - Cannot be one of the reserved keywords: `False,
as,
continue, else, form, in not return, yield, None, assert, def, except, global, is, or, try, True, break, del, finally, if, lambda, pass, while, and, class, elif, for, import, nonlocal, raise, with`

* Variable naming styles: (1) camelCase and snake_case

* The **object** (or value) of the assignment is on the right-hand side of assignment (`=`)

"""

# Assignment statement (name = temperature, value = 98.6)
temperature = 98.6

x = 98.6 # body temperature
body_temperature = 98.6

# Alias
a = 7
b = a   # same memory location as a
c = 7   # quincedentlly same value as a, but different memory location

"""## 1.2.2 - Creating and using objects
* instantiation = process of creating an instance new object
    - by invoking constructor (method)
    - x = Widget(a,b,c)
    - y = Fidget()
    - z = Account(name,balance)

#### Methods (or member functions)
* Function that belongs to a class
* Call method (other than constructor) using .dot notation.
  - data.sort()
  - data.sort('desc')
* Accessor method (or "get") = access the value (or "get" the value)
  - get the state
* Mutator methods (or "set") = "set" the value, i.e., change the state

## 1.2.3 - Built-in Classes

## INT and FLOAT

Integers and floating point numbers are primitive numeric types in python.  Python, unlike C++, automatically chooses the internal representation (based on the length).  `int()` returns `0` by default.

In other languages floats come in different sizes and varieties.  In particular, single (32-bits) or double (64-bits) precision.  Now-a-days there is even half-precision (16-bits) also called `bfloat16`.   

**NOTE**: It is important to use the decimal to defined a float when computing.  For example:
"""

x = 2.
y = 3
type(x)  # type of object?
# type(x/y)



2./3.

int()               # 0   
x = 17              
type(x)

float()             # 0.0
pi = float(3.14159265)   

# You do not need to use the constructor
pi = 3.14159265

x = 5
type(x)

id(x) # unique ID assigned to identifier x

"""## bool (Boolean)
* `True` and `False`

"""

x = True
y = False

"""## Str (Strings)
* 'hello'
* "hello"
* Beware of punctations, apostrophes
"""

"Joe's"

'3/2'  # how to put a backslash in a string

"""## List = array
An zero-indexed array-based sequence of objects delimited by square brackets [ ]
"""

# Lists
empty = []                         # Empty
colors = ['red','blue','green']    # Primary colors
primes = [2,3,5,7,11,13]           # First 6 prime numbers

"""## Tuple
A immutable sequence delimited by ().  Note: a singleton must contain a comma after the element.  
"""

# Some tuples
(5,)              # one-element tuple
(2,3)             # ordered pair
(3,2)             # different ordered pair
(1,2,3)           # three-element tuple
(9,3,12,8,0,4)    # six-element tuple

"""## Dictionary
`dict` class represents a **dictionary** (i.e., key/value pairs).  
  * Delimited with curly brackets { }
  * Contains key:value

It can also be thought of as a **mapping** from a set of keys to a set of values.  For example, English-Spanish dictionary.  
 
"""

# A dictionary
dictionary = {'key1':'value1','key2':'value2'}
D = {'Hello':'Hola', 'Cat':'Gato', 'Dog':'Perro'}
D['Hello']

"""## Sets
The **set** class is an unordered collection of elements, without duplicates.  Sets are equivalent to the mathematical meaning of set and use the same notation as well.   
"""

# Sets
empty_set = set()   # to get an empty set
empty = {}          # not an empty set, but empty dictionary
example_of_set = {3, 5, 7, 11, 13}



"""## 1.3 - Expressions, Operators, and Precedence

#### Logical Operators
* ```not, and, or```
* Short-circuit

#### Equality Operators
* ```is, is not, ==, !=```
* ```is``` determines if two objects are aliases 
* ```==``` evaluates `True` if different objects have same value

#### Comparison Operators
* Compare order of same type (at least numeric, string, etc)
* ```<, <=, >, >=```
* ```5 > 'hello'``` are incompatable data types

#### Arithmetic Operators
* ```+, -, *, /, //, %```
* ```//``` is integer division
* ```%``` is modulo operator (e.g., ```5 % 2```)
* Take caution with ```//``` and `%` with negative numbers.  

### Exercises:
1. Find `27 // 4`
2. Find `-27 // 4`
3. Find `99 % 7` 

#### Bitwise Operators
* ```~``` complement
* ```&``` and
* ```|``` or
* ```^``` xor   # not exponetial 
* ```<<``` shift left, zero fill
* ```>>``` shift right, sign fill

#### Sequence Operators
* ```x[i]``` get i-th element of list x
* ```x[start:stop]``` slice include [start,stop) (exclude stop)
* ```x[start:stop:step]``` 
* ```x+y``` concat sequences
* ```k*x``` shorthand ```x + x +...+x```, x k times
* ```val in x``` containment check
* ```val not in x```
* Negative indices supported.  
  - ```x[-1]``` is last element, ```x[-2]``` second to last, etc.
* Comparisons on sequence are based on __lexicographic order__
  - ```[5,6,9] < [5,7]```
* ```x == y``` equivalent element by element
* ```x < y``` lexicographically less than, similar for, ```>, >=,<=, !=```

#### Set (and dictionary) Operators
Sets are unordered.

* Comparison operators define partial order, not total order.  For instance, 
```{1, 2, 3} < {4,5,6}``` is `False`.  This asks if X is a subset of Y.
* ```<``` proper subset
* ```<=``` subset
* ```A | B``` Union
* ```A & B``` Intersection
* ```A - B``` Set difference
* ```A ^ B``` 
* ```A == B``` equivalent sets
"""

a = 5
b = 5.
a == b

-15 % 7

"""# 1.4 - Flow Control

## 1.4.1 IF-THEN-ELSE Statements

Conditional constructs (also known as **if** statements) execute a chosen block of code based on the run-time evaluation of one or more Boolean expressions.

General syntax is:
```python
if condition1: 
  block1
elif condition2: 
  block2
elif condition3: 
  block3
else:
  block4
```
"""

x = 2
y = 1
if x < y:
  print(x)
elif y < x:
  print('y<x')

"""## 1.4.2 - Loops

Python offers **while** loops and **for** loops.  

* `while` loops are mostly appropriate when there is an unknown number of items.  The general syntax is:

```python
while condition:
    code_block
```

* `for` loops are used to iterate over values in a list or a given range.  The general syntax is:

```python
for value in data:
    code_block
```
"""

data = [4, 1, 3, 9]
for i in data:
  print(i)

data = [5, 1, 2, 3, 9, 6, 8, 7, 11, 29]
for i in range(10):
  print(data[i])

X = ['c','a','t','d','o','g']

"""# 1.5 - Functions

* Built-in (`print`, `sort`, )
* User-defined
"""

def name_of_function(parameter_list):
  # y = f(x)
  # code block
  # body that "computes" a value

  # return value as needed
  return value

def myprint(x):
  print(x)

x = 5
myprint(x)

# R-1.1
'''
Write function is_multiple(m,n) that determines if m = kn for some k in Z.
Is m a multiple of n?  For example, 15 is a multiple of 3.  
'''

def is_multiple(m,n):
  # make sure m and n are integers
  # use if statement to verify
  if m % n == 0:
    return True
  else: 
    return False


# Main program
is_multiple(155,1)

"""# 1.8 - Iterators and Generators

### Iterators

> An __iterator__ is an object that manages iteration through a series of values.  An __iterable__ is an object that produces iterators, e.g., range(10).

* Used in ```for``` loops.
* A _list_ is an iterable.
* Possible to produce multiple iterators based on same iterable object.
* Implicit iterable series of values such as ```range()``` use __lazy evaluation__.  That is, ```range(10)``` does NOT produce a list stored in memory, but instead returns a value as needed.  The advantage is that there is no need to _compute_ and _store_ big lists.  
* Lazy evaluation is akin to a SQL View.  



### Generators

> __Generators__ are implemented with similar syntax to a function, but instead of returning values, a __yield__ statement is used to indicate the value in a series.  

* Convenient method to create interators.
* Results are only computed if requested (i.e., lazy evaluation)
"""



"""# 1.9  - Python Conveniences

> Syntax features in python for writing clean, concise code.  

### 1.9.1 - Conditional Expressions

```{python}
expression_1 if condition else expression_2
```
"""

n = 6
print('Odd') if n % 2 == 1 else print('Even')

"""### 1.9.2 - Compreshensions

#### List Comprehension
```{python}
[expression for value in iterable if condition]
```
"""

# Example
[x for x in range(10) if x < 5]

# Example - First 5 squares
[k*k for k in range(1,6)]

[x if x != 7 else 5  for x in range(10)]

# Example - Factors of n
n = 100
[k for k in range(1,n+1) if n % k == 0]

# Using list comprehension to iterate through loop
List = [character for character in 'List comprehensions are great!']
 
# Displaying list
print(List)

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)

[i+j for i in range(5) for j in range(3)]

# Explicit function
def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)

Sums = [x+y for x in [1,2,3] for y in [10,20,30]]
print(Sums)

"""#### Other Compreshension

Similar comprehensions exist for _sets_, _dictionaries_, and _generators_.  See examples below.

"""

# Set comprehension
{k*k for k in range(1,6)}

# Dictionary comprehension
{k : k*k for k in range(1,6)}

# Generator Comprehension (uses parenthesis)
S = (k*k for k in range(1,6))

# NOTE: result not stored in memory, but generator object
# This can be used as needed, for instance to calculate the
# sum of squares.  
# This is preferred to storing entire list.  
sum(S)

"""### 1.9.3 - Packing and unpacking sequences

* A series of comma-separted expressions are treated as a single tuple.
* Automatic packing of a tuple
"""

data = 1,2,3,4
print(data)

"""* Packing can be used when returning multiple values from a function.
```{python}
return x,y
```
Returns (x,y) as a single tuple object.

__Unpack__ a sequence allows assigning a series to individual elements.
* Right-hand side can be any _iterable_.
"""

# Example
a,b,c,d = range(1,5)
print(a,b,c,d)

# Example
quotient, remainder = divmod(100,23)
print(quotient, ",",remainder)

"""* Also used in ```for``` loops, such as:"""

# Two iterations of the loop.  First assigns x = 1 and y = 2.  
# The second will assign x = 3 and y = 4.  
for x,y in [(1,2), (3,4)]:
  print(x,y)

"""### Simultaneous Assignments

> _Simultaneous assignment__ combines packing and unpacking, where a series of identifiers are assigned a series of values.  

* Expressions on RHS are evaluated first before assignments are made to left-hand side.  
"""

# Example of simultaneous assignment
a,b,c = 1,2,3
print(a,b,c)

# The RHS is automatically PACKED into a tuple, then
# UNPACKED during the assignment to the values on LHS.

"""### SWAPPING
* Swapping values in commonly required in an algorithm.  The common technique is to establish a third variable to temporarily hold a value, assign the second to the first, then the first to the temporary value.  For instance,  

"""

x = 1
y = 2
print(x,y)

# Goal, SWAP the two values, make x = 2 and y = 1.
temp = y
y = x
x = temp

print(x,y)

"""* Pythons _simultaneous assignments_ provides a convenient way to accomplish the same goal."""

# Set up
x = 1
y = 2
print(x,y)    # list original values

# SWAP
x,y = y,x
print(x,y)    # list new values

"""# 1.10 - Scopes and Namespaces
* To use identifiers in calculations, they must be previously associated with objects, a `NameError` will be raised if not.  
* This process of determining the value associated with an identifier is called __name resolution__.  
* Variables assigned within a function have __local__ scope and the main program will be unaware of it.
* There are several "scopes".  
* __Global__ variables, (i.e., top-level assignments) can be used anywhere in the program and have "global scope".  
"""

# Local scope of a variable

def myfunction(n): 
  local_variable = 2*n
  return n+1

# Main program
n = 5
print(myfunction(n))   # Note this value is returned and printed
print(local_variable)  # NameError: name 'localvariable' is not defined
# local_variable is out of scope of the main program.

"""### Namespaces

* Each distinct scope is known as a __namespace__.  
* A __namespace__ manages all variables currently defined in a given scope.  
"""

