import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 80))

print("Waiting connections!")

s.listen(1)
conn, addr = s.accept()
print("Connection received!")

while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

conn.close()
