def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
 
        left = arr[:mid]
        right = arr[mid:]
 
        mergeSort(left)
        mergeSort(right)

        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
            
        k = k + 1

    if i == len(left):
            for item in right[j:]:
                arr[k] = item
                k += 1
    else:
        for item in left[i:]:
            arr[k] = item
            k += 1

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(mergeSort(arr))
    print("Sorted array is: ", end="\n")
 
