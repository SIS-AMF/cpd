import random

def change(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def smaller_value(arr, init, end):
    smaller_value = arr[init]
    index_of_smaller_value = init
    for index in range(init + 1, end):
        if arr[index] < smaller_value:
            smaller_value = arr[index]
            index_of_smaller_value = index
        
    return index_of_smaller_value  

def selection_sort(arr):
    lenght = len(arr)
    for index in range(lenght):
        small = smaller_value(arr, index, lenght)
        if small != index:
            change(arr, index, small)

def main():
    lista_inversa = [10,9,8,7,6,5,4,3,2,1]
    lista_ordenada = [1,2,3,4,5,6,7,8,9,10]
    lista_com_repeticoes = [4,7,2,5,6,7,4,3,2,6,7,4,3,2,5,7,7,5,3,5,7,]
    lista_aleatoria = [random.randint(0, 9) for X in range(20)]

    selection_sort(lista_inversa)
    print(lista_inversa)

    selection_sort(lista_ordenada)
    print(lista_ordenada)

    selection_sort(lista_com_repeticoes)
    print(lista_com_repeticoes)

    selection_sort(lista_aleatoria)
    print(lista_aleatoria)

main()