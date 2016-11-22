def extract_primes(param):
    '''
    Function returns primes numbers from given list
    :param list: list of numbers
    :return: list of prime nubers from initial list
    '''
    import math
    def is_prime(x):
        for i in range(2,math.floor(math.sqrt(x))):
            if x % i == 0:
                return False
        return True
    return [x for x in  param if is_prime(x)]
    primes = list(filter(is_prime,param))
    return primes
if __name__=="__main__":
    primes=extract_primes([1,4,5,19,28,30,119])
    print(primes)