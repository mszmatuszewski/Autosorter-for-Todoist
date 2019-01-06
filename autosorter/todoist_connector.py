from todoist import TodoistAPI

from autosorter.config import secret
from autosorter.model import Project, map_to_item

__all__ = ['api_retrieve_projects', 'api_update_projects', 'api_init']

__api = None


def api_init():
    """
    Initialises the API and retrieves the projects.

    :return: a dictionary of projects.
    :rtype: dict
    """
    global __api
    __api = TodoistAPI(secret())


def api_update_projects(trees):
    """
    Builds the update request and sends it to Todoist API.

    :param list trees: a list of project trees.
    """
    new_orders_indents = build_update_request(trees)
    __api.items.update_orders_indents(new_orders_indents)
    __api.commit()


def api_retrieve_projects():
    """
    Retrieves project data from Todoist.

    :return: dictionary of project trees.
    :rtype: dict
    """
    __api.sync()
    api_projects = __api.state['projects']
    api_items = __api.state['items']

    projects = {api_project['id']: Project(api_project['name'], api_project['id']) for api_project in api_projects}

    for api_item in api_items:
        if api_item['in_history'] != 0:
            continue
        item = map_to_item(api_item)
        projects[api_item['project_id']].items.append(item)
    for project in projects.values():
        project.items = sorted(project.items, key=lambda x: x.order)

    return projects


def build_update_request(trees):
    """
    Generates a Todoist update request from a list of project trees.

    :param trees: a list of project trees to update.
    :return: Todoist update request
    :rtype: dict
    """
    rq = {}
    for tree in trees:
        if tree is None:
            continue
        order = 0


        def traverse(node):
            nonlocal order
            nonlocal rq
            if node.item.id != -1:
                rq[node.item.id] = [order, node.item.indent]
                order += 1
            for child in node.children:
                traverse(child)


        traverse(tree)

    return rq
