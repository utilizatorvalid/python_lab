def ceck_special_chars(string):
    special_chars = ['\r', '\t', '\n', '\a', '\b', '\f', '\v']
    for c in string:
        if c in special_chars:
            return True
    return False


if __name__ == '__main__':
    print(ceck_special_chars("Buna ziua\aS"))
