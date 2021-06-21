from Data_Structures.hashtable.hashtable import Hashmap

def repeated_word(str):
    """
    Take a text and return the first repeated word
    """
    splitted_str = split_str(str)
    hashmap = Hashmap()
    for s in splitted_str:
        lower_word = s.lower()
        if hashmap.contains(lower_word):
            return lower_word
        hashmap.add(lower_word,1)


def split_str(str):
    """
    Split the text to a list of words
    """
    str = str.replace(',','')
    list_str = str.split(' ')
    return list_str


if __name__ == '__main__':
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))