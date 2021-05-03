def insertShiftArray(list,n):
    x = list
    x[int(len(list)/2): int(len(list)/2)] = [n]
    return x

print(insertShiftArray([1,2,3],8))