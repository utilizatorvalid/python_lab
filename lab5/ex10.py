# 10. Sa se scrie o functie search_by_content care primeste ca parametru doua siruri de caractere target si to_search
# si returneaza o lista de fisiere care contin to_search. Fisierele se vor cauta astfel:
#   daca target este un fisier, se cauta doar in fisierul respectiv iar daca este un
#   director se va cauta recursiv in toate fisierele din acel director. Daca target nu este nici fisier nici director,
# se va arunca o exceptie de tipul ValueError cu un mesaj corespunzator.

import os


def serach_by_content(target, to_search):
    matched_files = []
    if os.path.isfile(target):
        print('path', target, ' are file')
        with open(target, 'rt') as f:
            content = ''
            try:
                content = f.read()
            except:
                pass
            if content.__contains__(to_search):
                matched_files.append(target)
    elif os.path.isdir(target):
        print('path', target, ' are directory')
        for path, dirs, files in os.walk(target):
            for file in files:
                content = ''
                file_path = os.path.join(path, file)
                with open(file_path) as f:
                    try:
                        content = f.read()
                    except:
                        pass
                    if content.__contains__(to_search):
                        matched_files.append(file_path)

    else:
        raise(ValueError,'There is not such file or directory')
    return matched_files


if __name__ == "__main__":
    require_os = serach_by_content(r'D:\Laboratoxxries_python\lab5', 'import os')
    print("FILES:")
    print(require_os)
