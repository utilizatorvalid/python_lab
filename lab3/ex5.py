# Scrieti un script care primeste 2 parametri de la consola reprezentand un path catre un director de pe sistem
# si un nume de fisier. Scriptul va parcurge recursiv structura de fisiere si directoare din directorul
# dat ca parametru, utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a
# parcurs si tipul acestuia (FILE, DIRECTORY, UNKNOWN), separate de |. Fiecare path va fi scris pe cate o linie.

import os


def parse_and_write(path, filename):
    paths = []

    for path, dirs, files in os.walk(path):
        for file in files:
            paths.append("{f} | {d} | {type}".format(f=file,d=path,type=file.split('.')[-1]))

    with open(filename, 'wt') as file:
        file.writelines("\n".join(paths))



if __name__ == "__main__":
    parse_and_write("D:\Laboratories_python",'walk_result.txt')
