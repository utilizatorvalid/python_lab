def gcd(a, b):
    if b == 0:
        return a
    return (b, a%b)


def cmmdc_arg(*params):
    cmmdc = params[0]
    for number in params:
        cmmdc = gcd(cmmdc, number)
    return cmmdc


if __name__ == "__main__":
    print(cmmdc_arg(12, 30, 60))
    # CMMDC(1,2,3,5)
