# server.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(1)
  
    print("Server listening on port 12345...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        data = client_socket.recv(1024)
        client_socket.send(data)  # Echo back the received data
        client_socket.close()

if __name__ == "__main__":
    start_server()  # Run the server in one terminal
