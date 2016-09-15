num = input ('give me the number: ')
num = int (num)
if num < 0 or num > 36
    print ('give me a valid number')
    return
if num == 0
    color = 'green'
elif num >= 1 and num <= 10 \
or \
num >= 19 and num <= 28
    if num % 2 == 0
        color = 'black'
    else
        color = 'red'
elif num >= 11 and num <= 18 \
or \
num >= 29 and num <= 36
    if num % 2 == 0
        color = 'red'
    else
        color = 'black'
print ('your color is' color)