def get_functions_consts(params):
    def remove_dublicates(numbers):
        new_list = []
        for number in numbers:
            if number not in new_list:
                new_list.append(number)
        return new_list

    def compute_equation(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        try:
            return (float(y2) - y1) / (float(x2) - x1)
        except ZeroDivisionError:
            # line is vertical
            return None

    params = remove_dublicates(params)

    for i in range(0, len(params)):
        for j in range(i + 1, len(params)):
            compute_equation(params[i], params[j])


get_functions_consts([(1, 1), (1, 1), (2, 3), (3, 4), (6, 10)])
