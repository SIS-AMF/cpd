import random

def change(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def verify(arr, index):
    next_index = index + 1
    if arr[index] > arr[next_index]:
        change(arr, index, next_index)
        return True
    return False

def verify_previous(arr, index):
    for sec_index in range(index -1,-1, -1):
        # Faz a validação se esta ordenado novamente
        # Também verifica se achou ja a posicao correspondente e para o loop
        if not verify(arr, sec_index):
            break

def insertion_sort(arr):
    for index in range(len(arr) - 1):
        # Faz a validação se esta ordenado
        if verify(arr, index):
            # Se ouve uma troca ele faz a verificação com os anteriores
            verify_previous(arr, index)

def main():
    lista_inversa = [10,9,8,7,6,5,4,3,2,1]
    lista_ordenada = [1,2,3,4,5,6,7,8,9,10]
    lista_com_repeticoes = [4,7,2,5,6,7,4,3,2,6,7,4,3,2,5,7,7,5,3,5,7,]
    lista_aleatoria = [random.randint(0, 9) for X in range(20)]

    insertion_sort(lista_inversa)
    print(lista_inversa)

    insertion_sort(lista_ordenada)
    print(lista_ordenada)

    insertion_sort(lista_com_repeticoes)
    print(lista_com_repeticoes)

    insertion_sort(lista_aleatoria)
    print(lista_aleatoria)

main()