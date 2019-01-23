from autosorter.config import sorter
from autosorter.model import *
from autosorter.todoist_connector import *


def sort(root):
    """
    Sorts the task tree using the strategy provided in the configuration.

    :param Node root: the task tree to be sorted.
    :return: sorted task tree.
    :rtype: Node
    """
    if root is None:
        return root

    root.children = sorter(root.children)
    for child in root.children:
        sort(child)

    return root


def build_tree(project):
    """
    Builds a project tree from Project object.

    :param Project project: a Project object.
    :return: a Node object representing the root of the project tree.
    :rtype: Node
    """
    if len(project.items) == 0:
        return None

    root = Node(Item(project.name, id=-1, indent=-1))
    for item in project.items:
        node = Node(item, root)
        root.children.append(node)

    return root


def main():
    """Main script. Retrieves projects from the Todoist API, generates a new order scheme and updates the data on the server."""
    print("Initialising API connection")
    api_init()
    print("Initialised API connection")
    print("Retrieving projects")
    projects = api_retrieve_projects()
    print("Retrieved projects")
    print("Parsing data")
    trees = [build_tree(project) for project in projects.values()]
    print("Sorting")
    trees = list(map(sort, trees))
    print("Sorted")
    print("Updating remote data")
    api_update_projects(trees)
    print("Updated remote data")
    print("Done")


if __name__ == '__main__':
    main()
