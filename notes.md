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
if key in memo # safe for key's node present -vs- if memo[key]  # would KeyError

```

# if, elif, else
```python

if condition:
    
if condition:
elif condition:
else:
    
if condition:
else condition:

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
# bit
```
&  # bitwise and
>> # bitwise shift
```

# str
```
strings are immutable
s = ""
last_char = s[-1]
splice_excl_last_char = s[:-1]
s[a:b]    # b excluded
idx = ord(c) - ord('a') # Python string/char math: c - 'a' doesn’t work in Python (chars aren’t ints).

vowels = "aeiouAEIOU"
# python doesn't have chars
chars = list(s)
s = "".join(chars)
chars[i] not in vowels
len(s)

index() method raises a ValueError exception if the substring is not found 
find() method returns -1 if substring not found
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
pow(base, exp) # allows -ve exponent e.g., 2 ** 3 = 8 & 2 ** -3 == 0.125
pow(base, exp, mod)
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
for i, x in enumerate(nums):  # index and the value
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
Dict, List, Set -> from typing (mostly legacy now)
dict[int, int] -> modern, clean, recommended
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
The NumPy library is the standard for numerical operations in Python, offering powerful, multidimensional array  
objects (ndarray).

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
my_set= {}
my_set = {0} # add default val of zero
```

## dict
```
map = {}
map["key"] = val
map.get(key, default_val)

if key in map:  # check if key in map without raising KeyError
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
for tuple's heapq uses the natural tuple ordering: compare field 1, then field 2 if tied, then field 3, etc.

## deque
```
from collections import deque

q = deque(i for i in range(n) if deg[i] == 1)
...
q = deque()
q.append(x)  # no push method
x = q.popleft()  # return oldest elem
q.pop() # return newest element 
q = deque([0]) # add default val of zero
...
sz = len(q)
list(q)
```
## generators
* a lazily evaluated & memory efficient type of function or expression that produces a sequence of values one at a 
  time, only when requested
* unlike functions which returns results and terminate, a generator yields a value and can puase execution saving 
  it's state to pick up from where it left off

## comprehensions
* concise syntax for creating new sequences (lists, dictionaries, sets & generators) from existing iterables using 
  single line of code

### List Comprehensions
```
[print(x) for x in the_list]
[x for x in employees if "su" in x]
[x if x == 'banana'  else x for x in fruits]
```

## Set Comprehension
```python
{x ** 2 for x in range(5)}
```

# dict Comprehension
```python
{x : x **2 for x in range(3)}
```

### generator Comprehensions
```python
# Generator expressions don't use yield 
min(x ** 2 for x in range(5))
```
# generator functions
yield and execution is paused & state is saved
use next() to get the next value

```python
def get_cost(i, j):
    for k in range (i, j + 1):
        yield max(get_cost(i, k - 1), get_cost(k + 1, j)) + k

min(get_cost(i, j)) # use yield

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
sum = lambda x, y : x+y
sum(2, 3)

# filter df rows with lambda
filtered_df = df.filter(lambda row: row['name'].startswith('A'))
```

# OOPS
dunder methods in python oops

self -> for providing behavior methods
invoke behavior methods using self.method

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
* use @ to decorate a method with the decorated method

# dataclass
* special type of decorator for storing data with minimum boilerplate code
* mutable by default

# functools
```python
@functools.lru_cache(maxsize=128)
@functools.cache  # is same as @functools.lru_cache(None)
```

There are two ways to correctly apply the decorators:
1. Without parentheses (as a direct decorator):
@functools.cache
2. With parentheses (when passing arguments):
@functools.lru_cache

# modules
* A Python module is simply a .py file. The file name (without the extension) is the module name

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
## threading:
  * Pass a target function (preferred)
  * lambda
  * Subclass Thread and override run()
  * Use a callable object (__call__)
    * This combines the flexibility of the target approach with the statefulness of subclassing. The callable
      object holds state, but isn't coupled to Thread.
### Thread Lifecycle Management
* Calling start() tells Python to begin executing the thread's run() method in a new thread of control
* The join() method blocks the calling thread until the target thread terminates
* No interrupt() in Python, uses cooperative cancellation with threading primitives like Event

### Returning Results from Threads
* Shared Variables with Locks
* Queue-Based Communication
* Using concurrent.futures or executor.map (for simpler cases)
* Thread-Local Storage

### Exception Handling in Threads
* Exceptions in threads don't propagate to the parent thread. They must be handled within the thread
* For more sophisticated exception handling, use concurrent.futures
* Global Exception Handler: You can set a global exception handler for uncaught exceptions in threads

### Thread Synchronization Primitives
* Lock: provides mutual exclusion
* RLock: RLock (reentrant lock) allows the same thread to acquire the lock multiple times.
    * This is useful when a method that holds a lock calls another method that also needs the lock.
* Event: Event provides simple signaling between threads
    * One thread can wait for a signal, and another can set it.
* Condition: Condition allows threads to wait for arbitrary conditions to become true.
    * It combines a lock with the ability to wait and notify.
* Semaphore limits the number of threads that can access a resource simultaneously. 
  * Think of it as a lock with a counter.
    
## GIL
### GIL Internals
* GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode
  simultaneously. this has 2 consequences:
    * Python threads don't speed up CPU-bound work on multi-core machines.
    * they remain incredibly useful for I/O-bound tasks where threads spend most of their time waiting for external  
      resources, as the GIL is released during I/O operations.
* Threads have 3 states w.r.t GIL: Holding, Released, Waiting
* GIL exists to facilitate garbage collection and multiple threads can corrupt the count and cause memory leaks
* Fine-grained locking adds overhead to every object operation, Since most Python programs are single-threaded or 
  I/O-bound, this trade-off was rejected.
* GIL uses a time-based switching mechanism. By default, a thread can hold the GIL for at most 5 milliseconds
* GIL Release Points:
  - I/O operations: Reading from files, network sockets, or pipes
  - Sleep: time.sleep() releases the GIL while waiting
  - C extensions: Many C extensions release the GIL during computation
  - Check interval: After approximately 5ms of execution
### Working Around the GIL:
* GIL limits CPU-bound parallelism, but python provides several ways to achieve true parallelism when you need it
* Multiprocessing: stop fighting the GIL and use processes instead of threads
  * multiprocessing module creates separate processes, each with its own Python interpreter and its own GIL. Since  
    the GILs are independent, the processes run truly in parallel.
  * trade-off: processes have higher overhead than threads, and sharing data between them requires explicit  
    mechanisms (queues, shared memory, pipes).
  * **2 api models:**
    * pool
    * thread like start() and join()
  * **Inter Process Communication (IPC):** Sharing data across Process
    * Queue: Message Passing for Multiple Processes
    * Pipe: Direct Two-Way Communication
    * Shared Memory: High-Performance Data Sharing
* C Extensions: NumPy, SciPy, scikit-learn
  * Many performance-critical libraries are written in C and release the GIL during computation, you still use  
    threads, but the heavy lifting happens in GIL-free C code.
* Option 3: asyncio for I/O Concurrency
  * For I/O-bound code, there is another approach that sidesteps the GIL entirely: asyncio
  * Instead of using threads, asyncio uses a single thread that cooperatively switches between tasks at await points.
    Since there is only one thread, the GIL is never contended.
  * asyncio is ideal for network-heavy applications like web servers, API clients, and crawlers
* Option 4: Cython with nogil
  * Cython offers a way to write Python-like code that compiles to C and can release the GIL