import re
from copy import deepcopy

step_re = re.compile(r'Step\s([A-Z])\smust\sbe\sfinished\sbefore\sstep\s([A-Z])\scan\sbegin\.')


def parse_list(lines):
    edges = []
    for line in lines:
        match = step_re.match(line)
        t = (match.group(1), match.group(2))
        edges.append(t)
    return edges


def build_dependencies(edges):
    nodes = {}
    for edge in edges:
        if not edge[1] in nodes:
            nodes[edge[1]] = []
        nodes[edge[1]].append(edge[0])
        if not edge[0] in nodes:
            nodes[edge[0]] = []
    return nodes


def part1(nodes):
    order = []
    while len(nodes) > 0:
        currently_available_nodes = sorted([x for x in nodes.keys() if len(nodes[x]) == 0])
        node_doing = currently_available_nodes[0]
        order.append(node_doing)
        for node in nodes.values():
            if node_doing in node:
                node.remove(node_doing)
        del nodes[node_doing]
    return order


def part2(nodes):
    available_workers = 5
    time_passed = 0
    nodes_in_work = []
    while len(nodes) > 0 or len(nodes_in_work) > 0:
        currently_available_nodes = sorted([x for x in nodes.keys() if len(nodes[x]) == 0])
        while available_workers > 0 and len(currently_available_nodes) > 0:
            available_workers -= 1
            node_doing = currently_available_nodes.pop(0)
            nodes_in_work.append([node_doing, ord(node_doing) - 4])
            del nodes[node_doing]
        node_finished = nodes_in_work.pop(0)
        available_workers += 1
        time_passed += node_finished[1]
        for node in nodes_in_work:
            node[1] -= node_finished[1]
        for node in nodes.values():
            if node_finished[0] in node:
                node.remove(node_finished[0])
    return time_passed


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

list_edges = parse_list(input_lines)
list_nodes = build_dependencies(list_edges)
print(''.join(part1(deepcopy(list_nodes))))
print(part2(deepcopy(list_nodes)))
