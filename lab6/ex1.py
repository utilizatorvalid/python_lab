# 1.Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru.
# Un cuvant este definit ca o secventa de caractere alfa-numerice.
import re


def get_words(string):
    r = re.compile('[\da-zA-Z]+')
    return r.findall(string)


if __name__ == "__main__":
    print(get_words("Vasile are 12 mere frumoase !!!"))
