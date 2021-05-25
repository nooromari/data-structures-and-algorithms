def multi_bracket_validation(input):
    """
    function should take a string as its only argument, and should return a boolean representing whether or not
    the brackets in the string are balanced. 
    """
    opening=['(','[','{']
    closing=[')',']','}']
    check_list = []
    for i in input:
        if i in opening:
            check_list.append(i)
        elif i in closing:
            pos = closing.index(i)
            if ((len(check_list) > 0) and
                (opening[pos] == check_list[len(check_list)-1])):
                check_list.pop()
            else:
                return  False
    if len(check_list) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(multi_bracket_validation('[Extra Characters'))