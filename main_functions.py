import os


def clear_console(): os.system('cls' if os.name == 'nt' else 'clear')


def create_graph():
    graph = {}
    qtd_vertices = int(input("Insira o número de vértices: "))

    for i in range(qtd_vertices):
        graph[i+1] = []

    while True:
        clear_console()
        print('\n*** Digite "-1" para terminar a criação do grafo ***\n')

        v1 = int(input('Insira um vértice: '))

        if(v1 == -1):
            break

        v2 = int(input('Insira o vértice que se conecta: '))

        graph[v1].append((v1, v2))
        # graph[v2].append((v2, v1))

    return graph


def load_graph():
    file = open('grafo.txt', 'r')
    qtd_vertices = int(file.readline())
    graph = {}

    # writing vertices in graph
    for i in range(qtd_vertices):
        graph[i+1] = []

    for line in file:
        line.split('\n')

        v1 = int(line[0])
        v2 = int(line[2])

        graph[v1].append((v1, v2))

    file.close()
    print('\n\tGrafo carregado com sucesso!\n')

    return graph


def save_graph(graph):
    file = open("grafo.txt", "w")
    stream = list()

    qtd_vertices = str(len(graph.keys()))
    stream.append(qtd_vertices+'\n')

    for edges in graph.values():
        for edge in range(len(edges)):

            line = str(edges[edge])

            # remove stuff
            line = line.replace(")", "")
            line = line.replace("(", "")
            line = line.replace(" ", "")

            line += '\n'

            stream.append(line)

    file.writelines(stream)
    file.close()

    print(f'\n\tGrafo salvo com sucesso!')


def get_vertices(graph):
    vertices = []

    for vertex in graph.keys():
        vertices.append(vertex)

    return vertices


def get_edges(graph):
    edges = []

    for i in graph.values():
        for j in range(len(i)):
            edge = i[j]
            edges.append(edge)

    return edges


def adjacency_matrix(graph):
    vertices = get_vertices(graph)
    edges = get_edges(graph)

    matrix = [[0 for _ in vertices] for _ in vertices]

    for edge in edges:
        v1 = int(edge[0])
        v2 = int(edge[1])

        matrix[v1-1][v2-1] = 1

        # mirror diagonals
        matrix[v2-1][v1-1] = 1

    return matrix


def incidence_matrix(graph):
    vertices = get_vertices(graph)
    edges = get_edges(graph)

    matrix = [[0 for _ in edges] for _ in vertices]

    for vertex in vertices:
        count = 0

        for edge in edges:

            if(edge[0] == vertex and edge[1] == vertex):
                value = 2

            elif (vertex in edge):
                value = 1

            else:
                value = 0

            matrix[(vertex-1)][count] = value
            count += 1

    return matrix


def adjacency_list(graph):
    vertices = get_vertices(graph)
    edges = get_edges(graph)
    adjacency_list = {}

    for vertex in vertices:
        neighbors = []

        for edge in edges:
            if (vertex in edge):

                neighbor = edge[1 if(vertex == edge[0]) else 0]

                neighbors.append(neighbor)

        adjacency_list[vertex] = neighbors

    return adjacency_list


def show(graph):
    clear_console()

    print(f'   Vértice\tAresta(s)\n')
    for vertex, edge in graph.items():
        print(f'\t{vertex}:\t{edge}')
