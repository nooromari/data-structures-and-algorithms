def business_trip(gragh, cities):
    """  """
    cost = 0
    flag = False

    for i in range(len(cities)-1):
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
    return flag, str(cost)+'$'