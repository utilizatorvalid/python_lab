# Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza cuvintele care incep si se termina cu vocale.
#  Prin cenzurare se intelege inlocuirea caracterelor de pe pozitii impare cu caracterul * .

import re


def cens(s):
    word = s.group()
    if word[0] in "aeiouAEIOU" and word[-1] in "aeiouAEIOU":
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 1:
                new_word += '*'
            else:
                new_word += word[i]
    else:
        new_word = word

    return new_word


def censore_test(text):
    r = re.compile('\w+')
    censored = r.sub(cens, text)
    return censored
    pass


if __name__ == "__main__":
    t = censore_test("Ana are mere")
    print(t)
