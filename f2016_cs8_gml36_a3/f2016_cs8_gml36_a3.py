def parse_file_list(file_list):
    open_files = []
    for data in file_list:
        open_files.append(open(data))
    return open_files

def read_data_files(data_files):
    running_distances = {}
    for data_file in data_files:
        for line in data_file:
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
read_data_files(data_files)