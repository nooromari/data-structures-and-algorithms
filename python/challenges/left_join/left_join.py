from Data_Structures.hashtable.hashtable import Hashmap

def left_join(hash_left,hash_right):
    """
    returns all the values from the left table, plus matched values from the right table or 'None' in case of no matching join predicate.
    """
    result_hash = Hashmap()
    for key in hash_left :
        result_hash.add(key, [hash_left.get(key),hash_right.get(key)])
    
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