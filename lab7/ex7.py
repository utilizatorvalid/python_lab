# 7. Sa se simuleze extragerea 6/49.
import random


def extract_6(elements):
    print("list is:", elements)
    chosen = []
    for iteration in range(6):
        random.shuffle(elements)
        chosen.append(elements.pop())
    print("The chosen x are:", chosen)


if __name__ == "__main__":
    l = [x for x in range(49)]
    extract_6(l)
