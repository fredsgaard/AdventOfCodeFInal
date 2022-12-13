import csv
import string

def get_heightmap():
    heightmap = []
    start = []
    with open('dec12_test.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        pos_y = 0
        for y in csv_reader:
            row = []
            pos_x = 0
            for elev in y[0]:
                if elev == 'S':
                    start = [pos_x, pos_y]
                    row.append(string.ascii_lowercase.index('a'))
                    pos_x += 1
                    continue
                elif elev == 'E':
                    end = [pos_x, pos_y]
                    row.append(string.ascii_lowercase.index('z'))
                    pos_x += 1
                    continue
                else:
                    row.append(string.ascii_lowercase.index(elev))
                    pos_x += 1
            pos_y += 1
            heightmap.append(row)
    return heightmap, start, end

def max_elev():
    heightmap = get_heightmap()

def dec12_part1():
    heightmap = get_heightmap()
    print(heightmap)