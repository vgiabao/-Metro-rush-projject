class Node:
    def __init__(self, id, line, name=None, extra=None, train=None):
        self.name = name
        self.id = id
        self.line = line
        self.extra = extra
        self.train = None
    def __eq__(self, other):
        return (self.line == other.line and self.id == other.id)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.name, self.id, self.line,
                                       self.extra)


class Start_end():
    def __init__(self, id, line):
        self.id = id
        self.line = line

    def __eq__(self, other):
        return self.id == other.id, self.line == other.line

    def __str__(self):
        return '{}, {}'.format(self.id, self.line)




