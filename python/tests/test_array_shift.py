from challenges.array_shift.array_shift import insertShiftArray


def test_insertShiftArray():
    input_list = [2, 4, 6, 8]
    input_n = 5
    expected = [2, 4, 5, 6, 8]
    actual = insertShiftArray(input_list, input_n)
    assert actual == expected


def test_insertShiftArray2():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertShiftArray([4, 8, 15, 23, 42], 16)
    assert actual == expected
