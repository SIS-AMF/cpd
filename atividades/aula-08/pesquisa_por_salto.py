
def linear(vet, alvo):
    for item in reversed(vet):
        print(item)
        if alvo == item:
            return item


def pesquisa(vetor, alvo):
    raiz = int(len(vetor) ** (1/2))

    last = 0

    for index in range(raiz, len(vetor), raiz):
        if alvo < vetor[index]:
            return linear(vetor[index-raiz:index], alvo)
        last = index

    for item in vetor[last:]:
        if item == alvo:
            return item


def main():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print(pesquisa(vetor, 10))
    return 0


main()
