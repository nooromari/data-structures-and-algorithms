from Data_Structures.hashtable.hashtable import Hashmap
import pytest


def test_hashmap_get(hashmap):
    keys = ['Lara', 'Noor', 'Tala', 'Manar']
    expected = [None, 23, 25, 26]
    actual = [hashmap.get(key) for key in keys]
    assert expected == actual

def test_hashmap_contains(hashmap):
    keys = ['Noura', 'Tala', 'Lara', 'Manar']
    expected = [True, True, False, True]
    actual = [hashmap.contains(key) for key in keys]
    assert expected == actual
    actual = str(hashmap)
    expected = 'Noor: 23 -> Manar: 26 -> Noura: 24 -> Tala: 25'
    assert actual == expected

def test_hashmap_collision(hash_map):
    actual = str(hash_map)
    expected = 'Noor: 23 -> Tala: 25 -> Noura: 24 -> Manar: 26'
    assert actual == expected
    keys = ['Lara', 'Noor', 'Tala', 'Manar']
    expected = [None, 23, 25, 26]
    actual = [hash_map.get(key) for key in keys]
    assert actual == expected


@pytest.fixture
def hashmap():
    hashmap = Hashmap()
    hashmap.add('Noura',24)
    hashmap.add('Noor',23)
    hashmap.add('Tala',25)
    hashmap.add('Manar', 26)
    return hashmap

@pytest.fixture
def hash_map():
    hashmap = Hashmap(2)
    hashmap.add('Noura',24)
    hashmap.add('Noor',23)
    hashmap.add('Tala',25)
    hashmap.add('Manar', 26)
    return hashmap