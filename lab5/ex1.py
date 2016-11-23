# Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
# a) a-b
# b) a+b
# c) a/b
# d) a*b


def op(a, b):
    try:
        print('{op1}-{op2}={rez}'.format(op1=a,
                                         op2=b,
                                         rez=a - b
                                         ))
    except ArithmeticError as e:
        print('ArithmeticError on - operation')

    try:
        print('{op1}+{op2}={rez}'.format(op1=a,
                                         op2=b,
                                         rez=a + b
                                         ))
    except ArithmeticError:
        print('ArithmeticError on + operation')
        raise

    try:
        print('{op1}/{op2}={rez}'.format(op1=a,
                                         op2=b,
                                         rez=a / b
                                         ))
    except ArithmeticError:
        print('ArithmeticError on / operation')
        raise

    try:
        print('{op1}*{op2}={rez}'.format(op1=a,
                                         op2=b,
                                         rez=a * b
                                         ))
    except ArithmeticError:
        print('ArithmeticError on - operation')
        raise


if __name__ == "__main__":
    op(1, 2)
    # op(1, 0)
    op('alfa', 5)
