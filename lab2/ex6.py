def check(x, *params):
    '''

    :param params:
    :param x:
    :return:
    '''
    big_list = []
    for list in params:
        big_list += list
    new_list = []

    for element in big_list:
        if (big_list.count(element) == x) and (element not in new_list):
            new_list.append(element)
    return new_list


print(check(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
