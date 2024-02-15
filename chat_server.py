# chat_server.py
import socket

def handle_client(client_socket):
    header = client_socket.recv(4)  # Read the header (message length)
    message_length = int.from_bytes(header, "big")
    message = client_socket.recv(message_length).decode()
    print(f"Received from client: {message}")
    client_socket.send("You said {}".format(message).encode()) # Send it back
    client_socket.close

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
