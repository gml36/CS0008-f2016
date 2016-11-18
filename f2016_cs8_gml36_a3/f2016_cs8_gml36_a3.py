# name: Genevieve Laymon
# email: gml36@pitt.edu
# date: 11-15-2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# description: Assignment 3
# notes: I spent the most time on finding a way to get the data from the files loaded in a way that made sense

import sys
# needed to get max and min values


def parse_file_list(file_list):
# open all of the data files
    open_files = []
    for data in file_list:
        open_files.append(data.rstrip())
    return open_files

def read_data_files(data_files):
# read the data files and make a dictionary
    running_distances = {'num_lines_read': 0}
    # I'm also storing the number of lines read here
    # This could be a problem if someone was named "num_lines_read", but that probably won't happen
    for data_file_unopened in data_files:
        data_file = open(data_file_unopened, 'r')
        next(data_file)
        for line in data_file:
            running_distances['num_lines_read'] += 1
            runner_info = line.split(',')
            # info is stored like "name: [distance run, number of records]"
            if runner_info[0] in running_distances:
                (running_distances[runner_info[0]])[0] += float(runner_info[1])
                (running_distances[runner_info[0]])[1] += 1
            else:
                running_distances[runner_info[0]] = [float(runner_info[1]), 1]
        data_file.close()
    return running_distances

master_data_name = 'f2016_cs8_a3.data.txt'
master_data_file = open(master_data_name, 'r')
data_file_list = []
for line in master_data_file:
    data_file_list.append(line)
# get the master data file and read the names of the individual data files
data_files = parse_file_list(data_file_list)
master_data_file.close()
# close the master data file
runner_info = read_data_files(data_files)
num_files_read = len(data_files)
num_lines_read = runner_info['num_lines_read']
runner_info.pop('num_lines_read')

current_max = -sys.maxsize - 1
# getting the maximum
max_name = ''
for name, distance in runner_info.items():
    if distance[0] > current_max:
        current_max = distance[0]
        max_name = name

current_min = sys.maxsize
# getting the minimum
min_name = ''
for name, distance in runner_info.items():
    if distance[0] < current_min:
        current_min = distance[0]
        min_name = name

multiple_records = 0
# figuring out who has multiple records
for runner in runner_info:
    if runner_info[runner][1] > 1:
        multiple_records += 1

total_dist_run = 0
# calculating the total distance run
for runner in runner_info:
    total_dist_run += runner_info[runner][0]

print('Number of input files read: ' + str(num_files_read))
print('Total number of lines read: ' + str(num_lines_read))
print('Total distance run: ' + str(total_dist_run))
print('Max distance run: ' + str(current_max))
print('By participant: ' + str(max_name))
print('Min distance run: ' + str(current_min))
print('By participant: ' + str(min_name))
print('Total number of participants: ' + str(len(runner_info)))
print('Number of participants with multiple records: ' + str(multiple_records))
# printing the output

with open('output.txt', 'w') as output_file:
# creating the output file
    for name, info in runner_info.items():
        output_file.write(name + ', ' + str(info[1]) + ', ' + str(info[0]) + '\n')
    output_file.close()