
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
    arr = [24,14,29,4,18,24,24,13,13]
    selection_sort(arr)
    print(arr)

main()