import sys

def parse_file_list(file_list):
    open_files = []
    for data in file_list:
        open_files.append(open(data))
    return open_files

def read_data_files(data_files):
    running_distances = {'num_lines_read': 0}
    for data_file in data_files:
        for line in data_file:
            running_distances['num_lines_read'] += 1
            runner_info = line.split(',')
            if runner_info[0] in running_distances:
                (running_distances[runner_info[0]])[0] += float(runner_info[1])
                (running_distances[runner_info[0]])[1] += 1
            else:
                running_distances[runner_info[0]] = [float(runner_info[1]), 1]
    return running_distances

master_data_name = raw_input('Enter the name of the master data file: ')
master_data_file = open(master_data_name, 'r')
data_file_list = []
for line in master_data_file:
    data_file_list.append(line)
data_files = parse_file_list(data_file_list)
master_data_file.close()
runner_info = read_data_files(data_files)
num_files_read = len(data_files)
num_lines_read = runner_info['num_lines_read']
for item in data_files:
    item.close()

current_max = -sys.maxsize - 1
max_name = ''
for name, distance in runner_info:
    if distance[0] > current_max:
        current_max = distance[0]
        max_name = name

current_min = sys.maxsize
min_name = ''
for name, distance in runner_info:
    if distance[0] < current_min:
        current_min = distance[0]
        min_name = name