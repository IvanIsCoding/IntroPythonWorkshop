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


# list comprehension
 
some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
negative_evens = [-i for i in some_list if i % 2 == 0]


# this is equivalent to

negative_evens_2 =[]
for i in some_list:
    if i % 2 == 0:
        negative_evens_2.append(-i)



# Functions


def add_all(a, b, c, d=0):
    # if d is not given into the function,
    # the value of d is zero by default
    return a + b + c + d

def function_in_fuction():
    # you can have a function in a function
    print('a=4, b=9, c=-10, d=9')
    sum = add_all(4,9,-10,9)
    print('the sum of a, b, c, d is', sum)

print(add_all(0,1,0,9))



# Object Oriented Programming

class Robot:
    '''
    This is a Robot
    '''
    def __init__(self, metal_type, ai=True):
        self.metal_type = metal_type
        self.ai=ai
    
    def do_robot_thing(self):
        self.spin()
    
    @static
    def spin():
        return

def SpecialRobot(Robot):
    '''
    This is a Robot that has been extended to have a special item
    '''
    def __init__(self, metal_type, special_item='love and affection', ai=True):
        super(Robot)
        self.special_item = special_item
    
    def use_special_item(self):
        return self.special_item
    
    def change_special_item(self):
        new_item = input('What is the Robot\'s new item?')
        self.special_item = new_item
