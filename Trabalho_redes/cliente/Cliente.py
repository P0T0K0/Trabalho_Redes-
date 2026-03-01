
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 5000))

cliente.send("Olá servidor!".encode())

resposta = cliente.recv(1024)
print("Resposta do servidor:", resposta.decode())

cliente.close()