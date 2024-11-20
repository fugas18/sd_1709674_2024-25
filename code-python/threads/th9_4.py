from threading import *
import time
def fun():
    print("Geeks for Geeks")

T= Thread(target=fun)
print(T.daemon)
T.daemon=True
print(T.daemon)
T.start()
