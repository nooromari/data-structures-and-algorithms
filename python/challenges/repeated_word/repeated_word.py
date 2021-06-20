def repeated_word(str):
    splitted_str = split_str(str)
    new_list = []
    for s in splitted_str:
        print(s.lower())
        if s.lower() in new_list:
            return s
        new_list.append(s.lower()) 

def split_str(str):
    str = str.replace(',','')
    list_str = str.split(' ')
    return list_str


if __name__ == '__main__':
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))