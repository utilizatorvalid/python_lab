# 9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem:
# versiunea de python folosita. Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ==="
# iar daca se foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
# numele user-ului care a executat scriptul,
# path-ul complet al scriptului.
# path-ul directorului in care se afla scriptul,
# tipul sistemului de operare,
# numarul de core-uri,
# # directoarele din PATH-ul procesului cate unul pe linie,

import sys
import os


def print_general_info():
    if sys.version.index('2') == 0:
        print('=== Python 2 ===')
    elif sys.version.index('3') == 0:
        print('Running under Py3')
    print("User: {user}".format(user=os.getlogin()))
    print("Script location: {loc}".format(loc=os.path.abspath(__file__)))
    path = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
    print("Script dir: {dir}".format(dir = path))
    print("OS: {type_os}".format(type_os=sys.platform))
    print("NrCores: {nr_core}".format(nr_core=os.environ["NUMBER_OF_PROCESSORS"]))

    directories = [element for element in os.listdir(path) if os.path.isdir(element)]
    print("Directories are:\n",'\n'.join(directories))
    pass


if __name__ == "__main__":
    print_general_info()
