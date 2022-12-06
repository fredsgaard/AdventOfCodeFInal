import csv
import math
import string
from collections import Counter
from dec3_part2 import dec3_part2

def dec3_part1():
    with open('dec3.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        priority = 0
        for row in csv_reader:
            items = row[0]
            wc = Counter(items)
            no_items = math.floor(len(items)/2)
            first = row[0][0:no_items]
            second = row[0][no_items:]
            print('Row: ' + row[0])
            print('First part: ' + first)
            print('Second part: ' + second)
            for item, count in wc.items():
                if count > 1:
                    if first.__contains__(item) and second.__contains__(item):
                        print('Item in both compartments: ' + item)
                        if item.isupper():
                            priority += string.ascii_uppercase.index(item) + 27
                        else:
                            priority += string.ascii_lowercase.index(item) + 1
            print('Priority: ' + str(priority))