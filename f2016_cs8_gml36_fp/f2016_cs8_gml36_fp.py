# name: Genevieve Laymon
# email: gml36@pitt.edu
# date: 12-6-16
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# description: Final Project
# notes: I had some difficulty getting the code from project 3 to work with the class

import sys
# needed to get max and min values

class Participants:
# adding the class
    def __init__(self, n, d=0):
        self.name = n
        self.distance = d
        if d == 0:
            self.runs = 0
        else:
            self.runs = 1

    def addDistance(self, d):
        self.distance += d
        self.runs += 1

    def addDistances(self, ld):
        for distance in ld:
            self.distance += distance
            self.runs += 1

    def getDistance(self):
        return self.distance

    def getName(self):
        return self.name

    def __str__(self):
        return 'Name: {:>20s}. Distance run: {:09.4f}. Runs: {:04.0f} \n'.format(self.name, self.distance, self.runs)

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
                (running_distances[runner_info[0]]).addDistance(float(runner_info[1]))
            else:
                running_distances[runner_info[0]] = Participants(runner_info[0], float(runner_info[1]))
        data_file.close()
    return running_distances

master_data_name = input("Please provide the master file: ")
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
for runner in list(runner_info.values()):
    if runner.getDistance() > current_max:
        current_max = runner.getDistance()
        max_name = runner.getName()

current_min = sys.maxsize
# getting the minimum
min_name = ''
for runner in list(runner_info.values()):
    if runner.getDistance() < current_min:
        current_min = runner.getDistance()
        min_name = runner.getName()

multiple_records = 0
# figuring out who has multiple records
for runner in list(runner_info.values()):
    if runner.runs > 1:
        multiple_records += 1

total_dist_run = 0
# calculating the total distance run
for runner in list(runner_info.values()):
    total_dist_run += runner.getDistance()

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
    for runner in list(runner_info.values()):
        output_file.write(str(runner))
    output_file.close()