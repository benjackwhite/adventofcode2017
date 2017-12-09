import re

reg = re.compile("([a-z]+) \((\d+)\)(?: -> ([a-z,\s]+))?")


class Node:
    name: None
    parent: None
    weight: None

    def __init__(self, name=None, parent=None, weight=None):
        self.name = name
        self.parent = parent
        self.weight = weight

def parse_tree(txt):
    lines = txt.split("\n")
    tree = {}

    for line in lines:
        matches = reg.match(line)

        name = matches.group(1)
        if name in tree:
            node = tree[name]
        else:
            node = Node(name=name)
            tree[name] = node

        node.weight = matches.group(2)

        if matches.group(3):
            children = matches.group(3).split(", ")

            for child in children:
                if child not in tree:
                    tree[child] = Node(name=child)

                tree[child].parent = node
        
    return tree


def find_bottom(txt):
    tree = parse_tree(txt)

    for key, node in tree.items():
        if not node.parent:
            return key


def find_weight_change(txt):
    tree = parse_tree(txt)
