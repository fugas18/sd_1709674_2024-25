# example of the creating a daemon process after create a process
# example of checking each one if it is a daemon process

from multiprocessing import current_process
from multiprocessing import Process


# function to be executed in a new process
def task():
    # get the current process
    process = current_process()
    # report if daemon process
    print(f'Daemon process: {process.daemon}')


# entry point
if __name__ == '__main__':
    # create a new process with a default value for "daemon"
    process1 = Process(target=task)
    # start the new process
    print("moment-0=",process1.is_alive())
    process1.start()
    # create a new daemon process
    print("moment-1=",process1.is_alive())
    process2 = Process(target=task, daemon=True)
    # start the new process
    print("moment-2=",process1.is_alive())
    process2.start()
    print("moment-3=",process1.is_alive())
    # wait for the new process to finish
    process2.join()
    print("moment-4=",process1.is_alive())