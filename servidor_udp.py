import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso")
host = 'localhost'
port = 5432

# ligação do cliente e servidor através do host e da porta
s.bind(host, port)
mensagem = 'Servidor: Olá Cliente.'

# se a conexão for verdadeira
while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)

