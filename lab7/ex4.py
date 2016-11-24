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
import hashlib
import json
import time
from ex3 import get_file_SHA


def get_file_md5(file_path):
    try:
        m = hashlib.md5()
        f = open(file_path, 'rb')
        while True:
            data = f.read(4096)
            if len(data) == 0:
                break
            m.update(data)
        f.close()
        # print(m.hexdigest())
        return m.hexdigest()
    except Exception as e:
        print(e)
        return ''


def get_dictionary_for_file(filePath):
    print("collecting data for:", filePath)
    dict = {}
    dict['nume_fisier'] = filePath.split(os.sep)[-1]
    dict['sha256_fisier'] = get_file_SHA(filePath, type_sha=256)
    dict['md5_fisier'] = get_file_md5(filePath)
    dict['size_fisier'] = os.path.getsize(filePath)
    dict['data_creare'] = time.asctime(time.localtime(os.path.getctime(filePath)))
    dict['cale_abs'] = os.path.abspath(filePath)
    return dict


def get_dir_info(path):
    d = {}
    if not os.path.isdir(path):
        return
    with open("ex4serialisation.json", 'wt') as f:
        list_files = []
        for path, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)
                d[file_path] = get_dictionary_for_file(file_path)
        s = json.dumps(d, indent=4, sort_keys=True)
        f.write(s + '\n')



if __name__ == "__main__":
    get_dir_info(r'D:\Laboratories_python\lab7')
