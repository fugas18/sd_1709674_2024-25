from threading import *
import time
def thread_1():
    for i in range(5):
        print('this is daemon thread')
        time.sleep(2)

T= Thread(target=thread_1,daemon=True)
T.start()
#time.sleep(5)
print('\nmain Thread execution\n')
