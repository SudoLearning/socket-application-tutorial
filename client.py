# client.py
import socket

def send_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    message = "Hello, server!"
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")

if __name__ == "__main__":
    send_message()  # Run the client in another terminal
