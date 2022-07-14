'''
Created on Jun 3, 2020

@author: ruded
'''
import math
import random


x = pow(4,6)
y = min(55,2,99)
z = max(23,3,66)
print(x)
print(y)
print(z)


'''
Math module examples
'''
a = math.sqrt(64)
print(a)

b = math.ceil(1.4)
c = math.floor(1.4)

print(b) # returns 2
print(c) # returns 1

d = math.pi
print(d)

'''
Random module examples
'''
# seed generated by the system clock
# Returns a random float number between 0 and 1
print(random.random())


# The randint() method returns an integer number selected element from the specified range.
# Return a number between 1 and 6 (both included)
print(random.randint(1, 6))

# Return a number between 3 and 9
print(random.randrange(3, 9))

# Select an even number in 100 <= number < 1000
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))

# Select another number in 100 <= number < 1000
print("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))

# The seed() method is used to initialize the random number generator.
print()
random.seed(5)
print(random.random())
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
print()
for i in range (10):
    if i % 3 == 0:
        random.seed(10)
    print(random.random())
