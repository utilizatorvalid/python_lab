def sort_tuples(s):
    return list(sorted(s, key=lambda point: ((point[0] - 0) ** 2 + (point[1] - 0) ** 2) ** 0.5))


if __name__ == "__main__":
    print(sort_tuples(s={(1, 1), (10, 10), (-1, 1)}))
    pass
