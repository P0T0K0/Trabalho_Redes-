import socket

# Criar socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associar IP e porta
servidor.bind(("localhost", 5000))

# Escutar conexões
servidor.listen()

print("Servidor aguardando conexão...")

# Aceitar conexão
conn, endereco = servidor.accept()
print("Conectado por", endereco)

# Receber dados
mensagem = conn.recv(1024)
print("Mensagem recebida:", mensagem.decode())

# Enviar resposta
conn.send("Mensagem recebida!".encode())

conn.close()