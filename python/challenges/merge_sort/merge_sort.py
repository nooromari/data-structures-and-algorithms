def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
 
        left = arr[:mid]
        right = arr[mid:]
        print('left: ',left, 'right: ', right)
        mergeSort(left)
        mergeSort(right)

        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = j = k = 0
    # print('arr inside merge',arr, 'left  ',left, 'right', right)
    while i < len(left) and j < len(right):
        print(f'arr before: {arr}')
        print(f'i =',i,', j =',j,', k =',k)
        if left[i] <= right[j]:
            print(f"left[{i}] <= right[{j}] --> {left[i]} <= {right[j]}")
            arr[k] = left[i]
            print(f"arr[{k}] = {left[i]} --> arr: {arr}")
            i = i + 1
        else:
            print(f"left[{i}] > right[{j}] --> {left[i]} > {right[j]}")
            arr[k] = right[j]
            print(f"arr[{k}] = {right[i]} --> arr: {arr}")
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
    print('- merge ',arr)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(mergeSort(arr))
 
