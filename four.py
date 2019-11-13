#!/usr/bin/python

#4.1 Route between nodes

class Graf:
    nodes = []

    def __init__(self, value):
        node = Node(value, [])
        self.nodes.append(node)

    def add(self, node):
        self.nodes.append(node)


class Node:
    value = ''
    children = []

    def __init__(self, value, children):
        self.value = value
        self.children = children


def isRouteBetweenNodes(start, end, visited):
    if (start == None):
        return 0
    if (start == end):
        return 1
    visited[start.value] = 1
    for node in start.children:
        if (visited.get(node.value) == None):
            if isRouteBetweenNodes(node, end, visited):
                return 1



graf = Graf(0)
#for node in graf.nodes:
#    print node.value

for i in range(1,5):
    node = Node(i, [graf.nodes[i-1]])
    graf.add(node)


#out(graf.nodes[4])
#visited = {}
print isRouteBetweenNodes(graf.nodes[4], graf.nodes[1], {})
print isRouteBetweenNodes(graf.nodes[1], graf.nodes[4], {})
print isRouteBetweenNodes(graf.nodes[3], graf.nodes[2], {})
print isRouteBetweenNodes(graf.nodes[3], graf.nodes[2], {})
