def change(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def verify(arr, index):
    next_index = index + 1
    if arr[index] > arr[next_index]:
        change(arr, index, next_index)

def insertion_sort(arr):
    for index in range(len(arr) - 1):
        verify(arr, index)
        for sec_index in range(index -1,-1, -1):
            verify(arr, sec_index)
    print("=>", arr)
    return arr



def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        ##print(arr[:middle], arr[middle:])
        return insertion_sort(merge_sort(arr[:middle]) + merge_sort(arr[middle:]))
        
    else:
        return arr

def main():
    arr = [24,14,29,4,18,24,24,13,13,22]
    #arr = [10,9,8,9,8,7,6,5,4,3,2,1]
    teste = merge_sort(arr)

    print(arr)
    print(teste)

main()