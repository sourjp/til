import socket

# TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data: break
                print('data: {}, addr: {}'.format(data, addr))
                conn.sendall(b'Recieved: ' + data)

# UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data. addr = s.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))

'''
Well-known 0-1023
reserver port 1024-49151
private: 49152-65535
'''

