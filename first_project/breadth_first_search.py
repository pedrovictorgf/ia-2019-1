from input import read_graph


def breadth_first_search(graph, initial_vertex, destination_vertex):
    frontier_path_queue = []  # This is the queue of paths to be explored in this graph

    if initial_vertex == destination_vertex:  # If the initial vertex is equal to the destination vertex, then there
        # is no search to be done, we already have the path
        return initial_vertex

    if destination_vertex not in graph:  # If the destination vertex does not belong to the graph, then there is no
        # search to be done
        return None

    frontier_path_queue.append([(initial_vertex, 0)])  # Our path list contains tuples of the node and the weigth of
    # the edge with the previous vertex [[(Node, Cost), (Node, Cost), (Node,Cost)]], so we added the initial vertex with
    # the value 0

    while frontier_path_queue:  # When the queue is empty it means we looked all the possible paths
        path = frontier_path_queue.pop(0)  # Current path we are analyzing

        node = path[-1][0]  # Last node of the path

        if node == destination_vertex:  # We've reached the destination vertex, so the path is returned
            return path, calc_path_cost(path)

        for adjacent in graph.get(node, []):  # We're adding this node's edges to the frontier_path_queue
            new_path = list(path)
            new_path.append(adjacent)
            frontier_path_queue.append(new_path)


def calc_path_cost(path):
    cost = 0
    for tuple in path:
        cost = cost + int(tuple[1])
    return cost


graph = read_graph()
print(breadth_first_search(graph, "Sibiu", "Bucharest"))
