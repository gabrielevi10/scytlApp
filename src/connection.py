import socket
import binascii

class Connection:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port):
        try:
            self.sock.connect_ex((ip, port))
            return 'ok'
        except:
            print("Some error occurred in connection")
            return 'error'

    def disconnect(self):
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            return 'ok'
        except:
            print("Some error occurred in disconnetion")
            return 'error'

    def receive(self):
        received_bytes = []
        rcv_byte = binascii.hexlify(self.sock.recv(1))
        if rcv_byte == b'c6':
            while rcv_byte != b'21':
                rcv_byte = binascii.hexlify(self.sock.recv(1))
                received_bytes.append(rcv_byte)
        return received_bytes

    def send(self, message):
        try:
            self.sock.send(message)
            response = self.sock.recv(7)
            print(response)
            return response
        except Exception as e:
            print("Some error occured on send")
            return 'error'
