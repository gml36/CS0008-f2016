def parse_file_list(file_list):
    open_files = []
    for data in file_list:
        open_files.append(open(data))
    return open_files

master_data_name = raw_input('Enter the name of the master data file: ')
master_data_file = open(master_data_name, 'r')
data_file_list = []
for line in master_data_file:
    data_file_list.append(line)