from autosorter.spi import *

""" 
Primary configuration hook. See SPI docs for details. Defaults to SortingBy(due_date).

Example usage:
sorter = SortingBy(name).then_by(due_date, reversed=True).then_by(project_id)

Sorting criteria provided out-of-the-box:
 -  task_id
 -  item_order
 -  due_date
 -  user_id
 -  project_id
 -  name
 -  priority
 -  responsible_uid
 -  date_added
"""
sorter = DefaultSorter()


def secret():
    """
    Provides a Todoist API key.

    :rtype: str
    """
    with open('secret.txt', 'r') as f:
        return f.readline().strip()
