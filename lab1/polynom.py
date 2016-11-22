# eval string
def eval_polynom(x, string):
    new_string = string[0] if string[0] is not 'x' else str(x)
    for i in range(1, len(string)):
        if string[i] == 'x':
            if string[i - 1].isdigit():
                new_string += '*' + str(x)
            else:
                new_string += str(x)
        else:
            new_string += string[i]
    new_string = new_string.replace("^", "**")
    return eval(new_string)


if __name__ == "__main__":
    print(eval_polynom(2, "3x^3 + 5x^2 - 2x - 5 + x"))
