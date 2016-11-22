# Scrieti o functie care primeste ca parametru un nume de fisier.
# Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar,
# sub forma cheie [tab] valoare.

import os


def mk_osfenv(filename):
    lines = []
    for key, value in os.environ.items():
        lines.append('{cheie}   {valoare}\n'.format(cheie=key, valoare=value))
    with open(filename, 'wt') as file:
        file.writelines(lines)


if __name__ == "__main__":
    mk_osfenv("os_env.txt")
