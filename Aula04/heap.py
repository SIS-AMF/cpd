
def troca(arr, root, child):
    temp = arr[root]
    root[root] = arr[child]
    arr[child] = temp

def core(arr, index):
    if index == 0:
        return arr
    else:
        if arr[index] > arr[index * 2 + 1] and arr[index * 2 + 1] > arr[index * 2 + 2]:
            troca(arr, arr[index], arr[index * 2 + 1])
            if len(arr)/2-1 < index * 2 + 1:
                core(arr, index * 2 + 1)
        elif arr[index] < arr[index * 2 + 2] and arr[index * 2 + 2] > arr[index * 2 + 1]:
            troca(arr, arr[index], arr[index * 2 + 2])
            if len(arr)/2-1 < arr[index * 2 + 2]:
                core(arr, arr[index * 2 + 2])
        core(arr, index -1)


arr = [1,4,2,3,9,7,8,10,14,16]
tam = int(len(arr)/2-1)

core(arr, 4)