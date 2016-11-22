def combine_dicts(d1, d2):
    result_dict = {}
    keys_d1 = set(d1.keys())
    keys_d2 = set(d2.keys())
    sim_dif = keys_d1.symmetric_difference(keys_d2)
    intersection = keys_d1.intersection(keys_d2)
    for key in sim_dif:
        val = d1.get(key, None)
        if val is None:
            val = d2.get(key, None)
        result_dict[key] = val
    for key in intersection:
        val = d1[key] + d2[key]
        result_dict[key] = val
    return result_dict


if __name__ == "__main__":
    print(combine_dicts(d1={1: "a", 2: 'b'}, d2={1: 'x', "y": "y"}))
    print(combine_dicts(d1={1: "​a​", 2: "​b​"}, d2={1: "​x​", "y":"y"}))
    pass
