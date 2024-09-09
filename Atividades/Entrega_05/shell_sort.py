import random

def change(arr_insertion, index1, index2):
    # Alteracao feita para ele trocar o indice do array e tambem trocar o array de posicao
    temp = arr_insertion[index1][0]
    arr_insertion[index1][0] = arr_insertion[index2][0]
    arr_insertion[index2][0] = temp

    temp = arr_insertion[index1]
    arr_insertion[index1] = arr_insertion[index2]
    arr_insertion[index2] = temp

def verify(arr_insertion, index):
    next_index = index + 1
    # Feita a alteração par que acesse o valor da tupla e não o indice
    if arr_insertion[index][1] > arr_insertion[next_index][1]:
        change(arr_insertion, index, next_index)
        return True
    return False

def verify_previous(arr_insertion, index):
    for sec_index in range(index -1,-1, -1):
        # Faz a validação se esta ordenado novamente
        # Também verifica se achou ja a posicao correspondente e para o loop
        if not verify(arr_insertion, sec_index):
            break

def insertion_sort(arr_insertion):
    for index in range(len(arr_insertion) - 1):
        # Faz a validação se esta ordenado
        if verify(arr_insertion, index):
            # Se ouve uma troca ele faz a verificação com os anteriores
            verify_previous(arr_insertion, index)
    return arr_insertion



def troca(arr, index, incrementador, temp):
    while index >= incrementador and arr[index - incrementador] > temp:
        arr[index] = arr[index - incrementador]
        index = index - incrementador
    arr[index] = temp

def verify_shell(arr, start_point, incrementador):
    ordena = [[index, arr[index]] for index in range(start_point, len(arr), incrementador)]
    insertion_sort(ordena)
    for [index, valor] in ordena: 
        arr[index] = valor
        

def shell_sort(arr):
    incrementador = len(arr) // 2
    while incrementador > 0:
        for start_point in range(incrementador):
            verify_shell(arr, start_point, incrementador)
        incrementador = incrementador // 2


def main():
    lista_inversa = [10,9,8,7,6,5,4,3,2,1]
    lista_ordenada = [1,2,3,4,5,6,7,8,9,10]
    lista_com_repeticoes = [4,7,2,5,6,7,4,3,2,6,7,4,3,2,5,7,7,5,3,5,7,]
    lista_aleatoria = [random.randint(0, 9) for X in range(20)]

    shell_sort(lista_inversa)
    print(lista_inversa)

    shell_sort(lista_ordenada)
    print(lista_ordenada)

    shell_sort(lista_com_repeticoes)
    print(lista_com_repeticoes)

    shell_sort(lista_aleatoria)
    print(lista_aleatoria)

main()