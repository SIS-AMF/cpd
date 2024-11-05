def search(arr, alvo):
    index_meio = len(arr) // 2
    meio = arr[index_meio]
    print(arr, meio)

    if meio > alvo:
        return search(arr[:index_meio], alvo)
    elif meio < alvo:
        return search(arr[index_meio + 1:], alvo)
    else:
        return meio


def main():
    vetor = [1, 2, 3, 4, 5,6,7,8,9,10,11]

    resultado = search(vetor, 11)

    print(resultado)

    return 0


main()
