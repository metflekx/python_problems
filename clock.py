# Write a script that reads the current time and converts it to a time of day in hours, minutes, and
# seconds, plus the number of days since the epoch

from lib2to3.pgen2.token import MINUS
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
