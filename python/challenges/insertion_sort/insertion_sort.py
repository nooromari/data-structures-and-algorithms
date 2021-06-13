def InsertionSort(arr):

    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]
        
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp

    return arr


if __name__ == '__main__':

    arr = [8,4,23,42,16,15]
    print(InsertionSort(arr))