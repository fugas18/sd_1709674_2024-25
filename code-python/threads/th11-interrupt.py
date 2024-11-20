from time import sleep
from threading import Thread
from threading import Event

class MyThread(Thread):
    def __init__(self,event):
        super(MyThread,self).__init__()
        self.event=event
    def run(self):
        i=0
        while True:
            i+=1
            print('Child thread running...',i)
            sleep(0.5)
            if self.event.is_set():
                break
            print()
        print('Child Thread Interrupted')
event=Event()
thread1=MyThread(event)
thread1.start()
sleep(3)
print('Main thread stopping child thread')
event.set()
thread1.join()
