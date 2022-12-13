import copy
import csv
import re


def dec10_part1():
    re_instr = re.compile(r'([a-z]{4})')
    re_amount = re.compile(r'([0-9]+)')
    re_minus = re.compile(r'(\-)')
    x = 1
    cc = 0
    add_time = 2
    signals = []
    mod20_sig = []
    sum_signal = 0
    with open('dec10.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            instruction = re.search(re_instr, row[0]).group(1)
            if instruction == 'noop':
                cc += 1
                if cc % 20 == 0:
                    strength = x * cc
                    signals.append(strength)
            else:
                while add_time:
                    cc += 1
                    add_time -= 1

                    if cc % 20 == 0:
                        strength = x * cc
                        signals.append(strength)

                add_time = 2
                amount = int(re.search(re_amount, row[0]).group(1))
                if re.findall(re_minus, row[0]):
                    x -= amount
                else:
                    x += amount

    # s =< 5
    mod20_sig = signals[::2]
    # for n in range(0, s):
    #     sum_signal += mod20_sig[s]

    print('X register: ' + str(x))
    print('Signal strength sum: ' + str(sum(mod20_sig)))


def sprite(sprite_pos, x):
    sprite_pos[1] = x
    sprite_pos[2] = x + 1
    if x > 0:
        sprite_pos[0] = x - 1
    else:
        sprite_pos[0] = 0

    return sprite_pos


def print_crt(crt_rows):
    for row in crt_rows:
        print(row)


def dec10_part2():
    re_instr = re.compile(r'([a-z]{4})')
    re_amount = re.compile(r'([0-9]+)')
    re_minus = re.compile(r'(\-)')
    x = 1
    cc = 0
    add_duration = 2
    sprite_pos = [0, 0, 0]
    current_crt_row = ''
    crt_screen = []
    crt_line_idx = 0
    sprite_pos = sprite(sprite_pos, x)
    with open('dec10_test.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            instruction = re.search(re_instr, row[0]).group(1)
            if instruction == 'noop':
                # sprite_pos = sprite(sprite_pos, x)
                if sprite_pos.count(crt_line_idx):
                    current_crt_row += '#'
                else:
                    current_crt_row += '.'
                cc += 1
                crt_line_idx += 1

                if len(current_crt_row) == 40:
                    crt_screen.append(current_crt_row)
                    current_crt_row = ''
                    crt_line_idx = 1
            else:
                while add_duration:
                    if sprite_pos.count(crt_line_idx):
                        current_crt_row += '#'
                    else:
                        current_crt_row += '.'
                    add_duration -= 1
                    crt_line_idx += 1
                    cc += 1

                    if len(current_crt_row) == 40:
                        crt_screen.append(current_crt_row)
                        current_crt_row = ''
                        crt_line_idx = 1

                add_duration = 2
                amount = int(re.search(re_amount, row[0]).group(1))
                if re.findall(re_minus, row[0]):
                    x -= amount
                else:
                    x += amount
                sprite_pos = sprite(sprite_pos, x)

    print_crt(crt_screen)
