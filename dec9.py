import copy
import csv
import re
import math
from typing import List


def dec9_part1():
    rows = 5
    cols = 6
    field = [[0 for _ in range(cols)] for _ in range(rows)]
    move = re.compile(r'([LRUD])')
    count = re.compile(r'^[A-Z]+\s([0-9]+)')
    s: list[int] = [1, 1]
    h = copy.deepcopy(s)
    t = copy.deepcopy(s)
    h_last_pos = copy.deepcopy(s)
    t_positions_list = []
    count_pos = 0
    with open('dec9.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            direction = re.search(move, row[0]).group(1)
            steps = int(re.search(count, row[0]).group(1))
            if direction == 'L':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[1] -= 1
                    if math.dist(h, t) > math.sqrt(2):
                        t = h_last_pos
                    if t not in t_positions_list:
                        t_positions_list.append(t)
                        count_pos += 1
            if direction == 'R':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[1] += 1
                    if math.dist(h, t) > math.sqrt(2):
                        t = h_last_pos
                    if t not in t_positions_list:
                        t_positions_list.append(t)
                        count_pos += 1
            if direction == 'U':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[0] += 1
                    if math.dist(h, t) > math.sqrt(2):
                        t = h_last_pos
                    if t not in t_positions_list:
                        t_positions_list.append(t)
                        count_pos += 1
            if direction == 'D':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[0] -= 1
                    if math.dist(h, t) > math.sqrt(2):
                        t = h_last_pos
                    if t not in t_positions_list:
                        t_positions_list.append(t)
                        count_pos += 1
    print('Number of positions covered by tail: ' + str(count_pos))


def dec9_part2():
    rows = 5
    cols = 6
    field = [[0 for _ in range(cols)] for _ in range(rows)]
    move = re.compile(r'([LRUD])')
    count = re.compile(r'^[A-Z]+\s([0-9]+)')
    s: list[int] = [6, 12]
    length = 10
    knots = []
    for k in range(length - 1):
        knots.append(k)
    h = []
    h_last_pos = []
    for knot in range(0, length):
        h.append(copy.deepcopy(s))
        h_last_pos.append(copy.deepcopy(s))

    t_positions_list = []
    count_snake_tail_pos = 0
    line = 0
    with open('dec9_test2.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            line += 1
            direction = re.search(move, row[0]).group(1)
            steps = int(re.search(count, row[0]).group(1))
            if direction == 'L':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[0][1] -= 1
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > math.sqrt(2):
                            h[knot + 1] = copy.deepcopy(h_last_pos[knot])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(h[-1])
                            count_snake_tail_pos += 1
            elif direction == 'R':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[0][1] += 1
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > math.sqrt(2):
                            h[knot + 1] = copy.deepcopy(h_last_pos[knot])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(h[-1])
                            count_snake_tail_pos += 1
            elif direction == 'U':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[0][0] += 1  # Move head
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > math.sqrt(2):
                            h[knot + 1][0] += 1  # copy.deepcopy(h_last_pos[knot])
                            h[knot + 1][1] += 1  # copy.deepcopy(h_last_pos[knot])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(h[-1])
                            count_snake_tail_pos += 1
            elif direction == 'D':
                for s in range(0, steps):
                    h_last_pos = copy.deepcopy(h)
                    h[0][0] -= 1
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > math.sqrt(2):
                            h[knot + 1] = copy.deepcopy(h_last_pos[knot])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(h[-1])
                            count_snake_tail_pos += 1
    print('Number of positions covered by the snake\'s tail: ' + str(count_snake_tail_pos))
