def read_graph():
    graph = {}

    with open("input.txt", 'r') as f:
        for line in f.read().splitlines():
            values = line.split(" ")
            if values[0] not in graph:
                graph[values[0]] = [(values[1], values[2])]
            else:
                graph[values[0]].append((values[1], values[2]))
            if values[1] not in graph:
                graph[values[1]] = [(values[0], values[2])]
            else:
                graph[values[1]].append((values[0], values[2]))

    return graph
