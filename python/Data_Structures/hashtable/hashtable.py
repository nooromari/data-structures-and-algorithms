from ..linked_list.linked_list import LinkedList


class Hashmap:

    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size


    def _hash(self, key):
        """
        takes in an arbitrary key and returns an index in the collection.
        """
        sum = 0
        for char in key:
            sum += ord(char)
        hashed_key = (sum *13)% self.size
        return hashed_key


    def add(self, key, value):
        """
        takes in both the key and value hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        hashed_key = self._hash(key)
        if self.contains(key):
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0]:
                    current.data[1] =  value
                    return self
                current = current.next
                
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].append([ key, value])
        return self

    def get(self, key):
        """
        takes in the key and returns the value from the table.
        """
        hashed_key = self._hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0]:
                    return current.data[1]
                current = current.next
        # return None

    def contains(self, key):
        """
        takes in the key and returns a boolean, indicating if the key exists in the table already.
        """
        hashed_key = self._hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0]:
                    return True
                current = current.next
        return False

    def __str__(self):
        """
        return the content of the table as string
        """
        output = []
        for i in self.map:
            if i:
                current = i.head
                while current:
                    output.append(f"{current.data[0]}: {current.data[1]}")
                    current = current.next
        string_hashmap = ' -> '.join(output)
        return string_hashmap

    def __iter__(self):
        """
        iter throw the keys in the hashmap
        """
        for x in self.map:
            if x:
                current = x.head
                while current:
                    yield current.data[0]
                    current = current.next


if __name__ == "__main__":
    hashmap = Hashmap(2)
    hashmap.add('Noura',24)
    hashmap.add('Noor',23)
    hashmap.add('Tala',25)
    hashmap.add('Manar', 26)
    print(hashmap)
    print(hashmap.get('noor'))
    print(hashmap.get('Tala'))
    print(hashmap.contains('lolo'))
    print(hashmap.contains('Manar'))


