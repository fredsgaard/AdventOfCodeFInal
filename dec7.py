import csv
import re


def dec7_part1():
    regex_filesize = re.compile(r'(^\d+)')
    regex_ls = re.compile(r'(^(\$\sls))')
    with open('dec7.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        total_dir_size = 0
        dir_size = 0
        for row in csv_reader:
            ls_command = re.fullmatch(regex_ls, row[0])
            if ls_command:
                print('$ ls')
                if dir_size <= 100000:
                    total_dir_size += dir_size
                    print('Total dir size:' + str(total_dir_size))
                dir_size = 0
            file = re.search(regex_filesize, row[0])
            if file:
                file_size = int(file.group(1))
                print('File size: ' + str(file_size))
                dir_size += file_size
                print('Dir size: ' + str(dir_size))
        print('Total dir sizes of dirs < 100000: ' + str(total_dir_size))

#
#
#
#
# def dec7_part2():
#     with open('dec7.csv') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for row in csv_reader: