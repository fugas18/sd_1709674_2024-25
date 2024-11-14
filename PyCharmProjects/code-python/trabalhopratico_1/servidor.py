import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000


# Função que calcula os primeiros x múltiplos de 9 e retorna a soma
def Multiplo9(x):
    if x <= 0:
        return "O valor de x deve ser maior que 0."

    # Calcula os primeiros x múltiplos de 9
    multiplos = [9 * i for i in range(1, x + 1)]
    soma = sum(multiplos)  # Calcula a soma dos múltiplos

    # Retorna tanto os múltiplos quanto a soma
    multiplos_str = ", ".join(map(str, multiplos))
    return f"Múltiplos de 9: {multiplos_str}. Soma: {soma}"


# Função para atender o cliente
def handle_client(client_socket):
    try:
        while True:
            # Recebe o comando do cliente
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # Tenta converter o valor para inteiro
            try:
                x = int(data)
            except ValueError:
                client_socket.send("Entrada inválida. Envie um número inteiro.".encode())
                continue

            # Calcula os múltiplos de 9 e envia a resposta
            response = Multiplo9(x)
            client_socket.send(response.encode())
    finally:
        client_socket.close()


# Função para iniciar o servidor e aguardar conexões
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print(f"Servidor iniciado em {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Cliente {client_address} conectado.")
        # Inicia uma thread para atender o cliente
        threading.Thread(target=handle_client, args=(client_socket,)).start()


# Inicia o servidor
if __name__ == "__main__":
    start_server()
