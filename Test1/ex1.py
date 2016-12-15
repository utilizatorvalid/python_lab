import sys
import os
import json
import time


def genereaza_dictionar(path):
    print("Generating info for {p}".format(p=path))
    if not os.path.exists(path):
        return None
    big_d = {}
    d_info = {}

    d_info['path'] = os.path.abspath(path)
    d_info['last_modified_time'] = os.path.getmtime(path)
    if os.path.isfile(path):
        d_info['specific'] = os.path.getsize(path)
    elif os.path.isdir(path):
        array_dict = []
        for element in os.listdir(path):
            child = os.path.join(path, element)
            d = None
            try:
                d = genereaza_dictionar(child)
            except Exception as e:
                print(e)
                d = None
            if d is not None:
                array_dict.append(d)

        d_info['specific'] = array_dict
    big_d[path] = d_info
    return big_d


def writejson(d):

    s = json.dumps(d,indent=4)
    with open("ser.json", 'wt') as f:
        f.write(s)


#
# def get_file_info(path):
#     d_info = {}
#     d_info['path'] = os.path.abspath(path)
#     d_info['last_modified_time'] = os.path.getmtime(path)
#     d_info['specific'] = os.path.getsize(path)
if __name__ == "__main__":
    args = sys.argv
    # if len(args) <= 1:
    #     raise Exception("No sufficient arguments/ file_name.py dir_name")

    # print(args[1])
    startime = time.time()
    # writejson(genereaza_dictionar(args[1]))
    writejson(genereaza_dictionar('E:'))
    seconds = time.time() - startime
    print("Time passed %.2f" % (seconds))
