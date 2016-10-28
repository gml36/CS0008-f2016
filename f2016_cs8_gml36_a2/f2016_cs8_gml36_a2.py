# name: Genevieve Laymon
# email: gml36@pitt.edu
# date: 10-28-2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# description: Assignment 2

# this function takes the handle to a file object
# and returns the number of lines and the total distance
def processFile(fh):
    # here I am defining variables
    num_lines = 0
    total_distance = 0
    # loop through each line in the file
    for line in fh:
        # count this line
        num_lines += 1
        # gets the distance and adds it to the total
        line = line.rstrip('\n')
        line = line.split(',')
        distance = line[1]
        total_distance += float(distance)
    # returns the number of lines and the total distance
    return [num_lines, total_distance]

# this prints a key and a value with consistent formatting
def printKV(key,value,klen = 0):
    # figures out how many spaces to give the key
    max_len = max(len(key), klen)
    if isinstance(value, str):
        # formats and prints string values
        format_str = '{:' + str(max_len) + '}:{:20)'
        print(format_str.format(key, value))
    elif isinstance(value, float):
        #formats and prints float values
        format_str = '{:' + str(max_len) + '}:{:6.3)'
        print(format_str.format(key, value))
    else:
        # formats and prints all other values, including ints
        format_str = '{:' + str(max_len) + '}:{:10)'
        print(format_str.format(key, value))

