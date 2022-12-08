import csv
import re


def dec7_part1():
    regex_filesize = re.compile(r'(^\d+)')
    regex_ls = re.compile(r'(^(\$\sls))')
    regex_cd_up = re.compile(r'(^\$\scd\s\.+)')
    regex_cd_in = re.compile(r'^\$\scd\s([a-zA-Z]+)')
    with open('dec7_test.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        total_dir_size = 0
        dir_size = 0
        dir_name = 'root'
        exec(f'{dir_name} = []')
        line = 1
        dir_level = 0
        filesystem = {dir_name: []}
        dir_path = 'root'
        dir_path_stack = ['root']
        for row in csv_reader:
            print('line: ' + str(line))
            ls_command = re.fullmatch(regex_ls, row[0])
            cd_up = re.fullmatch(regex_cd_up, row[0])
            cd_in = re.search(regex_cd_in, row[0])
            file = re.search(regex_filesize, row[0])
            if cd_in:
                dir_name = cd_in.group(1)
                dir_path = dir_path_stack[-1] + '_' + dir_name
                dir_level += 1  # Go down 1 level
                # for lvl in range(dir_level, 0, -1):
                #     prefix += dir_path_stack[lvl] + '_'
                # dir_path = prefix + cd_in.group(1)
                filesystem[dir_path_stack[-1]] = {dir_name: []}
                dir_path_stack.append(dir_path)
            if cd_up:  # Move up
                dir_path_stack.pop()
            if file:  # Read file size
                file_size = int(file.group(1))
                if dir_level > 0:
                    filesystem[dir_path][dir_name].append(int(file.group(1)))
                else:
                    filesystem[dir_path].append(int(file.group(1)))
                dir_size += file_size
                print('File size: ' + str(file_size) + ', ' + 'Dir size: ' + str(dir_size))
                # dir_level -= 1
            # if ls_command:
            #     print('$ ls')
            #     if dir_size <= 100000:
            #         total_dir_size += dir_size
            #         print('Total dir size:' + str(total_dir_size))
            #         dir_size = 0

                # exec(f'{dir_name}.append(file_size)')

            # if cd_in:
            #     dir = cd_in.group(1)
            #     exec(f'dir_name = []')
            # if file:  # Read file size
            #     file_size = int(file.group(1))
            #     dir_size += file_size
            #     print('File size: ' + str(file_size) + ', ' + 'Dir size: ' + str(dir_size))
            line += 1
        print('Total dir sizes of dirs < 100000: ' + str(total_dir_size))
        return filesystem

#
#
#
#
# def dec7_part2():
#     with open('dec7.csv') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for row in csv_reader:
