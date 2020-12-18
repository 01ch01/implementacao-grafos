from main_functions import adjacency_matrix, get_edges, get_vertices


def is_simple(graph):
    edges = get_edges(graph)
    unique_edges = set()

    for edge in edges:

        loop = edge[0] == edge[1]
        is_inverted = edge[::-1] in edges
        same_edge = False

        if edge in unique_edges:
            same_edge = True

        else:
            unique_edges.add(edge)

        if loop or is_inverted or same_edge:
            return False

    return True


def is_multi(graph):
    edges = get_edges(graph)
    unique_edges = set()
    minimum_conditions = 0

    for edge in edges:

        if edge[::-1] in edges:
            minimum_conditions += 1

        if edge in unique_edges:
            minimum_conditions += 1

        else:
            unique_edges.add(edge)

    if minimum_conditions >= 2:
        return True

    else:
        return False


def is_pseudo(graph):
    edges = get_edges(graph)

    for edge in edges:

        if edge[0] == edge[1]:
            return True

    return False


def is_connected(graph):
    adj_matrix = adjacency_matrix(graph)

    for row in adj_matrix:
        if not 1 in row:
            return False

    return True


def is_disconnected(graph):

    if not is_connected(graph):
        return True
    else:
        return False


def is_complete(graph):
    matrix = adjacency_matrix(graph)
    adjacency = []
    count = 0

    for i in matrix:
        adjacency += i[count+1:]
        count += 1

    if 0 in adjacency:
        return False
    else:
        return True


def is_eulerian(graph):
    pass


def is_hamiltonian(graph):
    pass
