import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % 2 == 0:
            return False
    return True


def findPrime(string):
    import re
    match = re.findall('\d+', string);
    if not match:
        return -1

    match = [int(x) for x in match]
    match.sort(reverse=True)

    for number in match:
        if is_prime(number):
            return number
    return -1


if __name__ == "__main__":
    print(findPrime('ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'))
