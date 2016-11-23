# 11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de caractere care reprezinta calea
#  catre un fisier si returneaza un dictionar cu urmatoarele campuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read si can_write = True/False daca se poate citi din/scrie in fisier.

import os


def get_file_info(file_path):
    if not os.path.isfile(file_path):
        return None
    file_info={}
    file_info["full_path"] = os.path.abspath(file_path)
    if len(file_path.split('.'))>1:
        ext = file_path.split('.')[-1]
    else:
        ext = ''
    file_info['file_extension'] = ext
    file_info["file_size"] = os.path.getsize(file_path)
    file_info['car_read'] = os.access(file_path, os.R_OK)
    file_info['car_write'] = os.access(file_path, os.W_OK)
    return file_info

if __name__=="__main__":
    print(get_file_info(r'D:\Laboratories_python\lab5\test\file0'))