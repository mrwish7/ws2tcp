import socket
import threading
import websocket
import argparse

parser = argparse.ArgumentParser(description='Websocket and TCP server address options.')

parser.add_argument('-W', '--websocket', type=str, dest="websocket", default='ws://127.0.0.1/rdsspy', help='address of the FM-DX Webserver RDS websocket')
parser.add_argument('-I', '--server-ip', type=str, dest="host", default='0.0.0.0', help='IP address for the forwarding TCP server')
parser.add_argument('-P', '--server-port', type=int, dest="port", default=7373, help='port for the forwarding TCP server')

args = parser.parse_args()

# Define the WebSocket URL
WEBSOCKET_URL = args.websocket
# Define the TCP server settings
TCP_HOST = args.host
TCP_PORT = args.port

# Function to handle the TCP client
def handle_client(client_socket, ws):
    try:
        while True:
            # Receive data from the WebSocket
            data = ws.recv()

            # Make sure the variable is bytes
            if isinstance(data, str):
                data = data.encode('utf-8')

            # Forward the data to the client
            client_socket.send(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket
        client_socket.close()

# Function to start the WebSocket connection
def start_websocket_connection():
    ws = websocket.WebSocket()
    try:
        ws.connect(WEBSOCKET_URL)
        return ws
    except Exception as e:
        print(f"WebSocket connection failed: {e}")
        return None

# Main function to start the TCP server
def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((TCP_HOST, TCP_PORT))
    server_socket.listen(1)
    print(f"Listening on {TCP_HOST}:{TCP_PORT}...")

    while True:
        try:
            # Accept a client connection
            client_socket, _ = server_socket.accept()
            print("Accepted connection from a client.")

            # Start the WebSocket connection
            ws = start_websocket_connection()
            if ws is not None:
                # Start a new thread to handle the client
                client_thread = threading.Thread(target=handle_client, args=(client_socket, ws))
                client_thread.start()
            else:
                client_socket.close()
        except (SystemExit, KeyboardInterrupt):
            if connection:
                connection.close()
            break

# Start the server
start_tcp_server()
