
def func(list_a, list_b):
    '''
    Function returns
    :param list_a:
    :param list_b:
    :return: list_a and list_b, list_a or list_b, list_a - list_b, list_b - list_a
    '''

    def remove_dublicates(numbers):
        new_list = []
        for number in numbers:
            if number not in new_list:
                new_list.append(number)
        return new_list

    list_a = remove_dublicates(list_a)
    list_b = remove_dublicates(list_b)
    a_and_b = [x for x in list_a if x in list_b]
    a_or_b = remove_dublicates(list_a+list_b)
    a_minus_b = [x for x in list_a if x not in list_b]
    b_minus_a = [x for x in list_b if x not in list_a]

    return a_and_b, a_or_b, a_minus_b, b_minus_a


print(func([1, 2, 3, 1], [1, 2, 6]))
