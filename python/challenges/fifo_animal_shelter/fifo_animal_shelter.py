class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ Add an item to the rear fo the queue """
        node = Node(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def dequeue(self):
        """ removed an item to the front fo the queue """
        try:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        except Exception:
            return "the queue is empty"
            
    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        list_data = ""
        current = self.front
        while current:
            list_data += f"{current.value} -> "
            current = current.next
        list_data += "NULL"
        return list_data

class Dog:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = "dog"

class Cat:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = "cat"

class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, pet):
        """
        adds animal to the shelter. animal can be either a dog or a cat object.
        """
        if pet.type == "cat":
            self.cat.enqueue(pet.name)
        elif pet.type == "dog":
            self.dog.enqueue(pet.name)
        else:
            return "only cats and dogs"

    def dequeue(self, pref):
        """
        returns either a dog or a cat. If pref is not "dog" or "cat" then return null.
        """
        try:
            if pref == "cat":
                self.cat.dequeue()
                return "cat"
            if pref == "dog":
                self.dog.dequeue()
                return "dog"
        except:
            return None



if __name__ == "__main__":
    # dog1 = Dog("bobi")
    # dog2 = Dog("lulu")
    # cat1 = Cat("kitty")
    # cat2 = Cat("lucy")
    animal_sh = AnimalShelter()
    # animal_sh.enqueue(dog2)
    # animal_sh.enqueue(dog1)
    # animal_sh.enqueue(cat1)
    # animal_sh.enqueue(cat2)
    # print(animal_sh.cat)
    # print(animal_sh.dequeue("cat"))
    # print(animal_sh.cat)
    # print(animal_sh.dog)
    # # print(animal_sh.dequeue("dog"))


