
def reverseArray(list):
    newlist = []
    for i in range(1, len(list) + 1):
        newlist.append(list[-i])
    return newlist


# testlist=[1, 2, 3, 4, 5, 6]
# print(reverseArray(testlist))
