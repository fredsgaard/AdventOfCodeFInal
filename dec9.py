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


def diag_move(k1, k2):
    k2_new_pos = k2
    if k1[0] > k2[0]:  # E
        if k1[1] > k2[1]:  # NE
            k2_new_pos[0] += 1
            k2_new_pos[1] += 1
        else:  # SE
            k2_new_pos[0] += 1
            k2_new_pos[1] -= 1
    else:  # W: k1[0] < k2[0]
        if k1[1] > k2[1]:  # NW
            k2_new_pos[0] -= 1
            k2_new_pos[1] += 1
        else:  # SW
            k2_new_pos[0] -= 1
            k2_new_pos[1] -= 1
    return k2_new_pos


def motion(k1, k2):
    k2_new_pos = k2
    if k1[0] > k2[0] and k1[1] == k2[1]: # move Right
        k2_new_pos[0] += 1
    elif k1[0] < k2[0] and k1[1] == k2[1]: # move Left
        k2_new_pos[0] -= 1
    elif k1[1] > k2[1] and k1[0] == k2[0]: # move Up
        k2_new_pos[1] += 1
    elif k1[1] < k2[1] and k1[0] == k2[0]: # move Down
        k2_new_pos[1] -= 1
    return k2_new_pos


def dec9_part2():
    move = re.compile(r'([LRUD])')
    count = re.compile(r'^[A-Z]+\s([0-9]+)')
    s: list[int] = [12, 6]
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
    with open('dec9.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            line += 1
            direction = re.search(move, row[0]).group(1)
            steps = int(re.search(count, row[0]).group(1))
            if direction == 'L':
                for s in range(0, steps):
                    h[0][0] -= 1
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > 2:  # diagonal move
                            h[knot + 1] = diag_move(h[knot], h[knot + 1])
                        elif math.dist(h[knot], h[knot + 1]) == 2:
                            h[knot + 1] = motion(h[knot], h[knot + 1])
                    if h[-1] not in t_positions_list:
                        t_positions_list.append(copy.deepcopy(h[-1]))
                        count_snake_tail_pos += 1
            elif direction == 'R':
                for s in range(0, steps):
                    h[0][0] += 1
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > 2:  # diagonal move
                            h[knot + 1] = diag_move(h[knot], h[knot + 1])
                        elif math.dist(h[knot], h[knot + 1]) == 2:
                            h[knot + 1] = motion(h[knot], h[knot + 1])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(copy.deepcopy(h[-1]))
                            count_snake_tail_pos += 1
            elif direction == 'U':
                for s in range(0, steps):
                    h[0][1] += 1  # Move head
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > 2:  # diagonal move
                            h[knot + 1] = diag_move(h[knot], h[knot + 1])
                        elif math.dist(h[knot], h[knot + 1]) == 2:
                            h[knot + 1] = motion(h[knot], h[knot + 1])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(copy.deepcopy(h[-1]))
                            count_snake_tail_pos += 1
            elif direction == 'D':
                for s in range(0, steps):
                    h[0][1] -= 1
                    for knot in knots:
                        if math.dist(h[knot], h[knot + 1]) > 2:  # diagonal move
                            h[knot + 1] = diag_move(h[knot], h[knot + 1])
                        elif math.dist(h[knot], h[knot + 1]) == 2:
                            h[knot + 1] = motion(h[knot], h[knot + 1])
                        if h[-1] not in t_positions_list:
                            t_positions_list.append(copy.deepcopy(h[-1]))
                            count_snake_tail_pos += 1
    print('Number of positions covered by the snake\'s tail: ' + str(count_snake_tail_pos))
