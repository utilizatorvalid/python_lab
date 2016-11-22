# Scrieti un script care primeste ca parametru de la linia de comanda un path si afiseaza primii 4096 bytes
# daca path-ul duce la un fisier, intrarile din acesta daca path-ul reprezinta un director si un mesaj de eroare
# daca path-ul nu este unul valid.

import os


def first_4096():
    print('give us a path :)')
    path = input()
    try:
        with open(path, 'rt') as file:
            print(file.read(4096))
    except IOError as e:
        print('File couldn\'t be read, or this isn\'t a file')
        if os.path.isdir(path):
            print("Yeah this is an directory here is this content :D")
            print(os.listdir(path))
        raise Exception("Test", e)

if __name__ == "__main__":
    first_4096()
