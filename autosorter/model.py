class Project:

    def __init__(self, name, id):
        """
        Represents a Todoist project.

        :param str name: project name.
        :param int id: project ID.
        """
        self.name = name
        self.id = id
        self.items = []


    def __repr__(self):
        return "%s %s %s" % (self.id, self.name, list(map(str, self.items)))


class Item:

    def __init__(self, name, id=None, order=None, due_date=None, user_id=None, project_id=None,
                 priority=None, responsible_uid=None, date_added=None):
        """
        Represents a Todoist task.

        :param str name: The text of the task.
        :param int id: The id of the task.
        :param int order: The order of the task inside a project (the smallest value would place the task at the top).
        :param str due_date: The date of the task in the format Mon 07 Aug 2006 12:34:56 +0000 (or None if not set). For all day task (i.e. task due “Today”), the time part will be set as xx:xx:59.
        :param int user_id: The owner of the task.
        :param int project_id: Project that the task resides in.
        :param int priority: The priority of the task (a number between 1 and 4, 4 for very urgent and 1 for natural).
            Note: Keep in mind that very urgent is the priority 1 on clients. So, p1 will return 4 in the API.
        :param int responsible_uid: The id of user who is responsible for accomplishing the current task. This makes sense for shared projects only.
            Accepts any user id from the list of project collaborators or None or an empty string to unset.
        :param str date_added: The date when the task was created.
        """
        self.name = name
        self.id = id
        self.order = order
        self.due_date = due_date
        self.user_id = user_id
        self.project_id = project_id
        self.priority = priority
        self.responsible_uid = responsible_uid
        self.date_added = date_added


    def __repr__(self):
        return "%s (%s)" % (self.name, self.due_date)


def map_to_item(api_item):
    """
    Creates an Item corresponding to a Todoist task.

    :param api_item: a Todoist API item.
    :return: an Item corresponding to a Todoist task.
    :rtype: Item
    """
    return Item(api_item['content'],
                api_item['id'],
                api_item['child_order'],
                api_item['due']['date'],
                api_item['user_id'],
                api_item['project_id'],
                api_item['priority'],
                api_item['responsible_uid'],
                api_item['date_added']
                )


class Node:

    def __init__(self, item, parent=None):
        """
        Represents an Item in the project tree

        :param Item item: the Todoist task Item.
        :param Node parent: a parent task or the project Node
        """
        self.item = item
        self.parent = parent
        self.children = []

    def __repr__(self):
        return repr(self.item) + '\n    ' + '\n    '.join(map(repr, self.children))

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
