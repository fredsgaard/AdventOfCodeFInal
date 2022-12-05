import re
import csv

def dec5_part1():
    with open('dec5_init.csv') as csv_file:
        regex_init = re.compile(r'([A-Z])')
        csv_reader = csv.reader(csv_file)
        stack1 = []
        stack2 = []
        stack3 = []
        stack4 = []
        stack5 = []
        stack6 = []
        stack7 = []
        stack8 = []
        stack9 = []
        for row in csv_reader:
            for stack in row[0]:
                print(stack)
                # crate = re.search(regex_init, stack)
    #
    #             print('Crate: ' + crate.group(1))
    #
    # with open('dec5.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     regex = re.compile(r'([0-9]).*([0-9]).*([0-9])')
    #     for row in csv_reader:
    #         instruction = re.search(regex, row[0])
    #         number = int(instruction.group(1))
    #         source = int(instruction.group(2))
    #         dest = int(instruction.group(3))
    #
    #         print('Number: ' + str(number) + ', ' + 'Source: ' + str(source) + ', ' + 'Dest: ' + str(dest))
    #

