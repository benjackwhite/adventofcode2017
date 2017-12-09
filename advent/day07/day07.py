import re

reg = re.compile("([a-z]+) \((\d+)\)(?: -> ([a-z,\s]+))?")


class Tree:
    def __init__(self, name=None):
        self.name = name
        self.children = set()
        self.weight = 0
        self.parent = None

    def __repr__(self):
        return "[T: {} ({}) ]".format(self.name, len(self.children))


def parse_tree(txt):
    lines = txt.split("\n")
    local_map = {}

    for line in lines:
        matches = reg.match(line)

        name = matches.group(1)
        if name in local_map:
            tree = local_map[name]
        else:
            tree = Tree(name=name)
            local_map[name] = tree

        tree.weight = int(matches.group(2))

        if matches.group(3):
            children = matches.group(3).split(", ")

            for child in children:
                if child not in local_map:
                    local_map[child] = Tree(name=child)                
                local_map[child].parent = tree
                tree.children.add(local_map[child])

    root = None
    for key, tree in local_map.items():
        if not tree.parent:
            root = tree

    return root


def find_bottom(txt):
    root = parse_tree(txt)

    return root

def get_weight(tree):
    weight = tree.weight
    if tree.children:
        weight += sum([ get_weight(x) for x in tree.children])

    return weight

def find_imbalance(tree):
    weights = {}

    for child in tree.children:
        weight = get_weight(child)
        if weight not in weights:
            weights[weight] = []
        weights[weight].append(child)

    for weight, items in weights.items():
        if len(items) == 1:
            weights.pop(weight)
            normal, _ = weights.popitem()
            return items[0], normal

    
    return None


def find_weight_change(txt):
    root = parse_tree(txt)

    return find_weight_diff(root)

def find_weight_diff(node):
    node, other_weight = find_imbalance(node)

    if not find_imbalance(node):
        return other_weight - get_weight(node) + node.weight

    return find_weight_diff(node)
