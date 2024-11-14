import threading

def imprimir (nome, inicio, fim):
    for i in range(inicio, fim + 1):
        z = nome + str(i) + "\n"
        print(z)
    z = "\nA thread " + nome + " terminou\n"
    print(z)

x1 = threading.Thread(target=imprimir(), args=("th1 ", 1, 100))
x2 = threading.Thread(target=imprimir, args=("th2 ", 101, 200))
x3 = threading.Thread(target=imprimir, args=("th3 ", 201, 300))


x1.start()
x2.start()
x3.start()


print("FIM")
