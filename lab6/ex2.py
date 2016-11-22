# 2. Sa se scrie o functie care primeste ca parametru un sir de caractere regex, un sir de caractere text si un numar
# intreg x si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.

import re


def find(regex, text, x):
    r = re.compile(regex)
    return list(filter(lambda word: x >= len(word) > 0, r.findall(text)))


if __name__=="__main__":
    print(find('\d+', "123 12 3456", 3))