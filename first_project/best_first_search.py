from input import read_graph

# Our heuristic, with the distance in a straight line from the city to Bucharest
h = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu_Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}


def insert_priority_queue(queue, element):
    size = len(queue)
    if size > 0:
        for i in range(size):
            if h[element[-1][0]] < h[queue[i][-1][0]]:
                return queue[:i] + [element] + queue[i:]
            elif i == size - 1:
                return queue + [element]
    else:
        return [element]


def uniform_cost_search(graph, initial_vertex, destination_vertex):
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
            return path

        for adjacent in graph.get(node, []):  # We're adding this node's edges to the frontier_path_queue, ordering
            # by the total cost of the new path
            new_path = list(path)
            new_path.append(adjacent)
            frontier_path_queue = insert_priority_queue(frontier_path_queue, new_path)


graph = read_graph()
print(uniform_cost_search(graph, "Oradea", "Eforie"))
