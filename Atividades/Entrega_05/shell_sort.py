import random

def troca(arr, index, incrementador, temp):
    while index >= incrementador and arr[index - incrementador] > temp:
        arr[index] = arr[index - incrementador]
        index = index - incrementador
    arr[index] = temp

def verify(arr, start_point, incrementador):
    for index in range(start_point + incrementador, len(arr), incrementador):
        temp = arr[index]
        troca(arr, index, incrementador, temp)

def shell_sort(arr):
    incrementador = len(arr) // 2
    while incrementador > 0:
        for start_point in range(incrementador):
            verify(arr, start_point, incrementador)
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