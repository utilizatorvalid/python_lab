# 1. Scrieti un program care la fiecare x secunde unde x va fi aleator ales la fiecare iteratie (din intervalul [a, b] ,
# unde a, b sunt date ca argumente) afiseaza de cate minute ruleaza programul (in minute, cu doua zecimale).
# Programul va rula la infinit.

import time
import random


def running_time(a, b, start_time):
    while True:
        x = random.randint(a, b)
        time.sleep(x)
        print("Running time after {seconds} is:".format(seconds=x))
        time_sec = time.time() - start_time
        print("%.2f" % (time_sec / 60))


if __name__ == "__main__":
    start_time = time.time()
    running_time(3, 4, start_time)
