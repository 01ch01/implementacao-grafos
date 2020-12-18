from main_functions import get_edges


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
            print(f'\n\tO grafo NÃO é simples')
            return False

    print(f'\n\tO grafo é simples')
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
        print(f'Este grafo é multigrafo')
        return True

    else:
        print(f'Este grafo NÃO é multigrafo')
        return False


def is_pseudo(graph):
    pass


def is_connected(graph):
    pass


def is_disconnected(graph):
    pass


def is_complete(graph):
    pass


def is_eulerian(graph):
    pass


def is_hamiltonian(graph):
    pass
