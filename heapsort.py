def heapify(array, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and array[largest] < array[left]:
        largest = left

    if right < size and array[largest] < array[right]:
        largest = right

    if largest != index:
        aux = array[index]
        array[index] = array[largest]
        array[largest] = aux

        heapify(array, size, largest)

def heapSort(array):
    size = len(array)

    for i in range(size, -1, -1):
        heapify(array, size, i)

    for i in range(size - 1, 0, - 1):
        aux = array[i]
        array[i] = array[0]
        array[0] = aux
        heapify(array, i, 0)

arr = [28, 25, 26, 48, 1, 2, 6, 20, 20] 
heapSort(arr)
print(arr)