# 2. Scrieti doua functii de verificare daca un numar
# este prim, si verificati care dintre ele este mai
# eficienta din punct de vedere al timpului.


import time


def ctime_millis():
    """:returns: Current time in milliseconds."""
    return int(round(time.time() * 1000))


def nice_time(millis):
    """:returns: Nice displaying of time."""
    return "{m} mins, {s} seconds, {mm} millis".format(
        m=str(millis // 1000 // 60),
        s=str(millis // 1000 % 60),
        mm=str(millis % 1000))


def running_time_function(function, *args):
    start_time = time.time()
    print("Start Function...")
    function(args[0])
    print("Finish Function")
    running_time = time.time() - start_time
    print("Running time is:{time}".format(time=nice_time(running_time * 1000)))
    return running_time


def is_prime1(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    print("Numarul {nr} este prim: {prime}".format(nr=number, prime=str(is_prime)))
    return is_prime


def is_prime2(number):
    is_prime = False
    for x in range(2, int(number ** 1 / 2)):
        if number % x == 0:
            is_prime = False
    print("Numarul {nr} este prim: {prime}".format(nr=number, prime=str(is_prime)))
    return is_prime


if __name__ == "__main__":
    running_time_function(is_prime1, 99957)

    running_time_function(is_prime2, 99957)
