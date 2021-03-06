# Sa se scrie o functie care parcurge recursiv un director si afiseaza acele fisiere a caror nume face match pe o
# expresie regulata data ca parametru sau contine un sir de caractere care face match pe aceeasi expresie.
# Fisierele care satisfac ambele conditii vor fi afisate prefixate cu ">>"


import re
import os


def recursive_matching(path, regex, r=None):
    if r is None:
        r = re.compile(regex)

    for path, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.sep.join([path, file])
            content_match = False
            file_name_match = False
            if r.match(file):
                file_name_match = True
            with open(file_path, 'rt') as f:
                try:
                    file_content = f.read()
                    # file_content.decode('ascii')
                    # print(file_content)
                    match_obj = r.search(file_content)
                    if match_obj:
                        content_match = True
                except Exception as e:
                    pass
                    # raise Exception("can't open or read file : " + os.path.sep.join([path, file]), e)
            if content_match and file_name_match:
                print('>>   ' + file_path)
            elif content_match or file_name_match:
                print(file_path)


if __name__ == "__main__":
    recursive_matching(r'D:\Laboratories_python', 'ex\d')
