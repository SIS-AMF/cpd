def search(arr, alvo):
    while len(arr) > 1:
        index_meio = len(arr) // 2
        meio = arr[index_meio]
        print(meio)
        print(arr)
        if meio > alvo:
            arr = arr[:index_meio]
        elif meio < alvo:
            arr = arr[index_meio:]
        else:
            arr = [meio]
    return arr


def main():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    resultado = search(vetor, 1)

    print(resultado)

    return 0


main()
