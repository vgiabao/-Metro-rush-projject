from csv import reader
import re
from node import Node


class Graph():
    def __init__(self):
        self.nodes = []
        self.start_point = None
        self.end_point = None
        self.simulate_line = ''
        self.train = []
        self.num_train = 0
        self.goin = 0

    def add_node(self, node):
        self.nodes.append(node)

    def add_start(self, start):
        self.start_point = start

    def add_end(self, end):
        self.end_point = end

    def add_train(self, num, train):
        self.train.append(train)

    def read_file(self):
        with open('delhi-metro-stations') as csv_file:
            f = csv_file.readline()
            while f != '':
                if f.startswith('#'):
                    content = re.sub('#', '', f)
                    self.simulate_line = content[:-1]
                elif 'Conn' in f:
                    information = f.split(':')
                    self.add_node(Node(information[0], self.simulate_line,
                                       information[1], information[3][1:-1]))
                elif 'START=' in f:
                    information = re.sub('START=', '', f)
                    information = information.split(':')
                    self.add_start(Node(information[1][:-1], information[0]))
                elif 'END=' in f:
                    information = re.sub('END=', '', f)
                    information = information.split(':')
                    self.add_end(Node(information[1][:-1], information[0]))
                elif 'TRAINS' in f:
                    information = f.split('=')
                    self.num_train = int(information[1])
                else:
                    information = f.split(':')
                    self.add_node(Node(information[0], self.simulate_line,
                                       information[1]))
                f = csv_file.readline()

    def compare(self):
        first = None
        last = None
        for item in self.nodes:
            if self.start_point == item:
                first = item
            elif self.end_point == item:
                last = item
        for index in range(self.num_train):
            name = 'T' + str(index + 1)
            self.train.append(Node(first.id, first.line, name))
        return first, last

    def check_direction(self, node, checked_list):
        up = str(int(node.id) + 1)
        down = str(int(node.id) - 1)
        list_moving = []
        for item in self.nodes:
            if Node(up, node.line) == item and item not in checked_list:
                if item.extra:
                    list_moving.append([Node(item.id, item.line, item.name),
                                        Node(item.id, item.extra, item.name)])
                list_moving.append([Node(item.id, item.line, item.name)])
            if Node(down, node.line) == item and item not in checked_list:
                if item.extra:
                    list_moving.append([Node(item.id, item.line, item.name),
                                        Node(item.id, item.extra, item.name)])
                list_moving.append([Node(item.id, item.line, item.name)])
        return list_moving


    def check_near(self):
        first, last = self.compare()
        checked_item = []
        list_moving = []
        initial_list = self.check_direction(first, checked_item)
        for item in initial_list:
            list_moving.append([first] + item)
        while True:
            for extension in self.check_direction(list_moving[0][-1],
                                                  checked_item):
                list_moving.append(list_moving[0] + extension)
                if extension[-1] == last:
                    return list_moving[0] + extension
            list_moving.pop(0)
            checked_item.append(list_moving[0][-1])

    def define_train(self, map):
        i_max = len(map) - 1
        for train in self.train:
            for station in map:
                if train == station:
                    station.train = train.name

