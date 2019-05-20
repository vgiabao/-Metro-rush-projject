#!/bin/python3
import argparse
from Graph import Graph
from node import Node
from re import sub

def handle_parser():
    parser = argparse.ArgumentParser(usage='./tsp.py <country> [<algorithm>]')
    parser.add_argument('file_name', help='the start country')
    parser.add_argument('-t', '--type', help='select the algorithm',
                        choices=['flexibility', 'straight'],
                        default='straight')
    args = parser.parse_args()
    return args


def get_data():
    p = Graph()
    p.read_file()
    list = ''
    map_road = p.check_near()
    print(map_road)
    for index, item in enumerate(map_road):
        if index == 0:
            for train in p.train:
                list += train.name + ' '
            print(item.id, item.line, list, end='------->>>')
        else:
            print(item.id, item.line, item.train, end='------->>>')

def main():
    args = handle_parser()
    road = get_data()

if __name__ == '__main__':
    main()
