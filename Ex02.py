list_ord = [1,2,3,4,5]
list_inv = [5,4,3,2,1]
list_des = [3,1,5,2,4]
list_rep = [6,4,3,3,2,1]

def insertionsort(lista):
    for x in len(lista):
        menor = lista[x]
        for y in range(x + 1, len(lista)):
            if lista[y] < menor:
                menor = lista[y]
                menor_id = y

print(insertionsort(list_ord), insertionsort(list_inv), insertionsort(list_des),insertionsort(list_rep))