from threading import current_thread
from threading import Thread

def task(other):
    print(f'[{current_thread().name} waiting on [{other.name}]]...')
    other.join()

main_thread = current_thread()

new_thread =Thread(target=task,args=(main_thread,))
new_thread.start()
task(new_thread)
print("fim")
