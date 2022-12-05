import re
import csv
from queue import LifoQueue


def dec5_part1():
    stack = [['R', 'P', 'C', 'D', 'B', 'G'],\
             ['H', 'V', 'G'],\
             ['N', 'S', 'Q', 'D', 'J', 'P', 'M'], \
             ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],\
             ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'], \
             ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'], \
             ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'], \
             ['C', 'M', 'D', 'B', 'F'], \
             ['F', 'C', 'Q', 'G']]
    with open('dec5.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        regex = re.compile(r'([0-9]{1,2}).*([0-9]).*([0-9])')
        message = ''
        for row in csv_reader:
            instruction = re.search(regex, row[0])
            number = int(instruction.group(1))
            source = int(instruction.group(2))-1
            dest = int(instruction.group(3))-1
            print('Number: ' + str(number) + ', ' + 'Source: ' + str(source) + ', ' + 'Dest: ' + str(dest))
            while number > 0:
                if bool(stack[source]):
                    stack[dest].append(stack[source].pop())
                    number -= 1

        for s in range(0,9,1):
            message += stack[s][len(stack[s])-1]
        print('Message: ' + message)


def dec5_part2():
    stack = [['R', 'P', 'C', 'D', 'B', 'G'], \
             ['H', 'V', 'G'], \
             ['N', 'S', 'Q', 'D', 'J', 'P', 'M'], \
             ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'], \
             ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'], \
             ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'], \
             ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'], \
             ['C', 'M', 'D', 'B', 'F'], \
             ['F', 'C', 'Q', 'G']]
    with open('dec5.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        regex = re.compile(r'([0-9]{1,2}).*([0-9]).*([0-9])')
        message = ''
        for row in csv_reader:
            instruction = re.search(regex, row[0])
            number = int(instruction.group(1))
            source = int(instruction.group(2)) - 1
            dest = int(instruction.group(3)) - 1

            temp = stack[source][(len(stack[source])-number):len(stack[source])]
            stack[dest] += temp
            del(stack[source][(len(stack[source])-number):len(stack[source])])

        for s in range(0, 9, 1):
            message += stack[s][len(stack[s]) - 1]
        print('Message: ' + message)
