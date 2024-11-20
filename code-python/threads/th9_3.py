from threading import *
import time
def fun_daemon():
    print("GFC")

thread_1= Thread(target=fun_daemon)
print(thread_1.daemon)
thread_1.start()
print(thread_1.daemon)