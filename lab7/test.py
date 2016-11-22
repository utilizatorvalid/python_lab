import time

w = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("Time in seconds:", time.time())
print("Today :", time.ctime())
tmobj = time.localtime()
print("Year :", tmobj.tm_year)
print("Month :", tmobj.tm_mon)
print("Day :", tmobj.tm_mday)
print("Day of week :", w[tmobj.tm_wday])
print("Day from year :", tmobj.tm_yday)
print("Hour :", tmobj.tm_hour)
print("Min :", tmobj.tm_min)
print("Sec :", tmobj.tm_sec)

