# Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem,
# parcurge recursiv structura de fisiere si directoare pe care acesta le contine si afiseaza in consola toate path-urile
#  pe care le-a parcurs. NU aveti voie sa folositi os.walk.

import os


def parse_folder(path, depth=0):
    try:
        folder_content = os.listdir(path)
        for element in folder_content:
            element_path = os.path.join(path, element)
            print('     ' * depth + element_path)
            if os.path.isdir(element_path):
                parse_folder(element_path, depth + 1)

    except IOError as e:
        raise Exception("ParsingFolder Exception", e)


if __name__ == "__main__":
    parse_folder('D:\Laboratories_python')
    # parse_folder("")
