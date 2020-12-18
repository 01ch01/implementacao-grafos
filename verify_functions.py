from main_functions import clear_console, get_edges


def is_simple(graph):
    edges = get_edges(graph)
    unique_edges = set()

    for edge in edges:
        loop = edge[0] == edge[1]
        is_inverted = edge[::-1] in edges
        same_edge = False

        if(edge in unique_edges):
            same_edge = True
        else:
            unique_edges.add(edge)

        if (loop or is_inverted or same_edge):
            clear_console()
            print(f'O grafo NÃO é simples')
            return False

    clear_console()
    print(f'O grafo é simples')
    return True


def is_multi(graph):
    pass


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
