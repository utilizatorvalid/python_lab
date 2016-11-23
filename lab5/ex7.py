
import os
def dummy_tree(path, tree_depth, filesize, filecount, dircount):
    root_path = os.path.join(os.getcwd(), path)
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    for i in range(filecount):
        new_file = os.path.join(root_path, 'file' + str(i))
        if not os.path.exists(new_file):
            with open(new_file, 'wb') as file:
                file.write(b'a' * filesize)

    if tree_depth <= 1:
        return
    for i in range(dircount):
        new_path = os.path.join(root_path, 'dir' + str(i))
        if not os.path.exists(new_path):
            dummy_tree(new_path, tree_depth - 1, filesize, filecount, dircount)
