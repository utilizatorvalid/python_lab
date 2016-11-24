# 3. Gasiti toate fisierele duplicate dintr-un director dat
# ca argument si afisati timpul de rulare. Calea grupurilor
# de fisiere duplicate vor fi scrise intr-un fisier output.txt.

import hashlib
import os


def get_file_SHA(file_path, type_sha = 1):
    try:
        if type_sha ==1:
            m = hashlib.sha1()
        if type_sha ==256:
            m = hashlib.sha256()
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


def search_for_dublicates(directory):
    dict = {}
    if not os.path.isdir(directory):
        raise Exception("This is not an directory")

    for path, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(path, file)
            file_hash = get_file_SHA(file_path)
            h_files = dict.get(file_hash, [])
            h_files.append(file_path)
            dict[file_hash] = h_files
    return dict


def write_summary(dic):
    try:
        with open("output.txt", 'wt') as f:
            group = 0
            for key, value in dic.items():
                print(value)
                if len(value) > 1:
                    group += 1
                    f.write("Duplicate group{nr}\n".format(nr=group))
                    f.write("Hash: {h}\n\t".format(h=key))
                    f.write('\n\t'.join(value))
    except Exception as e:
        return ''

if __name__ == "__main__":
    dict = search_for_dublicates(r'D:\Laboratories_python\lab5')
    write_summary(dict)
    print(dict)
