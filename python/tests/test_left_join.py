from challenges.left_join.left_join import left_join

from challenges.left_join.left_join import *
import pytest


def test_left_join(left_hash, right_hash):
    result_hash = left_join(left_hash, right_hash)
    actual = str(result_hash)
    expected = 'Ahmad: [\'TA\', \'male\'] -> Farah: [\'TA\', None] -> Noor: [\'student\', \'female\'] -> Manar: [\'student\', \'female\'] -> Tala: [\'student\', None]'
    assert actual == expected
    actual2 = result_hash.get('Noor')
    expected2 = ['student', 'female']
    assert actual2 == expected2
    actual3 = result_hash.get('Farah')
    expected3 = ['TA', None]
    assert actual3 == expected3


@pytest.fixture
def left_hash():
    hash1 = Hashmap()
    hash1.add('Noor','student')
    hash1.add('Manar','student')
    hash1.add('Tala','student')
    hash1.add('Ahmad','TA')
    hash1.add('Farah','TA')
    return hash1

@pytest.fixture
def right_hash():
    hash2 = Hashmap()
    hash2.add('Noor','female')
    hash2.add('Manar','female')
    hash2.add('Omar','male')
    hash2.add('Ahmad','male')
    return hash2

