def comb(vector, k):
    '''

    :param vector:list of elements
    :param k: combinations  din n luate cate k
    :return:
    '''
    import itertools
    return list(itertools.combinations(vector,k))

print(comb([1, 2, 3, 4], 3))
