'''
Created on Oct 7, 2020
@author: ruded
'''

sum = 0
for i in range(1,11):
    sum += i
print('Sum from 1 to 10 is', sum)

sum = 0
for i in range(20, 38):
    sum += i
print('Sum from 20 to 37 is', sum)

sum = 0
for i in range(35, 50):
    sum += i
print('Sum from 35 to 49 is', sum)


def sumBetween(start_value, stop_value):
    sum = 0
    for i in range(start_value, stop_value + 1):
        sum += i
    print(f'Sum from {start_value} to {stop_value}.')
