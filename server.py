import sqlite3
import hashlib
import socket
import threading

server = socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 999))

server.listen()

def handle_connection(c):