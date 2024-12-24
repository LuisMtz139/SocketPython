import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 55555

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error al recibir mensaje")
            client.close()
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_HOST, SERVER_PORT))
    print("Conectado al servidor!")

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'salir':
            break
        client.send(message.encode('utf-8'))

except ConnectionRefusedError:
    print("No se pudo conectar al servidor")
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()