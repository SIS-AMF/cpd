
list_ord = [1,2,3,4,5]
list_inv = [5,4,3,2,1]
list_des = [3,1,5,2,4]
list_rep = [6,4,3,3,2,1]

def insertionsort(lista):
    for index in range(1, len(lista)):
        temp = lista[index]
        index_before = index - 1
        while index_before >= 0 and temp < lista[index_before]:
            lista[index_before + 1] = lista[index_before]
            index_before -= 1
        
        lista[index_before + 1] = temp
    
    return lista

print(insertionsort(list_ord), insertionsort(list_inv), insertionsort(list_des),insertionsort(list_rep))


