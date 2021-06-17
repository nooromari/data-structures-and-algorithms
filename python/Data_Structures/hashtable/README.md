# Hashtables
<!-- Short summary or background information -->

**Hashtables** are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value. This is done through what we call a `hash`. A hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.

## Challenge
<!-- Description of the challenge -->
- Implement a Hashtable with the following methods:

    1. `add()`: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
    2. `get()`: takes in the key and returns the value from the table.
    3. `contains()`: takes in the key and returns a boolean, indicating if the key exists in the table already.
    4. `hash()`: takes in an arbitrary key and returns an index in the collection.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The hash function takes a key and returns an integer. We use the integer to determine where the key/value pair should be placed in the array. The hash code is calculated in constant time and writing to an array at one index is O(1) so the hash map has O(1) access.

The hash code is used again to read something from the hash map. Take the key, run it through the hash code to get a number, use that number to index the array. Calculating the hash code and reading an array at that index is all constant time to the hash map has O(1) read access.


## API
<!-- Description of each method publicly available in each of your hashtable -->

- `add()`

    send the key to the hash method. Once you determine the index of where it should be placed, go to that index. Check if something exists at that index already, if it doesn’t, add it with the key/value pair. If something does exist, add the new key/value pair to the data structure within that bucket.

- `get()`

    The Find takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.

- `contains()`

    The Contains method will accept a key, and return a bool on if that key exists inside the hashtable. The best way to do this is to have the contains call the hash and check the hashtable if the key exists in the table given the index returned.

- `hash()`

    The hash will accept a key as a string, conduct the hash, and then return the index of the array where the key/value should be placed.