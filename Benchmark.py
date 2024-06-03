# --------------------------------------------------------------------
# Python-Benchmark                                                    |
# --------------------------------------------------------------------
# -Made By 3Doge                                                      |
# -Works on most os (not all tested)                                  |
# -Free to use and distribute, but it would be nice for credit :)     |
# -Thanks for using!                                                  |
# --------------------------------------------------------------------

import time
from datetime import datetime

Tests = input("How many mini tests would you like to do? (Going over 100 can cause bugs sorry!) ")

testings = 0

FirstTime = currentDateAndTime = datetime.now()

while True:
    time.sleep(0.5)
    LastTime = currentDateAndTime = datetime.now()
    print("test test test test")
    print("The current date and time is", currentDateAndTime)
    testings += 1
    print(testings)
    if int(Tests) == testings:
        break

text1 = LastTime - FirstTime

besttime = str(text1)[5:]

expectedTime = 0.5 * int(Tests)

print("Expected time:", expectedTime, "Real Time:", besttime)

k = input("press enter to exit")
