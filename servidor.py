import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 55555
clients = []

def handle_client(client_socket, client_address):
    print(f"Nueva conexión desde {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Mensaje de {client_address}: {message}")
            broadcast(message, client_socket)
        except:
            break
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen()

print(f"Servidor escuchando en {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.daemon = True
    thread.start()