def quickSort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quickSort(arr, left, position - 1)
        quickSort(arr, position + 1, right)

    return arr

def partition(arr, left, right):
    pivot = arr[right]
    print('pivot', pivot)

    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)
    return low + 1

def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    print('arr swap', arr)



if __name__ =="__main__":
    arr = [8,4,23,42,16,15]
    n = len(arr)
    print(quickSort(arr, 0, n-1))
