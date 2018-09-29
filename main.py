import dateutil.parser
from todoist.api import TodoistAPI

from model import Item, Node, Project


def sort(node):
    if node is None:
        return node

    node.children = sorted(node.children,
                           key=lambda x: dateutil.parser.parse(x.item.due_date) if x.item.due_date is not None else dateutil.parser.parse('01 Jan 1970 01:59:59 +0000'))
    for child in node.children:
        sort(child)

    return node


def fetch_secret():
    print("Retrieving API key")
    with open('secret.txt', 'r') as f:
        return f.readline().strip()


def populate_projects(api):
    api.sync()
    projects = {}
    api_projects = api.state['projects']
    api_items = api.state['items']

    for api_project in api_projects:
        projects[api_project['id']] = Project(api_project['name'], api_project['id'])
        print('Processed', api_project['name'])

    for api_item in api_items:
        if api_item['in_history'] != 0:
            continue
        item = Item(api_item['content'], api_item['id'], api_item['item_order'], api_item['indent'], api_item['due_date_utc'])
        projects[api_item['project_id']].items.append(item)
        print('Added task', api_item['content'], 'to project', api.projects.get_by_id(api_item['project_id'])['name'])
    for id, project in projects.items():
        project.items = sorted(project.items, key=lambda x: x.order)

    return projects


def build_tree(project):
    if len(project.items) == 0:
        print('Empty project: %s' % project.name)
        return None

    root = Node(Item(project.name, -1, None, -1, None), None)
    parent = root
    previous = root
    for item in project.items:
        if item.indent > previous.item.indent:
            parent = previous
        if item.indent < previous.item.indent:
            for i in range(previous.item.indent - item.indent):
                parent = parent.parent

        node = Node(item, parent)
        parent.children.append(node)
        previous = node

    return root


def build_request(trees):
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


def main():
    api = TodoistAPI(fetch_secret())
    projects = populate_projects(api)
    trees = [build_tree(project) for id, project in projects.items()]
    trees = list(map(sort, trees))
    print()
    print("New order: ")
    for tree in trees:
        tree.display()

    print()
    print("Building Sync API request")
    new_orders_indents = build_request(trees)
    api.items.update_orders_indents(new_orders_indents)
    print("Committing changes")
    api.commit()
    print("Done!")


if __name__ == '__main__':
    main()
