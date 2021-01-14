
def QuickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] # опорний елемент, 
                         # далі відберемо більші нього і менші елементи у 2 окремих массива
        less = [i for i in array[1:] if i <= pivot] # відбір елементів менших чисел
        
        greater = [i for i in array[1:] if i > pivot] # відбір елементів більших чисел
        
        return QuickSort(less) + [pivot] + QuickSort(greater)

print(QuickSort([10,12,3,9]))

