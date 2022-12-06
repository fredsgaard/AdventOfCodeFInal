import csv
import  string
from collections import Counter


def dec6_part1():
    with open('dec6.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for symbol_streams in csv_reader:
            symbols = symbol_streams[0]
            for idx in range(4,len(symbols),1):
                packet = symbols[idx-4:idx]
                wc = Counter(packet)
                packet_found = True
                for item, count in wc.items():
                    packet_found = True
                    if count > 1:
                        packet_found = False
                if packet_found:
                    print('Packet found! Packet: ' + packet + ', at: ' + str(idx))
                    packet_found = False
                    # break


