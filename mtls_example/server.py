import os
import ssl
import socket

CERT_DIR = os.path.join(os.path.dirname(__file__), 'certs')
SERVER_CERT = os.path.join(CERT_DIR, 'server.crt')
SERVER_KEY = os.path.join(CERT_DIR, 'server.key')
CA_CERT = os.path.join(CERT_DIR, 'ca.crt')

HOST = '0.0.0.0'
PORT = 8443

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=SERVER_CERT, keyfile=SERVER_KEY)
context.load_verify_locations(cafile=CA_CERT)

bindsocket = socket.socket()
bindsocket.bind((HOST, PORT))
bindsocket.listen(5)
print(f'Server listening on {PORT} ...')

try:
    while True:
        newsocket, fromaddr = bindsocket.accept()
        print('Connection from', fromaddr)
        with context.wrap_socket(newsocket, server_side=True) as ssock:
            data = ssock.recv(4096)
            if not data:
                continue
            print('Received:', data.decode('utf-8', errors='ignore'))
            ssock.sendall(b'OK')
finally:
    bindsocket.close()
