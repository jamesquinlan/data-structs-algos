# Fri Aug 26 12:45:52 EDT 2021
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Intro. OOP - Data Structures and Algorithms
#            		:  Quinlan, J 
#            		:  University of New England
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Object-Oriented Programming

## 2.1 Goals, Principles, and Patterns




### 2.1.2 Objected-Oriented Design Principles

* Modularity
* Abstraction
* Encapsulation

---

#### Modularity

> __Modularity__ is an organizational principle in which different components are divided into separte functional units.  It provides clarity of thought and clarity to implementation.  



* Modern software has interactive componenets.  These components need to be well organized to work properly.  

* This principle is the organizational framework of python libraries, called __modules__ (e.g., ```math, numpy, os```).  

* Modularity supports the design goals: _robustness_, _adaptability_, and _reusability_.

* Aid in debugging as an error may be traced to a component and therefore isolated during the fix.  

* Modules lead to reusability as components may be used in different contexts. 

---

#### Abstraction

> The notion of __abstraction__ is to distill a complicated system down to its most fundamental parts.   

* The application of the abstraction to the design of data structures gives rise to __abstract data types__ (ADTs).  A mathematical model that specifies they data type, the operations, and the parameters of the operations.  
* Abstraction provides __what__ is done, but not __how__.  
* The collective set of behaviors supported by an ADT is its __public interface__.
* Python uses __duck typing__, and dynamically identifies the type during the code interpretation.  ``If if walks like a duck, quacks like a duck, then it is a duck".
* __Abstract Base Class__ (ABC) is a (python) mechanism to support ADT, by identifying common methods that all ADT must have.  ABC cannot be instaniated, but realized by concrete classes that inherit from ABC.  

---


#### Encapsulation

> __Encapsulation__ is an object-oriented design principle that hides internal details of the code (blackbox).  

* Easier bug fixes
* Yields robustness and adaptibility
* Python only losely supports encapsulation
* NOTE: nonpublic data members and member functions (properties and methods) by convention start with a single underscore character (e.g., _secret).  

---

### 2.1.3 Design Patterns

> __Design pattern__ describes a general tempate for a software solution.

A pattern involves:
* a name - identifier
* a context - describing the scenarios for which the pattern can be applied
* a template - describing how the pattern is applied
* a result - descirbe and analyze the product

##### Algorithm design patterns:
* Recursion
* Divide-and-conquer
* Prune-and-search
* Brute force
* Dynamic programming
* Greedy methods

##### Software design patterns:
* Iteration
* Adapter
* Position
* Composition
* Template
* Locator
* Factory

## 2.2 Software Development

Software development involves a sequence of steps:

1. Design
2. Implementation
3. Testing and Debugging

### 2.2.1 Design

> The __design__ step includes deciding on classes, how the classes interact, what data each class will store, and what actions each class will perform.
"""



"""# 2.3 - Class Definitions

### Self Indentifier
The self identifier plays a key role.  
* Self identifies the instance upon whic a method is invoked.

### Constructor
The `__init__` method signifies the __constructor__ method.  
* It establishes a new class object with default instance variables.  
* Note the namespace of the state variables.  If not fully qualified, (i.e. unqualified), it references the local namespace variable.  
* Contains the __state__ or __instance__ variables.  
* Member functions are provided after the constructor method. 
"""

x=5
class(x)

class CreditCard:
  """
  Credit card class
  """

  def __init__(self, customer, bank, acct, limit):
    """Constructor
        customer = name of customer
        bank = Name of bank
        acct = account number (str)
        limit = credit limit (float.2)
    """
    self._customer = customer
    self._bank = bank
    self._account = acct
    self._limit = limit
    self._balance = 0       # default new credit card instance
  
  def get_customer(self):
    return self._customer

  def get_bank(self):
    return self._bank
  
  def get_account(self):
    return self._account

  def get_limit(self):
    return self._limit

  def get_balance(self):
    return self._balance

  def charge(self, cost):
    if cost + self._balance > self._limit:
      return False
    else:
      self._balance += cost
      return True
  
  def make_payment(self, pay):
    self._balance -= pay

# Test CreditCard Class.  
cc1 = CreditCard('Joe','BOA','123',5000.00)
cc1.charge(109.00)
cc1.get_balance()
cc1.make_payment(50)
cc1.get_balance()

"""# 2.3.3 - Example: Multidimensional Vector Class
Vectors are important objects in science and mathematics. Vectors contain coordinates in a multidimensional space.  For example, in three-dimensions, the vector with coordinates (1,2,3).   

This example highlights:
* Class defintion, that encapsulates an (internal) list as its storage mechanism, but operates as a public interfaced coordinate vector.  
* Use of operator overloading via special methods
* Lists are ineffective to represent vectors because [1,2,3]+[4,5,6]  = [1,2,3,4,5,6], instead of [5,7,9].
* Implement a custom ```__add__``` overloaded method.  


"""

class Vector:
  """Represent a mathematical vector"""

  # CONSTRUCTOR METHOD
  def __init__(self,dim):
    """CONSTRUCTOR: Create a zero vector of dimension dim"""
    self._coords = [0]*dim

  # Member functions
  def __len__(self):
    return len(self._coords)

  def __getitem__(self,i):
    return self._coords[i]  # ith coordinate of vector

  def __setitem__(self,i,x):
    """Set the ith element to x"""

  def __add__(self, other):
    """Return elementwise sum of two vectors"""
    if len(self) != len(other):
      raise ValueError('Dimensions must agree')
    result = Vector(len(self))  # zero vector
    for i in range(len(self)):
      result[i] = self[i] + other[i]
    return result

  def __eq__(self, other):
    return self._coords == other._coords

  def __ne__(self, other):
    return not self == other

  def __str__(self):
    return '<'+str(self._coords)[1:-1]+'>'

# Test Vector Class
x = Vector(3)
print(x)

"""## 2.3.4 - Iterators
Iteration is important in the design of data structures.


"""

class SequenceIterator:
  """
  An iterator for any Python sequence type.
  """

  def __init__(self,sequence):
    self._k = -1
    self._seq = sequence

  def __next__(self):
    self._k += 1
    if self._k < len(self._seq):
      return(self._seq[self._k])
    else:
      raise StopIteration()

  def __iter__(self):
    return self  #iterators return itself as an iterator

class Range:
  """
  Mimic range() function but exclusive stop

  For example, Range(3) --> 0,1,2,3 and range(1,3) --> 1,2,3
  """

  def __init__(self, start, stop = None, step = 1):

    if step == 0:
      raise ValueError('Step cannont be 0')
    
    if stop is None:
      start, stop = 0, start
    
    self._length = max(0,(stop - start + step ) // step)

    self._start = start
    self._step = step

  
  def __len__(self):
    return self._length

  def __getitem__(self, k):
    if k < 0:
      k += len(self)

    if not 0 <= k < self._length:
      raise IndexError('Index out of range')

    return self._start + k*self._step

# Test Range
for i in Range(10):
  print(i)

"""# 2.4 - Inhertitance

## References

Deitel, P., & Deitel, H. (2020). *Intro to Python: For Computer Science and Data Science*. Pearson Education.



```bibtex
% BibTeX
@book{deitel2020intro,
  title={Intro to Python: For Computer Science and Data Science},
  author={Deitel, Paul and Deitel, Harvey},
  year={2020},
  publisher={Pearson Education}
}
```
"""

