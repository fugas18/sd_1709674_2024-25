import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Função para conectar ao servidor e enviar o comando
def connect_to_server():
    # Cria o socket e conecta-se ao servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    print("Digite um número inteiro para calcular os primeiros múltiplos de 9:")
    print("Digite 'sair' para encerrar.")

    while True:
        # Solicita ao usuário um número de múltiplos de 9
        command = input("Número de múltiplos: ")

        if command.lower() == "sair":
            print("Saindo...")
            break

        # Verifica se o comando é um número inteiro
        if not command.isdigit():
            print("Por favor, insira um número inteiro válido.")
            continue

        # Envia o comando para o servidor
        client_socket.send(command.encode())

        # Recebe a resposta do servidor e exibe
        response = client_socket.recv(1024).decode()
        print("Resposta do servidor:", response)

    client_socket.close()

# Inicia o cliente
if __name__ == "__main__":
    connect_to_server()
