import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    s.connect(('kun.uz', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: kun.uz\r\n\r\n')
    data = s.recv(1024)
    print(data)
