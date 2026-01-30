# operators
```
//: This is the floor division operator in Python. 
It divides the number and rounds down to the nearest whole integer

ex: 5 // 2 = 2
```

# if exists
```
if key in d:
if x:
if not stack:  # same as java if(stack.isEmpty())
```

# ternary
```
age = 25
status = "Adult" if age >= 18 else "Minor"
```

# conversion
```
third = str(int(first) + int(second))
```

# str
```
s = ""
last_char = s[-1]
splice_excl_last_char = s[:-1]
s[a:b]    # b excluded
idx = ord(c) - ord('a') # Python string/char math: c - 'a' doesn’t work in Python (chars aren’t ints). 
```

# formatted strings
f strings
```
price = 5000000
print(f"price is {price:,}")
```
- str format with index & named index

# user prompt
user input is via input()

# math
```
max_val = max(a, b)
max_val = max(my_list)
longest_string = max(my_string_list, key=len)
map_largest_key = max(my_map)
map_largets_val = max(my_map, key=lambda k: map[k])
```

# loop styles

## range
range is a python in built class
```
range(n)  # [0, n)
range(0, n) # [0, n)
range (n - 1, -1, -1) # (n, 0]
...
for i in range(n):
for x in arr:
for i, x in enumerate(nums):
for key in map:
# Iterate with 'i' from 0-2 and 'j' from 10-12 in parallel
for i, j in zip(range(3), range(10, 13)):
    print(f"i: {i}, j: {j}")


...

[0] * 26 # works for primitive
[[] for _ in range(n)] -vs- [[]] * 26 # same list shared across all indices 
[{}] * 26 
[set()] * 26
```

# collections
Built-in: list, dict, set, tuple "immutable"
collections module (standard library): deque, Counter, defaultdict, OrderedDict (mostly historical now), namedtuple
itertools module (iterables - sorting, grouping, chaining): chain, product, groupby, islice
collections.abc (Typed/abstract interfaces): Iterable, Mapping, Sequence
built-in functions: sorted(), min(), max(), plus modules like itertools.

## arr
Python lists function as arrays - can store items of mixed types.
```
my_list = [10, 20, 30, 40, 50]
my_list.append(60) # Adds 60 to the end
my_list.insert(1, 15) # Inserts 15 at index 1
my_list.reverse()
my_list.append([60, 70]) vs my_list.extend([60, 70])
```

large arrays of a single, primitive data type (like integers or floats), the array module is more memory-efficient than a list.
``` Create an array of signed integers
import array as arr

my_array = arr.array('i', [1, 2, 3, 4, 5])
'i' for signed integer
'f' for float
'd' for double float
'u' for Unicode character
```

## numpy
The NumPy library is the standard for numerical operations in Python, offering powerful, multidimensional array objects (ndarray).

import numpy as np
``` Create a 2D array (matrix)
numpy_array_2d = np.array([[1, 2, 3], [4, 5, 6]])
```

## sort vs sorted
```
arr.sort()            # in-place
the_list.sort(key = lambda x: abs(x-50))

sorted(arr)           # new list
sorted(arr, key=lambda x: x[1])

fruits.sort(key = str.lower)
```
sorted works on more than lists
```
tuple = (4,3,2,1) 
sorted_tuple = sorted(tuple)
```

## list
```
stack = []
stack.append(ch)
stack.pop()
"".join(stack) # stack to str
```
## set
```
my_set.update(list_to_add)
my_set |= set(my_list)
my_set.add(elem)
```

## hashmap
```
map = {}
map["key"] = val
map.get(key, default_val)
```

defaultdict (avoids “if key not present” checks) # key not found error
```
from collections import defaultdict

d = defaultdict(int) # int is the default factory function that defaults new key's to 0 
d["a"] = 1
d["a"] += 1
```

## counter (fast frequency map in 1 line)
```
from collections import Counter
freq = Counter(arr) # freq is a map 
```
## heap
heapq # python's min-heap 
```
import heapq
heapq.heappush(h, x)
x = heapq.heappop(h)
```

## deque
```
from collections import deque

q = deque(i for i in range(n) if deg[i] == 1)
...
q = deque()
q.append(x)  # no push method
x = q.popleft()  # return oldest elem
q.pop() # return newest element 
...
sz = len(q)
list(q)
```

## comprehensions
```
[print(x) for x in the_list]
[x for x in employees if "su" in x]
[x if x == 'banana'  else x for x in fruits]
```

