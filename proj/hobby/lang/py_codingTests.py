# a cannot be replaced with in - as in is a reserved keyword
def fun(a=2, out=3):
    return a * out

print(fun(3))

# single element tuple should be (1,)
tup = (1, )+ (1,)
tup = tup + tup
print (len(tup))
print (tup)
print ((1,))

tup2 = (1)
print (tup2)


# name collision - TypeError: 'function' object does not support item deletion
my_list = ['Mary','had','a','little','lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

# print(my_list(my_list))  - TypeError: 'function' object does not support item deletion
