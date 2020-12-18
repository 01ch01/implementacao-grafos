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
            adjacency_matrix(graph)

        if main_option == 5:
            incidence_matrix(graph)

        if main_option == 6:
            adjacency_list(graph)

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

    if verify_option == 1:
        is_simple(graph)

    if verify_option == 2:
        is_multi(graph)

    if verify_option == 3:
        is_pseudo(graph)

    if verify_option == 4:
        is_connected(graph)

    if verify_option == 5:
        is_disconnected(graph)

    if verify_option == 6:
        is_complete(graph)

    if verify_option == 7:
        is_eulerian(graph)

    if verify_option == 8:
        is_hamiltonian(graph)

    if verify_option == 9:
        main_menu()
