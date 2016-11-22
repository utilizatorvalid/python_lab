# '''Sa se scrie o functie care primeste ca parametri un numar x default egal cu 1,
# un numar variabil de siruri de caractere si un flag boolean setat default pe True.
# Pentru fiecare sir de caractere, sa se genereze o lista care sa contina caracterele care au codul ASCII divizibil cu x
#  in caz ca flag-ul este setat pe True, in caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x.
#  Exemplu: x=2, "test", "hello", "lab002", flag=False va returna (["e", "s"], ["e", "o"], ["a"]).
#  Atentie: functia trebuie sa returneze un numar variabil de liste care sa corespunda cu numarul de siruri de caractere
#  primite ca input.'''

def filter_strings(*params, x=1, flag=True):
    def is_good(char, x, flag):
        if flag:
            return ord(char) % x == 0
        else:
            return ord(char) % x != 0

    lists = []
    for string in params:
        list = []
        for char in string:
            if is_good(char, x, flag):
                list.append(char)
        lists.append(list)
    return lists


if __name__=="__main__":
    print(filter_strings("test", "hello", "lab002", x=2, flag=False))
