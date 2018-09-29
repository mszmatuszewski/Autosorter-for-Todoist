import dateutil.parser


class Project:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.items = []


    def __str__(self):
        return "%s %s %s" % (self.id, self.name, list(map(str, self.items)))


class Item:

    def __init__(self, name, id, order, indent, due_date):
        self.name = name
        self.id = id
        self.order = order
        self.indent = indent
        self.due_date = due_date
        self.subitems = []


    def __str__(self):
        return "%s %s %s %s (%s) %s" % \
               (self.id, self.name, self.order, self.indent, self.due_date, list(map(str, self.subitems)))


class Node:

    def __init__(self, item, parent):
        self.item = item
        self.parent = parent
        self.children = []


    def display(self):
        if self is None:
            print("Empty tree")
            return

        indent_level = 0
        temp = self
        while temp is not None:
            temp = temp.parent
            indent_level += 1

        print(self.item)
        for child in self.children:
            print(end=' ' * 4 * indent_level)
            child.display()

        return self


    def sort(self):
        if self is None:
            return self

        self.children = sorted(self.children,
                               key=lambda x: dateutil.parser.parse(x.item.due_date) if x.item.due_date is not None else dateutil.parser.parse('01 Jan 1970 01:59:59 +0000'))
        for child in self.children:
            child.sort()

        return self
