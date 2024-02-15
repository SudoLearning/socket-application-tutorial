# chat_client.py
import socket

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    message_length = len(message)
    header = message_length.to_bytes(4, "big")
    client_socket.send(header + message.encode())
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")

if __name__ == "__main__":
    # Send "Sockets are awesome!" to the server.
    send_message("Sockets are awesome!")
