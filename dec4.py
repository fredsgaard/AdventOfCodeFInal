import csv
import re


def dec4_part1():
    with open('dec4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        all_assignments = []
        overlapping = 0
        for row in csv_reader:
            assignment_1 = row[0]
            assignment_2 = row[1]
            a = re.search(r'(.*)-(.*)', assignment_1)
            b = re.search(r'(.*)-(.*)', assignment_2)

            begin_1 = int(a.group(1))
            end_1 = int(a.group(2))
            begin_2 = int(b.group(1))
            end_2 = int(b.group(2))

            if (begin_1 <= begin_2 and end_1 >= end_2) or (begin_2 <= begin_1 and end_2 >= end_1):
                overlapping += 1
        print('Part 1: Overlapping assignments: ' + str(overlapping))


def dec4_part2():
    with open('dec4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        all_assignments = []
        overlapping = 0
        for row in csv_reader:
            assignment_1 = row[0]
            assignment_2 = row[1]
            a = re.search(r'(.*)-(.*)', assignment_1)
            b = re.search(r'(.*)-(.*)', assignment_2)

            begin_1 = int(a.group(1))
            end_1 = int(a.group(2))
            begin_2 = int(b.group(1))
            end_2 = int(b.group(2))

            if (begin_1 <= begin_2 <= end_1) or (begin_2 <= begin_1 <= end_2):
                overlapping += 1
        print('Part 2: Overlapping assignments: ' + str(overlapping))
