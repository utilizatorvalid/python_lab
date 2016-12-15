import zipfile
import os
import random
import time


def is_zip(path):
    ext = path.split('.')[-1]
    return ext == 'zip'


def make_new_zip(folder, new_zip_path):
    z = zipfile.ZipFile(new_zip_path, 'w')
    for path, dir, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(path, file)
            random_token = ''.join([str(random.randint(0,9)) for i in range(5)])
            file_name, ext = os.path.basename(file_path).split('.')
            random_name = file_name +random_token +'.'+ ext
            random_path = os.sep.join(file_path.split(os.sep)[:-1]+ [random_name])
            z.write(file_path,random_path)


def recursive_unzip_file(zip_path, new_zip_path):
    if not os.path.isfile(zip_path):
        return
    if not is_zip(zip_path):
        raise Exception("path is not an zip file")
    z = zipfile.ZipFile(zip_path)
    temp_dir_path = os.path.join(new_zip_path)
    temp_dir_path = ''.join(temp_dir_path.split('.')[:-1])
    if not os.path.exists(temp_dir_path):
        os.mkdir(temp_dir_path)

    for i in z.infolist():
        z.extract(i.filename, temp_dir_path)
    make_new_zip(temp_dir_path, new_zip_path)
    z.close()


# def rename_recursive()
if __name__ == "__main__":
    start_time = time.time()
    try:
        recursive_unzip_file(r'D:\Test2\subiect_5.zip', r'D:\Test2\subiect_5_new.zip')
    except:
        print('broblem')
    seconds = time.time()-start_time
    print("Time passed %.2f" % (seconds))
    # args = sys.argv
    # if len(args)<3:
    #     raise Exception("Need more arguments")
    # zip1 = args[1]
    # zip2 = args[2]
    # recursive_unzip_file(zip1, zip2)
