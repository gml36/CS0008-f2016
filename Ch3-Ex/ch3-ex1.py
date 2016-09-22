# name: Genevieve Laymon
# email: gml36@pitt.edu
# date: 9-22-2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 1
# notes:

num = input ('Enter a number from 1 to 7, please: ')
num = int(num)
if num < 1 or num > 7:
    print 'Please enter a valid number'
    'return'
if num == 1:
    day = 'Monday'
elif num == 2:
    day = 'Tuesday'
elif num == 3:
    day = 'Wednesday'
elif num == 4:
    day = 'Thursday'
elif num == 5:
    day = 'Friday'
elif num == 6:
    day = 'Saturday'
elif num == 7:
    day = 'Sunday'
print 'The day is ' +str(day)