import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA512
import sys,time

server_ip='127.0.0.1'
port=1234
key=b'+\x01\xfd\x89\x12\x15E\xceah\xe9^J\\\xa9['
iv=b'\xd4/\x03\x8br\xc2d\xb3\x1fg\x05]\xd2h\xb5k'
HMAC_KEY= b'\x9a$o\xad\xa4\xd18\xeb\x8c\xd74N\xda\xc5\x80\x95'


def hmac(recv_msg):
    obj=HMAC.new(HMAC_KEY,digestmod=SHA512)
    obj.update(recv_msg.encode('utf-8'))
    global digest
    digest=obj.digest()


def encryption(msg):
    msg=msg.encode('utf-8')
    cipher=AES.new(key,AES.MODE_CBC,iv)
    global encrypted_data
    encrypted_data=cipher.encrypt(pad(msg,AES.block_size))

def decryption(req):
    cipher=AES.new(key,AES.MODE_CBC,iv=iv)
    request=unpad(cipher.decrypt(req),AES.block_size)
    global decrypted_data
    decrypted_data=request.decode('utf-8')

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((server_ip,port))
        server.listen(0)
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        while True:
            request1=client_socket.recv(1024)
            request2=client_socket.recv(1024)
            if request1:
                decryption(request1)
                hmac(decrypted_data)
            if digest != request2:
                print('The message is corrupted')
                sys.exit()
            if decrypted_data.lower()=='close':
                encryption('closed')
                hmac('closed')
                client_socket.send(encrypted_data)
                time.sleep(0.25)
                client_socket.send(digest)
                break
            print(f'Client : {decrypted_data}')
            x=input('Server :')
            hmac(x)
            if x:
                encryption(x)
            client_socket.send(encrypted_data)
            time.sleep(0.25)
            client_socket.send(digest)
    except Exception as e:
        print(e)
    client_socket.close()
    print('The connection to client closed')
    server.close()
run_server()
