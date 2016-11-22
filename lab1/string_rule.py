def string_rule(n, *args):
    if len(args) <= 1:
        return True
    a = args[0]
    b = args[1]
    if a[-n:] == b[0:n]:
        return string_rule(n, args[1:])
    else:
        return False


if __name__ == "__main__":
    print(string_rule(2, "vasile", 'lebada'))
