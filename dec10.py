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

def dec10_part2():
