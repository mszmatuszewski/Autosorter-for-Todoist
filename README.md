# Autosorter-for-Todoist

A script sorting all Todoist tasks by configurable criteria.

Requires a Todoist API key in a 'secret.txt' file in the main folder.

To configure, edit the config.py file.
Example configuration: 
```python
sorter = SortingBy(name).then_by(due_date, reversed=True).then_by(project_id)
```

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
 
Additional customisation possible via extending the SPI.

Not created by, affiliated with, or supported by Doist.

No warranties beyond *works on my machine* given.
