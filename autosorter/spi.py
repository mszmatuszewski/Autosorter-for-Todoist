import dateutil.parser


class SortingBy:

    def __init__(self, key_function, reversed=False, *, _successor=None):
        """
        Represents a sorting strategy.

        :param callable key_func: the key extractor function. Several common functions are included in the SPI.
        :param bool reversed: specifies whether the sorting order should be reversed.
        :param SortingBy _successor: a SortingBy object to be used for further sorting.
        """
        self._key_function = key_function
        self._successor = _successor
        self._reversed = reversed


    def __call__(self, coll):
        """
        Sorts the provided collection in accordance with the chain of sorting strategies represented by this object.

        :param  list coll: collection to be sorted.
        :return: sorted collection.
        :rtype: list
        """
        temp = sorted(coll, key=self._key_function, reverse=self._reversed)
        return self._successor(temp) if self._successor else temp


    def then_by(self, key_func, *, reversed=False):
        """
        Allows for chaining of sorting strategies.

        :param callable key_func: the key extractor function. Several common functions are included in the SPI.
        :param bool reversed: specifies whether the sorting order should be reversed.
        :return: a SortingBy object representing the chain of sorting strategies.
        :rtype: SortingBy
        """
        return SortingBy(key_func, reversed=reversed, _successor=self)


class DefaultSorter(SortingBy):
    """Sorts tasks by their due date."""


    def __init__(self):
        super().__init__(due_date)


def task_id(node):
    """
    Extracts task ID from a project tree node.

    :param Node node: project tree node.
    :return: task ID.
    :rtype: int
    """
    return node.item.id


def item_order(node):
    """
    Extracts item order value from a project tree node.

    :param Node node: project tree node.
    :return: item order value or -1 if not present.
    :rtype: int
    """
    return node.item.order if node.item.order else -1


def due_date(node):
    """
    Extracts task due date from a project tree node.

    :param Node node: project tree node.
    :return: due date or epoch start if not present.
    :rtype: datetime
    """
    if node.item.due_date is not None:
        return dateutil.parser.parse(node.item.due_date)
    else:
        return dateutil.parser.parse('01 Jan 1970 01:59:59 +0000')


def user_id(node):
    """
    Extracts owner's user ID from a project tree node.

    :param Node node: project tree node.
    :return: task owner's ID or -1 if not present.
    :rtype: int
    """
    return node.item.user_id if node.item.user_id else -1


def project_id(node):
    """
    Extracts project ID from a project tree node.

    :param Node node: project tree node.
    :return: project ID or -1 if not present.
    :rtype: int
    """
    return node.item.project_id if node.item.project_id else -1


def name(node):
    """
    Extracts task name from a project tree node.

    :param Node node: project tree node.
    :return: task name or empty string if not present.
    :rtype: str
    """
    return node.item.name if node.item.name else ""


def priority(node):
    """
    Extracts task's priority level from a project tree node.

    :param Node node: project tree node.
    :return: task's prority or 1 (lowest) if not present.
    :rtype: int
    """
    return node.item.priority if node.item.priority else 1


def responsible_uid(node):
    """
    Extracts responsible user ID from a project tree node.

    :param Node node: project tree node.
    :return: responsible user ID or -1 if not present.
    :rtype: int
    """
    return node.item.responsible_uid if node.item.responsible_uid else -1


def date_added(node):
    """
    Extracts task creation date from a project tree node.

    :param Node node: project tree node.
    :return: task creation date or epoch start if not present.
    :rtype: datetime
    """
    if node.item.date_added is not None:
        return dateutil.parser.parse(node.item.date_added)
    else:
        return dateutil.parser.parse('01 Jan 1970 01:59:59 +0000')
