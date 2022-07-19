# from the book "Think Python second edition"
# author : Allen Downey

# "Exercise 5.1. The time module provides a function, also named time, that returns the current
# Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
# UNIX systems, the epoch is 1 January 1970."


import time
import math

myTime = time.time()

daysSince = myTime // 86400

hoursSince = myTime / 3600

minSince = myTime / 60

hour = int(hoursSince % 24)

minute = int(minSince % 60)

seconde = int(myTime % 60)  # myTime = secondesSince

print(f"{hour : } {minute : } {seconde}.")
