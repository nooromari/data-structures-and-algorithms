from Data_Structures.hashtable.hashtable import Hashmap

def left_join(hash_left,hash_right):
    """
    returns all the values from the left table, plus matched values from the right table or 'None' in case of no matching join predicate.
    """
    result_hash = Hashmap()
    for key in hash_left.map :
        if key :
            result_hash.add(key.head.data[0], [key.head.data[1],None])
    for key in hash_right.map :
        if key :
            if result_hash.contains(key.head.data[0]):
                result_hash.add(key.head.data[0], [hash_left.get(key.head.data[0]),key.head.data[1]])
    
    return result_hash





if __name__ == "__main__":
    hash1 = Hashmap()
    hash1.add('Noor','student')
    hash1.add('Manar','student')
    hash1.add('Tala','student')
    hash1.add('Ahmad','TA')
    hash1.add('Farah','TA')

    hash2 = Hashmap()
    hash2.add('Noor','female')
    hash2.add('Manar','female')
    hash2.add('Omar','male')
    hash2.add('Ahmad','male')

    print(left_join(hash1, hash2))