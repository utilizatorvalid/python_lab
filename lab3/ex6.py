# 6. Scrieti un script care primeste 3 parametri de la consola.
# Primul va fi un path catre un fisier, al doilea un path catre
# un director iar al treilea va fi dimensiunea unui buffer.
# Scriptul va copia fisierul dat ca parametru in directorul dat ca parametru,
# utilizand un buffer de marimea celui de-al treilea parametru, in bytes.

import os


def copy_file(file_path, dir_path, buffer=4096):
    if not os.path.isfile(file_path):
        raise Exception("inexistent file")
        # return False
    if not os.path.isdir(dir_path):
        raise Exception("inexistent dir for copy")
        # return False
    new_file_path = os.path.join(dir_path, file_path.split(os.path.sep)[-1])
    with open(file_path, 'rt') as file_from, open(new_file_path, "wt") as file_to:
        content = file_from.read(buffer)
        while content:
            file_to.write(content)
            content = file_from.read(buffer)

if __name__ == "__main__":
    file_path = input("file to copy >>")
    dir_path = input('dir copy to >>')
    copy_file(file_path, dir_path)
