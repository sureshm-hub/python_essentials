# copy
import copy
from collections import OrderedDict

a = [1,2,3,4]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

c[1] = 22

# is vs ==
print(b is a)
print(c == a)
print(d == a)

print(a[1])
print(d[1])

d1 = [[1,2,3],[4,5,6],[7,8,9]]
d5 = copy.copy(d1) # Shallow: copies outer list
d2 = copy.deepcopy(d1) # Deep: copies inner lists too
d2[1][1] = 'X'

print(d1[1][1])
print(d2[1][1])
print(d5[1][1])

e = a[:]
print(e)

# list append, extend
a.append([5,6])
print(a)

del a[len(a)-1]
print(a)

a.extend([5,6])
print(a)

h =  a[0:len(a)-1:2]
print(h)

# OOP - class
class Example:

    class_var = 'Class Ownership'

    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

    @classmethod
    def class_method(cls):
        print(cls.class_var)

    @staticmethod
    def static_method():
        print('Static method')

obj = Example('Instance Ownership')
obj.print_value()

# obj.class_method() - supported but  bad usage
Example.class_method()

#obj.static_method() - supported but  bad usage
Example.static_method()


## - Mutable Defaults - lst initialized during function initialization
def append_val(lst=[]):
    lst.append(1)
    return lst

print(append_val())  # [1]
print(append_val())  # [1, 1] ← gotcha!

def append_val_noMutation(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
print(append_val_noMutation()) # [1]
print(append_val_noMutation()) # [1]

tuple = (1,)
print("type of tuple >> ", type(tuple), tuple)

# {expression for item in iterable} - set comprehension unique and unordered
result = {i+1 for i in range(10) if i%2 == 0}
print(result)
print("type of result >> ", type(result))

# [expression for item in iterable] - list comprehension ordered & allows duplicates
result = [i*i for i in range(10) if i%2 == 0]
print(result)
print("type of result >> ", type(result))

# {k: v for item in iterable} - dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)
print("type of squares >> ", type(squares))

# dictionary comprehension 2  using other dictionaries
original_dict = {'a': 1, 'b': 2, 'c': 3}
doubled_values = {key: value * 2 for key, value in original_dict.items()}
print("type of doubled_values >> ", type(doubled_values))

# (expression for item in iterable) - generator comprehension
even_nums_gen = (x for x in range(10) if x % 2 == 0)
print(even_nums_gen)
for num in even_nums_gen:
    print(num, end = " >> ")
print()
print("type of even_nums_gen >> ", type(even_nums_gen))

# dummy generator
dummy_gen = (x for x in range(5) if x == 0 or x == 1 )
for num in dummy_gen:
    print(num, end = " >> ")
print()
print("type of dummy_gen >> ", type(dummy_gen))

# truthy
y = -5
z = 0

if y:
    print("y is truthy")

if z:
    print("z is truthy")
else:
    print("z is falsy")

# zip
a = [1, 2, 3]
b = ['a','b','c']
print(a)
print (b)

d = {k: v for k,v in zip(a,b)}
print(d)

# unzip
x, y = zip(*d.items())

print (x)
print(y)

# multi varialbe assignment
a, b, c = 1, 2, 3

# multiple assignment
a = b= c = "multiple assignment"

# Unpack a Collection
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a,b,c)

# Basic Logging
import logging as log
log.basicConfig(level = log.INFO)
log.warning("Remain Calm!")
# log.basicConfig(level = log.INFO) - won't work as set basic config before any  log statement
log.info("This is an info message")
log.debug("this won't be seen at info level")


x = 5
y = "John"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(x + y)
print(x,y)

# string
a = "Hello, World!"
print(a[4])
print(a)
print(a[4:6])
print(a[-4])
print(a[-12:-6])
print(a[-6:-12])

x = [1,2,3,4,5,6,7,8,9]
print(x[2:6])
print(x[2:5])

for x in a:
    print(x)

b = [ x for x in a if x != ' ']
print(b)
print (str(b))
x = "".join(b)
print(x)
[print(x) for x in a]

# formatted strings
price = 59
print(f"prie is {price}")
print(f"price for 2 items is { 2 * price}")
print(f"price is {price:.3f}")

# boolean
print(bool("hello"))
print(bool("0"))
print(bool(15))
print("bool evaluates to False")
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
print(bool(False))

# generator
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fib_series = fib_gen()

for _ in range(10):
    print(next(fib_series), end=">>")
else:
    print(next(fib_series))
print(next(fib_series))

# iterator
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.n:
            val = self.i
            self.i += 1
            if val%2 == 0:
                return val
        raise StopIteration

for even in EvenIterator(5):
    print(even)

# closure:
def multiplier(factor):
    def inner(x):
        return factor * x
    return inner

twice = multiplier(2)
thrice = multiplier(3)

print(twice(7))
print(thrice(7))

# decorator
def logged_call(func):
    def wrapper(*args, ** kwargs):
        print("calling:",func.__name__)
        func(*args, ** kwargs)
        print("called:", func.__name__)
    return wrapper

@logged_call
def hello():
    print("hello")

hello()

# LRU Cache
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

under5 = LRUCache(3)
keys = [1,2,1,3,4]
values = [1,2,3,4,5]
dict2 = dict(zip(keys, values))
print(dict2)
dict = {k:v for k, v in zip(keys, values)}
print(dict)
for k, v in dict.items():
    under5.put(k, v)

print(under5.cache)

# Asynch IO
import asyncio

async def fetch_data(n):
    await asyncio.sleep(n)
    return f"Done after {n}s"

async def main():
    res = await asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))
    print(res)

asyncio.run(main())