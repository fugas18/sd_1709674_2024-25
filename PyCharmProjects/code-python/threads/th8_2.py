import sched
from datetime import datetime
import time
def addition(a,b):
    print("Performing Addition : ", datetime.now())
    print("Time : ", time.monotonic())
    print("Result : ", a+b)
s = sched.scheduler()
print("Start Time : ", datetime.now())
event1 = s.enter(10, 1, addition, argument = (5,6))
print("Event Created : ", event1)
s.run()
print("End Time : ", datetime.now())
