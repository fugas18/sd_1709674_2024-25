from threading import *
import time
def thread_1():
    for i in range(5):
        print('this is non-daemon thread')
        time.sleep(2)

T= Thread(target=thread_1)
T.start()
#time.sleep(5)
print('\nmain Thread execution\n')
