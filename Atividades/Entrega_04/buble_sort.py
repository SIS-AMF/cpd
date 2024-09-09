import random

def change(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def bubble_sort(arr):
    for ref in range(len(arr) - 1):
        for index in range(len(arr) - 1):
            next_index = index + 1
            if arr[index] > arr[next_index]:
                change(arr, index, next_index)


def main():
    lista_inversa = [10,9,8,7,6,5,4,3,2,1]
    lista_ordenada = [1,2,3,4,5,6,7,8,9,10]
    lista_com_repeticoes = [4,7,2,5,6,7,4,3,2,6,7,4,3,2,5,7,7,5,3,5,7,]
    lista_aleatoria = [random.randint(0, 9) for X in range(20)]

    bubble_sort(lista_inversa)
    print(lista_inversa)

    bubble_sort(lista_ordenada)
    print(lista_ordenada)

    bubble_sort(lista_com_repeticoes)
    print(lista_com_repeticoes)

    bubble_sort(lista_aleatoria)
    print(lista_aleatoria)

main()