import re



def parse(txt):
    lines = txt.split("\n")
    graph = {}

    for line in lines:
        parts = line.split("<->")
        index = int(parts[0])

        connections = [int(x) for x in parts[1].split(",")]
        graph[index] = connections

    return graph



def fn(txt):
    graph = parse(txt)

    seen = set()

    def recurse(node):
        for i in node:
            if i not in seen:
                seen.add(i)
                recurse(graph[i])

    recurse(graph[0])

    print(seen)

    return len(seen)


def fn2(txt):
    graph = parse(txt)
    groups = []
    seen = set()
    all_seen = set()

    def recurse(node):
        for i in node:
            if i not in seen:
                seen.add(i)
                all_seen.add(i)
                recurse(graph[i])

    for i, connections in graph.items():
        if seen and i not in all_seen:
            groups.append(seen)
            seen = set()
        
        seen.add(i)
        recurse(graph[i])

    groups.append(seen)
    print(len(groups))

    return len(groups)
