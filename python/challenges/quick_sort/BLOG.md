# Quick Sort

## Pseudo Code

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Trace

- Sample Array: [8,4,23,42,16,15]

- *Pass 1:*
    - pivot 15

    if  8  <=  15 True

        - before swep : [8, 4, 23, 42, 16, 15] 
        - swep between arr[0] = 8 and arr[0] = 8
        - after swap [8, 4, 23, 42, 16, 15]

    if  4  <=  15 True

        - before swep : [8, 4, 23, 42, 16, 15] 
        - swep between arr[1] = 4 and arr[1] = 4
        - after swap [8, 4, 23, 42, 16, 15]

    if  23  <=  15 False

    if  42  <=  15 False

    if  16  <=  15 False


    - before swep : [8, 4, 23, 42, 16, 15] 
    - swep between arr[5] = 15 and arr[2] = 23
    - after swap [8, 4, 15, 42, 16, 23]

- *Pass 2:*
    - pivot 4

    if  8  <=  4 False

        - before swep : [8, 4, 15, 42, 16, 23] 
        - swep between arr[1] = 4 and arr[0] = 8
        - after swap [4, 8, 15, 42, 16, 23]

- *Pass 3:*
    - pivot 23

    if  42  <=  23 False

    if  16  <=  23 True

        - before swep : [4, 8, 15, 42, 16, 23] 
        - swep between arr[4] = 16 and arr[3] = 42
        - after swap [4, 8, 15, 16, 42, 23]

    - before swep : [4, 8, 15, 16, 42, 23] 
    - swep between arr[5] = 23 and arr[4] = 42
    - after swap [4, 8, 15, 16, 23, 42]

- **Result:** [4, 8, 15, 16, 23, 42]