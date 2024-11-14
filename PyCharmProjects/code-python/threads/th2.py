import threading
import time
from concurrent.futures import ThreadPoolExecutor


def multiplos(nome,x):
    for i in range(0,11):
        z=nome+str(i*x)+"\n"
        print(z)
    z="\nA thread "+ nome + "terminou\n";
    print(z)

def soma(nome,x):
    for i in range(0,11):
        z=nome+str(i+x)+"\n"
        print(z)
    z="\nA thread "+ nome + "terminou\n";
    print(z)

executor = ThreadPoolExecutor(max_workers=4)
executor.submit(multiplos("th1-mullt ",2))
executor.submit(multiplos("th2-mult ",3))
executor.submit(soma("th3-sum ",5))
executor.submit(soma("th4-sum ",7))

