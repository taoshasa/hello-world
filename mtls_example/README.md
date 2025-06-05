# Mutual TLS Demo for Vehicle Controller

This example demonstrates how an intelligent driving domain controller can
securely send telemetry data to a cloud service using mutual TLS (mTLS).

## Generating certificates

Run the provided script to create a Certificate Authority (CA), a server
certificate and a client certificate:

```bash
./generate_certs.sh
```

The certificates are placed in the `certs/` directory.

## Running the server (cloud side)

```bash
python3 server.py
```

The server listens on port `8443` and requires clients to present a valid
certificate signed by the demo CA.

## Running the client (vehicle side)

```bash
python3 client.py
```

The client connects to `localhost:8443` using its certificate and sends a
sample telemetry message. The server prints the received data and replies
with `OK`.

This setup can be adapted for real vehicle controllers by deploying the
server code in the cloud and running the client on the vehicle's domain
controller with proper certificates.
