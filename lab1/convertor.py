def convertor(string):
    newstring = ''
    for char in string:
        if (char.isupper()) and (newstring == ''):
            newstring += char.lower()
        else:
            if (char.isupper()) and (newstring[len(newstring) - 1].isalnum()):
                newstring += "_" + char.lower()
            else:
                newstring += char.lower()
    return newstring

if __name__ == "__main__":
    print(convertor('Upper CamelCase'))
