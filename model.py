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


    def __str__(self):
        return "%s (%s)" % (self.name, self.due_date)


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
