# 6. Sa se scrie un script care afiseaza in ce zi a saptamanii este anul nou,
# pentru ultimii x ani (x este dat ca argument).
import time


def new_year_day(x):
    w = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    time_obj = time.localtime()
    this_year = time_obj.tm_year
    print(this_year)
    for x in range(x):
        year = this_year - x
        new_time_obj = time.strptime("31-12-{y}".format(y=year), "%d-%m-%Y")
        day_of_week = w[new_time_obj.tm_wday]
        print("New year for ", year, '->', day_of_week)

    pass


if __name__ == "__main__":
    new_year_day(5)
