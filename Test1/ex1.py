def ascii_sum(s):
    # return sum([ord(s[i]) for i in range(1, len(s), 2)])
    new_list = []
    for i in range(len(s)):
        if i % 2 == 1:
            new_list.append(ord(s[i]))
    print(new_list)

    return sum(new_list)


if __name__ == "__main__":
    # print(ascii_sum('Hello-world'))
    print(ascii_sum("Hello-world"))
    pass
