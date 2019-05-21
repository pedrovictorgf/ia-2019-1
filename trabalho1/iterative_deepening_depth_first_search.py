from input import read_graph

DEPTH_LIMIT = 10
FAILURE = -1


def depth_limited_search(graph, initial_vertex, destination_vertex, limit):  # The initial dls function call
    return recursive_dls(graph, [(initial_vertex, 0)], destination_vertex, limit)


# Out path is something like that [(Node, Cost), (Node, Cost), ...]
def recursive_dls(graph, path, destination_vertex, limit):
    node = path[-1][0]  # Gets the last node on the path

    if node == destination_vertex:  # If we are on the destination node, then we return the path
        return path
    elif limit == 0:  # If our search hit the depth limit we established in the beginning, then we cutoff
        return None
    else:  # There is still search to be done in this node
        cutoff_ocorruded = False

        for adjacent in graph.get(node, []):  # For each adjacent node we create the new paths
            new_path = list(path)
            new_path.append(adjacent)
            result = recursive_dls(graph, new_path, destination_vertex, limit - 1)
            if result is None:  # If the result was None, it means a cutoff occurred
                cutoff_ocorruded = True
            elif result != FAILURE:  # If the result wasn't None nor FAILURE we return it
                return result
        if cutoff_ocorruded:  # At last, if a cutoff occurred we return None
            return None
        else:
            return FAILURE  # If the search failed, we return the constant FAILURE


def iterative_deepening_depth_first_search(graph, initial_vertex, destination_vertex):
    for i in range(DEPTH_LIMIT):
        result = depth_limited_search(graph, initial_vertex, destination_vertex, i)
        if result is not None and result != FAILURE:
            print(i)
            return result


graph = read_graph()
print(iterative_deepening_depth_first_search(graph, 'Iasi', 'Fagaras'))
