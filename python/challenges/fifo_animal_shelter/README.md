# Challenge Summary
<!-- Description of the challenge -->

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
- enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
- dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![fifo-animal-shelter](../assets/fifo-animal-shelter.jpg)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O
- time :O(1)
- space: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->

1. creat new inectance from `AnimalShelter` class.
```
animal_shelter = AnimalShelter()
```

2. create inectace for each cat:
```
    cat1 = Cat("kitty")
    cat2 = Cat("lucy")
```

3. add the cats to the shelter:
```
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(cat2)
```

4. to see the cats added:
```
    print(animal_sh.cat)
```

- output: `kitty -> lucy -> NULL`


5. to delete the first cat:
```
    print(animal_shelter.dequeue("cat"))
```

- output: `cat`

*the same steps for the dog*