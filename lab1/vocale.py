def count_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiou':
            count += 1
    return count


if __name__ == '__main__':
    print(count_vowels("Vasile are mere"))
