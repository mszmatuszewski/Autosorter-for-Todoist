from spi import *
import os

""" 
Primary configuration hook. See SPI docs for details. Defaults to OrderBy(due_date).

Example usage:
sorter = OrderBy(name).then_by(due_date, reversed=True).then_by(project_id)

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
order = DefaultOrder()


def secret():
    """
    Provides a Todoist API key.

    :rtype: str
    """
    return os.environ['TODOIST_API_KEY']
