import socket

# Função para calcular os primeiros x múltiplos de 9 e a sua soma
def Multiplo9(x):
    if x <= 0:
        return "Erro: o valor deve ser maior que 0."

    # Calcula os múltiplos de 9 e a sua soma
    multiplos = [9 * i for i in range(1, x + 1)]
    soma = sum(multiplos)

    # Formata a resposta como uma string
    multiplos_str = ", ".join(map(str, multiplos))
    return f"\nMúltiplos de 9: {multiplos_str}.\nSoma: {soma}"

# Função para gerir a comunicação com o cliente
def handle_client(client_socket):
    try:
        # Recebe o valor de 'x' do cliente
        data = client_socket.recv(1024).decode()

        # Converte o valor para inteiro e chama a função Multiplo9
        x = int(data)
        response = Multiplo9(x)

        # Envia a resposta para o cliente
        client_socket.send(response.encode())
    finally:
        client_socket.close()
    
# Configuração do servidor
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))  # Define o endereço IP e a porta para o servidor
    server.listen(5)  # Limita o número de conexões em espera

    print("Servidor a aguardar conexões...")

    # Ciclo para aceitar e gerir conexões de clientes
    while True:
        client_socket, addr = server.accept()
        print(f"Conexão estabelecida com {addr}")
        handle_client(client_socket)


if __name__ == "__main__":
    main()