def fibMonaccianSearch(lista, x, n):

    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1

    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while (fibM > 1):

        i = min(offset+fibMMm2, n-1)

        if (lista[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        elif (lista[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        else:
            return i

    if (fibMMm1 and lista[n-1] == x):
        return n-1

    return -1


def main():
    lista = [50, 58, 64, 74, 80, 85, 90, 99]
    n = len(lista)
    x = 58
    ind = fibMonaccianSearch(lista, x, n)
    if ind >= 0:
        print("Encontrado na posição:", ind)
    else:
        print(x, "Não encontrado na lista")


main()
