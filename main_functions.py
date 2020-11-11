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
        graph[v2].append((v2, v1))

    return graph


def load_graph():
    pass


def save_graph(graph):
    file = open("grafo.txt", "w")
    stream = list()

    qtd_vertices = str(len(graph.keys()))
    stream.append(qtd_vertices+'\n\n')

    for i in graph.values():
        for j in range(len(i)):
            edge = str(i[j])
            edge.replace('(', '')
            edge.replace(')', '')
            edge.replace(' ', '')
            edge += '\n'
            stream.append(edge)

    file.writelines(stream)
    file.close()

    print(f'\n\tGrafo salvo com sucesso! ^-^')


def adjacency_matrix(graph):
    pass


def incidence_matrix(graph):
    pass


def adjacency_list(graph):
    pass


def show(graph):
    clear_console()
    # print(f'graph.items(): {graph.items()}')

    for i in graph.values():
        for j in range(len(i)):
            print(i[j])

    print(f'\n\tQuantidade de vértices: {len(graph.keys())}')
    # print(f'Vértice\t\tAresta')
    # for i, j in graph.items():
    #     print(f'{i}\t\t{j}')
