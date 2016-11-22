def word_count(string):
    count = 0
    word_len = 0
    for char in string:
        if (char in ',;, ? !.') and (word_len > 0):
            word_len = 0
            count += 1
        else:
            word_len += 1
    return count


if __name__ == "__main__":
    print(word_count('Vasile are mere. Merele sunt gustoase!'))
