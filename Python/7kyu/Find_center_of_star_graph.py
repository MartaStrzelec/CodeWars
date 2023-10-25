#Write a function that given the list of edges, returns the center of the star graph as an integer.

def center(graph_edges):
    node1, node2, node3, node4 = graph_edges[0][0], graph_edges[0][1], graph_edges[1][0], graph_edges[1][1]
    if node1 == node3 or node1 == node4:
        return node1
    return node2
