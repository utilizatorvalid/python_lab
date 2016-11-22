def get_n_fib(n):
    '''
    Function return list with first n numbers from fibonacci sequence
    :param n: int
    :return: list [0,1,1,2...]
    '''
    if n <= 0:
        return None
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        list = [0, 1]
        for i in range(2, n):
            list.append(list[i - 2] + list[i - 1])
    return list


if __name__ == "__main__":
    print(get_n_fib(100))
