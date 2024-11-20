import threading

def multiplos(nome, x):
    for i in range(10):  # Algarismos de 0 a 9
        z = nome + str(i * x) + "\n"
        print(z)
    z = "\nA thread " + nome + " terminou\n"
    print(z)


x1 = threading.Thread(target=multiplos, args=("th1 ", 2))
x2 = threading.Thread(target=multiplos, args=("th2 ", 3))
x3 = threading.Thread(target=multiplos, args=("th3 ", 5))


x1.start()
x2.start()
x3.start()


x1.join()
x2.join()
x3.join()

print("FIM")
