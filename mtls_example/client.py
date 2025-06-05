import os
import ssl
import socket

CERT_DIR = os.path.join(os.path.dirname(__file__), 'certs')
CLIENT_CERT = os.path.join(CERT_DIR, 'client.crt')
CLIENT_KEY = os.path.join(CERT_DIR, 'client.key')
CA_CERT = os.path.join(CERT_DIR, 'ca.crt')

HOST = 'localhost'
PORT = 8443

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=CA_CERT)
context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)

with context.wrap_socket(socket.socket(), server_hostname=HOST) as s:
    s.connect((HOST, PORT))
    message = 'Telemetry data from domain controller'
    s.sendall(message.encode('utf-8'))
    data = s.recv(4096)
    print('Server replied:', data.decode('utf-8', errors='ignore'))
