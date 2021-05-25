from challenges.multi_bracket_validation.multi_bracket_validation import *

def test_multi_bracket_validation():
    test_array=['{}','{}(){}','()[[Extra Characters]]','(){}[[]]','{}{Code}[Fellows]','(())','[({}]','(](','{(})','{',')','{]','string without bracket']
    expected=[True,True,True,True,True,True,False,False,False,False,False,False,True]
    actual=[multi_bracket_validation(string) for string in test_array]
    assert actual == expected