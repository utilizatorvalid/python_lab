# lab1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_args(*arg):
    gcd_v = arg[0]
    for element in arg:
        gcd_v = gcd(element,gcd_v)
    return gcd_v

if __name__ == "__main__":
        print(gcd_args(15, 35, 3))
