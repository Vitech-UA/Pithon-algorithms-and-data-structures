def partition(arr, first, last):
    i = (first - 1)
    reference = arr[last]

    for j in range(first, last):
        if arr[j] <= reference:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return (i + 1)


def quickSort(inputData, first, last):
    if len(inputData) == 1:
        return inputData

    if first < last:
        pi = partition(inputData, first, last)

        quickSort(inputData, first, pi - 1)
        quickSort(inputData, pi + 1, last)



inputArray = [10, 7, 8, 9, 1, 5]
quickSort(inputArray, 0, len(inputArray) - 1)
print("Sorted array is:")
for i in range(len(inputArray)):
   print("%d" % inputArray[i]),