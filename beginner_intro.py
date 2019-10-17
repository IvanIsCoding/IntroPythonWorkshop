'''
INTRO TO PYTHON

Beginner Notes
'''



# this is a comment
# the program will ignore comments
# they are for developer use

# variables
name = "Ivan"
age = 19

print(name, "is", age, "years old.")

# suppose a year passes
age = 20
print(name, "is", age, "years old.")


# arithmatic

x = 5
y = 3

add = x + y
sub = x - y
mul = x * y
div = x / y
exp = x ** y

# modulus gets the remainder
mod = x % y


# increment x by y
# x = x + y
x += y

# decrement x by y
# x = x - y
x -= y

# This also works for other operators
x *= y
x /= y


# if statements

condition = True

if condition:
    # do something
elif condition:
    # do something
else:
    # do something

if 5 < 9:
    print("5 < 9")
elif 5 > 9:
    print("5 > 9")
else:
    print("5 == 9")


# thats my note for myself
# for p in itertools.permutations('ABCD'):


# loops! :)

i = 1
while i < 10:
    print(i)
    i += 1

for i in range(0,10):
    print(i)

sample_list = ['this', 'is', 'a', 'list', ':)']
for item in sample_list:
    print(item)



# iterables

# iterables are a collection of items
# that can be iterated over
# usually in a loop

sample_list = ['i', 'am','stressed', 'for', 'my', 'cosc', 328, 'midterm']

sample_tuple = ('cosc', 328, 'should', 'stay', 'an', 'immutable', 'unit')

sample_set = {'a', 'duplicate', 'in', 'a', 'set', 'is', 'deleted'}


# list





