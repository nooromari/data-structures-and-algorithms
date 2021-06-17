from challenges.quick_sort.quick_sort import *

def test_sort():
    input = [[8,4,23,42,16,15], [20,18,12,8,5,-2] , [5,12,7,5,5,7] , [2,3,5,7,13,11]]
    actual = [ quickSort(arr, 0, len(arr)-1) for arr in input]
    expected = [[4, 8, 15, 16, 23, 42] , [-2, 5, 8, 12, 18, 20] , [5, 5, 5, 7, 7, 12] , [2, 3, 5, 7, 11, 13]]
    assert actual == expected