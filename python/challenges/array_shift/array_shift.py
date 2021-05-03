def insertShiftArray(list,n):
    """
    return an array with the new value
    added at the middle index.
    """
    if not len(list)%2:
       i = int(len(list)/2)
    else:
        i = int(len(list)/2)+1
    list[i: i] = [n]
    return list
