'''
4. Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date despre
    toate fisierele din acel director. Pentru fiecare fisier vor fi afisate urmatoarele
informatii:
    nume_fisier,
    md5_fisier,
    sha256_fisier,
    size_fisier (in bytes),
    cand a fost creat fisierul (in format human-readable)
    calea absoluta catre fisier.
'''

import os


def get_dictionary_for_file(filePath):
    print("collecting data for:", filePath)
    pass


def get_dir_info(path):
    if not os.path.isdir(path):
        return
    list_files = []
    for path, dirs, files in os.walk(path):
        for file in files:
            get_dictionary_for_file(os.path.join(path, file))
    pass


if __name__ == "__main__":
    get_dir_info(r'D:\Laboratories_python\lab7')
