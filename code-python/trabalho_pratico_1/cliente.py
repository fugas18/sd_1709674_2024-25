import socket


def main():
    # Conectar ao servidor
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000
                    ))  # Define o endereço e a porta do servidor

    while True:
        # Solicitar ao utilizador o número de múltiplos de 9 que deseja
        x = input("Insira o número de múltiplos de 9 que pretende calcular (ou 'sair' para terminar): ")

        # Termina o cliente se o utilizador inserir 'sair'
        if x.lower() == 'sair':
            print("A terminar a conexão com o servidor.")
            break

        try:
            # Enviar o valor 'x' ao servidor
            client.send(x.encode())

            # Receber e exibir a resposta do servidor
            resposta = client.recv(1024).decode()
            print("Resposta do servidor:", resposta)

        except ValueError:
            print("Por favor, insira um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break

    # Fechar a conexão com o servidor
    client.close()


if __name__ == "__main__":
    main()