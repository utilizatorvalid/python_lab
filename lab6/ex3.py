# Sa se scrie o functie care primeste ca parametru un sir de caractere text si o lista de expresii regulate si
# rurneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata daca ca parametru.

import re


def serach_for_expresion(text, *list_of_expresion):
    list_of_matchings= []
    compiled_expresions = [re.compile(exp) for exp in list_of_expresion]
    for r in compiled_expresions:
        if r.match(text):
            list_of_matchings.append(r.match(text).group())

    return list_of_matchings

if __name__=="__main__":
    list = serach_for_expresion("Python Course 30 course, PythonCourse", '\d+', '(Python)\s+(?=Course)')
    print(list)