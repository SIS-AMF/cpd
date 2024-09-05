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

def main():
    arr = [1,5,3,7,87,98,4,6,4,5,76,23,45,6,7,4,54,6,43,45,42,45,6,6,4]
    insertion_sort(arr)
    print(arr)

main()