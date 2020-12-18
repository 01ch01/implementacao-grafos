import os
from main_functions import *
from verify_functions import *

main_menu_text = '''\n
    ***************************
    ****** MENU PRINCIPAL *****
    ***************************

    [1] - Criar Grafo
    [2] - Abrir Grafo salvo
    [3] - Salvar Grafo
    [4] - Matriz de Adjacência
    [5] - Matriz de Incidência
    [6] - Lista de Adjacência
    [7] - Verificações
    [8] - Mostrar
    [0] - Sair
'''

verify_menu_text = '''\n
    ***************************
    ******* VERIFICAÇÕES ******
    ***************************

    [1] - Simples
    [2] - Multigrafo
    [3] - Pseudografo
    [4] - Conexo
    [5] - Desconexo
    [6] - Completo
    [7] - Euleriano
    [8] - Hamiltoniano
    [9] - Voltar
    '''


def main_menu():
    graph = {}

    while True:

        print(main_menu_text)
        main_option = int(input('Escolha uma opção: '))
        clear_console()

        if main_option == 1:
            graph = create_graph()

        if main_option == 2:
            file_graph = load_graph()
            graph = file_graph

        if main_option == 3:
            save_graph(graph)

        if main_option == 4:

            matrix = adjacency_matrix(graph)
            print(f'\n\tMatriz de Adjacência:\n')

            for row in matrix:
                print(f'\t{row}')

        if main_option == 5:

            matrix = incidence_matrix(graph)
            print(f'\n\tMatriz de Incidência:\n')

            for row in matrix:
                print(f'\t{row}')

        if main_option == 6:

            adjacency_list = adjacency_list(graph)
            print(f'\n\tLista de Adjacência:\n')

            for row in adjacency_list.items():
                print(row)

        if main_option == 7:
            verify_menu(graph)

        if main_option == 8:
            show(graph)

        if main_option == 0:
            quit()

        input()


def verify_menu(graph):
    clear_console()

    print(verify_menu_text)
    verify_option = int(input('Escolha uma opção: '))

    clear_console()

    if verify_option == 1:

        if is_simple(graph):
            print(f'\n\tO grafo é simples')
        else:
            print(f'\n\tO grafo NÃO é simples')

    if verify_option == 2:

        if is_multi(graph):
            print(f'\n\tEste grafo é multigrafo')
        else:
            print(f'\n\tEste grafo NÃO é multigrafo')

    if verify_option == 3:

        if is_pseudo(graph):
            print(f'\n\tEste grafo é um pseudografo')
        else:
            print(f'\n\tEste grafo NÃO é um pseudografo')

    if verify_option == 4:

        if is_connected(graph):
            print(f'\n\tEste grafo é conexo')
        else:
            print(f'\n\tEste grafo NÃO é conexo')

    if verify_option == 5:

        if is_disconnected(graph):
            print(f'\n\tEste grafo é desconexo')
        else:
            print(f'\n\tEste grafo NÃO é desconexo')

    if verify_option == 6:
        is_complete(graph)

    if verify_option == 7:
        is_eulerian(graph)

    if verify_option == 8:
        is_hamiltonian(graph)

    if verify_option == 9:
        main_menu()
