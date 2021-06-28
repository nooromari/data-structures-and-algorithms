def business_trip(gragh, cities):
    """ return true if trip is possible with direct flights, and how much it would cost, otherwise return false. """
    cost = 0
    flag = True

    for i in range(len(cities)-1):
        if not flag:
            return False, '$0'
        neighbors = gragh.get_neighbors(cities[i])
        for neighbor in neighbors:
            if cities[i+1] == neighbor[0]:
                cost += neighbor[1]
                flag = True
                break
            else:
                flag = False
    if not flag :
        cost = 0
    return flag, '$'+str(cost)