## Iterator
```
iter()
__iter__()
__next__()

StopIteration
```

# lambdas
```
lambda x, y : x+y
```

# generators
yield and execution is paused & state is saved
use next() to get the next value

# OOPS
dunder methods in python oops

self -> for providing behavior methods

@classmethod & cls -> for alternate constructors or factory patterns.

@staticmethod -> for helper/utility methods

class Child(Parent):
pass

super().__init__()  --> overide but call super implementation

## polymorphism
function poly like  len()
class poly like multiple classes with same method name
inheritance class poly

## variable scope
global
nonlocal --> nested functions

## closure
- nested functions & lambdas use closure mechanism
- the outer variables are called free variables
- Late Binding:
    - variables are not bound to the closure at the time of closure creation
    - They are bound when the closure is called
    - this includes primitives as well (hene closure captures variables by reference instead of value)
    - To capture by value (or effectively "snapshot" the value) "use a default argument in the inner function, as default arguments are evaluated when the function is"
  
    | Version           | Meaning                                            | Works with `f()`?               |
    | ----------------- | -------------------------------------------------- | --------------------------------|
    | `lambda x: x * 2` | Takes input `x`, returns `x * 2`                   | ❌ needs argument               |
    | `lambda: i`       | No arg, returns current `i` (late bound)           | ✅ but returns same `i` for all |
    | `lambda i=i: i`   | No arg, captures `i` at definition (default param) | ✅ and returns correct values   |

- resolution process is called lexical/static scoping

# decorators
use @ to decorate a method with the decorated method

# modules
- A Python module is simply a .py file. The file name (without the extension) is the module name

## package
- A Python package is a directory that contains multiple modules and potentially sub-packages
- __init__.py => file in a directory is optional

## How to use modules (import)
- **Importing:** You use the import keyword to bring a module's contents into your current file
```
import my_module
```
- **Selective Imports:** You can import specific items using from ... import ...
```
from my_module import function as alias
```

- **Hierarchical Import:** use dot notation
```
import myapp.utils.logic
Usage: myapp.utils.logic.my_func()

import myapp.utils.logic as log
Usage: log.my_func().

from myapp.utils import logic
Usage: logic.my_func()
```

## example: importing a class from a file
```
file: range_sum_mutable.py

class NumArray:

... And you’d import it like 

from range_sum_mutable import NumArray
```
## built-in modules
- datetime
- json
- math
- re (regex)
    * findall()
    * search()
    * returns a match object
    * sub()

## monkey patching
* If you do:
```
import math
...
You can re-assign things like math.sqrt = my_func in your file, and it only affects your local reference.
```

* But if you do:

```
from math import sqrt
...
That imported sqrt name won’t change even if later you modify math.sqrt.
```

# exceptions
* handle exceptions:

```
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
```

* raise Exception: 

```
if x < 0:
  raise Exception("Sorry, no numbers below zero")
```

# venv
a separate python env for each project
 - the built-in, lightweight solution
 - manual control over env creation:
   - python -m venv <env_name> 
   - source <env_name>/bin/activate.
 - Dependency management with requirements.txt
   - rely on pip to install packages
   - pip freeze > requirements.tx

**others:** pipenv, poetry

# pipenv
 - Combines virtual environment and package management
 - Automatic environment creation outside the project folder
 - Declarative dependency management with Pipfile and Pipfile.lock instead of requirements.txt
 - features:
   - streamlined package management instead of multiple commands create, source
     - pipenv run <command> vs  source  >> python my.py >> deactivate
   - pip install automatically updates pipfile & lock file
   - dev vs prod dependencies
     - pipenv install flask sqlalchemy
     - pipenv install pytest black mypy --dev
     - pipenv install --deploy # when deploying to prod
     - pipenv install --dev    # another dev setting up local env
     - Sample Pipfile
           [[source]]
           url = "https://pypi.org/simple"
           verify_ssl = true
           name = "pypi"
           [packages]
           flask = "*"
           sqlalchemy = "*"
             
           [dev-packages]
           pytest = "*"
           black = "*"
           mypy = "*"
    
           [requires]
           python_version = "3.11" # (Or your chosen Python version)
   - vulnerability scanning
     - pipenv check

# conventions
- A leading underscore (like _dfs) means: “internal/helper method, not part of the public API.”
- Common Python convention:
  * Module/file: descriptive, snake_case (what the module is about)
  * Class: PascalCase (the type it defines)

# concurrency, parallelism & async