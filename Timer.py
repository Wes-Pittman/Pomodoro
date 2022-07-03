# Python program to illustrate a Pomodoro Timer with built-in intervals 25/10 then after 4 sets a 30min break and sounds chimes or dings
# Imports
import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time lapsed = {0}:{1}".format(int(mins), sec))


input("Press Enter to start the Pomodoro cycle")
start_time = time.time()
try:
    hours = 0

    while True:
        for minutes in range(0, 60):
            for seconds in range(0, 60):
                time.sleep(1)
                print(minutes, ":", seconds+1)

except KeyboardInterrupt:
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
