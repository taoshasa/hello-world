#!/usr/bin/env bash
# Generate certificates for mutual TLS authentication
set -euo pipefail
CERT_DIR=$(dirname "$0")/certs
mkdir -p "$CERT_DIR"

# CA
openssl req -newkey rsa:2048 -nodes -keyout "$CERT_DIR/ca.key" \
    -x509 -days 365 -out "$CERT_DIR/ca.crt" -subj "/CN=Demo CA"

# Server certificate signed by CA
openssl req -newkey rsa:2048 -nodes -keyout "$CERT_DIR/server.key" \
    -out "$CERT_DIR/server.csr" -subj "/CN=localhost"
openssl x509 -req -in "$CERT_DIR/server.csr" -CA "$CERT_DIR/ca.crt" \
    -CAkey "$CERT_DIR/ca.key" -CAcreateserial -out "$CERT_DIR/server.crt" -days 365

# Client certificate signed by CA
openssl req -newkey rsa:2048 -nodes -keyout "$CERT_DIR/client.key" \
    -out "$CERT_DIR/client.csr" -subj "/CN=client"
openssl x509 -req -in "$CERT_DIR/client.csr" -CA "$CERT_DIR/ca.crt" \
    -CAkey "$CERT_DIR/ca.key" -CAcreateserial -out "$CERT_DIR/client.crt" -days 365

echo "Certificates generated in $CERT_DIR"
